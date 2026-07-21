#!/usr/bin/env python3
"""Validate a Godot import validation Markdown report."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from rules.markdown_fields import CheckResult, add_required_field_checks, add_stage_check, extract_fields, read_text, render_validation_report

VERSION = "0.1.0"

REQUIRED_FIELDS = [
    "report_id", "asset_id", "stage_id", "created_by", "created_at", "status", "godot_version",
    "asset_manifest", "glb_or_gltf", "godot_project", "imported_scene", "preview_scene", "export_package_report",
    "import_succeeded", "scene_opens", "root_node_name", "mesh_count_matches_manifest",
    "material_slots_match_manifest", "texture_paths_resolve", "lod_policy_documented",
    "skeleton3d_expected", "skeleton3d_present", "bone_names_stable", "skin_weights_present",
    "animations_expected", "animations_imported", "animations_play_in_preview",
    "blend_shapes_expected", "blend_shapes_imported", "markers_expected", "markers_present",
    "collision_expected", "collision_present", "preview_renders", "preview_screenshot",
    "hard_failures_present", "hard_failures", "blocked_stage_progression", "decision",
    "decision_reason", "required_next_actions",
]

VALID_DECISIONS = {"approve", "approve_with_notes", "revise", "block"}
VALID_STATUS = {"draft", "pass", "warning", "blocked"}


def check_value(failures: list[CheckResult], fields: dict[str, str], field: str, allowed: set[str]) -> None:
    value = fields.get(field, "")
    if value and value not in allowed:
        failures.append(CheckResult("valid_state", f"`{field}` has an invalid value", f"value is `{value}`", f"Use one of: {', '.join(sorted(allowed))}."))


def validate(path: Path, repo_root: Path) -> tuple[list[CheckResult], list[CheckResult], dict[str, str], dict[str, object]]:
    markdown = read_text(path)
    fields = extract_fields(markdown)
    failures: list[CheckResult] = []
    warnings: list[CheckResult] = []

    add_required_field_checks(failures, fields, REQUIRED_FIELDS)
    add_stage_check(failures, fields, "stage_id")

    if fields.get("stage_id") and fields["stage_id"] != "export_godot_validation":
        failures.append(CheckResult("godot_stage_required", "Godot validation reports must use export stage", f"stage_id is `{fields.get('stage_id')}`", "Set `stage_id` to `export_godot_validation`."))
    if fields.get("status") and fields["status"] not in VALID_STATUS:
        failures.append(CheckResult("valid_status", "`status` must be known", f"value is `{fields['status']}`", f"Use one of: {', '.join(sorted(VALID_STATUS))}."))
    if fields.get("decision") and fields["decision"] not in VALID_DECISIONS:
        failures.append(CheckResult("valid_decision", "`decision` must be known", f"value is `{fields['decision']}`", f"Use one of: {', '.join(sorted(VALID_DECISIONS))}."))

    yes_no = {"yes", "no"}
    yes_no_unknown = {"yes", "no", "unknown"}
    yes_no_not_required_unknown = {"yes", "no", "not_required", "unknown"}
    for field in ["import_succeeded", "scene_opens", "lod_policy_documented", "skeleton3d_expected", "animations_expected", "blend_shapes_expected", "markers_expected", "collision_expected", "preview_renders", "hard_failures_present", "blocked_stage_progression"]:
        check_value(failures, fields, field, yes_no)
    for field in ["mesh_count_matches_manifest", "material_slots_match_manifest", "texture_paths_resolve"]:
        check_value(failures, fields, field, yes_no_unknown)
    for field in ["skeleton3d_present", "bone_names_stable", "skin_weights_present", "animations_imported", "animations_play_in_preview", "blend_shapes_imported", "markers_present", "collision_present"]:
        check_value(failures, fields, field, yes_no_not_required_unknown)

    blocking = [
        ("import_failed", fields.get("import_succeeded") == "no", "Godot import failed."),
        ("scene_does_not_open", fields.get("scene_opens") == "no", "Imported scene does not open."),
        ("textures_missing", fields.get("texture_paths_resolve") == "no", "Texture paths do not resolve."),
        ("preview_missing", fields.get("preview_renders") == "no", "Preview scene does not render."),
        ("lod_policy_missing", fields.get("lod_policy_documented") == "no", "LOD policy is not documented."),
    ]
    if fields.get("skeleton3d_expected") == "yes" and fields.get("skeleton3d_present") != "yes":
        blocking.append(("skeleton_missing", True, "Expected Skeleton3D is missing."))
    if fields.get("animations_expected") == "yes" and (fields.get("animations_imported") != "yes" or fields.get("animations_play_in_preview") != "yes"):
        blocking.append(("animations_missing", True, "Expected animations are missing or cannot play."))
    if fields.get("blend_shapes_expected") == "yes" and fields.get("blend_shapes_imported") != "yes":
        blocking.append(("blend_shapes_missing", True, "Expected blend shapes are missing."))
    if fields.get("markers_expected") == "yes" and fields.get("markers_present") != "yes":
        blocking.append(("markers_missing", True, "Expected markers are missing."))
    if fields.get("collision_expected") == "yes" and fields.get("collision_present") != "yes":
        blocking.append(("collision_missing", True, "Expected collision nodes are missing."))

    for rule_id, condition, message in blocking:
        if condition:
            failures.append(CheckResult(rule_id, message, message, "Fix the Godot validation report before final approval."))

    if (failures or fields.get("hard_failures_present") == "yes") and fields.get("decision") in {"approve", "approve_with_notes"}:
        failures.append(CheckResult("decision_blocks_failures", "Godot reports with hard failures cannot approve progression", f"decision is `{fields.get('decision')}`", "Use `revise` or `block` until failures are fixed."))

    return failures, warnings, fields, {"field_count": len(fields)}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    try:
        failures, warnings, fields, measurements = validate(args.path, args.repo_root)
        print(render_validation_report(validator_name="validate_godot_validation", validator_version=VERSION, input_path=args.path, repo_root=args.repo_root, asset_id=fields.get("asset_id", ""), stage_id=fields.get("stage_id", ""), failures=failures, warnings=warnings, measurements=measurements))
        return 1 if failures else 0
    except Exception as exc:
        print(f"validator error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
