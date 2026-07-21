#!/usr/bin/env python3
"""Validate a UV bake readiness Markdown report."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from rules.markdown_fields import (
    CheckResult,
    add_required_field_checks,
    add_stage_check,
    extract_fields,
    read_text,
    render_validation_report,
)

VERSION = "0.1.0"

REQUIRED_FIELDS = [
    "report_id",
    "asset_id",
    "stage_id",
    "created_by",
    "created_at",
    "status",
    "retopo_mesh",
    "high_poly_source",
    "uv_sets_present",
    "required_uv_sets",
    "overlap_policy",
    "disallowed_overlaps_present",
    "texel_density_target",
    "texel_density_status",
    "padding_target_pixels",
    "padding_status",
    "bake_pairing_defined",
    "cage_strategy",
    "required_maps",
    "baked_maps_present",
    "bake_artifacts_present",
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
        failures.append(
            CheckResult(
                "yes_no_field",
                f"`{field}` must be yes or no",
                f"value is `{fields.get(field, '')}`",
                f"Set `{field}` to `yes` or `no`.",
            )
        )


def validate(path: Path, repo_root: Path) -> tuple[list[CheckResult], list[CheckResult], dict[str, str], dict[str, object]]:
    markdown = read_text(path)
    fields = extract_fields(markdown)
    failures: list[CheckResult] = []
    warnings: list[CheckResult] = []

    add_required_field_checks(failures, fields, REQUIRED_FIELDS)
    add_stage_check(failures, fields, "stage_id")

    if fields.get("stage_id") and fields["stage_id"] != "uvs_and_baking":
        failures.append(
            CheckResult(
                "uv_stage_required",
                "UV bake readiness reports must use the UV/bake stage",
                f"stage_id is `{fields.get('stage_id')}`",
                "Set `stage_id` to `uvs_and_baking`.",
            )
        )

    if fields.get("status") and fields["status"] not in VALID_STATUS:
        failures.append(CheckResult("valid_status", "`status` must be known", f"value is `{fields['status']}`", f"Use one of: {', '.join(sorted(VALID_STATUS))}."))

    if fields.get("decision") and fields["decision"] not in VALID_DECISIONS:
        failures.append(CheckResult("valid_decision", "`decision` must be known", f"value is `{fields['decision']}`", f"Use one of: {', '.join(sorted(VALID_DECISIONS))}."))

    for field in ["uv_sets_present", "bake_pairing_defined", "hard_failures_present", "blocked_stage_progression"]:
        require_yes_no(failures, fields, field)

    for field in ["texel_density_status", "padding_status"]:
        value = fields.get(field, "")
        if value and value not in VALID_CHECK_STATUS:
            failures.append(CheckResult("valid_check_status", f"`{field}` must be known", f"value is `{value}`", f"Use one of: {', '.join(sorted(VALID_CHECK_STATUS))}."))

    overlap_policy = fields.get("overlap_policy", "")
    if overlap_policy and overlap_policy not in {"allowed", "disallowed", "partial", "unknown"}:
        failures.append(
            CheckResult(
                "valid_overlap_policy",
                "`overlap_policy` must be known",
                f"value is `{overlap_policy}`",
                "Use `allowed`, `disallowed`, `partial`, or `unknown`.",
            )
        )

    overlaps = fields.get("disallowed_overlaps_present", "")
    if overlaps and overlaps not in {"yes", "no", "unknown"}:
        failures.append(CheckResult("valid_overlap_state", "`disallowed_overlaps_present` must be yes, no, or unknown", f"value is `{overlaps}`", "Use `yes`, `no`, or `unknown`."))

    bake_artifacts = fields.get("bake_artifacts_present", "")
    if bake_artifacts and bake_artifacts not in {"yes", "no", "unknown"}:
        failures.append(CheckResult("valid_artifact_state", "`bake_artifacts_present` must be yes, no, or unknown", f"value is `{bake_artifacts}`", "Use `yes`, `no`, or `unknown`."))

    blocking_conditions = [
        ("missing_uvs", fields.get("uv_sets_present", "").lower() == "no", "Required UV sets are missing."),
        ("missing_overlap_policy", overlap_policy == "unknown", "UV overlap policy is unknown."),
        ("disallowed_overlaps", overlaps == "yes", "Disallowed UV overlaps are present."),
        ("missing_bake_pairing", fields.get("bake_pairing_defined", "").lower() == "no", "Bake source/target pairing is missing."),
        ("missing_required_maps", none_like(fields.get("required_maps", "")), "Required baked maps are not declared."),
        ("bake_artifacts", bake_artifacts == "yes", "Bake artifacts are present."),
    ]
    for rule_id, condition, message in blocking_conditions:
        if condition:
            failures.append(CheckResult(rule_id, message, message, "Fix the UV/bake report before approval."))

    has_failures_field = fields.get("hard_failures_present", "").lower() == "yes"
    if (failures or has_failures_field) and fields.get("decision") in {"approve", "approve_with_notes"}:
        failures.append(
            CheckResult(
                "decision_blocks_failures",
                "UV bake reports with hard failures cannot approve progression",
                f"decision is `{fields.get('decision')}`",
                "Use `revise` or `block` until failures are fixed.",
            )
        )

    return failures, warnings, fields, {"field_count": len(fields)}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    args = parser.parse_args()

    try:
        failures, warnings, fields, measurements = validate(args.path, args.repo_root)
        print(render_validation_report(validator_name="validate_uv_bake_readiness", validator_version=VERSION, input_path=args.path, repo_root=args.repo_root, asset_id=fields.get("asset_id", ""), stage_id=fields.get("stage_id", ""), failures=failures, warnings=warnings, measurements=measurements))
        return 1 if failures else 0
    except Exception as exc:
        print(f"validator error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
