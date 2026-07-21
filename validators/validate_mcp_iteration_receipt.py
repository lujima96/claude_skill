#!/usr/bin/env python3
"""Validate a compact Blender MCP quick-iteration scene-delta receipt."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

from rules.markdown_fields import CheckResult, render_validation_report
from validate_screenshot_manifest import validate as validate_screenshot_manifest


VERSION = "0.1.0"
SAFE_CHANGE_TYPES = {"transform", "visibility", "collection_membership", "vertex_positions"}
REQUIRED_FIELDS = {
    "receipt_version", "evidence_tier", "created_at", "asset_id", "stage_id", "microtask_id",
    "iteration_id", "iteration_index", "target_objects", "allowed_change_types", "changed_objects",
    "unexpected_changed_objects", "missing_objects", "added_objects", "topology_count_changes",
    "material_changes", "protected_objects_checked", "destructive_operations", "hard_failures",
    "source_file", "backup_file", "working_file", "source_sha256_before", "source_sha256_after",
    "backup_sha256", "working_sha256_before", "working_sha256_after", "screenshot_manifest",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate(path: Path):
    data = json.loads(path.read_text(encoding="utf-8"))
    failures: list[CheckResult] = []
    warnings: list[CheckResult] = []
    for field in sorted(REQUIRED_FIELDS - set(data)):
        failures.append(CheckResult("required_field", f"`{field}` is required", "missing", f"Add `{field}` to the receipt."))

    if data.get("evidence_tier") != "quick_iteration":
        failures.append(CheckResult("quick_tier_required", "Receipt must use quick_iteration", str(data.get("evidence_tier")), "Set the correct evidence tier."))
    targets = data.get("target_objects", [])
    if not isinstance(targets, list) or not 1 <= len(set(targets)) <= 6:
        failures.append(CheckResult("target_budget", "Quick iterations require 1-6 unique targets", str(targets), "Reduce and deduplicate the target allowlist."))
    try:
        index = int(data.get("iteration_index", 0))
    except (TypeError, ValueError):
        index = 0
    if not 1 <= index <= 3:
        failures.append(CheckResult("iteration_budget", "Quick iteration index must be 1-3", str(data.get("iteration_index")), "Run a gate review after three iterations."))

    change_types = set(data.get("allowed_change_types", []))
    unsafe = sorted(change_types - SAFE_CHANGE_TYPES)
    if unsafe:
        failures.append(CheckResult("safe_change_types", "Quick iteration contains unsafe change types", ", ".join(unsafe), "Escalate to gate_review."))
    for field in ("unexpected_changed_objects", "missing_objects", "added_objects", "topology_count_changes", "hard_failures"):
        if data.get(field):
            failures.append(CheckResult("clean_delta_required", f"`{field}` must be empty", str(data.get(field)), "Rollback or escalate to gate_review."))
    if data.get("material_changes") is not False:
        failures.append(CheckResult("no_material_changes", "Quick iteration cannot change materials", str(data.get("material_changes")), "Rollback or use gate_review."))
    if data.get("destructive_operations") is not False:
        failures.append(CheckResult("no_destructive_operations", "Quick iteration cannot be destructive", str(data.get("destructive_operations")), "Rollback and use an explicitly approved gate task."))
    changed = set(data.get("changed_objects", []))
    if not changed:
        warnings.append(CheckResult("no_effect", "Quick iteration changed no objects", "changed_objects is empty", "Skip or explain the no-op iteration.", "warning"))
    if changed - set(targets):
        failures.append(CheckResult("target_allowlist", "Changed objects must be targets", str(sorted(changed - set(targets))), "Rollback unexpected drift."))

    paths = {name: Path(data.get(name, "")).expanduser() for name in ("source_file", "backup_file", "working_file")}
    if len({str(item.resolve()) for item in paths.values()}) != 3:
        failures.append(CheckResult("distinct_paths", "Source, backup, and working paths must be distinct", str(paths), "Use protected distinct files."))
    for name, artifact in paths.items():
        if not artifact.is_file():
            failures.append(CheckResult("artifact_exists", f"`{name}` must exist", str(artifact), "Restore the protected artifact."))
    if all(item.is_file() for item in paths.values()):
        actual = {name: sha256(item) for name, item in paths.items()}
        if data.get("source_sha256_before") != actual["source_file"] or data.get("source_sha256_after") != actual["source_file"]:
            failures.append(CheckResult("source_unchanged", "Source hash must remain unchanged", actual["source_file"], "Do not edit the source file."))
        if data.get("backup_sha256") != actual["backup_file"]:
            failures.append(CheckResult("backup_hash", "Backup hash must match", actual["backup_file"], "Restore the verified backup."))
        if data.get("working_sha256_after") != actual["working_file"]:
            failures.append(CheckResult("working_hash", "Working after-hash must match", actual["working_file"], "Regenerate the receipt after saving."))

    manifest = Path(data.get("screenshot_manifest", "")).expanduser()
    if not manifest.is_file():
        failures.append(CheckResult("screenshot_manifest", "Quick screenshot manifest must exist", str(manifest), "Capture front and three-quarter previews."))
    else:
        shot_failures, _, shot_data, _ = validate_screenshot_manifest(manifest, {"front", "three_quarter"})
        failures.extend(CheckResult("quick_screenshots", item.rule, item.evidence, item.fix) for item in shot_failures)
        if paths["working_file"].is_file() and Path(shot_data.get("source_file", "")).resolve() != paths["working_file"].resolve():
            failures.append(CheckResult("screenshot_source", "Screenshots must target the working file", str(shot_data.get("source_file")), "Recapture from the current working file."))

    measurements = {
        "target_count": len(targets) if isinstance(targets, list) else 0,
        "changed_object_count": len(changed),
        "protected_objects_checked": data.get("protected_objects_checked", 0),
        "iteration_index": index,
    }
    return failures, warnings, data, measurements


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    try:
        failures, warnings, data, measurements = validate(args.path)
        print(render_validation_report(
            validator_name="validate_mcp_iteration_receipt", validator_version=VERSION,
            input_path=args.path, repo_root=args.repo_root, asset_id=data.get("asset_id", ""),
            stage_id=data.get("stage_id", ""), failures=failures, warnings=warnings,
            measurements=measurements,
        ))
        return 1 if failures else 0
    except Exception as exc:
        print(f"validator error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
