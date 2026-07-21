#!/usr/bin/env python3
"""Validate a Blender MCP action log Markdown document."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from rules.markdown_fields import (
    CheckResult,
    add_required_field_checks,
    add_stage_check,
    extract_fields,
    parse_markdown_table,
    read_text,
    render_validation_report,
)

VERSION = "0.1.0"

REQUIRED_FIELDS = [
    "log_id",
    "asset_id",
    "stage_id",
    "microtask_id",
    "created_by",
    "created_at",
    "status",
    "execution_mode",
    "task_card",
    "specialist_owner",
    "microtask_goal",
    "allowed_tools",
    "disallowed_tools",
    "acceptance_tests",
    "stop_conditions",
    "source_file",
    "backup_file",
    "working_file",
    "backup_verified",
    "destructive_operations_requested",
    "destructive_operations_approved_by",
    "destructive_operations_approved_at",
    "screenshots",
    "blender_reports",
    "validation_reports",
    "specialist_review",
    "qa_audit",
    "structural_change_made",
    "hard_failures_present",
    "blocked_stage_progression",
    "rollback_required",
    "rollback_artifact",
    "decision",
    "decision_reason",
    "human_approval_required",
    "approved_by",
    "approved_at",
]

VALID_STATUSES = {"draft", "executed", "approved", "rejected", "rolled_back", "blocked"}
VALID_EXECUTION_MODES = {"real_mcp", "dry_run", "example"}
VALID_DECISIONS = {"approved", "rejected", "rolled_back", "blocked"}
BROAD_GOAL_PHRASES = {
    "finish the character",
    "finish the whole character",
    "complete the character",
    "fix the model",
    "make it better",
    "finish model",
    "complete model",
}


def yes_no_check(
    failures: list[CheckResult],
    fields: dict[str, str],
    field: str,
) -> None:
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


def value_is_none(value: str) -> bool:
    return value.strip().lower() in {"", "none", "n/a", "pending"}


def validate(path: Path, repo_root: Path) -> tuple[list[CheckResult], list[CheckResult], dict[str, str], dict[str, object]]:
    markdown = read_text(path)
    fields = extract_fields(markdown)
    failures: list[CheckResult] = []
    warnings: list[CheckResult] = []

    add_required_field_checks(failures, fields, REQUIRED_FIELDS)
    add_stage_check(failures, fields, "stage_id")

    if fields.get("status") and fields["status"] not in VALID_STATUSES:
        failures.append(
            CheckResult(
                "valid_status",
                "`status` must be known",
                f"value is `{fields['status']}`",
                f"Use one of: {', '.join(sorted(VALID_STATUSES))}.",
            )
        )

    if fields.get("execution_mode") and fields["execution_mode"] not in VALID_EXECUTION_MODES:
        failures.append(
            CheckResult(
                "valid_execution_mode",
                "`execution_mode` must be known",
                f"value is `{fields['execution_mode']}`",
                f"Use one of: {', '.join(sorted(VALID_EXECUTION_MODES))}.",
            )
        )

    if fields.get("decision") and fields["decision"] not in VALID_DECISIONS:
        failures.append(
            CheckResult(
                "valid_decision",
                "`decision` must be known",
                f"value is `{fields['decision']}`",
                f"Use one of: {', '.join(sorted(VALID_DECISIONS))}.",
            )
        )

    for field in [
        "backup_verified",
        "destructive_operations_requested",
        "structural_change_made",
        "hard_failures_present",
        "blocked_stage_progression",
        "rollback_required",
        "human_approval_required",
    ]:
        yes_no_check(failures, fields, field)

    goal = fields.get("microtask_goal", "").lower()
    if any(phrase in goal for phrase in BROAD_GOAL_PHRASES):
        failures.append(
            CheckResult(
                "bounded_microtask",
                "MCP goal must be one bounded microtask",
                f"goal is `{fields.get('microtask_goal', '')}`",
                "Replace broad wording with one specific, reviewable edit.",
            )
        )

    if fields.get("backup_verified", "").lower() != "yes":
        failures.append(
            CheckResult(
                "source_backup_required",
                "Source backup must be verified before MCP edits",
                f"backup_verified is `{fields.get('backup_verified', '')}`",
                "Copy the source file, set `backup_file`, and set `backup_verified: yes`.",
            )
        )

    if fields.get("source_file") and fields.get("working_file") and fields["source_file"] == fields["working_file"]:
        failures.append(
            CheckResult(
                "working_copy_required",
                "MCP edits must target a working copy",
                "`source_file` and `working_file` are identical",
                "Create a separate working file and keep the source file unchanged.",
            )
        )

    destructive_requested = fields.get("destructive_operations_requested", "").lower() == "yes"
    if destructive_requested and value_is_none(fields.get("destructive_operations_approved_by", "")):
        failures.append(
            CheckResult(
                "destructive_approval_required",
                "Destructive operations require explicit approval",
                "`destructive_operations_requested` is yes but no approver is recorded",
                "Record the approver and approval time before destructive work.",
            )
        )

    structural_change = fields.get("structural_change_made", "").lower() == "yes"
    if structural_change and value_is_none(fields.get("screenshots", "")):
        failures.append(
            CheckResult(
                "screenshots_required",
                "Structural MCP changes require screenshots",
                "`structural_change_made` is yes but screenshots are missing",
                "Capture screenshot set and link the manifest.",
            )
        )

    for field in ["validation_reports", "specialist_review", "qa_audit"]:
        if value_is_none(fields.get(field, "")):
            failures.append(
                CheckResult(
                    "review_evidence_required",
                    f"`{field}` is required before action log approval",
                    f"`{field}` is `{fields.get(field, '')}`",
                    f"Link the required `{field}` artifact.",
                )
            )

    hard_failures = fields.get("hard_failures_present", "").lower() == "yes"
    decision = fields.get("decision", "")
    if hard_failures and decision == "approved":
        failures.append(
            CheckResult(
                "approval_blocks_hard_failures",
                "Action logs with hard failures cannot be approved",
                "hard failures are present but decision is approved",
                "Use `rejected`, `rolled_back`, or `blocked` until hard failures are fixed.",
            )
        )

    if fields.get("human_approval_required", "").lower() == "yes" and decision == "approved":
        if value_is_none(fields.get("approved_by", "")) or value_is_none(fields.get("approved_at", "")):
            failures.append(
                CheckResult(
                    "human_approval_record",
                    "Approved MCP logs must record human approval",
                    "approval is required but approver or approval time is missing",
                    "Set `approved_by` and `approved_at`.",
                )
            )

    if fields.get("rollback_required", "").lower() == "yes" and value_is_none(fields.get("rollback_artifact", "")):
        failures.append(
            CheckResult(
                "rollback_artifact_required",
                "Required rollback must identify rollback artifact",
                "`rollback_required` is yes but rollback artifact is missing",
                "Link the backup or restored file used for rollback.",
            )
        )

    rows = parse_markdown_table(
        markdown,
        ["Step", "Tool Or Command", "Intent", "Result", "Artifact"],
    )
    if not rows:
        failures.append(
            CheckResult(
                "action_trace_required",
                "Action trace must have at least one action row",
                "no action rows found",
                "Add one row per MCP command, script, validator, or review action.",
            )
        )

    if len(rows) > 12:
        warnings.append(
            CheckResult(
                "loop_too_large",
                "Action trace is large for a bounded MCP loop",
                f"{len(rows)} action rows found",
                "Consider splitting the work into smaller microtasks.",
                "warning",
            )
        )

    return failures, warnings, fields, {"field_count": len(fields), "action_count": len(rows)}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    args = parser.parse_args()

    try:
        failures, warnings, fields, measurements = validate(args.path, args.repo_root)
        print(
            render_validation_report(
                validator_name="validate_mcp_action_log",
                validator_version=VERSION,
                input_path=args.path,
                repo_root=args.repo_root,
                asset_id=fields.get("asset_id", ""),
                stage_id=fields.get("stage_id", ""),
                failures=failures,
                warnings=warnings,
                measurements=measurements,
            )
        )
        return 1 if failures else 0
    except Exception as exc:
        print(f"validator error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
