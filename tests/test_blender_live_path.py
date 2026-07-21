from __future__ import annotations

import base64
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
from validate_screenshot_manifest import DEFAULT_VIEWS, validate as validate_screenshot_manifest
from validate_stage_task_card import validate as validate_stage_task_card


def load_prepare_module():
    path = ROOT / "skills/blender-mcp-operator/scripts/prepare_working_copy.py"
    spec = importlib.util.spec_from_file_location("prepare_working_copy", path)
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


class ValidatorTests(unittest.TestCase):
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
        png = base64.b64decode(
            "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII="
        )
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "working.blend"
            source.write_bytes(b"fixture")
            items = []
            for view in sorted(DEFAULT_VIEWS):
                image = root / f"{view}.png"
                image.write_bytes(png)
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
