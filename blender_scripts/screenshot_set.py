#!/usr/bin/env python3
"""Capture review screenshots and write a screenshot manifest."""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.reporting import add_warning, base_report, blender_args, build_parser, finalize, write_report

DEFAULT_VIEWS = ["front", "side", "back", "three_quarter", "gameplay_distance"]


def set_view(scene, view_name: str) -> None:
    import math
    import bpy

    camera = scene.camera or next((obj for obj in bpy.data.objects if obj.type == "CAMERA"), None)
    if camera is None:
        return
    scene.camera = camera
    camera.rotation_euler = (math.radians(70), 0, 0)
    camera.location = (0, -6, 2.2)
    if view_name == "side":
        camera.location = (6, 0, 2.2)
        camera.rotation_euler = (math.radians(70), 0, math.radians(90))
    elif view_name == "back":
        camera.location = (0, 6, 2.2)
        camera.rotation_euler = (math.radians(70), 0, math.radians(180))
    elif view_name == "three_quarter":
        camera.location = (4, -5, 2.5)
        camera.rotation_euler = (math.radians(65), 0, math.radians(38))
    elif view_name == "gameplay_distance":
        camera.location = (0, -10, 3)
        camera.rotation_euler = (math.radians(72), 0, 0)


def collect_report(asset_id: str, stage_id: str, screenshot_dir: Path, views: list[str], dry_run: bool) -> dict:
    import bpy

    source_file = bpy.data.filepath or "unsaved_blender_file"
    report = base_report(
        report_type="screenshot_set",
        asset_id=asset_id,
        stage_id=stage_id,
        source_file=source_file,
    )
    scene = bpy.context.scene
    screenshot_dir.mkdir(parents=True, exist_ok=True)

    if not scene.camera and not any(obj.type == "CAMERA" for obj in bpy.data.objects):
        add_warning(report, "no_camera", "No camera exists; screenshots cannot be captured.")

    manifest_items = []
    original_camera = scene.camera
    original_filepath = scene.render.filepath
    for view in views:
        output_path = screenshot_dir / f"{asset_id}_{stage_id}_{view}.png"
        item = {
            "view": view,
            "path": str(output_path),
            "status": "planned" if dry_run else "captured",
            "required_for_review": True,
        }
        if not dry_run and not report["warnings"]:
            set_view(scene, view)
            scene.render.filepath = str(output_path)
            bpy.ops.render.render(write_still=True)
        manifest_items.append(item)

    scene.camera = original_camera
    scene.render.filepath = original_filepath
    manifest_path = screenshot_dir / f"{asset_id}_{stage_id}_screenshot_manifest.json"
    manifest = {
        "asset_id": asset_id,
        "stage_id": stage_id,
        "source_file": source_file,
        "screenshots": manifest_items,
    }
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    report["items"] = manifest_items
    report["summary"].update(
        {
            "screenshot_count": len(manifest_items),
            "manifest_path": str(manifest_path),
            "dry_run": dry_run,
        }
    )
    report["measurements"]["screenshot_manifest_status"] = "written"
    return finalize(report)


def main() -> int:
    parser = build_parser(__doc__ or "")
    parser.add_argument("--screenshot-dir", type=Path, default=Path("screenshots"))
    parser.add_argument("--views", default=",".join(DEFAULT_VIEWS))
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(blender_args(sys.argv))
    views = [view.strip() for view in args.views.split(",") if view.strip()]
    report = collect_report(args.asset_id, args.stage_id, args.screenshot_dir, views, args.dry_run)
    write_report(report, args.out, args.format)
    return 0 if not report["hard_failures"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
