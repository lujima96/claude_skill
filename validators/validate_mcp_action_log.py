#!/usr/bin/env python3
"""Validate a Blender MCP action log Markdown document."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
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
    "project_root",
    "blender_version",
    "mcp_server",
    "mcp_server_version",
    "connection_status",
    "required_capabilities",
    "available_capabilities",
    "capability_preflight",
    "isolated_workspace_verified",
    "arbitrary_python_requested",
    "arbitrary_python_approved_by",
    "task_card",
    "specialist_owner",
    "microtask_goal",
    "allowed_tools",
    "disallowed_tools",
    "acceptance_tests",
    "stop_conditions",
    "target_objects",
    "allowed_change_types",
    "source_file",
    "backup_file",
    "working_file",
    "source_protection_receipt",
    "backup_verified",
    "source_sha256_before",
    "backup_sha256",
    "working_sha256_before",
    "source_sha256_after",
    "source_unchanged_verified",
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
    "working_copy_disposition",
    "decision",
    "decision_reason",
    "human_approval_required",
    "approved_by",
    "approved_at",
]

VALID_STATUSES = {"draft", "executed", "approved", "rejected", "rolled_back", "blocked"}
VALID_EXECUTION_MODES = {"real_mcp", "dry_run", "example"}
VALID_DECISIONS = {"approved", "rejected", "rolled_back", "blocked"}
VALID_CONNECTION_STATUSES = {"ready", "unavailable", "incompatible"}
VALID_PREFLIGHT = {"pass", "fail"}
VALID_DISPOSITIONS = {"retained_for_review", "discarded", "promoted_by_human", "not_applicable"}
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


def clean_value(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] == "`":
        return value[1:-1]
    return value


def resolve_artifact(value: str, document_path: Path, repo_root: Path) -> Path:
    candidate = Path(clean_value(value)).expanduser()
    if candidate.is_absolute():
        return candidate.resolve()
    choices = [(repo_root / candidate).resolve(), (document_path.parent / candidate).resolve()]
    return next((path for path in choices if path.exists()), choices[0])


def list_values(value: str) -> list[str]:
    return [clean_value(item) for item in re.split(r"[;,]", value) if clean_value(item)]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


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

    for field, valid in (
        ("connection_status", VALID_CONNECTION_STATUSES),
        ("capability_preflight", VALID_PREFLIGHT),
        ("working_copy_disposition", VALID_DISPOSITIONS),
    ):
        if fields.get(field) and fields[field] not in valid:
            failures.append(CheckResult("valid_enum", f"`{field}` must be known", fields[field], f"Use one of: {', '.join(sorted(valid))}."))

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
        "isolated_workspace_verified",
        "arbitrary_python_requested",
        "source_unchanged_verified",
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

    path_values = [clean_value(fields.get(field, "")) for field in ("source_file", "backup_file", "working_file")]
    if all(path_values) and len(set(path_values)) != 3:
        failures.append(CheckResult("distinct_source_paths", "Source, backup, and working paths must be distinct", str(path_values), "Create separate non-overwriting paths."))

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

    execution_mode = fields.get("execution_mode", "")
    status = fields.get("status", "")
    final_status_map = {"approved": "approved", "rejected": "rejected", "rolled_back": "rolled_back", "blocked": "blocked"}
    if status in final_status_map and decision != final_status_map[status]:
        failures.append(CheckResult("status_decision_consistency", "Final status and decision must agree", f"status `{status}`, decision `{decision}`", f"Set decision to `{final_status_map[status]}` or use a non-final status."))
    if decision == "approved":
        for field in ("hard_failures_present", "blocked_stage_progression", "rollback_required"):
            if fields.get(field, "").lower() != "no":
                failures.append(CheckResult("approved_state_consistency", f"Approved logs require `{field}: no`", fields.get(field, ""), f"Set `{field}` truthfully before approval."))
    if fields.get("working_copy_disposition") == "promoted_by_human" and decision != "approved":
        failures.append(CheckResult("promotion_requires_approval", "Only an approved loop may record human promotion", decision, "Retain or discard the working copy instead."))

    if execution_mode in {"example", "dry_run"} and decision == "approved":
        warnings.append(CheckResult("non_live_approval", "Example and dry-run approval does not satisfy a live MCP gate", execution_mode, "Run a validated `real_mcp` loop for live approval.", "warning"))

    if execution_mode == "real_mcp":
        for field, expected in (
            ("connection_status", "ready"),
            ("capability_preflight", "pass"),
            ("isolated_workspace_verified", "yes"),
            ("backup_verified", "yes"),
            ("source_unchanged_verified", "yes"),
        ):
            if fields.get(field, "").lower() != expected:
                failures.append(CheckResult("real_mcp_preflight", f"Real MCP execution requires `{field}: {expected}`", fields.get(field, ""), "Complete the preflight before execution."))
        required_caps = set(list_values(fields.get("required_capabilities", "")))
        available_caps = set(list_values(fields.get("available_capabilities", "")))
        missing_caps = sorted(required_caps - available_caps)
        if missing_caps:
            failures.append(CheckResult("missing_capabilities", "Required MCP capabilities are unavailable", ", ".join(missing_caps), "Connect a compatible server or reduce the task scope."))
        if fields.get("arbitrary_python_requested", "").lower() == "yes" and value_is_none(fields.get("arbitrary_python_approved_by", "")):
            failures.append(CheckResult("python_approval", "Arbitrary Blender Python requires explicit approval", fields.get("arbitrary_python_approved_by", ""), "Record the approver or remove Python execution from scope."))

        root = resolve_artifact(fields.get("project_root", ""), path, repo_root)
        if not (root / "AGENTS.md").is_file():
            failures.append(CheckResult("project_root_contract", "Project root must contain AGENTS.md", str(root), "Resolve the repository root before MCP execution."))

        artifact_fields = ("task_card", "source_file", "backup_file", "working_file", "source_protection_receipt", "screenshots", "blender_reports", "validation_reports", "specialist_review", "qa_audit")
        resolved: dict[str, list[Path]] = {}
        for field in artifact_fields:
            values = list_values(fields.get(field, ""))
            resolved[field] = [resolve_artifact(value, path, repo_root) for value in values]
            if not values:
                failures.append(CheckResult("real_evidence_required", f"`{field}` is required in real MCP mode", fields.get(field, ""), f"Record real `{field}` evidence."))
            for artifact in resolved[field]:
                if not artifact.is_file():
                    failures.append(CheckResult("artifact_exists", f"`{field}` artifact must exist", str(artifact), "Create and validate the artifact before closing the loop."))

        blend_paths = [resolve_artifact(fields.get(field, ""), path, repo_root) for field in ("source_file", "backup_file", "working_file")]
        if len(set(blend_paths)) != 3 or any(item.suffix.lower() != ".blend" for item in blend_paths):
            failures.append(CheckResult("protected_blend_paths", "Protected Blender paths must be three distinct .blend files", str(blend_paths), "Rerun working-copy preparation."))

        receipt_paths = resolved.get("source_protection_receipt", [])
        if receipt_paths and receipt_paths[0].is_file() and all(item.is_file() for item in blend_paths):
            try:
                receipt = json.loads(receipt_paths[0].read_text(encoding="utf-8"))
                source, backup, _working = blend_paths
                expected_pairs = {
                    "asset_id": fields.get("asset_id", ""),
                    "microtask_id": fields.get("microtask_id", ""),
                    "source_file": str(source.resolve()),
                    "backup_file": str(backup.resolve()),
                    "working_file": str(_working.resolve()),
                    "source_sha256_before": clean_value(fields.get("source_sha256_before", "")),
                    "backup_sha256": clean_value(fields.get("backup_sha256", "")),
                    "working_sha256_before": clean_value(fields.get("working_sha256_before", "")),
                }
                for key, expected in expected_pairs.items():
                    if str(receipt.get(key, "")) != expected:
                        failures.append(CheckResult("receipt_match", f"Receipt `{key}` must match the action log", f"receipt {receipt.get(key)!r}, log {expected!r}", "Regenerate or correct the protection receipt."))
                actual_source_hash = sha256(source)
                actual_backup_hash = sha256(backup)
                if clean_value(fields.get("source_sha256_after", "")) != actual_source_hash or clean_value(fields.get("source_sha256_before", "")) != actual_source_hash:
                    failures.append(CheckResult("source_hash_unchanged", "Source hash must remain unchanged", actual_source_hash, "Do not save or overwrite the source .blend."))
                if clean_value(fields.get("backup_sha256", "")) != actual_backup_hash:
                    failures.append(CheckResult("backup_hash", "Backup hash must match the protected copy", actual_backup_hash, "Recreate the backup from source."))
            except Exception as exc:
                failures.append(CheckResult("valid_protection_receipt", "Source-protection receipt must be valid JSON", str(exc), "Regenerate the receipt with prepare_working_copy.py."))

        task_paths = resolved.get("task_card", [])
        if task_paths and task_paths[0].is_file():
            try:
                from validate_stage_task_card import validate as validate_task_card
                task_failures, _, task_fields, _ = validate_task_card(task_paths[0], repo_root)
                if task_failures:
                    failures.append(CheckResult("valid_task_card", "Referenced task card must pass validation", ", ".join(item.rule_id for item in task_failures), "Fix and revalidate the task card."))
                for field in ("asset_id", "stage_id"):
                    if task_fields.get(field) != fields.get(field):
                        failures.append(CheckResult("task_log_match", f"Task-card `{field}` must match the action log", f"task {task_fields.get(field)!r}, log {fields.get(field)!r}", "Use the task card that authorized this loop."))
                if task_fields.get("status") not in {"ready", "in_progress", "review", "approved"}:
                    failures.append(CheckResult("task_ready", "Real MCP execution requires an authorized non-draft task card", str(task_fields.get("status")), "Move the task card to ready only after execution authorization."))
                if task_fields.get("mcp_microtask_id") != fields.get("microtask_id"):
                    failures.append(CheckResult("microtask_match", "Task-card microtask ID must match the action log", f"task {task_fields.get('mcp_microtask_id')!r}, log {fields.get('microtask_id')!r}", "Use the task card that authorized this exact microtask."))
            except Exception as exc:
                failures.append(CheckResult("task_card_runtime", "Task-card validation failed to run", str(exc), "Run validate_stage_task_card.py directly."))

        for manifest_path in resolved.get("screenshots", []):
            if manifest_path.is_file():
                try:
                    from validate_screenshot_manifest import DEFAULT_VIEWS, validate as validate_manifest
                    manifest_failures, _, _, _ = validate_manifest(manifest_path, DEFAULT_VIEWS)
                    if manifest_failures:
                        failures.append(CheckResult("valid_screenshots", "Screenshot manifest must pass validation", ", ".join(item.rule_id for item in manifest_failures), "Regenerate and validate the screenshot set."))
                except Exception as exc:
                    failures.append(CheckResult("screenshot_runtime", "Screenshot validation failed to run", str(exc), "Run validate_screenshot_manifest.py directly."))

        for report_path in resolved.get("blender_reports", []):
            if report_path.is_file() and report_path.suffix.lower() == ".json":
                try:
                    from validate_blender_report import validate as validate_report
                    report_failures, _, _, _ = validate_report(report_path, fields.get("asset_id"), fields.get("stage_id"), blend_paths[2])
                    if report_failures:
                        failures.append(CheckResult("valid_blender_report", "Blender reports must pass validation", f"{report_path}: {', '.join(item.rule_id for item in report_failures)}", "Regenerate and validate the Blender report."))
                except Exception as exc:
                    failures.append(CheckResult("blender_report_runtime", "Blender-report validation failed to run", str(exc), "Run validate_blender_report.py directly."))

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
