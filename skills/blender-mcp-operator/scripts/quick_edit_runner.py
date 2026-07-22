#!/usr/bin/env python3
"""Apply one declarative, topology-preserving edit inside protected Blender."""

from __future__ import annotations

import hashlib
import json
import struct
import time
from pathlib import Path
from typing import Any


MAX_TARGETS = 6
OPERATION_TYPES = {"absolute_transform", "visibility", "collection_membership", "vertex_positions"}


def sha256(path: str | Path) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _vector(value: Any, label: str) -> list[float]:
    if not isinstance(value, (list, tuple)) or len(value) != 3:
        raise ValueError(f"{label} must contain exactly three numbers")
    return [float(item) for item in value]


def normalize_request(request: dict[str, Any]) -> dict[str, Any]:
    targets = request.get("target_objects", [])
    if not isinstance(targets, list) or not 1 <= len(set(targets)) <= MAX_TARGETS or len(targets) != len(set(targets)):
        raise ValueError("quick edit requires 1-6 unique target objects")
    if any(not isinstance(item, str) or not item for item in targets):
        raise ValueError("target names must be non-empty strings")
    collections = request.get("authorized_collections", [])
    if not isinstance(collections, list) or not collections:
        raise ValueError("authorized_collections must be a non-empty list")
    operations = request.get("operations", [])
    if not isinstance(operations, list) or not operations:
        raise ValueError("operations must be a non-empty list")
    normalized = []
    for raw in operations:
        if not isinstance(raw, dict) or raw.get("type") not in OPERATION_TYPES:
            raise ValueError("operation type is not safe for quick edit")
        if raw.get("target") not in targets:
            raise ValueError("operation target is outside target_objects")
        kind = raw["type"]
        item: dict[str, Any] = {"target": raw["target"], "type": kind}
        if kind == "absolute_transform":
            provided = False
            for key in ("location", "rotation_euler", "scale"):
                if key in raw:
                    item[key] = _vector(raw[key], key)
                    provided = True
            if not provided:
                raise ValueError("absolute_transform must set location, rotation_euler, or scale")
        elif kind == "visibility":
            if not {"hide_viewport", "hide_render"} & set(raw):
                raise ValueError("visibility must set hide_viewport or hide_render")
            for key in ("hide_viewport", "hide_render"):
                if key in raw:
                    item[key] = bool(raw[key])
        elif kind == "collection_membership":
            memberships = raw.get("collections")
            if not isinstance(memberships, list) or not memberships or any(name not in collections for name in memberships):
                raise ValueError("collection memberships must be a non-empty subset of authorized_collections")
            item["collections"] = sorted(set(memberships))
        else:
            updates = raw.get("vertices")
            if not isinstance(updates, list) or not updates:
                raise ValueError("vertex_positions requires vertex updates")
            vertices = []
            seen = set()
            for update in updates:
                index = update.get("index") if isinstance(update, dict) else None
                if not isinstance(index, int) or index < 0 or index in seen:
                    raise ValueError("vertex indices must be unique non-negative integers")
                seen.add(index)
                vertices.append({"index": index, "co": _vector(update.get("co"), "co")})
            item["vertices"] = sorted(vertices, key=lambda value: value["index"])
        normalized.append(item)
    return {
        "request_version": "0.1.0",
        "working_file": str(Path(request["working_file"]).resolve()),
        "expected_working_sha256": request.get("expected_working_sha256", ""),
        "expected_scene_hash": request.get("expected_scene_hash", ""),
        "authorized_collections": sorted(set(collections)),
        "target_objects": sorted(targets),
        "operations": normalized,
    }


def _material_signature(material: Any) -> dict[str, Any]:
    nodes = []
    if material.use_nodes and material.node_tree:
        for node in sorted(material.node_tree.nodes, key=lambda value: value.name):
            inputs = []
            for socket in node.inputs:
                value = getattr(socket, "default_value", None)
                if isinstance(value, (str, bool, int, float)):
                    inputs.append([socket.name, value])
                elif value is not None:
                    try:
                        inputs.append([socket.name, [round(float(item), 8) for item in value]])
                    except (TypeError, ValueError):
                        pass
            nodes.append([node.name, node.type, inputs])
    return {
        "name": material.name,
        "use_nodes": bool(material.use_nodes),
        "diffuse_color": [round(float(value), 8) for value in material.diffuse_color],
        "nodes": nodes,
    }


