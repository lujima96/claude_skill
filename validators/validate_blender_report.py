#!/usr/bin/env python3
"""Validate Blender JSON report structure and internal status consistency."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from rules.markdown_fields import CheckResult, VALID_STAGE_IDS, render_validation_report

VERSION = "0.1.0"


def validate(path: Path, expected_asset_id: str | None, expected_stage_id: str | None, expected_source: Path | None):
    data = json.loads(path.read_text(encoding="utf-8"))
    failures: list[CheckResult] = []
    warnings: list[CheckResult] = []
    metadata = data.get("metadata", {})
    summary = data.get("summary", {})
    required_metadata = {
        "report_type", "asset_id", "stage_id", "created_at", "script_version", "blender_version",
        "source_file", "source_read_only", "writes_artifacts",
    }
    for field in sorted(required_metadata - metadata.keys()):
        failures.append(CheckResult("required_metadata", f"metadata `{field}` is required", "missing", f"Add `{field}` to report metadata."))
    stage_id = metadata.get("stage_id", "")
    if stage_id not in VALID_STAGE_IDS:
        failures.append(CheckResult("valid_stage_id", "Report stage must be canonical", stage_id, "Use a canonical pipeline stage ID."))
    if metadata.get("source_read_only") is not True:
        failures.append(CheckResult("source_read_only", "Evidence scripts must not save or overwrite the source .blend", str(metadata.get("source_read_only")), "Set source_read_only only after preserving source state."))
    warning_count = len(data.get("warnings", []))
    hard_failure_count = len(data.get("hard_failures", []))
    expected_status = "fail" if hard_failure_count else ("warning" if warning_count else "pass")
    for field, expected in (("warning_count", warning_count), ("hard_failure_count", hard_failure_count), ("status", expected_status)):
        if summary.get(field) != expected:
            failures.append(CheckResult("summary_consistency", f"summary `{field}` is inconsistent", f"reported {summary.get(field)!r}, expected {expected!r}", "Regenerate the report with the current reporting library."))
    if expected_asset_id and metadata.get("asset_id") != expected_asset_id:
        failures.append(CheckResult("asset_match", "Report asset ID must match expected asset", str(metadata.get("asset_id")), f"Use `{expected_asset_id}`."))
    if expected_stage_id and stage_id != expected_stage_id:
        failures.append(CheckResult("stage_match", "Report stage must match expected stage", stage_id, f"Use `{expected_stage_id}`."))
    if expected_source and Path(metadata.get("source_file", "")).resolve() != expected_source.resolve():
        failures.append(CheckResult("source_match", "Report source must match the protected working file", str(metadata.get("source_file")), str(expected_source.resolve())))
    if metadata.get("report_type") == "screenshot_set":
        measurements = data.get("measurements", {})
        items = data.get("items", [])
        if measurements.get("scene_state_restored") != "yes":
            failures.append(CheckResult("scene_state_restored", "Screenshot capture must restore temporary Blender state", str(measurements.get("scene_state_restored")), "Fix restoration before using the evidence."))
        if summary.get("captured_count") != summary.get("screenshot_count") or any(item.get("status") != "captured" for item in items):
            failures.append(CheckResult("complete_screenshot_report", "Every screenshot report item must be captured", str(summary), "Regenerate the complete screenshot set."))
        manifest_path = Path(str(summary.get("manifest_path", "")))
        if not manifest_path.is_file():
            failures.append(CheckResult("manifest_exists", "Screenshot report manifest must exist", str(manifest_path), "Write and validate the manifest."))
    return failures, warnings, metadata, {
        "report_type": metadata.get("report_type", "unknown"),
        "warning_count": warning_count,
        "hard_failure_count": hard_failure_count,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--expected-asset-id")
    parser.add_argument("--expected-stage-id")
    parser.add_argument("--expected-source", type=Path)
    args = parser.parse_args()
    try:
        failures, warnings, metadata, measurements = validate(args.path, args.expected_asset_id, args.expected_stage_id, args.expected_source)
        print(render_validation_report(
            validator_name="validate_blender_report", validator_version=VERSION, input_path=args.path,
            repo_root=args.repo_root, asset_id=str(metadata.get("asset_id", "")), stage_id=str(metadata.get("stage_id", "")),
            failures=failures, warnings=warnings, measurements=measurements,
        ))
        return 1 if failures else 0
    except Exception as exc:
        print(f"validator error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
