#!/usr/bin/env python3
"""Validate a stage task card, including Blender MCP execution bounds."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from rules.markdown_fields import (
    CheckResult,
    add_required_field_checks,
    add_stage_check,
    extract_fields,
    parse_list_value,
    read_text,
    render_validation_report,
)

VERSION = "0.2.0"
REQUIRED_FIELDS = [
    "task_id", "asset_id", "stage_id", "stage_name", "created_by", "created_at", "status",
    "goal", "current_stage", "allowed_tools", "disallowed_tools", "known_constraints",
    "input_refs", "required_outputs", "output_paths", "report_paths", "screenshot_requirements",
    "handoff_format", "acceptance_tests", "required_validators", "manual_review_required",
    "hard_failure_checks", "stop_conditions", "requires_human_approval", "do_not_continue_if",
    "assigned_specialist", "microtasks", "blocking_issues",
]
VALID_STATUSES = {"draft", "ready", "in_progress", "review", "approved", "blocked"}
VALID_EVIDENCE_TIERS = {"gate_review", "quick_iteration"}
QUICK_SAFE_CHANGE_TYPES = {"transform", "visibility", "collection_membership", "vertex_positions"}


def none_value(value: str) -> bool:
    return value.strip().lower() in {"", "none", "n/a", "pending"}


def validate(path: Path, repo_root: Path):
    markdown = read_text(path)
    fields = extract_fields(markdown)
    failures: list[CheckResult] = []
    warnings: list[CheckResult] = []
    add_required_field_checks(failures, fields, REQUIRED_FIELDS)
    add_stage_check(failures, fields, "stage_id")
    add_stage_check(failures, fields, "current_stage")

    if fields.get("status") and fields["status"] not in VALID_STATUSES:
        failures.append(CheckResult("valid_status", "`status` must be known", fields["status"], f"Use one of: {', '.join(sorted(VALID_STATUSES))}."))
    if fields.get("stage_id") and fields.get("current_stage") and fields["stage_id"] != fields["current_stage"]:
        failures.append(CheckResult("stage_consistency", "`stage_id` and `current_stage` must match", f"{fields['stage_id']} != {fields['current_stage']}", "Use the same canonical stage ID."))
    for field in ("manual_review_required", "requires_human_approval"):
        if fields.get(field, "").lower() not in {"yes", "no"}:
            failures.append(CheckResult("yes_no_field", f"`{field}` must be yes or no", fields.get(field, ""), f"Set `{field}` to `yes` or `no`."))

    is_mcp = "mcp" in fields.get("allowed_tools", "").lower()
    if is_mcp:
        for field in ("mcp_microtask_id", "target_objects", "allowed_change_types"):
            if none_value(fields.get(field, "")):
                failures.append(CheckResult("mcp_scope_required", f"`{field}` is required for Blender MCP work", fields.get(field, ""), f"Define `{field}` before execution."))
        microtasks = parse_list_value(fields.get("microtasks", ""))
        if len(microtasks) != 1:
            failures.append(CheckResult("single_microtask", "A Blender MCP task card must contain exactly one semicolon-delimited microtask", fields.get("microtasks", ""), "Keep one bounded microtask in the task card."))
        if fields.get("status") in {"ready", "in_progress", "review", "approved"}:
            for field in ("execution_authorized_by", "execution_authorized_at"):
                if none_value(fields.get(field, "")):
                    failures.append(CheckResult("execution_authorization", f"`{field}` is required before MCP execution", fields.get(field, ""), f"Record `{field}` before changing Blender."))
        evidence_tier = fields.get("evidence_tier", "gate_review") or "gate_review"
        if evidence_tier not in VALID_EVIDENCE_TIERS:
            failures.append(CheckResult("valid_evidence_tier", "`evidence_tier` must be known", evidence_tier, "Use `gate_review` or `quick_iteration`."))
        if "evidence_tier" not in fields:
            warnings.append(CheckResult("legacy_gate_tier", "MCP task omits `evidence_tier` and defaults to gate_review", fields.get("task_id", ""), "Add the explicit evidence tier when revising this task.", "warning"))
        if evidence_tier == "quick_iteration":
            for field in ("iteration_budget", "iteration_views"):
                if none_value(fields.get(field, "")):
                    failures.append(CheckResult("quick_iteration_contract", f"`{field}` is required for quick iteration", fields.get(field, ""), f"Define `{field}`."))
            try:
                budget = int(fields.get("iteration_budget", "0"))
            except ValueError:
                budget = 0
            if not 1 <= budget <= 3:
                failures.append(CheckResult("iteration_budget", "Quick iteration budget must be 1-3", fields.get("iteration_budget", ""), "Use a maximum of three iterations before gate review."))
            targets = parse_list_value(fields.get("target_objects", ""))
            if not 1 <= len(set(targets)) <= 6:
                failures.append(CheckResult("target_budget", "Quick iteration requires 1-6 unique targets", fields.get("target_objects", ""), "Reduce the regional target allowlist."))
            change_types = set(parse_list_value(fields.get("allowed_change_types", "")))
            unsafe = sorted(change_types - QUICK_SAFE_CHANGE_TYPES)
            if unsafe:
                failures.append(CheckResult("quick_safe_changes", "Quick iteration contains unsafe change types", ", ".join(unsafe), "Use only transform, visibility, collection_membership, or vertex_positions; otherwise use gate_review."))
            views = set(parse_list_value(fields.get("iteration_views", "")))
            if not {"front", "three_quarter"}.issubset(views):
                failures.append(CheckResult("quick_views", "Quick iteration requires front and three_quarter views", fields.get("iteration_views", ""), "Add both quick preview views."))

    return failures, warnings, fields, {"field_count": len(fields), "mcp_task": is_mcp, "evidence_tier": fields.get("evidence_tier", "gate_review") if is_mcp else "not_applicable"}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    try:
        failures, warnings, fields, measurements = validate(args.path, args.repo_root)
        print(render_validation_report(
            validator_name="validate_stage_task_card", validator_version=VERSION,
            input_path=args.path, repo_root=args.repo_root, asset_id=fields.get("asset_id", ""),
            stage_id=fields.get("stage_id", ""), failures=failures, warnings=warnings,
            measurements=measurements,
        ))
        return 1 if failures else 0
    except Exception as exc:
        print(f"validator error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
