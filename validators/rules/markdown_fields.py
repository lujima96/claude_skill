"""Small Markdown helpers for pipeline validators."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Iterable


VALID_STAGE_IDS = {
    "concept_interpretation",
    "reference_gathering",
    "proportion_planning",
    "blockout",
    "primary_forms",
    "secondary_anatomy",
    "tertiary_detail",
    "clothing_hardsurface_hair",
    "retopology",
    "uvs_and_baking",
    "texturing_materials",
    "rigging_skinning",
    "deformation_testing",
    "optimization_lods",
    "export_godot_validation",
    # Phase 5 manual-slice planning aliases.
    "style_lock",
    "anatomy_blockout_planning",
    "manual_blockout",
}


@dataclass
class CheckResult:
    rule_id: str
    rule: str
    evidence: str
    fix: str
    severity: str = "failure"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def extract_fields(markdown: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    pattern = re.compile(r"^\s*-\s+`([^`]+)`:\s*(.*)$")
    for line in markdown.splitlines():
        match = pattern.match(line)
        if match:
            fields[match.group(1)] = match.group(2).strip()
    return fields


def parse_list_value(value: str) -> list[str]:
    value = value.strip()
    if not value or value.lower() in {"none", "n/a"}:
        return []
    return [item.strip() for item in value.split(";") if item.strip()]


def missing_required(fields: dict[str, str], required: Iterable[str]) -> list[str]:
    missing = []
    for field in required:
        value = fields.get(field, "").strip()
        if not value:
            missing.append(field)
    return missing


def add_required_field_checks(
    failures: list[CheckResult],
    fields: dict[str, str],
    required: Iterable[str],
) -> None:
    for field in missing_required(fields, required):
        failures.append(
            CheckResult(
                "required_field",
                f"`{field}` is required",
                f"`{field}` is missing or blank",
                f"Fill `{field}` in the document metadata or relevant section.",
            )
        )


def add_stage_check(failures: list[CheckResult], fields: dict[str, str], field: str) -> None:
    stage_id = fields.get(field, "").strip()
    if stage_id and stage_id not in VALID_STAGE_IDS and stage_id != "none":
        failures.append(
            CheckResult(
                "valid_stage_id",
                f"`{field}` must be a known stage ID",
                f"`{field}` is `{stage_id}`",
                f"Use one of: {', '.join(sorted(VALID_STAGE_IDS))}.",
            )
        )


def parse_markdown_table(markdown: str, required_headers: list[str]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    lines = markdown.splitlines()
    for index, line in enumerate(lines):
        if not line.strip().startswith("|"):
            continue
        headers = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if headers != required_headers:
            continue
        if index + 1 >= len(lines):
            continue
        for row_line in lines[index + 2 :]:
            if not row_line.strip().startswith("|"):
                break
            cells = [cell.strip() for cell in row_line.strip().strip("|").split("|")]
            if len(cells) != len(headers):
                continue
            rows.append(dict(zip(headers, cells)))
        break
    return rows


def to_float(value: str) -> float | None:
    cleaned = value.strip().replace("%", "")
    if cleaned.lower() in {"", "pending", "n/a", "none"}:
        return None
    try:
        return float(cleaned)
    except ValueError:
        return None


def repo_relative(path: Path, repo_root: Path) -> str:
    try:
        return str(path.relative_to(repo_root))
    except ValueError:
        return str(path)


def render_validation_report(
    *,
    validator_name: str,
    validator_version: str,
    input_path: Path,
    repo_root: Path,
    asset_id: str,
    stage_id: str,
    failures: list[CheckResult],
    warnings: list[CheckResult],
    measurements: dict[str, object] | None = None,
) -> str:
    status = "fail" if failures else ("warning" if warnings else "pass")
    blocked = "yes" if failures else "no"
    hard_failure_count = len(failures)
    validation_id = f"{asset_id or 'unknown_asset'}-{validator_name}-validation"
    measurements = measurements or {}
    rules = [
        {
            "rule_id": item.rule_id,
            "severity": item.severity,
            "evidence": item.evidence,
        }
        for item in [*failures, *warnings]
    ]

    failure_rows = "\n".join(
        f"| {item.rule_id} | {item.rule} | {item.evidence} | {item.fix} |"
        for item in failures
    ) or "| none | none | none | none |"
    warning_rows = "\n".join(
        f"| {item.rule_id} | {item.rule} | {item.evidence} | {item.fix} |"
        for item in warnings
    ) or "| none | none | none | none |"
    measurement_lines = "\n".join(
        f"- `{key}`: {value}" for key, value in sorted(measurements.items())
    )
    if not measurement_lines:
        measurement_lines = "- `missing_files`: none\n- `godot_import_status`: not_applicable\n- `screenshot_manifest_status`: not_applicable"

    result = {
        "validation_id": validation_id,
        "status": status,
        "hard_failures_present": bool(failures),
        "blocked_stage_progression": bool(failures),
        "rules": rules,
    }

    return f"""# Validation Report

## Metadata

- `validation_id`: {validation_id}
- `asset_id`: {asset_id or 'unknown'}
- `stage_id`: {stage_id or 'unknown'}
- `validator_name`: {validator_name}
- `validator_version`: {validator_version}
- `created_at`: {date.today().isoformat()}
- `status`: {status}

## Execution

- `command_or_tool`: validators/{validator_name}.py {repo_relative(input_path, repo_root)}
- `input_artifacts`: {repo_relative(input_path, repo_root)}
- `output_artifacts`: stdout
- `environment`: python stdlib
- `duration_seconds`: not_measured

## Summary

- `passed_checks`: not_counted
- `warning_count`: {len(warnings)}
- `failure_count`: {len(failures)}
- `hard_failure_count`: {hard_failure_count}
- `blocked_stage_progression`: {blocked}

## Hard Failures

| Rule ID | Rule | Evidence | Required Fix |
|---|---|---|---|
{failure_rows}

## Warnings

| Rule ID | Rule | Evidence | Suggested Fix |
|---|---|---|---|
{warning_rows}

## Measurements

{measurement_lines}

## Machine-Readable Result

```json
{json.dumps(result, indent=2)}
```
"""

