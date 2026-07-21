#!/usr/bin/env python3
"""Validate an asset manifest Markdown document."""

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

VERSION = "0.1.0"

REQUIRED_FIELDS = [
    "asset_id",
    "asset_name",
    "character_name",
    "created_by",
    "created_at",
    "last_updated",
    "status",
    "project_root",
    "brief",
    "references_dir",
    "task_cards_dir",
    "handoffs_dir",
    "reviews_dir",
    "validations_dir",
    "target_engine",
    "interchange_format",
    "latest_stage",
    "latest_qa_audit",
    "hard_failures_present",
    "approved_for_next_stage",
]

PATH_FIELDS = [
    "brief",
    "references_dir",
    "task_cards_dir",
    "handoffs_dir",
    "reviews_dir",
    "validations_dir",
    "screenshots_dir",
    "exports_dir",
    "godot_project_dir",
    "latest_handoff",
    "latest_qa_audit",
]

LIST_PATH_FIELDS = [
    "source_blend_files",
    "sculpt_files",
    "retopo_files",
    "rig_files",
    "texture_source_files",
    "external_dependencies",
    "glb_files",
    "gltf_files",
    "texture_files",
    "animation_files",
    "lod_files",
    "collision_files",
    "imported_scenes",
    "material_resources",
]


def resolve_manifest_path(value: str, manifest_dir: Path, project_root: Path) -> Path:
    raw = Path(value)
    if raw.is_absolute():
        return raw
    candidate = (manifest_dir / raw).resolve()
    if candidate.exists():
        return candidate
    return (project_root / raw).resolve()


def validate(path: Path, repo_root: Path) -> tuple[list[CheckResult], list[CheckResult], dict[str, str], dict[str, object]]:
    markdown = read_text(path)
    fields = extract_fields(markdown)
    failures: list[CheckResult] = []
    warnings: list[CheckResult] = []
    missing_files: list[str] = []

    add_required_field_checks(failures, fields, REQUIRED_FIELDS)
    add_stage_check(failures, fields, "latest_stage")

    manifest_dir = path.parent.resolve()
    project_root_value = fields.get("project_root", ".")
    project_root = resolve_manifest_path(project_root_value, manifest_dir, repo_root)
    if not project_root.exists():
        failures.append(
            CheckResult(
                "project_root_exists",
                "`project_root` must exist",
                f"`{project_root_value}` resolved to `{project_root}`",
                "Point `project_root` at the example or asset project folder.",
            )
        )
        project_root = manifest_dir

    for field in PATH_FIELDS:
        value = fields.get(field, "").strip()
        if not value or value.lower() in {"none", "n/a", "not_applicable"}:
            continue
        resolved = resolve_manifest_path(value, manifest_dir, project_root)
        if not resolved.exists():
            missing_files.append(f"{field}: {value}")

    for field in LIST_PATH_FIELDS:
        for item in parse_list_value(fields.get(field, "")):
            resolved = resolve_manifest_path(item, manifest_dir, project_root)
            if not resolved.exists():
                missing_files.append(f"{field}: {item}")

    for missing in missing_files:
        failures.append(
            CheckResult(
                "manifest_path_exists",
                "Manifest paths must exist",
                missing,
                "Create the referenced artifact or update the manifest path.",
            )
        )

    if fields.get("target_engine") and fields["target_engine"] != "Godot":
        failures.append(
            CheckResult(
                "target_engine_godot",
                "Initial workflow target engine must be Godot",
                f"value is `{fields['target_engine']}`",
                "Set `target_engine` to `Godot` for this workflow.",
            )
        )
    if fields.get("interchange_format") and fields["interchange_format"] not in {"GLB", "glTF"}:
        failures.append(
            CheckResult(
                "interchange_format",
                "Interchange format must be GLB or glTF",
                f"value is `{fields['interchange_format']}`",
                "Use `GLB` or `glTF`.",
            )
        )

    hard_failures = fields.get("hard_failures_present", "").lower()
    approved = fields.get("approved_for_next_stage", "").lower()
    if hard_failures not in {"yes", "no"}:
        failures.append(
            CheckResult(
                "hard_failure_explicit",
                "`hard_failures_present` must be yes or no",
                f"value is `{fields.get('hard_failures_present', '')}`",
                "Use `yes` or `no`.",
            )
        )
    if approved not in {"yes", "no"}:
        failures.append(
            CheckResult(
                "approved_explicit",
                "`approved_for_next_stage` must be yes or no",
                f"value is `{fields.get('approved_for_next_stage', '')}`",
                "Use `yes` or `no`.",
            )
        )
    if hard_failures == "yes" and approved == "yes":
        failures.append(
            CheckResult(
                "approval_blocks_hard_failures",
                "Manifest cannot approve progression while hard failures exist",
                "hard failures are present and approved_for_next_stage is yes",
                "Fix hard failures or set `approved_for_next_stage` to `no`.",
            )
        )

    return failures, warnings, fields, {
        "missing_files": ", ".join(missing_files) if missing_files else "none",
        "field_count": len(fields),
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
                validator_name="validate_manifest",
                validator_version=VERSION,
                input_path=args.path,
                repo_root=args.repo_root,
                asset_id=fields.get("asset_id", ""),
                stage_id=fields.get("latest_stage", ""),
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

