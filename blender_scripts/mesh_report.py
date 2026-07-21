#!/usr/bin/env python3
"""Generate a read-only Blender mesh geometry report."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.reporting import add_warning, base_report, blender_args, build_parser, finalize, write_report


def collect_report(asset_id: str, stage_id: str) -> dict:
    import bpy

    source_file = bpy.data.filepath or "unsaved_blender_file"
    report = base_report(
        report_type="mesh",
        asset_id=asset_id,
        stage_id=stage_id,
        source_file=source_file,
        blender_version=bpy.app.version_string,
    )
    mesh_objects = [obj for obj in bpy.data.objects if obj.type == "MESH"]
    totals = {
        "vertices": 0,
        "edges": 0,
        "faces": 0,
        "triangles": 0,
        "material_slots": 0,
        "shape_keys": 0,
        "vertex_groups": 0,
    }
    items = []
    for obj in mesh_objects:
        mesh = obj.data
        triangle_count = sum(max(0, len(poly.vertices) - 2) for poly in mesh.polygons)
        shape_key_count = 0
        if mesh.shape_keys and mesh.shape_keys.key_blocks:
            shape_key_count = max(0, len(mesh.shape_keys.key_blocks) - 1)
        item = {
            "object": obj.name,
            "mesh": mesh.name,
            "vertices": len(mesh.vertices),
            "edges": len(mesh.edges),
            "faces": len(mesh.polygons),
            "triangles": triangle_count,
            "material_slots": len(obj.material_slots),
            "modifiers": [modifier.type for modifier in obj.modifiers],
            "shape_keys": shape_key_count,
            "vertex_groups": len(obj.vertex_groups),
            "has_armature_modifier": any(modifier.type == "ARMATURE" for modifier in obj.modifiers),
        }
        items.append(item)
        totals["vertices"] += item["vertices"]
        totals["edges"] += item["edges"]
        totals["faces"] += item["faces"]
        totals["triangles"] += item["triangles"]
        totals["material_slots"] += item["material_slots"]
        totals["shape_keys"] += item["shape_keys"]
        totals["vertex_groups"] += item["vertex_groups"]
        if item["material_slots"] == 0:
            add_warning(report, "mesh_without_material", "Mesh object has no material slots.", obj.name)
        if not item["has_armature_modifier"] and len(obj.vertex_groups) > 0:
            add_warning(report, "vertex_groups_without_armature", "Mesh has vertex groups but no armature modifier.", obj.name)

    report["summary"].update({"mesh_object_count": len(mesh_objects), **totals})
    report["measurements"] = totals
    report["items"] = items
    if not mesh_objects:
        add_warning(report, "no_mesh_objects", "Scene contains no mesh objects.")
    return finalize(report)


def main() -> int:
    parser = build_parser(__doc__ or "")
    args = parser.parse_args(blender_args(sys.argv))
    report = collect_report(args.asset_id, args.stage_id)
    write_report(report, args.out, args.format, overwrite=args.overwrite)
    return 0 if not report["hard_failures"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
