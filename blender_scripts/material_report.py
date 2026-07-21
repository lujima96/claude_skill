#!/usr/bin/env python3
"""Generate a read-only Blender material and texture report."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.reporting import add_warning, base_report, blender_args, build_parser, finalize, write_report


def image_path_status(image) -> str:
    if not image.filepath:
        return "embedded_or_generated"
    resolved = Path(image.filepath_from_user())
    return "exists" if resolved.exists() else "missing"


def collect_report(asset_id: str, stage_id: str) -> dict:
    import bpy

    source_file = bpy.data.filepath or "unsaved_blender_file"
    report = base_report(
        report_type="material",
        asset_id=asset_id,
        stage_id=stage_id,
        source_file=source_file,
        blender_version=bpy.app.version_string,
    )
    items = []
    missing_images = []
    for material in bpy.data.materials:
        image_nodes = []
        if material.use_nodes and material.node_tree:
            for node in material.node_tree.nodes:
                if node.type == "TEX_IMAGE" and node.image:
                    status = image_path_status(node.image)
                    image_nodes.append(
                        {
                            "node": node.name,
                            "image": node.image.name,
                            "filepath": node.image.filepath,
                            "status": status,
                        }
                    )
                    if status == "missing":
                        missing_images.append(f"{material.name}:{node.image.filepath}")
        items.append(
            {
                "material": material.name,
                "use_nodes": material.use_nodes,
                "users": material.users,
                "image_node_count": len(image_nodes),
                "images": image_nodes,
            }
        )

    report["items"] = items
    report["summary"].update(
        {
            "material_count": len(bpy.data.materials),
            "image_count": len(bpy.data.images),
            "missing_image_count": len(missing_images),
        }
    )
    report["measurements"]["missing_images"] = missing_images or "none"
    if not bpy.data.materials:
        add_warning(report, "no_materials", "Scene contains no materials.")
    for missing in missing_images:
        add_warning(report, "missing_image_file", "Image texture path does not exist.", missing)
    return finalize(report)


def main() -> int:
    parser = build_parser(__doc__ or "")
    args = parser.parse_args(blender_args(sys.argv))
    report = collect_report(args.asset_id, args.stage_id)
    write_report(report, args.out, args.format, overwrite=args.overwrite)
    return 0 if not report["hard_failures"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