def _object_signature(obj: Any) -> dict[str, Any]:
    mesh = None
    if obj.type == "MESH":
        coordinates = hashlib.sha256()
        vertex_coordinates = []
        for vertex in obj.data.vertices:
            coordinate = [round(float(value), 10) for value in vertex.co]
            coordinates.update(struct.pack("3d", *coordinate))
            vertex_coordinates.append(coordinate)
        mesh = {
            "vertices": len(obj.data.vertices),
            "edges": len(obj.data.edges),
            "faces": len(obj.data.polygons),
            "coordinate_sha256": coordinates.hexdigest(),
            "coordinates": vertex_coordinates,
        }
    return {
        "name": obj.name,
        "type": obj.type,
        "location": [round(float(value), 10) for value in obj.location],
        "rotation_euler": [round(float(value), 10) for value in obj.rotation_euler],
        "scale": [round(float(value), 10) for value in obj.scale],
        "matrix_world": [round(float(value), 10) for row in obj.matrix_world for value in row],
        "parent": obj.parent.name if obj.parent else None,
        "data_name": obj.data.name if obj.data else None,
        "modifiers": [[modifier.name, modifier.type] for modifier in obj.modifiers],
        "collections": sorted(collection.name for collection in obj.users_collection),
        "hide_viewport": bool(obj.hide_viewport),
        "hide_render": bool(obj.hide_render),
        "materials": [slot.material.name if slot.material else None for slot in obj.material_slots],
        "mesh": mesh,
    }


def capture_scene(bpy: Any) -> dict[str, Any]:
    snapshot = {
        "objects": {obj.name: _object_signature(obj) for obj in bpy.data.objects},
        "materials": {material.name: _material_signature(material) for material in bpy.data.materials},
    }
    encoded = json.dumps(snapshot, sort_keys=True, separators=(",", ":")).encode("utf-8")
    snapshot["scene_hash"] = hashlib.sha256(encoded).hexdigest()
    return snapshot


def _apply_operation(bpy: Any, operation: dict[str, Any]) -> None:
    obj = bpy.data.objects.get(operation["target"])
    if obj is None:
        raise ValueError(f"target object is missing: {operation['target']}")
    kind = operation["type"]
    if kind == "absolute_transform":
        for key in ("location", "rotation_euler", "scale"):
            if key in operation:
                setattr(obj, key, operation[key])
    elif kind == "visibility":
        for key in ("hide_viewport", "hide_render"):
            if key in operation:
                setattr(obj, key, operation[key])
    elif kind == "collection_membership":
        desired = set(operation["collections"])
        for collection in list(obj.users_collection):
            if collection.name not in desired:
                collection.objects.unlink(obj)
        for name in desired:
            collection = bpy.data.collections.get(name)
            if collection is None:
                raise ValueError(f"authorized collection is missing: {name}")
            if collection not in obj.users_collection:
                collection.objects.link(obj)
    else:
        if obj.type != "MESH":
            raise ValueError(f"vertex update target is not a mesh: {obj.name}")
        for update in operation["vertices"]:
            if update["index"] >= len(obj.data.vertices):
                raise ValueError(f"vertex index is out of range: {update['index']}")
            obj.data.vertices[update["index"]].co = update["co"]
        obj.data.update()


