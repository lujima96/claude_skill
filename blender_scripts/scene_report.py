#!/usr/bin/env python3
"""Generate a read-only Blender scene report."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.reporting import add_warning, base_report, blender_args, build_parser, finalize, write_report


def collect_report(asset_id: str, stage_id: str) -> dict:
    import bpy

    source_file = bpy.data.filepath or "unsaved_blender_file"
    report = base_report(
        report_type="scene",
        asset_id=asset_id,
        stage_id=stage_id,
        source_file=source_file,
    )
    scene = bpy.context.scene
    objects = list(bpy.data.objects)
    type_counts: dict[str, int] = {}
    for obj in objects:
        type_counts[obj.type] = type_counts.get(obj.type, 0) + 1

    report["summary"].update(
        {
            "scene_name": scene.name,
            "object_count": len(objects),
            "collection_count": len(bpy.data.collections),
            "mesh_count": type_counts.get("MESH", 0),
            "armature_count": type_counts.get("ARMATURE", 0),
            "camera_count": type_counts.get("CAMERA", 0),
            "light_count": type_counts.get("LIGHT", 0),
            "frame_start": scene.frame_start,
            "frame_end": scene.frame_end,
            "render_engine": scene.render.engine,
            "unit_system": scene.unit_settings.system,
            "scale_length": scene.unit_settings.scale_length,
        }
    )
    report["measurements"]["object_type_counts"] = type_counts
    report["items"] = [
        {
            "name": obj.name,
            "type": obj.type,
            "collection_count": len(obj.users_collection),
            "visible_viewport": obj.visible_get(),
            "hide_render": obj.hide_render,
        }
        for obj in objects
    ]

    if type_counts.get("MESH", 0) == 0:
        add_warning(report, "no_mesh_objects", "Scene contains no mesh objects.")
    if type_counts.get("CAMERA", 0) == 0:
        add_warning(report, "no_camera", "Scene contains no camera for screenshot capture.")
    if type_counts.get("ARMATURE", 0) == 0:
        add_warning(report, "no_armature", "Scene contains no armature yet.")

    return finalize(report)


def main() -> int:
    parser = build_parser(__doc__ or "")
    args = parser.parse_args(blender_args(sys.argv))
    report = collect_report(args.asset_id, args.stage_id)
    write_report(report, args.out, args.format)
    return 0 if not report["hard_failures"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
