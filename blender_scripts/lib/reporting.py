"""Shared helpers for Blender report scripts.

These helpers intentionally depend only on the Python standard library so report
scripts can be syntax-checked outside Blender. Blender-specific modules should be
imported inside each script's `collect_report` function.
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SCRIPT_VERSION = "0.2.0"

CANONICAL_STAGE_IDS = (
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
)


def build_parser(description: str) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("--out", type=Path, help="Optional output path.")
    parser.add_argument(
        "--format",
        choices=("json", "markdown"),
        default="json",
        help="Output format. Defaults to json.",
    )
    parser.add_argument(
        "--asset-id",
        default="unknown_asset",
        help="Asset ID to include in the report.",
    )
    parser.add_argument(
        "--stage-id",
        choices=CANONICAL_STAGE_IDS,
        default="blockout",
        help="Pipeline stage ID to include in the report.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Replace an existing report artifact. Refused by default.",
    )
    return parser


def blender_args(argv: list[str]) -> list[str]:
    """Return args after Blender's `--` separator."""
    if "--" in argv:
        return argv[argv.index("--") + 1 :]
    return argv[1:]


def base_report(
    *,
    report_type: str,
    asset_id: str,
    stage_id: str,
    source_file: str,
    blender_version: str = "unknown",
    source_read_only: bool = True,
    writes_artifacts: bool = True,
) -> dict[str, Any]:
    return {
        "metadata": {
            "report_type": report_type,
            "asset_id": asset_id,
            "stage_id": stage_id,
            "created_at": datetime.now(timezone.utc).isoformat(),
            "script_version": SCRIPT_VERSION,
            "blender_version": blender_version,
            "source_file": source_file,
            # Retain `read_only` for report-schema compatibility. It means the
            # source .blend is not saved or overwritten, not that no evidence
            # artifacts are written.
            "read_only": source_read_only,
            "source_read_only": source_read_only,
            "writes_artifacts": writes_artifacts,
        },
        "summary": {},
        "warnings": [],
        "hard_failures": [],
        "measurements": {},
        "items": [],
    }


def add_warning(report: dict[str, Any], rule_id: str, message: str, evidence: str = "") -> None:
    report["warnings"].append(
        {"rule_id": rule_id, "message": message, "evidence": evidence}
    )


def add_hard_failure(report: dict[str, Any], rule_id: str, message: str, evidence: str = "") -> None:
    report["hard_failures"].append(
        {"rule_id": rule_id, "message": message, "evidence": evidence}
    )


def finalize(report: dict[str, Any]) -> dict[str, Any]:
    report["summary"]["warning_count"] = len(report["warnings"])
    report["summary"]["hard_failure_count"] = len(report["hard_failures"])
    report["summary"]["status"] = "fail" if report["hard_failures"] else (
        "warning" if report["warnings"] else "pass"
    )
    return report


def render_json(report: dict[str, Any]) -> str:
    return json.dumps(report, indent=2, sort_keys=True)


def render_markdown(report: dict[str, Any]) -> str:
    metadata = report.get("metadata", {})
    summary = report.get("summary", {})
    measurements = report.get("measurements", {})

    lines = [
        f"# {metadata.get('report_type', 'Blender')} Report",
        "",
        "## Metadata",
        "",
    ]
    for key, value in metadata.items():
        lines.append(f"- `{key}`: {value}")

    lines.extend(["", "## Summary", ""])
    for key, value in summary.items():
        lines.append(f"- `{key}`: {value}")

    lines.extend(["", "## Measurements", ""])
    if measurements:
        for key, value in measurements.items():
            lines.append(f"- `{key}`: {value}")
    else:
        lines.append("- `none`: none")

    lines.extend(["", "## Warnings", ""])
    if report.get("warnings"):
        for item in report["warnings"]:
            lines.append(
                f"- `{item['rule_id']}`: {item['message']} Evidence: {item.get('evidence', '')}"
            )
    else:
        lines.append("- none")

    lines.extend(["", "## Hard Failures", ""])
    if report.get("hard_failures"):
        for item in report["hard_failures"]:
            lines.append(
                f"- `{item['rule_id']}`: {item['message']} Evidence: {item.get('evidence', '')}"
            )
    else:
        lines.append("- none")

    lines.extend(["", "## Items", ""])
    items = report.get("items", [])
    if items:
        lines.append("```json")
        lines.append(json.dumps(items, indent=2, sort_keys=True))
        lines.append("```")
    else:
        lines.append("- none")

    return "\n".join(lines) + "\n"


def write_report(
    report: dict[str, Any],
    out: Path | None,
    output_format: str,
    *,
    overwrite: bool = False,
) -> None:
    rendered = render_markdown(report) if output_format == "markdown" else render_json(report)
    if out:
        out.parent.mkdir(parents=True, exist_ok=True)
        mode = "w" if overwrite else "x"
        with out.open(mode, encoding="utf-8") as handle:
            handle.write(rendered)
    else:
        print(rendered)
