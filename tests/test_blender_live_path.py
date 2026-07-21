from __future__ import annotations

import base64
import hashlib
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "validators"))

from validate_blender_report import validate as validate_blender_report
from validate_mcp_action_log import validate as validate_mcp_action_log
from validate_mcp_iteration_receipt import validate as validate_mcp_iteration_receipt
from validate_screenshot_manifest import DEFAULT_VIEWS, validate as validate_screenshot_manifest
from validate_stage_task_card import validate as validate_stage_task_card


def load_prepare_module():
    path = ROOT / "skills/blender-mcp-operator/scripts/prepare_working_copy.py"
    spec = importlib.util.spec_from_file_location("prepare_working_copy", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(module)
    return module


def load_scene_delta_module():
    path = ROOT / "skills/blender-mcp-operator/scripts/scene_delta.py"
    spec = importlib.util.spec_from_file_location("scene_delta", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(module)
    return module


class WorkingCopyTests(unittest.TestCase):
    def test_creates_verified_non_overwriting_copies(self):
        module = load_prepare_module()
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "source.blend"
            source.write_bytes(b"BLENDER-test-fixture")
            receipt = root / "workspace/protection.json"
            result = module.prepare(source, "asset", "microtask", root / "workspace", receipt)
            self.assertEqual(result["source_sha256_before"], result["backup_sha256"])
            self.assertEqual(result["backup_sha256"], result["working_sha256_before"])
            self.assertTrue(Path(result["backup_file"]).is_file())
            self.assertTrue(Path(result["working_file"]).is_file())
            with self.assertRaises(FileExistsError):
                module.prepare(source, "asset", "microtask", root / "workspace", receipt)

    def test_quick_iteration_bounds_reject_unsafe_work(self):
        module = load_scene_delta_module()
        module.validate_bounds(["ORC_arm_L"], ["transform"], 1)
        with self.assertRaises(ValueError):
            module.validate_bounds([f"target_{index}" for index in range(7)], ["transform"], 1)
        with self.assertRaises(ValueError):
            module.validate_bounds(["ORC_arm_L"], ["remesh"], 1)
        with self.assertRaises(ValueError):
            module.validate_bounds(["ORC_arm_L"], ["transform"], 4)


class ValidatorTests(unittest.TestCase):
    PNG = base64.b64decode(
        "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII="
    )

    def build_quick_fixture(self, root: Path) -> tuple[Path, Path]:
        source = root / "source.blend"
        backup = root / "backup.blend"
        working = root / "working.blend"
        source.write_bytes(b"BLENDER-source")
        backup.write_bytes(source.read_bytes())
        working.write_bytes(b"BLENDER-working-after")
        source_hash = hashlib.sha256(source.read_bytes()).hexdigest()
        working_before_hash = hashlib.sha256(b"BLENDER-working-before").hexdigest()
        working_after_hash = hashlib.sha256(working.read_bytes()).hexdigest()

        protection = root / "protection.json"
        protection.write_text(json.dumps({
            "asset_id": "asset", "microtask_id": "asset-arm-adjust-001",
            "source_file": str(source.resolve()), "backup_file": str(backup.resolve()),
            "working_file": str(working.resolve()), "source_sha256_before": source_hash,
            "backup_sha256": source_hash, "working_sha256_before": working_before_hash,
        }), encoding="utf-8")

        screenshots = []
        for view in ("front", "three_quarter"):
            image = root / f"{view}.png"
            image.write_bytes(self.PNG)
            screenshots.append({"view": view, "path": str(image), "status": "captured", "width": 1, "height": 1})
        manifest = root / "quick_manifest.json"
        manifest.write_text(json.dumps({
            "asset_id": "asset", "stage_id": "secondary_anatomy",
            "source_file": str(working.resolve()), "screenshots": screenshots,
        }), encoding="utf-8")

        receipt = root / "iteration_receipt.json"
        receipt.write_text(json.dumps({
            "receipt_version": "0.1.0", "evidence_tier": "quick_iteration",
            "created_at": "2026-07-21T00:00:00+00:00", "asset_id": "asset",
            "stage_id": "secondary_anatomy", "microtask_id": "asset-arm-adjust-001",
            "iteration_id": "arm-adjust-iter-001", "iteration_index": 1,
            "target_objects": ["ORC_arm_L"], "allowed_change_types": ["transform"],
            "changed_objects": ["ORC_arm_L"], "unexpected_changed_objects": [],
            "missing_objects": [], "added_objects": [], "topology_count_changes": [],
            "material_changes": False, "protected_objects_checked": 10,
            "destructive_operations": False, "hard_failures": [],
            "source_file": str(source.resolve()), "backup_file": str(backup.resolve()),
            "working_file": str(working.resolve()), "source_sha256_before": source_hash,
            "source_sha256_after": source_hash, "backup_sha256": source_hash,
            "working_sha256_before": working_before_hash, "working_sha256_after": working_after_hash,
            "screenshot_manifest": str(manifest.resolve()),
        }), encoding="utf-8")

        task = root / "task.md"
        task.write_text("""# Quick Task
- `task_id`: asset-arm-adjust-001
- `asset_id`: asset
- `stage_id`: secondary_anatomy
- `stage_name`: Secondary anatomy
- `created_by`: tester
- `created_at`: 2026-07-21
- `status`: in_progress
- `goal`: Adjust one arm.
- `current_stage`: secondary_anatomy
- `allowed_tools`: Blender MCP
- `disallowed_tools`: deletion and topology changes
- `known_constraints`: bounded arm adjustment
- `input_refs`: local evidence
- `required_outputs`: quick iteration receipt
- `output_paths`: working.blend
- `report_paths`: iteration_receipt.json
- `screenshot_requirements`: front and three_quarter
- `handoff_format`: templates/stage_handoff.md
- `acceptance_tests`: no non-target drift
- `required_validators`: validate_mcp_iteration_receipt
- `manual_review_required`: yes
- `hard_failure_checks`: unexpected drift
- `stop_conditions`: stop on drift
- `requires_human_approval`: yes
- `do_not_continue_if`: validator fails
- `assigned_specialist`: Anatomy Reviewer
- `microtasks`: Adjust one named arm target
- `mcp_microtask_id`: asset-arm-adjust-001
- `evidence_tier`: quick_iteration
- `iteration_budget`: 3
- `iteration_views`: front; three_quarter
- `target_objects`: ORC_arm_L
- `allowed_change_types`: transform
- `execution_authorized_by`: tester
- `execution_authorized_at`: 2026-07-21
- `blocking_issues`: none
""", encoding="utf-8")

        log = root / "quick_log.md"
        fields = {
            "log_id": "quick-log-001", "asset_id": "asset", "stage_id": "secondary_anatomy",
            "microtask_id": "asset-arm-adjust-001", "created_by": "tester", "created_at": "2026-07-21",
            "status": "executed", "execution_mode": "real_mcp", "evidence_tier": "quick_iteration",
            "iteration_id": "arm-adjust-iter-001", "iteration_index": "1", "project_root": str(ROOT),
            "blender_version": "5.2.0", "mcp_server": "mcp__blender", "mcp_server_version": "test",
            "connection_status": "ready", "required_capabilities": "execute_blender_code",
            "available_capabilities": "execute_blender_code", "capability_preflight": "pass",
            "isolated_workspace_verified": "yes", "arbitrary_python_requested": "yes",
            "arbitrary_python_approved_by": "tester", "task_card": str(task.resolve()),
            "specialist_owner": "Anatomy Reviewer", "microtask_goal": "Adjust one named arm target.",
            "allowed_tools": "Blender MCP", "disallowed_tools": "deletion and topology changes",
            "acceptance_tests": "no non-target drift", "stop_conditions": "stop on drift",
            "target_objects": "ORC_arm_L", "allowed_change_types": "transform",
            "source_file": str(source.resolve()), "backup_file": str(backup.resolve()),
            "working_file": str(working.resolve()), "source_protection_receipt": str(protection.resolve()),
            "backup_verified": "yes", "source_sha256_before": source_hash, "backup_sha256": source_hash,
            "working_sha256_before": working_before_hash, "source_sha256_after": source_hash,
            "source_unchanged_verified": "yes", "destructive_operations_requested": "no",
            "destructive_operations_approved_by": "none", "destructive_operations_approved_at": "none",
            "screenshots": str(manifest.resolve()), "iteration_receipt": str(receipt.resolve()),
            "blender_reports": "deferred_to_gate_review", "validation_reports": "deferred_to_gate_review",
            "specialist_review": "deferred_to_gate_review", "qa_audit": "deferred_to_gate_review",
            "structural_change_made": "yes", "hard_failures_present": "no",
            "blocked_stage_progression": "yes", "rollback_required": "no",
            "rollback_artifact": str(backup.resolve()), "working_copy_disposition": "retained_for_iteration",
            "decision": "continue_iteration", "decision_reason": "Delta and quick previews pass.",
            "human_approval_required": "no", "approved_by": "none", "approved_at": "none",
        }
        body = "# Quick Log\n\n" + "\n".join(f"- `{key}`: {value}" for key, value in fields.items())
        body += "\n\n| Step | Tool Or Command | Intent | Result | Artifact |\n|---:|---|---|---|---|\n| 1 | MCP | adjust target | pass | receipt |\n"
        log.write_text(body, encoding="utf-8")
        return receipt, log

    def test_quick_iteration_receipt_and_log_pass(self):
        with tempfile.TemporaryDirectory() as temporary:
            receipt, log = self.build_quick_fixture(Path(temporary))
            failures, warnings, _, _ = validate_mcp_iteration_receipt(receipt)
            self.assertEqual([], failures)
            self.assertEqual([], warnings)
            failures, _, _, _ = validate_mcp_action_log(log, ROOT)
            self.assertEqual([], failures)

    def test_quick_iteration_rejects_unexpected_drift(self):
        with tempfile.TemporaryDirectory() as temporary:
            receipt, _ = self.build_quick_fixture(Path(temporary))
            data = json.loads(receipt.read_text(encoding="utf-8"))
            data["unexpected_changed_objects"] = ["ORC_head"]
            receipt.write_text(json.dumps(data), encoding="utf-8")
            failures, _, _, _ = validate_mcp_iteration_receipt(receipt)
            self.assertIn("clean_delta_required", {failure.rule_id for failure in failures})

    def test_repository_examples_remain_schema_valid(self):
        failures, warnings, _, _ = validate_mcp_action_log(
            ROOT / "examples/stylized_orc_bruiser/mcp_logs/accepted_microtask_001.md", ROOT
        )
        self.assertEqual([], failures)
        self.assertIn("non_live_approval", {warning.rule_id for warning in warnings})
        failures, _, _, _ = validate_stage_task_card(
            ROOT / "examples/stylized_orc_bruiser/task_cards/concept_interpretation.md", ROOT
        )
        self.assertEqual([], failures)

    def test_real_mcp_mode_rejects_example_only_evidence(self):
        source = ROOT / "examples/stylized_orc_bruiser/mcp_logs/accepted_microtask_001.md"
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "forged_real_log.md"
            path.write_text(
                source.read_text(encoding="utf-8").replace("- `execution_mode`: example", "- `execution_mode`: real_mcp"),
                encoding="utf-8",
            )
            failures, _, _, _ = validate_mcp_action_log(path, ROOT)
            rule_ids = {failure.rule_id for failure in failures}
            self.assertIn("artifact_exists", rule_ids)
            self.assertGreaterEqual(sum(failure.rule_id == "artifact_exists" for failure in failures), 5)

    def test_blender_report_rejects_inconsistent_summary(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "report.json"
            path.write_text(json.dumps({
                "metadata": {
                    "report_type": "scene", "asset_id": "asset", "stage_id": "blockout",
                    "created_at": "2026-07-20T00:00:00+00:00", "script_version": "0.2.0",
                    "blender_version": "4.3.2", "source_file": "fixture.blend",
                    "source_read_only": True, "writes_artifacts": True,
                },
                "summary": {"warning_count": 0, "hard_failure_count": 0, "status": "fail"},
                "warnings": [], "hard_failures": [], "measurements": {}, "items": [],
            }), encoding="utf-8")
            failures, _, _, _ = validate_blender_report(path, None, None, None)
            self.assertIn("summary_consistency", {failure.rule_id for failure in failures})

    def test_screenshot_manifest_requires_real_pngs(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "working.blend"
            source.write_bytes(b"fixture")
            items = []
            for view in sorted(DEFAULT_VIEWS):
                image = root / f"{view}.png"
                image.write_bytes(self.PNG)
                items.append({"view": view, "path": str(image), "status": "captured", "width": 1, "height": 1})
            manifest = root / "manifest.json"
            manifest.write_text(json.dumps({
                "asset_id": "asset", "stage_id": "blockout", "source_file": str(source), "screenshots": items,
            }), encoding="utf-8")
            failures, _, _, _ = validate_screenshot_manifest(manifest, DEFAULT_VIEWS)
            self.assertEqual([], failures)
            Path(items[0]["path"]).unlink()
            failures, _, _, _ = validate_screenshot_manifest(manifest, DEFAULT_VIEWS)
            self.assertIn("valid_png", {failure.rule_id for failure in failures})


if __name__ == "__main__":
    unittest.main()
