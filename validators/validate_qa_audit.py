#!/usr/bin/env python3
"""Validate a QA audit Markdown document."""

from __future__ import annotations

import argparse
import math
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
    to_float,
)

VERSION = "0.1.0"

REQUIRED_FIELDS = [
    "audit_id",
    "asset_id",
    "stage_id",
    "created_by",
    "created_at",
    "status",
    "task_card",
    "stage_handoff",
    "review_reports",
    "validation_reports",
    "hard_failures_present",
    "blocked_stage_progression",
    "hard_failures",
    "required_fixes_before_progression",
    "total_score",
    "score_band",
    "decision",
    "decision_reason",
    "next_stage",
    "approval_required_from",
]

VALID_DECISIONS = {"approve_next_stage", "revise_current_stage", "return_to_previous_stage", "block_progression"}
VALID_SCORE_BANDS = {"ship_candidate", "targeted_revision", "structural_rework"}


def expected_band(total: float, has_hard_failures: bool) -> str:
    if has_hard_failures or total < 70:
        return "structural_rework"
    if total < 85:
        return "targeted_revision"
    return "ship_candidate"


def validate(path: Path, repo_root: Path) -> tuple[list[CheckResult], list[CheckResult], dict[str, str], dict[str, object]]:
    markdown = read_text(path)
    fields = extract_fields(markdown)
    failures: list[CheckResult] = []
    warnings: list[CheckResult] = []

    add_required_field_checks(failures, fields, REQUIRED_FIELDS)
    add_stage_check(failures, fields, "stage_id")
    add_stage_check(failures, fields, "next_stage")

    hard_failures = fields.get("hard_failures_present", "").lower()
    blocked = fields.get("blocked_stage_progression", "").lower()
    has_hard_failures = hard_failures == "yes"
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
    if has_hard_failures and fields.get("decision") == "approve_next_stage":
        failures.append(
            CheckResult(
                "decision_blocks_hard_failures",
                "Audits with hard failures cannot approve the next stage",
                "hard failures are present but decision approves progression",
                "Use `block_progression`, `return_to_previous_stage`, or fix the hard failures.",
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
    if fields.get("score_band") and fields["score_band"] not in VALID_SCORE_BANDS:
        failures.append(
            CheckResult(
                "valid_score_band",
                "`score_band` must be known",
                f"value is `{fields['score_band']}`",
                f"Use one of: {', '.join(sorted(VALID_SCORE_BANDS))}.",
            )
        )

    rows = parse_markdown_table(
        markdown,
        ["Category", "Weight", "Score", "Weighted Contribution", "Notes"],
    )
    calculated_total = 0.0
    scored_rows = 0
    for index, row in enumerate(rows, start=1):
        weight = to_float(row.get("Weight", ""))
        score = to_float(row.get("Score", ""))
        contribution = to_float(row.get("Weighted Contribution", ""))
        if weight is None or score is None or contribution is None:
            warnings.append(
                CheckResult(
                    "score_pending",
                    "Score row has pending or nonnumeric values",
                    f"row {index}: {row}",
                    "Fill numeric weight, score, and weighted contribution when the category is in scope.",
                    "warning",
                )
            )
            continue
        expected = weight * score / 10
        calculated_total += expected
        scored_rows += 1
        if not math.isclose(contribution, expected, abs_tol=0.05):
            failures.append(
                CheckResult(
                    "weighted_contribution_math",
                    "Weighted contribution must equal weight * score / 10",
                    f"row {index} has {contribution}, expected {expected:.2f}",
                    "Correct the weighted contribution value.",
                )
            )

    reported_total = to_float(fields.get("total_score", ""))
    if reported_total is None:
        failures.append(
            CheckResult(
                "total_score_numeric",
                "`total_score` must be numeric",
                f"value is `{fields.get('total_score', '')}`",
                "Set `total_score` to the sum of weighted contributions.",
            )
        )
    elif not math.isclose(reported_total, calculated_total, abs_tol=0.1):
        failures.append(
            CheckResult(
                "total_score_math",
                "`total_score` must match weighted contribution sum",
                f"reported {reported_total}, calculated {calculated_total:.2f}",
                "Correct `total_score` or the row contribution values.",
            )
        )

    if reported_total is not None and fields.get("score_band") in VALID_SCORE_BANDS:
        band = expected_band(reported_total, has_hard_failures)
        if fields["score_band"] != band:
            failures.append(
                CheckResult(
                    "score_band_math",
                    "`score_band` must match score and hard-failure state",
                    f"reported `{fields['score_band']}`, expected `{band}`",
                    "Correct `score_band`.",
                )
            )

    return failures, warnings, fields, {
        "score_rows": len(rows),
        "scored_rows": scored_rows,
        "calculated_total": round(calculated_total, 2),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    args = parser.parse_args()

    try:
        failures, warnings, fields, measurements = validate(args.path, args.repo_root)
        print(
            render_validation_report(
                validator_name="validate_qa_audit",
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
