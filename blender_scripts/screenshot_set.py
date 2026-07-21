#!/usr/bin/env python3
"""Capture bounded, reversible Blender review screenshots and a manifest."""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.reporting import (
    add_hard_failure,
    add_warning,
    base_report,
    blender_args,
    build_parser,
    finalize,
    write_report,
)

DEFAULT_VIEWS = ["front", "side", "back", "three_quarter", "gameplay_distance"]
VALID_VIEWS = {*DEFAULT_VIEWS, "face_closeup"}


def _target_objects(target_collection: str | None, target_names: list[str]) -> tuple[list, list[str]]:
    import bpy

    missing: list[str] = []
    if target_collection:
        collection = bpy.data.collections.get(target_collection)
        if collection is None:
            return [], [f"collection:{target_collection}"]
        candidates = list(collection.all_objects)
    elif target_names:
        candidates = []
        for name in target_names:
            obj = bpy.data.objects.get(name)
            if obj is None:
                missing.append(f"object:{name}")
            else:
                candidates.append(obj)
    else:
        candidates = [obj for obj in bpy.context.scene.objects if obj.visible_get()]
    return [obj for obj in candidates if obj.type == "MESH"], missing


def _world_bounds(objects: list) -> tuple:
    from mathutils import Vector

    corners = [obj.matrix_world @ Vector(corner) for obj in objects for corner in obj.bound_box]
    minimum = Vector((min(v.x for v in corners), min(v.y for v in corners), min(v.z for v in corners)))
    maximum = Vector((max(v.x for v in corners), max(v.y for v in corners), max(v.z for v in corners)))
    return minimum, maximum, (minimum + maximum) * 0.5


def _aim(obj, target) -> None:
    obj.rotation_euler = (target - obj.location).to_track_quat("-Z", "Y").to_euler()


def _create_review_rig(scene, center, extent: float):
    import bpy
    from mathutils import Vector

    collection = bpy.data.collections.new("MCP_REVIEW_TEMP")
    scene.collection.children.link(collection)

    camera_data = bpy.data.cameras.new("MCP_REVIEW_TEMP_CAMERA")
    camera_data.lens = 50
    camera = bpy.data.objects.new("MCP_REVIEW_TEMP_CAMERA", camera_data)
    collection.objects.link(camera)

    lights = []
    light_specs = [
        ("KEY", Vector((0.8, -1.0, 1.2)), 1200.0, 5.0),
        ("FILL", Vector((-1.0, -0.4, 0.7)), 700.0, 6.0),
        ("RIM", Vector((0.5, 1.0, 1.0)), 900.0, 4.0),
    ]
    for suffix, direction, energy, size in light_specs:
        data = bpy.data.lights.new(f"MCP_REVIEW_TEMP_{suffix}", "AREA")
        data.energy = energy
        data.shape = "DISK"
        data.size = size
        light = bpy.data.objects.new(data.name, data)
        collection.objects.link(light)
        light.location = center + direction.normalized() * max(extent * 2.5, 4.0)
        _aim(light, center)
        lights.append(light)
    return collection, camera, lights


def _remove_review_rig(collection, camera, lights) -> None:
    import bpy

    for light in lights:
        data = light.data
        bpy.data.objects.remove(light, do_unlink=True)
        bpy.data.lights.remove(data)
    camera_data = camera.data
    bpy.data.objects.remove(camera, do_unlink=True)
    bpy.data.cameras.remove(camera_data)
    bpy.data.collections.remove(collection)


def _camera_position(view: str, center, distance: float, height: float):
    from mathutils import Vector

    if view == "front":
        return center + Vector((0, -distance, 0))
    if view == "side":
        return center + Vector((distance, 0, 0))
    if view == "back":
        return center + Vector((0, distance, 0))
    if view == "three_quarter":
        diagonal = distance / math.sqrt(2)
        return center + Vector((diagonal, -diagonal, height * 0.08))
    if view == "gameplay_distance":
        return center + Vector((0, -distance * 1.8, height * 0.12))
    return center + Vector((0, -max(distance * 0.55, 1.0), height * 0.25))


def _set_review_render_engine(scene) -> str:
    """Select Eevee across Blender versions without assuming one enum name."""
    for engine in ("BLENDER_EEVEE_NEXT", "BLENDER_EEVEE"):
        try:
            scene.render.engine = engine
            return engine
        except (TypeError, ValueError):
            continue
    raise RuntimeError("No supported Eevee render engine is available.")


