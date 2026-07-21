#!/usr/bin/env python3
"""Capture and verify bounded Blender scene deltas for quick iterations."""

from __future__ import annotations

import hashlib
import json
import struct
from datetime import datetime, timezone
from pathlib import Path


SAFE_CHANGE_TYPES = {
    "transform",
    "visibility",
    "collection_membership",
    "vertex_positions",
}
MAX_TARGETS = 6
MAX_ITERATIONS = 3


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_bounds(target_objects: list[str], allowed_change_types: list[str], iteration_index: int) -> None:
    if not 1 <= len(set(target_objects)) <= MAX_TARGETS:
        raise ValueError(f"quick iteration requires 1-{MAX_TARGETS} unique target objects")
    unknown = sorted(set(allowed_change_types) - SAFE_CHANGE_TYPES)
    if unknown:
        raise ValueError("unsafe quick-iteration change types: " + ", ".join(unknown))
    if not 1 <= iteration_index <= MAX_ITERATIONS:
        raise ValueError(f"quick iteration index must be 1-{MAX_ITERATIONS}")


def _mesh_signature(obj) -> dict:
    mesh = obj.data
    coordinate_hash = hashlib.sha256()
    for vertex in mesh.vertices:
        coordinate_hash.update(struct.pack("3d", *vertex.co))
    return {
        "vertices": len(mesh.vertices),
        "edges": len(mesh.edges),
        "faces": len(mesh.polygons),
        "coordinate_sha256": coordinate_hash.hexdigest(),
    }


def _object_signature(obj) -> dict:
    return {
        "type": obj.type,
        "matrix_world": [round(value, 10) for row in obj.matrix_world for value in row],
        "collections": sorted(collection.name for collection in obj.users_collection),
        "hide_viewport": bool(obj.hide_viewport),
        "hide_render": bool(obj.hide_render),
        "materials": [slot.material.name if slot.material else None for slot in obj.material_slots],
        "mesh": _mesh_signature(obj) if obj.type == "MESH" else None,
    }


def _material_signature(material) -> dict:
    node_values = []
    if material.use_nodes and material.node_tree:
        for node in sorted(material.node_tree.nodes, key=lambda item: item.name):
            inputs = []
            for socket in node.inputs:
                value = getattr(socket, "default_value", None)
                if isinstance(value, (int, float, bool, str)):
                    inputs.append([socket.name, value])
                elif value is not None:
                    try:
                        inputs.append([socket.name, [round(float(item), 8) for item in value]])
                    except (TypeError, ValueError):
                        pass
            node_values.append([node.name, node.type, inputs])
    return {
        "use_nodes": bool(material.use_nodes),
        "diffuse_color": [round(float(item), 8) for item in material.diffuse_color],
        "nodes": node_values,
    }


def capture_scene() -> dict:
    import bpy

    working = Path(bpy.data.filepath).resolve() if bpy.data.filepath else None
    return {
        "snapshot_version": "0.1.0",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "working_file": str(working) if working else "",
        "working_sha256": sha256(working) if working and working.is_file() else "",
        "objects": {obj.name: _object_signature(obj) for obj in bpy.data.objects},
        "materials": {material.name: _material_signature(material) for material in bpy.data.materials},
    }


def write_snapshot(path: str | Path) -> dict:
    destination = Path(path).resolve()
    destination.parent.mkdir(parents=True, exist_ok=True)
    snapshot = capture_scene()
    with destination.open("x", encoding="utf-8") as handle:
        json.dump(snapshot, handle, indent=2, sort_keys=True)
        handle.write("\n")
    return snapshot


def finalize_receipt(
    before_path: str | Path,
    out_path: str | Path,
    *,
    asset_id: str,
    stage_id: str,
    microtask_id: str,
    iteration_id: str,
    iteration_index: int,
    target_objects: list[str],
    allowed_change_types: list[str],
    source_file: str | Path,
    backup_file: str | Path,
    working_file: str | Path,
    protection_receipt: str | Path,
    screenshot_manifest: str | Path,
) -> dict:
    import bpy

    validate_bounds(target_objects, allowed_change_types, iteration_index)
    source = Path(source_file).resolve(strict=True)
    backup = Path(backup_file).resolve(strict=True)
    working = Path(working_file).resolve(strict=True)
    if Path(bpy.data.filepath).resolve() != working:
        raise ValueError("current Blender file is not the protected working file")

    before = json.loads(Path(before_path).read_text(encoding="utf-8"))
    after = capture_scene()
    if Path(before.get("working_file", "")).resolve() != working:
        raise ValueError("pre-edit snapshot belongs to a different working file")

    before_objects = before.get("objects", {})
    after_objects = after.get("objects", {})
    before_names = set(before_objects)
    after_names = set(after_objects)
    missing = sorted(before_names - after_names)
    added = sorted(after_names - before_names)
    changed = sorted(name for name in before_names & after_names if before_objects[name] != after_objects[name])
    targets = set(target_objects)
    unexpected = sorted(set(changed) - targets)
    topology_changes = []
    for name in sorted(targets & before_names & after_names):
        old_mesh = before_objects[name].get("mesh")
        new_mesh = after_objects[name].get("mesh")
        old_counts = tuple(old_mesh.get(key) for key in ("vertices", "edges", "faces")) if old_mesh else None
        new_counts = tuple(new_mesh.get(key) for key in ("vertices", "edges", "faces")) if new_mesh else None
        if old_counts != new_counts:
            topology_changes.append(name)

    material_changes = before.get("materials", {}) != after.get("materials", {})
    protection = json.loads(Path(protection_receipt).read_text(encoding="utf-8"))
    hard_failures = []
    if missing:
        hard_failures.append("missing_objects")
    if added:
        hard_failures.append("added_objects")
    if unexpected:
        hard_failures.append("unexpected_changed_objects")
    if topology_changes:
        hard_failures.append("topology_count_changes")
    if material_changes:
        hard_failures.append("material_changes")

    payload = {
        "receipt_version": "0.1.0",
        "evidence_tier": "quick_iteration",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "asset_id": asset_id,
        "stage_id": stage_id,
        "microtask_id": microtask_id,
        "iteration_id": iteration_id,
        "iteration_index": iteration_index,
        "target_objects": sorted(targets),
        "allowed_change_types": sorted(set(allowed_change_types)),
        "changed_objects": changed,
        "unexpected_changed_objects": unexpected,
        "missing_objects": missing,
        "added_objects": added,
        "topology_count_changes": topology_changes,
        "material_changes": material_changes,
        "protected_objects_checked": len(before_names - targets),
        "destructive_operations": False,
        "hard_failures": hard_failures,
        "source_file": str(source),
        "backup_file": str(backup),
        "working_file": str(working),
        "source_sha256_before": protection["source_sha256_before"],
        "source_sha256_after": sha256(source),
        "backup_sha256": sha256(backup),
        "working_sha256_before": before.get("working_sha256", protection["working_sha256_before"]),
        "working_sha256_after": sha256(working),
        "screenshot_manifest": str(Path(screenshot_manifest).resolve()),
    }
    destination = Path(out_path).resolve()
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("x", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, sort_keys=True)
        handle.write("\n")
    return payload
