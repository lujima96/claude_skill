#!/usr/bin/env python3
"""Validate an optimization and LOD readiness Markdown report."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from rules.markdown_fields import CheckResult, add_required_field_checks, add_stage_check, extract_fields, read_text, render_validation_report, to_float

VERSION = "0.1.0"

REQUIRED_FIELDS = [
    "report_id",
    "asset_id",
    "stage_id",
    "created_by",
    "created_at",
    "status",
    "asset_manifest",
    "mesh_report",
    "material_report",
    "export_package_report",
    "target_platform",
    "lod_count",
    "lod_naming_status",
    "lod_polycount_status",
    "lod0_triangle_budget",
    "material_slot_status",
    "texture_memory_status",
    "glb_or_gltf_present",
    "package_completeness_status",
    "required_meshes_present",
    "required_materials_present",
    "required_textures_present",
    "required_skeleton_present",
    "required_animations_present",
    "godot_texture_paths_status",
    "hard_failures_present",
    "hard_failures",
    "blocked_stage_progression",
    "decision",
    "decision_reason",
    "required_next_actions",
]

VALID_DECISIONS = {"approve", "approve_with_notes", "revise", "block"}
VALID_STATUS = {"draft", "pass", "warning", "blocked"}
VALID_CHECK_STATUS = {"pass", "warning", "fail", "unknown"}


def require_yes_no(failures: list[CheckResult], fields: dict[str, str], field: str) -> None:
    value = fields.get(field, "").lower()
    if value not in {"yes", "no"}:
        failures.append(CheckResult("yes_no_field", f"`{field}` must be yes or no", f"value is `{fields.get(field, '')}`", f"Set `{field}` to `yes` or `no`."))


def validate(path: Path, repo_root: Path) -> tuple[list[CheckResult], list[CheckResult], dict[str, str], dict[str, object]]:
    markdown = read_text(path)
    fields = extract_fields(markdown)
    failures: list[CheckResult] = []
    warnings: list[CheckResult] = []

    add_required_field_checks(failures, fields, REQUIRED_FIELDS)
    add_stage_check(failures, fields, "stage_id")

    if fields.get("stage_id") and fields["stage_id"] != "optimization_lods":
        failures.append(CheckResult("optimization_stage_required", "LOD readiness reports must use the optimization stage", f"stage_id is `{fields.get('stage_id')}`", "Set `stage_id` to `optimization_lods`."))

    if fields.get("status") and fields["status"] not in VALID_STATUS:
        failures.append(CheckResult("valid_status", "`status` must be known", f"value is `{fields['status']}`", f"Use one of: {', '.join(sorted(VALID_STATUS))}."))

    if fields.get("decision") and fields["decision"] not in VALID_DECISIONS:
        failures.append(CheckResult("valid_decision", "`decision` must be known", f"value is `{fields['decision']}`", f"Use one of: {', '.join(sorted(VALID_DECISIONS))}."))

    for field in ["glb_or_gltf_present", "hard_failures_present", "blocked_stage_progression"]:
        require_yes_no(failures, fields, field)

    for field in ["lod_naming_status", "lod_polycount_status", "material_slot_status", "texture_memory_status", "package_completeness_status", "godot_texture_paths_status"]:
        value = fields.get(field, "")
        if value and value not in VALID_CHECK_STATUS:
            failures.append(CheckResult("valid_check_status", f"`{field}` must be known", f"value is `{value}`", f"Use one of: {', '.join(sorted(VALID_CHECK_STATUS))}."))

    for field in ["required_meshes_present", "required_materials_present", "required_textures_present", "required_skeleton_present"]:
        value = fields.get(field, "")
        if value and value not in {"yes", "no", "unknown"}:
            failures.append(CheckResult("valid_presence_state", f"`{field}` must be yes, no, or unknown", f"value is `{value}`", "Use `yes`, `no`, or `unknown`."))

    animations = fields.get("required_animations_present", "")
    if animations and animations not in {"yes", "no", "not_required", "unknown"}:
        failures.append(CheckResult("valid_animation_state", "`required_animations_present` must be yes, no, not_required, or unknown", f"value is `{animations}`", "Use `yes`, `no`, `not_required`, or `unknown`."))

    lod_count = to_float(fields.get("lod_count", ""))
    lod0_budget = to_float(fields.get("lod0_triangle_budget", ""))
    if lod_count is None:
        failures.append(CheckResult("lod_count_numeric", "`lod_count` must be numeric", f"value is `{fields.get('lod_count', '')}`", "Set a numeric LOD count."))
    if lod0_budget is None:
        failures.append(CheckResult("lod0_budget_numeric", "`lod0_triangle_budget` must be numeric", f"value is `{fields.get('lod0_triangle_budget', '')}`", "Set a numeric LOD0 triangle budget."))

    blocking_conditions = [
        ("missing_package", fields.get("glb_or_gltf_present", "").lower() == "no", "GLB/glTF package is missing."),
        ("missing_lods", lod_count == 0, "LOD count is zero."),
        ("missing_meshes", fields.get("required_meshes_present") == "no", "Required meshes are missing."),
        ("missing_materials", fields.get("required_materials_present") == "no", "Required materials are missing."),
        ("missing_textures", fields.get("required_textures_present") == "no", "Required textures are missing."),
        ("missing_skeleton", fields.get("required_skeleton_present") == "no", "Required skeleton is missing."),
    ]
    for rule_id, condition, message in blocking_conditions:
        if condition:
            failures.append(CheckResult(rule_id, message, message, "Fix the optimization/package report before approval."))

    for field in ["lod_naming_status", "lod_polycount_status", "material_slot_status", "texture_memory_status", "package_completeness_status", "godot_texture_paths_status"]:
        if fields.get(field) == "fail":
            failures.append(CheckResult("failed_optimization_check", f"`{field}` failed", f"`{field}` is fail", "Resolve the failed check before approval."))

    has_failures_field = fields.get("hard_failures_present", "").lower() == "yes"
    if (failures or has_failures_field) and fields.get("decision") in {"approve", "approve_with_notes"}:
        failures.append(CheckResult("decision_blocks_failures", "LOD reports with hard failures cannot approve progression", f"decision is `{fields.get('decision')}`", "Use `revise` or `block` until failures are fixed."))

    return failures, warnings, fields, {"field_count": len(fields)}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    args = parser.parse_args()

    try:
        failures, warnings, fields, measurements = validate(args.path, args.repo_root)
        print(render_validation_report(validator_name="validate_lod_readiness", validator_version=VERSION, input_path=args.path, repo_root=args.repo_root, asset_id=fields.get("asset_id", ""), stage_id=fields.get("stage_id", ""), failures=failures, warnings=warnings, measurements=measurements))
        return 1 if failures else 0
    except Exception as exc:
        print(f"validator error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
