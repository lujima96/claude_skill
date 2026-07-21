#!/usr/bin/env python3
"""Validate a material and texture readiness Markdown report."""

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
    "material_report",
    "texture_manifest",
    "material_slot_count",
    "max_material_slots",
    "material_slot_status",
    "material_naming_status",
    "required_material_families",
    "missing_material_families",
    "texture_sets_present",
    "texture_naming_status",
    "texture_size_status",
    "max_texture_size",
    "missing_textures",
    "channel_packing_policy",
    "channel_packing_status",
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


def none_like(value: str) -> bool:
    return value.strip().lower() in {"", "none", "n/a", "unknown", "pending"}


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

    if fields.get("stage_id") and fields["stage_id"] != "texturing_materials":
        failures.append(CheckResult("texture_stage_required", "Texture readiness reports must use the material stage", f"stage_id is `{fields.get('stage_id')}`", "Set `stage_id` to `texturing_materials`."))

    if fields.get("status") and fields["status"] not in VALID_STATUS:
        failures.append(CheckResult("valid_status", "`status` must be known", f"value is `{fields['status']}`", f"Use one of: {', '.join(sorted(VALID_STATUS))}."))

    if fields.get("decision") and fields["decision"] not in VALID_DECISIONS:
        failures.append(CheckResult("valid_decision", "`decision` must be known", f"value is `{fields['decision']}`", f"Use one of: {', '.join(sorted(VALID_DECISIONS))}."))

    for field in ["texture_sets_present", "hard_failures_present", "blocked_stage_progression"]:
        require_yes_no(failures, fields, field)

    for field in ["material_slot_status", "material_naming_status", "texture_naming_status", "texture_size_status", "channel_packing_status", "godot_texture_paths_status"]:
        value = fields.get(field, "")
        if value and value not in VALID_CHECK_STATUS:
            failures.append(CheckResult("valid_check_status", f"`{field}` must be known", f"value is `{value}`", f"Use one of: {', '.join(sorted(VALID_CHECK_STATUS))}."))

    material_slots = to_float(fields.get("material_slot_count", ""))
    max_slots = to_float(fields.get("max_material_slots", ""))
    if material_slots is None:
        failures.append(CheckResult("material_slot_count_numeric", "`material_slot_count` must be numeric", f"value is `{fields.get('material_slot_count', '')}`", "Set a numeric material slot count."))
    if max_slots is None:
        failures.append(CheckResult("max_material_slots_numeric", "`max_material_slots` must be numeric", f"value is `{fields.get('max_material_slots', '')}`", "Set a numeric material slot budget."))
    if material_slots is not None and max_slots is not None and material_slots > max_slots:
        failures.append(CheckResult("material_slot_budget", "Material slot count exceeds budget", f"{material_slots:g} > {max_slots:g}", "Reduce material slots or raise the approved budget."))

    channel_policy = fields.get("channel_packing_policy", "")
    if channel_policy and channel_policy not in {"declared", "not_required", "unknown"}:
        failures.append(CheckResult("valid_channel_policy", "`channel_packing_policy` must be known", f"value is `{channel_policy}`", "Use `declared`, `not_required`, or `unknown`."))

    blocking_conditions = [
        ("missing_material_families", not none_like(fields.get("missing_material_families", "")), "Required material families are missing."),
        ("missing_texture_sets", fields.get("texture_sets_present", "").lower() == "no", "Texture sets are missing."),
        ("missing_textures", not none_like(fields.get("missing_textures", "")), "Required textures are missing."),
        ("unknown_channel_packing", channel_policy == "unknown", "Channel packing policy is unknown."),
    ]
    for rule_id, condition, message in blocking_conditions:
        if condition:
            failures.append(CheckResult(rule_id, message, message, "Fix the material/texture report before approval."))

    for field in ["material_slot_status", "material_naming_status", "texture_naming_status", "texture_size_status", "channel_packing_status", "godot_texture_paths_status"]:
        if fields.get(field) == "fail":
            failures.append(CheckResult("failed_texture_check", f"`{field}` failed", f"`{field}` is fail", "Resolve the failed check before approval."))

    has_failures_field = fields.get("hard_failures_present", "").lower() == "yes"
    if (failures or has_failures_field) and fields.get("decision") in {"approve", "approve_with_notes"}:
        failures.append(CheckResult("decision_blocks_failures", "Texture reports with hard failures cannot approve progression", f"decision is `{fields.get('decision')}`", "Use `revise` or `block` until failures are fixed."))

    return failures, warnings, fields, {"field_count": len(fields)}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    args = parser.parse_args()

    try:
        failures, warnings, fields, measurements = validate(args.path, args.repo_root)
        print(render_validation_report(validator_name="validate_texture_readiness", validator_version=VERSION, input_path=args.path, repo_root=args.repo_root, asset_id=fields.get("asset_id", ""), stage_id=fields.get("stage_id", ""), failures=failures, warnings=warnings, measurements=measurements))
        return 1 if failures else 0
    except Exception as exc:
        print(f"validator error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
