#!/usr/bin/env python3
"""Generate a read-only Blender naming and transform report."""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.reporting import add_warning, base_report, blender_args, build_parser, finalize, write_report

NAME_PATTERN = re.compile(r"^[A-Za-z][A-Za-z0-9_]*$")
GENERATED_SUFFIX = re.compile(r"\.\d{3}$")


def near(value: float, target: float, tolerance: float = 0.001) -> bool:
    return abs(value - target) <= tolerance


def collect_report(asset_id: str, stage_id: str) -> dict:
    import bpy

    source_file = bpy.data.filepath or "unsaved_blender_file"
    report = base_report(
        report_type="naming",
        asset_id=asset_id,
        stage_id=stage_id,
        source_file=source_file,
        blender_version=bpy.app.version_string,
    )
    items = []
    for obj in bpy.data.objects:
        scale_applied = all(near(axis, 1.0) for axis in obj.scale)
        rotation_clear = all(near(axis, 0.0) for axis in obj.rotation_euler)
        name_valid = bool(NAME_PATTERN.match(obj.name)) and not GENERATED_SUFFIX.search(obj.name)
        item = {
            "object": obj.name,
            "type": obj.type,
            "name_valid": name_valid,
            "scale": [round(value, 5) for value in obj.scale],
            "rotation_euler": [round(value, 5) for value in obj.rotation_euler],
            "scale_applied": scale_applied,
            "rotation_clear": rotation_clear,
            "negative_scale": any(value < 0 for value in obj.scale),
        }
        items.append(item)
        if not name_valid:
            add_warning(report, "object_name_invalid", "Object name is not pipeline-friendly.", obj.name)
        if item["negative_scale"]:
            add_warning(report, "negative_scale", "Object has negative scale.", obj.name)
        if not scale_applied:
            add_warning(report, "scale_not_applied", "Object scale is not 1,1,1.", obj.name)

    report["items"] = items
    report["summary"].update(
        {
            "object_count": len(items),
            "invalid_name_count": sum(1 for item in items if not item["name_valid"]),
            "non_applied_scale_count": sum(1 for item in items if not item["scale_applied"]),
            "negative_scale_count": sum(1 for item in items if item["negative_scale"]),
        }
    )
    report["measurements"].update(report["summary"])
    return finalize(report)


def main() -> int:
    parser = build_parser(__doc__ or "")
    args = parser.parse_args(blender_args(sys.argv))
    report = collect_report(args.asset_id, args.stage_id)
    write_report(report, args.out, args.format, overwrite=args.overwrite)
    return 0 if not report["hard_failures"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
