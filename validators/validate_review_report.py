#!/usr/bin/env python3
"""Validate a specialist review report Markdown document."""

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
    "review_id",
    "asset_id",
    "stage_id",
    "review_type",
    "reviewer",
    "created_at",
    "status",
    "task_card",
    "artifacts",
    "hard_failures_present",
    "hard_failures",
    "blocked_stage_progression",
    "decision",
    "decision_reason",
    "required_next_actions",
]

VALID_DECISIONS = {"approve", "approve_with_notes", "revise", "block"}
VALID_REVIEW_TYPES = {
    "reference",
    "style",
    "anatomy",
    "topology",
    "rigging",
    "materials",
    "uv_bake",
    "optimization",
    "godot_export",
    "qa",
}


def validate(path: Path, repo_root: Path) -> tuple[list[CheckResult], list[CheckResult], dict[str, str], dict[str, object]]:
    markdown = read_text(path)
    fields = extract_fields(markdown)
    failures: list[CheckResult] = []
    warnings: list[CheckResult] = []

    add_required_field_checks(failures, fields, REQUIRED_FIELDS)
    add_stage_check(failures, fields, "stage_id")

    if fields.get("review_type") and fields["review_type"] not in VALID_REVIEW_TYPES:
        failures.append(
            CheckResult(
                "valid_review_type",
                "`review_type` must be known",
                f"value is `{fields['review_type']}`",
                f"Use one of: {', '.join(sorted(VALID_REVIEW_TYPES))}.",
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

    hard_failures = fields.get("hard_failures_present", "").lower()
    blocked = fields.get("blocked_stage_progression", "").lower()
    if hard_failures not in {"yes", "no"}:
        failures.append(
            CheckResult(
                "hard_failure_explicit",
                "`hard_failures_present` must be yes or no",
                f"value is `{fields.get('hard_failures_present', '')}`",
                "Use `yes` or `no`.",
            )
        )
    if blocked not in {"yes", "no"}:
        failures.append(
            CheckResult(
                "blocked_explicit",
                "`blocked_stage_progression` must be yes or no",
                f"value is `{fields.get('blocked_stage_progression', '')}`",
                "Use `yes` or `no`.",
            )
        )
    if hard_failures == "yes" and fields.get("decision") in {"approve", "approve_with_notes"}:
        failures.append(
            CheckResult(
                "decision_blocks_hard_failures",
                "Reviews with hard failures cannot approve progression",
                f"decision is `{fields.get('decision')}`",
                "Use `revise` or `block` until hard failures are fixed.",
            )
        )

    rows = parse_markdown_table(
        markdown,
        ["Severity", "Category", "Finding", "Evidence", "Recommendation", "Blocking"],
    )
    if not rows:
        failures.append(
            CheckResult(
                "findings_table",
                "Findings table must be present",
                "no findings rows found",
                "Add at least one findings row with severity, evidence, recommendation, and blocking status.",
            )
        )
    for index, row in enumerate(rows, start=1):
        if row.get("Blocking", "").lower() not in {"yes", "no"}:
            failures.append(
                CheckResult(
                    "blocking_explicit",
                    "Finding blocking value must be yes or no",
                    f"row {index} has `{row.get('Blocking', '')}`",
                    "Set `Blocking` to `yes` or `no`.",
                )
            )

    return failures, warnings, fields, {"finding_count": len(rows), "field_count": len(fields)}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    args = parser.parse_args()

    try:
        failures, warnings, fields, measurements = validate(args.path, args.repo_root)
        print(
            render_validation_report(
                validator_name="validate_review_report",
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