def _drift(
    before: dict[str, Any],
    after: dict[str, Any],
    targets: set[str],
    operations: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    before_objects, after_objects = before["objects"], after["objects"]
    before_names, after_names = set(before_objects), set(after_objects)
    issues = []
    if before_names - after_names:
        issues.append({"type": "deleted_or_renamed_objects", "objects": sorted(before_names - after_names)})
    if after_names - before_names:
        issues.append({"type": "added_or_renamed_objects", "objects": sorted(after_names - before_names)})
    changed = sorted(name for name in before_names & after_names if before_objects[name] != after_objects[name])
    unexpected = sorted(set(changed) - targets)
    if unexpected:
        issues.append({"type": "non_target_changes", "objects": unexpected})
    topology = []
    for name in sorted(targets & before_names & after_names):
        old, new = before_objects[name]["mesh"], after_objects[name]["mesh"]
        old_counts = tuple(old[key] for key in ("vertices", "edges", "faces")) if old else None
        new_counts = tuple(new[key] for key in ("vertices", "edges", "faces")) if new else None
        if old_counts != new_counts:
            topology.append(name)
    if topology:
        issues.append({"type": "topology_changes", "objects": topology})
    if before["materials"] != after["materials"]:
        issues.append({"type": "material_changes"})
    if operations is not None:
        allowed_fields: dict[str, set[str]] = {name: set() for name in targets}
        allowed_vertices: dict[str, set[int]] = {name: set() for name in targets}
        for operation in operations:
            kind, target = operation["type"], operation["target"]
            if kind == "absolute_transform":
                allowed_fields[target].update({key for key in ("location", "rotation_euler", "scale") if key in operation})
                allowed_fields[target].add("matrix_world")
            elif kind == "visibility":
                allowed_fields[target].update({key for key in ("hide_viewport", "hide_render") if key in operation})
            elif kind == "collection_membership":
                allowed_fields[target].add("collections")
            else:
                allowed_fields[target].add("mesh")
                allowed_vertices[target].update(update["index"] for update in operation["vertices"])
        unauthorized = []
        vertex_drift = []
        for name in sorted(targets & before_names & after_names):
            old, new = before_objects[name], after_objects[name]
            changed_fields = {key for key in old if old.get(key) != new.get(key)}
            extra = sorted(changed_fields - allowed_fields[name])
            if extra:
                unauthorized.append({"object": name, "fields": extra})
            if "mesh" in allowed_fields[name] and old.get("mesh") and new.get("mesh"):
                old_coordinates = old["mesh"].get("coordinates", [])
                new_coordinates = new["mesh"].get("coordinates", [])
                changed_indices = {index for index, pair in enumerate(zip(old_coordinates, new_coordinates)) if pair[0] != pair[1]}
                unexpected_indices = sorted(changed_indices - allowed_vertices[name])
                if unexpected_indices:
                    vertex_drift.append({"object": name, "vertices": unexpected_indices})
        if unauthorized:
            issues.append({"type": "unauthorized_target_changes", "changes": unauthorized})
        if vertex_drift:
            issues.append({"type": "unexpected_vertex_changes", "changes": vertex_drift})
    return {"status": "fail" if issues else "pass", "issues": issues, "changed_objects": changed}


def _acceptance_issues(after: dict[str, Any], operations: list[dict[str, Any]]) -> list[dict[str, Any]]:
    def matches(actual: Any, wanted: Any) -> bool:
        if isinstance(actual, list) and isinstance(wanted, list) and len(actual) == len(wanted):
            if all(isinstance(value, (int, float)) for value in [*actual, *wanted]):
                return all(abs(float(left) - float(right)) <= 1e-6 for left, right in zip(actual, wanted))
        return actual == wanted

    expected: dict[str, dict[str, Any]] = {}
    for operation in operations:
        target = expected.setdefault(operation["target"], {})
        if operation["type"] == "absolute_transform":
            for key in ("location", "rotation_euler", "scale"):
                if key in operation:
                    target[key] = [round(float(value), 10) for value in operation[key]]
        elif operation["type"] == "visibility":
            for key in ("hide_viewport", "hide_render"):
                if key in operation:
                    target[key] = operation[key]
        elif operation["type"] == "collection_membership":
            target["collections"] = operation["collections"]
        else:
            vertices = target.setdefault("vertices", {})
            for update in operation["vertices"]:
                vertices[update["index"]] = [round(float(value), 10) for value in update["co"]]
    issues = []
    for name, values in expected.items():
        actual = after["objects"].get(name, {})
        for key, expected_value in values.items():
            if key == "vertices":
                coordinates = (actual.get("mesh") or {}).get("coordinates", [])
                mismatched = sorted(index for index, coordinate in expected_value.items() if index >= len(coordinates) or not matches(coordinates[index], coordinate))
                if mismatched:
                    issues.append({"object": name, "field": "vertices", "indices": mismatched})
            elif not matches(actual.get(key), expected_value):
                issues.append({"object": name, "field": key, "expected": expected_value, "actual": actual.get(key)})
    return issues


def run_quick_edit(request: dict[str, Any], bpy_module: Any | None = None) -> dict[str, Any]:
    """Validate, apply, drift-check, and save a single edit; recover on failure."""
    started = time.perf_counter()
    phase: dict[str, float] = {}
    normalized = normalize_request(request)
    bpy = bpy_module
    if bpy is None:
        import bpy as bpy_module_imported
        bpy = bpy_module_imported
    working = Path(normalized["working_file"])
    if not working.is_file() or working.suffix.lower() != ".blend":
        raise ValueError("working_file must be an existing .blend file")
    if not bpy.data.filepath or Path(bpy.data.filepath).resolve() != working.resolve():
        raise ValueError("Blender is not displaying the protected working file")
    if bpy.data.is_dirty:
        raise ValueError("Blender working file must be clean before quick edit")
    file_hash_before = sha256(working)
    if normalized["expected_working_sha256"] and normalized["expected_working_sha256"] != file_hash_before:
        raise ValueError("working-file hash mismatch")

    mark = time.perf_counter()
    before = capture_scene(bpy)
    phase["fingerprint_before"] = (time.perf_counter() - mark) * 1000
    if normalized["expected_scene_hash"] and normalized["expected_scene_hash"] != before["scene_hash"]:
        raise ValueError("scene fingerprint mismatch")
    authorized = set(normalized["authorized_collections"])
    for name in normalized["target_objects"]:
        obj = bpy.data.objects.get(name)
        if obj is None:
            raise ValueError(f"target object is missing: {name}")
        memberships = {collection.name for collection in obj.users_collection}
        if not memberships & authorized:
            raise ValueError(f"target is outside authorized collections: {name}")

    try:
        mark = time.perf_counter()
        for operation in normalized["operations"]:
            _apply_operation(bpy, operation)
        phase["apply"] = (time.perf_counter() - mark) * 1000
        mark = time.perf_counter()
        after = capture_scene(bpy)
        drift = _drift(before, after, set(normalized["target_objects"]), normalized["operations"])
        acceptance_issues = _acceptance_issues(after, normalized["operations"])
        if acceptance_issues:
            drift["issues"].append({"type": "acceptance_mismatch", "changes": acceptance_issues})
            drift["status"] = "fail"
        phase["validate_delta"] = (time.perf_counter() - mark) * 1000
        if drift["status"] != "pass":
            raise RuntimeError("unexpected scene drift: " + json.dumps(drift["issues"], sort_keys=True))
        mark = time.perf_counter()
        bpy.ops.wm.save_as_mainfile(filepath=str(working))
        phase["save"] = (time.perf_counter() - mark) * 1000
        if bpy.data.is_dirty:
            raise RuntimeError("Blender remained dirty after save")
    except Exception:
        bpy.ops.wm.open_mainfile(filepath=str(working))
        raise

    total = (time.perf_counter() - started) * 1000
    return {
        "result_version": "0.1.0",
        "status": "accepted",
        "working_file": str(working.resolve()),
        "working_sha256_before": file_hash_before,
        "working_sha256_after": sha256(working),
        "before_hash": before["scene_hash"],
        "after_hash": after["scene_hash"],
        "targets": normalized["target_objects"],
        "operations": normalized["operations"],
        "drift": drift,
        "durations_ms": {**{key: round(value, 3) for key, value in phase.items()}, "total": round(total, 3)},
    }
