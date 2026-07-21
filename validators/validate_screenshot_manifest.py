#!/usr/bin/env python3
"""Validate screenshot-manifest completeness and PNG evidence on disk."""

from __future__ import annotations

import argparse
import json
import struct
import sys
from pathlib import Path

from rules.markdown_fields import CheckResult, VALID_STAGE_IDS, render_validation_report

VERSION = "0.1.0"
DEFAULT_VIEWS = {"front", "side", "back", "three_quarter", "gameplay_distance"}


def png_dimensions(path: Path) -> tuple[int, int]:
    with path.open("rb") as handle:
        header = handle.read(24)
    if len(header) < 24 or header[:8] != b"\x89PNG\r\n\x1a\n" or header[12:16] != b"IHDR":
        raise ValueError("not a valid PNG header")
    return struct.unpack(">II", header[16:24])


def validate(path: Path, required_views: set[str]):
    data = json.loads(path.read_text(encoding="utf-8"))
    failures: list[CheckResult] = []
    warnings: list[CheckResult] = []
    items = data.get("screenshots", [])
    stage_id = data.get("stage_id", "")
    if stage_id not in VALID_STAGE_IDS:
        failures.append(CheckResult("valid_stage_id", "Manifest stage must be canonical", stage_id, "Use a canonical pipeline stage ID."))
    source = Path(data.get("source_file", ""))
    if not source.is_file() or source.suffix.lower() != ".blend":
        failures.append(CheckResult("source_exists", "Manifest source must be an existing .blend working file", str(source), "Capture evidence from the protected working copy."))
    views = [str(item.get("view", "")) for item in items]
    paths = [str(item.get("path", "")) for item in items]
    if len(views) != len(set(views)) or len(paths) != len(set(paths)):
        failures.append(CheckResult("unique_evidence", "Screenshot views and paths must be unique", str(views), "Use one unique file per required view."))
    missing_views = sorted(required_views - set(views))
    if missing_views:
        failures.append(CheckResult("required_views", "Required screenshot views are missing", ", ".join(missing_views), "Capture every required view."))
    for item in items:
        view = str(item.get("view", "unknown"))
        image_path = Path(str(item.get("path", "")))
        if item.get("status") != "captured":
            failures.append(CheckResult("captured_status", f"View `{view}` is not captured", str(item.get("status")), "Render and verify the image before approval."))
            continue
        try:
            width, height = png_dimensions(image_path)
        except Exception as exc:
            failures.append(CheckResult("valid_png", f"View `{view}` is missing or invalid", f"{image_path}: {exc}", "Regenerate the screenshot."))
            continue
        if image_path.stat().st_size <= 0:
            failures.append(CheckResult("nonempty_png", f"View `{view}` is empty", str(image_path), "Regenerate the screenshot."))
        if item.get("width") != width or item.get("height") != height:
            failures.append(CheckResult("image_dimensions", f"View `{view}` dimensions do not match the manifest", f"actual {width}x{height}, manifest {item.get('width')}x{item.get('height')}", "Regenerate the manifest from captured files."))
    return failures, warnings, data, {"screenshot_count": len(items), "required_view_count": len(required_views)}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--required-views", default=",".join(sorted(DEFAULT_VIEWS)))
    args = parser.parse_args()
    try:
        required = {value.strip() for value in args.required_views.split(",") if value.strip()}
        failures, warnings, data, measurements = validate(args.path, required)
        print(render_validation_report(
            validator_name="validate_screenshot_manifest", validator_version=VERSION, input_path=args.path,
            repo_root=args.repo_root, asset_id=str(data.get("asset_id", "")), stage_id=str(data.get("stage_id", "")),
            failures=failures, warnings=warnings, measurements=measurements,
        ))
        return 1 if failures else 0
    except Exception as exc:
        print(f"validator error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
