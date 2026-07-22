from __future__ import annotations

import base64
import hashlib
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "validators"))

from validate_blender_report import validate as validate_blender_report
from validate_mcp_action_log import validate as validate_mcp_action_log
from validate_mcp_iteration_receipt import validate as validate_mcp_iteration_receipt
from validate_mcp_session import validate as validate_mcp_session
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


def load_script(name: str):
    path = ROOT / f"skills/blender-mcp-operator/scripts/{name}.py"
    spec = importlib.util.spec_from_file_location(name, path)
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


class ActiveSessionTests(unittest.TestCase):
    def _start(self, root: Path):
        module = load_script("mcp_session")
        journal = root / "asset/mcp_sessions/session-001.jsonl"
        artifacts = {}
        for name in ("source_file", "backup_file", "working_file"):
            path = root / f"{name}.blend"
            path.write_bytes(b"BLENDER-session")
            artifacts[name] = str(path.resolve())
        task = root / "task.md"; task.write_text("task", encoding="utf-8")
        receipt = root / "protection.json"; receipt.write_text("{}", encoding="utf-8")
        module.append_record(
            journal, session_id="session-001", record_type="session_started",
            before_hash="a" * 64, after_hash="a" * 64, durations_ms={"preflight": 2.0, "total": 3.0},
            details={
                "asset_id": "asset", "stage_id": "tertiary_detail", "task_card": str(task.resolve()),
                "authorized_collections": ["Face"], "safe_change_types": ["absolute_transform", "visibility", "collection_membership", "vertex_positions"],
                "max_targets_per_edit": 6, **artifacts, "source_protection_receipt": str(receipt.resolve()),
                "capability_preflight": {"server": "blender", "server_version": "1", "capabilities": ["edit"]},
            },
        )
        return module, journal

    def test_session_sequence_hash_chain_and_timings(self):
        with tempfile.TemporaryDirectory() as temporary:
            module, journal = self._start(Path(temporary))
            edit = module.append_record(
                journal, session_id="session-001", record_type="iteration_accepted",
                targets=["tusk_L", "tusk_R", "brow_L", "brow_R"],
                operations=[
                    {"type": "absolute_transform", "target": "tusk_L", "location": [1, 2, 3]},
                    {"type": "absolute_transform", "target": "tusk_R", "location": [-1, 2, 3]},
                    {"type": "vertex_positions", "target": "brow_L", "vertices": [{"index": 0, "co": [0, 0, 0]}]},
                    {"type": "vertex_positions", "target": "brow_R", "vertices": [{"index": 0, "co": [0, 0, 0]}]},
                ],
                before_hash="a" * 64, after_hash="b" * 64,
                drift={"status": "pass", "issues": []}, durations_ms={"apply": 1.0, "total": 4.0},
            )
            module.append_record(
                journal, session_id="session-001", record_type="preview_result",
                targets=edit["targets"], before_hash="b" * 64, after_hash="b" * 64,
                durations_ms={"total": 5.0}, details={
                    "iteration_sequence": edit["sequence"],
                    "preview": {"tool": "get_viewport_screenshot", "view": "face_three_quarter", "dimensions": [800, 600], "timestamp": "2026-07-22T00:00:00+00:00", "status": "captured"},
                },
            )
            failures, _, records, measurements = validate_mcp_session(journal)
            self.assertEqual([], failures)
            self.assertEqual([1, 2, 3], [record["sequence"] for record in records])
            self.assertEqual(records[1]["record_hash"], records[2]["previous_record_hash"])
            self.assertEqual(1, measurements["accepted_iterations"])

    def test_session_open_protects_once_and_refuses_overwrite(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "source.blend"
            source.write_bytes(b"BLENDER-session-source")
            task = root / "task.md"
            task.write_text("task", encoding="utf-8")
            module = load_script("mcp_session")
            kwargs = {
                "source_file": source, "asset_root": root / "asset", "asset_id": "asset",
                "stage_id": "tertiary_detail", "task_card": task, "session_id": "session-001",
                "authorized_collections": ["Face"], "safe_change_types": ["absolute_transform", "vertex_positions"],
                "server": "blender", "server_version": "1", "capabilities": ["edit", "view"],
            }
            result = module.open_session(**kwargs)
            self.assertTrue(Path(result["protection"]["backup_file"]).is_file())
            self.assertTrue(Path(result["protection"]["working_file"]).is_file())
            self.assertTrue(Path(result["journal"]).is_file())
            with self.assertRaises(FileExistsError):
                module.open_session(**kwargs)

    def test_combined_four_object_edit_creates_only_journal(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            module, journal = self._start(root)
            files_before_edit = {path.relative_to(root).as_posix() for path in root.rglob("*") if path.is_file()}
            record = module.append_record(
                journal, session_id="session-001", record_type="iteration_accepted",
                targets=["tusk_L", "tusk_R", "brow_L", "brow_R"],
                operations=[{"type": "visibility", "target": name, "hide_render": False} for name in ("tusk_L", "tusk_R", "brow_L", "brow_R")],
                before_hash="a" * 64, after_hash="b" * 64,
                drift={"status": "pass", "issues": []}, durations_ms={"total": 1.0},
            )
            module.append_record(
                journal, session_id="session-001", record_type="preview_result", targets=record["targets"],
                before_hash="b" * 64, after_hash="b" * 64, durations_ms={"total": 1.0},
                details={"iteration_sequence": 2, "preview": {"tool": "get_viewport_screenshot", "view": "face", "dimensions": [512, 512], "timestamp": "2026-07-22T00:00:00+00:00", "status": "captured"}},
            )
            files_after_edit = {path.relative_to(root).as_posix() for path in root.rglob("*") if path.is_file()}
            self.assertEqual(files_before_edit, files_after_edit)
            self.assertFalse(any(any(word in path for word in ("review", "audit", "action_log")) for path in files_after_edit))

    def test_target_authorization_and_safe_operation_rejections(self):
        module = load_script("quick_edit_runner")
        base = {
            "working_file": "/tmp/example.blend", "authorized_collections": ["Face"],
            "target_objects": ["a"], "operations": [{"type": "visibility", "target": "a", "hide_viewport": False}],
        }
        module.normalize_request(base)
        with self.assertRaises(ValueError):
            module.normalize_request({**base, "target_objects": list("abcdefg")})
        with self.assertRaises(ValueError):
            module.normalize_request({**base, "operations": [{"type": "material", "target": "a"}]})
        with self.assertRaises(ValueError):
            module.normalize_request({**base, "operations": [{"type": "collection_membership", "target": "a", "collections": ["Body"]}]})

    def test_drift_detects_structure_topology_material_and_non_targets(self):
        module = load_script("quick_edit_runner")
        mesh = {"vertices": 1, "edges": 0, "faces": 0, "coordinate_sha256": "a"}
        signature = {"name": "target", "type": "MESH", "location": [0, 0, 0], "rotation_euler": [0, 0, 0], "scale": [1, 1, 1], "collections": ["Face"], "hide_viewport": False, "hide_render": False, "materials": ["Skin"], "mesh": mesh}
        before = {"objects": {"target": signature, "other": {**signature, "name": "other"}}, "materials": {"Skin": {"value": 1}}}
        changed_target = {**signature, "mesh": {**mesh, "vertices": 2}}
        changed_other = {**signature, "name": "other", "location": [1, 0, 0]}
        after = {"objects": {"target": changed_target, "other": changed_other, "added": signature}, "materials": {"Skin": {"value": 2}}}
        drift = module._drift(before, after, {"target"})
        issue_types = {item["type"] for item in drift["issues"]}
        self.assertTrue({"added_or_renamed_objects", "non_target_changes", "topology_changes", "material_changes"}.issubset(issue_types))

    def test_wrong_and_dirty_blender_files_are_rejected_before_edit(self):
        module = load_script("quick_edit_runner")
        with tempfile.TemporaryDirectory() as temporary:
            working = Path(temporary) / "working.blend"
            working.write_bytes(b"BLENDER")
            request = {"working_file": str(working), "authorized_collections": ["Face"], "target_objects": ["a"], "operations": [{"type": "visibility", "target": "a", "hide_render": False}]}
            fake = mock.Mock()
            fake.data.filepath = str(Path(temporary) / "wrong.blend")
            fake.data.is_dirty = False
            with self.assertRaisesRegex(ValueError, "not displaying"):
                module.run_quick_edit(request, fake)
            fake.data.filepath = str(working)
            fake.data.is_dirty = True
            with self.assertRaisesRegex(ValueError, "must be clean"):
                module.run_quick_edit(request, fake)

    def test_cached_preflight_refresh_rules_and_pipeline_state(self):
        module = load_script("mcp_session")
        key = module.preflight_cache_key(server="blender", server_version="1", capabilities=["view", "edit"], working_file="/tmp/a.blend", working_sha256="abc")
        self.assertFalse(module.should_refresh_preflight(key, dict(key)))
        self.assertTrue(module.should_refresh_preflight(key, dict(key), reconnected=True))
        self.assertTrue(module.should_refresh_preflight(key, {**key, "server_version": "2"}))
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "pipeline_state.json"
            state = module.write_pipeline_state(path, current_stage="tertiary_detail", task_card="task.md", active_session="s", working_file="w.blend")
            self.assertEqual("s", json.loads(path.read_text(encoding="utf-8"))["active_session"])
            self.assertEqual("clear", state["hard_failure_state"])

    def test_viewer_sync_uses_clean_hash_fast_path(self):
        module = load_script("viewer_sync")
        with tempfile.TemporaryDirectory() as temporary:
            working = Path(temporary) / "working.blend"
            working.write_bytes(b"BLENDER-clean")
            data = SimpleNamespace(filepath=str(working), is_dirty=False)
            open_mainfile = mock.Mock()
            fake_bpy = SimpleNamespace(data=data, ops=SimpleNamespace(wm=SimpleNamespace(open_mainfile=open_mainfile)))
            with mock.patch.dict(sys.modules, {"bpy": fake_bpy}):
                result = module.sync_viewer(working, module.sha256(working))
            self.assertFalse(result["reloaded"])
            open_mainfile.assert_not_called()
            data.is_dirty = True
            with mock.patch.dict(sys.modules, {"bpy": fake_bpy}):
                with self.assertRaisesRegex(RuntimeError, "explicit recovery"):
                    module.sync_viewer(working)

    def test_replay_uses_only_accepted_absolute_operations(self):
        with tempfile.TemporaryDirectory() as temporary:
            module, journal = self._start(Path(temporary))
            module.append_record(journal, session_id="session-001", record_type="iteration_rejected", targets=["a"], operations=[{"type": "visibility", "target": "a", "hide_render": True}], drift={"status": "fail", "issues": ["drift"]}, durations_ms={"total": 1})
            module.append_record(journal, session_id="session-001", record_type="iteration_accepted", targets=["b"], operations=[{"type": "absolute_transform", "target": "b", "location": [1, 2, 3]}], before_hash="a", after_hash="b", drift={"status": "pass", "issues": []}, durations_ms={"total": 1})
            self.assertEqual([{"location": [1.0, 2.0, 3.0], "target": "b", "type": "absolute_transform"}], module.accepted_operations(journal))

    def test_validator_rejects_malformed_chain_and_missing_preview(self):
        with tempfile.TemporaryDirectory() as temporary:
            module, journal = self._start(Path(temporary))
            module.append_record(journal, session_id="session-001", record_type="iteration_accepted", targets=["a"], operations=[{"type": "visibility", "target": "a", "hide_render": False}], before_hash="a", after_hash="b", drift={"status": "pass", "issues": []}, durations_ms={"total": 1})
            failures, _, _, _ = validate_mcp_session(journal)
            self.assertIn("preview_required", {failure.rule_id for failure in failures})
            lines = journal.read_text(encoding="utf-8").splitlines()
            changed = json.loads(lines[0]); changed["details"]["asset_id"] = "tampered"; lines[0] = json.dumps(changed)
            journal.write_text("\n".join(lines) + "\n", encoding="utf-8")
            failures, _, _, _ = validate_mcp_session(journal)
            self.assertIn("record_hash", {failure.rule_id for failure in failures})

    def test_viewport_fallback_and_checkpoint_bundle_contract(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            module, journal = self._start(root)
            edit = module.append_record(journal, session_id="session-001", record_type="iteration_accepted", targets=["a"], operations=[{"type": "visibility", "target": "a", "hide_render": False}], before_hash="a", after_hash="b", drift={"status": "pass", "issues": []}, durations_ms={"total": 1})
            module.append_record(journal, session_id="session-001", record_type="preview_result", targets=["a"], before_hash="b", after_hash="b", durations_ms={"total": 2}, details={"iteration_sequence": edit["sequence"], "preview": {"tool": "eevee_render", "view": "relevant_angle", "dimensions": [512, 512], "timestamp": "2026-07-22T00:00:00+00:00", "status": "rendered_fallback"}})
            artifacts = []
            for index in range(5):
                path = root / f"artifact-{index}.json"; path.write_text("{}", encoding="utf-8"); artifacts.append(str(path))
            task_card = module.read_records(journal)[0]["details"]["task_card"]
            checkpoint = module.append_record(journal, session_id="session-001", record_type="checkpoint_completed", before_hash="b", after_hash="b", durations_ms={"bundle": 10, "total": 12}, details={"artifacts": artifacts, "task_card": task_card})
            module.append_record(journal, session_id="session-001", record_type="session_closed", before_hash="b", after_hash="b", durations_ms={"total": 1}, details={"task_card": task_card, "checkpoint_sequence": checkpoint["sequence"]})
            failures, _, records, measurements = validate_mcp_session(journal)
            self.assertEqual([], failures)
            self.assertEqual(1, measurements["checkpoint_count"])
            self.assertEqual("session_closed", records[-1]["record_type"])

    def test_checkpoint_runner_writes_five_artifacts_in_one_bundle(self):
        module = load_script("checkpoint_bundle")
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)

            class ScreenshotModule:
                @staticmethod
                def collect_report(asset_id, stage_id, screenshot_dir, views, dry_run, **kwargs):
                    screenshot_dir.mkdir(parents=True)
                    manifest = screenshot_dir / f"{asset_id}_{stage_id}_screenshot_manifest.json"
                    manifest.write_text("{}", encoding="utf-8")
                    return {"hard_failures": [], "summary": {"manifest_path": str(manifest)}}

            class ReportModule:
                @staticmethod
                def collect_report(asset_id, stage_id):
                    return {"summary": {"status": "pass"}, "hard_failures": []}

            with mock.patch.object(module, "_load", side_effect=lambda path, name: ScreenshotModule if "screenshot" in path.name else ReportModule):
                result = module.run_checkpoint_bundle(project_root=root, asset_id="asset", stage_id="tertiary_detail", output_dir=root / "checkpoint")
            self.assertEqual(1, result["blender_call_count"])
            self.assertEqual(5, len(result["artifacts"]))
            self.assertTrue(all(Path(path).is_file() for path in result["artifacts"]))

    def test_active_session_task_card_reuses_stage_envelope(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            task = root / "task.md"
            template = (ROOT / "templates/stage_task_card.md").read_text(encoding="utf-8")
            values = {
                "schema_version": "0.3", "task_id": "active-1", "asset_id": "asset", "stage_id": "tertiary_detail", "stage_name": "Tertiary", "created_by": "tester", "created_at": "2026-07-22", "status": "in_progress", "goal": "Refine facial shapes", "current_stage": "tertiary_detail", "allowed_tools": "Blender MCP", "disallowed_tools": "structural changes", "known_constraints": "safe only", "input_refs": "brief", "required_outputs": "working blend", "output_paths": "working.blend", "report_paths": "checkpoint", "screenshot_requirements": "session preview", "handoff_format": "templates/stage_handoff.md", "acceptance_tests": "clean delta", "required_validators": "validate_mcp_session", "manual_review_required": "yes", "hard_failure_checks": "drift", "stop_conditions": "stop on drift", "requires_human_approval": "yes", "do_not_continue_if": "validation fails", "assigned_specialist": "operator", "microtasks": "stage-scoped safe edits", "blocking_issues": "none", "workflow_mode": "active_session", "session_id": "session-001", "authorized_collections": "Face; Details", "safe_change_types": "absolute_transform; visibility; collection_membership; vertex_positions", "max_targets_per_edit": "6", "viewport_preview_policy": "one relevant-angle get_viewport_screenshot; fallback one 512px Eevee render", "checkpoint_triggers": "explicit checkpoint; stage transition; scope expansion; structural work; uncertainty; drift; evidence failure", "pipeline_state": "pipeline_state.json", "session_journal": "mcp_sessions/session-001.jsonl", "source_file": "source.blend", "backup_file": "backup.blend", "working_file": "working.blend", "source_protection_receipt": "protection.json", "execution_authorized_by": "tester", "execution_authorized_at": "2026-07-22",
            }
            for key, value in values.items():
                import re
                template = re.sub(rf"(- `{re.escape(key)}`:)[^\n]*", rf"\1 {value}", template, count=1)
            task.write_text(template, encoding="utf-8")
            failures, _, _, measurements = validate_stage_task_card(task, ROOT)
            self.assertEqual([], failures)
            self.assertEqual("active_session", measurements["workflow_mode"])


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
