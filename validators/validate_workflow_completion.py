#!/usr/bin/env python3
"""Validate a workflow completion Markdown report."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from rules.markdown_fields import CheckResult, add_required_field_checks, extract_fields, parse_markdown_table, read_text, render_validation_report

VERSION = "0.1.0"

REQUIRED_FIELDS = [
    "workflow_report_id", "asset_id", "workflow_id", "created_by", "created_at", "status",
    "asset_manifest", "final_qa_audit", "godot_validation_report", "godot_preview_screenshot",
    "hard_failures_present", "missing_stage_artifacts", "missing_reviews", "missing_validations",
    "decision", "decision_reason", "required_next_actions",
]

VALID_STAGES = [
    "concept_interpretation", "reference_gathering", "proportion_planning", "blockout", "primary_forms",
    "secondary_anatomy", "tertiary_detail", "clothing_hardsurface_hair", "retopology", "uvs_and_baking",
    "texturing_materials", "rigging_skinning", "deformation_testing", "optimization_lods", "export_godot_validation",
]


def validate(path: Path, repo_root: Path) -> tuple[list[CheckResult], list[CheckResult], dict[str, str], dict[str, object]]:
    markdown = read_text(path)
    fields = extract_fields(markdown)
    failures: list[CheckResult] = []
    warnings: list[CheckResult] = []
    add_required_field_checks(failures, fields, REQUIRED_FIELDS)

    rows = parse_markdown_table(markdown, ["Stage ID", "Task Card", "Handoff", "Specialist Review", "Validation Report", "Artifact", "Gate"])
    stage_ids = {row.get("Stage ID", "") for row in rows}
    for stage_id in VALID_STAGES:
        if stage_id not in stage_ids:
            failures.append(CheckResult("missing_stage_row", "Workflow completion report must include every stage", f"missing `{stage_id}`", "Add a row for every canonical stage."))
    bad_gates = [row for row in rows if row.get("Gate") not in {"complete", "partial", "blocked"}]
    for row in bad_gates:
        failures.append(CheckResult("valid_gate", "Stage gate must be complete, partial, or blocked", f"{row.get('Stage ID')} gate is `{row.get('Gate')}`", "Use `complete`, `partial`, or `blocked`."))

    if fields.get("decision") == "complete":
        if fields.get("hard_failures_present") != "no":
            failures.append(CheckResult("completion_blocks_hard_failures", "Complete workflows cannot have hard failures", f"hard_failures_present is `{fields.get('hard_failures_present')}`", "Fix hard failures before completion."))
        incomplete = [row.get("Stage ID") for row in rows if row.get("Gate") != "complete"]
        if incomplete:
            failures.append(CheckResult("all_stages_complete", "Complete workflows require every stage gate complete", f"incomplete stages: {', '.join(incomplete)}", "Complete every stage before final approval."))
    elif fields.get("decision") != "blocked":
        failures.append(CheckResult("valid_decision", "`decision` must be complete or blocked", f"value is `{fields.get('decision')}`", "Use `complete` or `blocked`."))

    return failures, warnings, fields, {"stage_rows": len(rows), "field_count": len(fields)}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    try:
        failures, warnings, fields, measurements = validate(args.path, args.repo_root)
        print(render_validation_report(validator_name="validate_workflow_completion", validator_version=VERSION, input_path=args.path, repo_root=args.repo_root, asset_id=fields.get("asset_id", ""), stage_id="export_godot_validation", failures=failures, warnings=warnings, measurements=measurements))
        return 1 if failures else 0
    except Exception as exc:
        print(f"validator error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