def _write_json(path: Path, value: object, overwrite: bool) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    mode = "w" if overwrite else "x"
    with path.open(mode, encoding="utf-8") as handle:
        json.dump(value, handle, indent=2)
        handle.write("\n")


def collect_report(
    asset_id: str,
    stage_id: str,
    screenshot_dir: Path,
    views: list[str],
    dry_run: bool,
    *,
    target_collection: str | None = None,
    target_names: list[str] | None = None,
    resolution: int = 768,
    overwrite: bool = False,
) -> dict:
    import bpy

    source_file = bpy.data.filepath or "unsaved_blender_file"
    report = base_report(
        report_type="screenshot_set",
        asset_id=asset_id,
        stage_id=stage_id,
        source_file=source_file,
        blender_version=bpy.app.version_string,
    )
    scene = bpy.context.scene
    target_names = target_names or []

    invalid_views = [view for view in views if view not in VALID_VIEWS]
    if invalid_views:
        add_hard_failure(report, "invalid_views", "Unknown review views were requested.", ", ".join(invalid_views))
    targets, missing = _target_objects(target_collection, target_names)
    if missing:
        add_hard_failure(report, "missing_targets", "Requested screenshot targets do not exist.", ", ".join(missing))
    if not targets:
        add_hard_failure(report, "no_mesh_targets", "No mesh targets are available for screenshot framing.")

    manifest_path = screenshot_dir / f"{asset_id}_{stage_id}_screenshot_manifest.json"
    output_paths = [screenshot_dir / f"{asset_id}_{stage_id}_{view}.png" for view in views]
    existing = [str(path) for path in [manifest_path, *output_paths] if path.exists()]
    if existing and not overwrite:
        add_hard_failure(report, "evidence_exists", "Refusing to overwrite screenshot evidence.", "; ".join(existing))

    manifest_items = [
        {
            "view": view,
            "path": str(path.resolve()),
            "status": "planned" if dry_run else "pending",
            "required_for_review": True,
            "width": resolution,
            "height": resolution,
        }
        for view, path in zip(views, output_paths)
    ]

    state = {
        "camera": scene.camera,
        "filepath": scene.render.filepath,
        "engine": scene.render.engine,
        "resolution_x": scene.render.resolution_x,
        "resolution_y": scene.render.resolution_y,
        "resolution_percentage": scene.render.resolution_percentage,
        "file_format": scene.render.image_settings.file_format,
        "film_transparent": scene.render.film_transparent,
        "hide_render": {obj: obj.hide_render for obj in scene.objects if obj not in targets and obj.type == "MESH"},
    }
    review_collection = camera = None
    lights: list = []
    bounds_payload: dict[str, list[float]] = {}

    if not report["hard_failures"] and not dry_run:
        try:
            minimum, maximum, center = _world_bounds(targets)
            size = maximum - minimum
            height = max(size.z, 0.1)
            extent = max(size.x, size.y, size.z, 0.1)
            bounds_payload = {
                "minimum": [round(v, 6) for v in minimum],
                "maximum": [round(v, 6) for v in maximum],
                "center": [round(v, 6) for v in center],
            }
            review_collection, camera, lights = _create_review_rig(scene, center, extent)
            for obj in state["hide_render"]:
                obj.hide_render = True
            scene.camera = camera
            _set_review_render_engine(scene)
            scene.render.resolution_x = resolution
            scene.render.resolution_y = resolution
            scene.render.resolution_percentage = 100
            scene.render.image_settings.file_format = "PNG"
            scene.render.film_transparent = False
            distance = max(extent / (2 * math.tan(camera.data.angle_y / 2)) * 1.45, 2.0)

            screenshot_dir.mkdir(parents=True, exist_ok=True)
            for item, output_path in zip(manifest_items, output_paths):
                camera.location = _camera_position(item["view"], center, distance, height)
                aim_target = center
                if item["view"] == "face_closeup":
                    aim_target = center.copy()
                    aim_target.z = maximum.z - height * 0.2
                _aim(camera, aim_target)
                scene.render.filepath = str(output_path.resolve())
                try:
                    bpy.ops.render.render(write_still=True)
                except Exception as exc:
                    item["status"] = "failed"
                    add_hard_failure(report, "render_failed", f"Failed to render {item['view']} view.", str(exc))
                    continue
                if output_path.is_file() and output_path.stat().st_size > 0:
                    item["status"] = "captured"
                    item["bytes"] = output_path.stat().st_size
                    item["camera_location"] = [round(v, 6) for v in camera.location]
                    item["camera_rotation_euler"] = [round(v, 6) for v in camera.rotation_euler]
                else:
                    item["status"] = "failed"
                    add_hard_failure(report, "missing_screenshot", f"Rendered {item['view']} view is missing or empty.", str(output_path))
        finally:
            scene.camera = state["camera"]
            scene.render.filepath = state["filepath"]
            scene.render.engine = state["engine"]
            scene.render.resolution_x = state["resolution_x"]
            scene.render.resolution_y = state["resolution_y"]
            scene.render.resolution_percentage = state["resolution_percentage"]
            scene.render.image_settings.file_format = state["file_format"]
            scene.render.film_transparent = state["film_transparent"]
            for obj, hidden in state["hide_render"].items():
                obj.hide_render = hidden
            if review_collection is not None and camera is not None:
                _remove_review_rig(review_collection, camera, lights)

    captured = sum(item["status"] == "captured" for item in manifest_items)
    state_restored = (
        scene.camera is state["camera"]
        and scene.render.filepath == state["filepath"]
        and scene.render.engine == state["engine"]
        and scene.render.resolution_x == state["resolution_x"]
        and scene.render.resolution_y == state["resolution_y"]
        and scene.render.resolution_percentage == state["resolution_percentage"]
        and scene.render.image_settings.file_format == state["file_format"]
        and scene.render.film_transparent == state["film_transparent"]
        and all(obj.hide_render == hidden for obj, hidden in state["hide_render"].items())
        and "MCP_REVIEW_TEMP" not in bpy.data.collections
    )
    if not state_restored:
        add_hard_failure(report, "scene_state_not_restored", "Temporary screenshot state was not fully restored.")
    if not dry_run and captured != len(manifest_items) and not report["hard_failures"]:
        add_hard_failure(report, "incomplete_screenshot_set", "Not all required screenshots were captured.")

    manifest = {
        "manifest_version": "0.2.0",
        "asset_id": asset_id,
        "stage_id": stage_id,
        "source_file": source_file,
        "blender_version": bpy.app.version_string,
        "target_collection": target_collection or "none",
        "target_objects": [obj.name for obj in targets],
        "target_bounds": bounds_payload or "not_measured",
        "screenshots": manifest_items,
    }
    try:
        _write_json(manifest_path, manifest, overwrite)
        manifest_status = "planned" if dry_run else "written"
    except FileExistsError:
        manifest_status = "blocked_existing"
        if not any(item.get("rule_id") == "evidence_exists" for item in report["hard_failures"]):
            add_hard_failure(report, "evidence_exists", "Refusing to overwrite screenshot manifest.", str(manifest_path))

    report["items"] = manifest_items
    report["summary"].update(
        {
            "screenshot_count": len(manifest_items),
            "captured_count": captured,
            "manifest_path": str(manifest_path.resolve()),
            "dry_run": dry_run,
        }
    )
    report["measurements"].update(
        {
            "screenshot_manifest_status": manifest_status,
            "scene_state_restored": "yes" if state_restored else "no",
            "target_objects": [obj.name for obj in targets],
            "hidden_non_target_meshes": [obj.name for obj in state["hide_render"]],
            "target_bounds": bounds_payload or "not_measured",
        }
    )
    if dry_run:
        add_warning(report, "dry_run", "Screenshot paths were planned but images were not rendered.")
    return finalize(report)


def main() -> int:
    parser = build_parser(__doc__ or "")
    parser.add_argument("--screenshot-dir", type=Path, default=Path("screenshots"))
    parser.add_argument("--views", default=",".join(DEFAULT_VIEWS))
    targets = parser.add_mutually_exclusive_group()
    targets.add_argument("--target-collection")
    targets.add_argument("--target-objects", help="Comma-separated exact Blender object names.")
    parser.add_argument("--resolution", type=int, default=768)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(blender_args(sys.argv))
    views = [view.strip() for view in args.views.split(",") if view.strip()]
    target_names = [name.strip() for name in (args.target_objects or "").split(",") if name.strip()]
    report = collect_report(
        args.asset_id,
        args.stage_id,
        args.screenshot_dir,
        views,
        args.dry_run,
        target_collection=args.target_collection,
        target_names=target_names,
        resolution=args.resolution,
        overwrite=args.overwrite,
    )
    write_report(report, args.out, args.format, overwrite=args.overwrite)
    return 0 if not report["hard_failures"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
