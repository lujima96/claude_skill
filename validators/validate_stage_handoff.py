#!/usr/bin/env python3
"""Validate a stage handoff Markdown document."""

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
    "handoff_id",
    "asset_id",
    "from_stage",
    "to_stage",
    "created_by",
    "created_at",
    "status",
    "stage_goal",
    "completed_work",
    "new_artifacts",
    "hard_failures_present",
    "hard_failure_summary",
    "human_review_required",
    "approval_decision",
    "next_stage_inputs",
    "next_stage_focus",
    "next_stage_stop_conditions",
    "next_stage_owner",
    "prepared_by",
]


def validate(path: Path, repo_root: Path) -> tuple[list[CheckResult], list[CheckResult], dict[str, str], dict[str, object]]:
    markdown = read_text(path)
    fields = extract_fields(markdown)
    failures: list[CheckResult] = []
    warnings: list[CheckResult] = []

    add_required_field_checks(failures, fields, REQUIRED_FIELDS)
    add_stage_check(failures, fields, "from_stage")
    add_stage_check(failures, fields, "to_stage")

    if fields.get("from_stage") == fields.get("to_stage") and fields.get("from_stage"):
        failures.append(
            CheckResult(
                "handoff_direction",
                "`from_stage` and `to_stage` must differ",
                f"both are `{fields.get('from_stage')}`",
                "Set `to_stage` to the actual next stage or create a revision task.",
            )
        )

    hard_failures = fields.get("hard_failures_present", "").lower()
    if hard_failures not in {"yes", "no"}:
        failures.append(
            CheckResult(
                "hard_failure_explicit",
                "`hard_failures_present` must be yes or no",
                f"value is `{fields.get('hard_failures_present', '')}`",
                "Use `yes` or `no` and summarize the result.",
            )
        )
    if hard_failures == "yes" and fields.get("approval_decision") == "approved":
        failures.append(
            CheckResult(
                "approval_blocks_hard_failures",
                "Handoffs with hard failures cannot be approved",
                "hard failures are present but approval decision is approved",
                "Resolve hard failures or set the handoff decision to revise or blocked.",
            )
        )

    if fields.get("human_review_required", "").lower() != "yes":
        warnings.append(
            CheckResult(
                "human_gate",
                "Human review should remain explicit",
                f"value is `{fields.get('human_review_required', '')}`",
                "Set `human_review_required` to `yes` unless this gate is intentionally automated.",
                "warning",
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
        print(
            render_validation_report(
                validator_name="validate_stage_handoff",
                validator_version=VERSION,
                input_path=args.path,
                repo_root=args.repo_root,
                asset_id=fields.get("asset_id", ""),
                stage_id=fields.get("to_stage", ""),
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

