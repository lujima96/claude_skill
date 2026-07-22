#!/usr/bin/env python3
"""Create and append tamper-evident Blender MCP edit-session journals."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import math
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SCHEMA_VERSION = "0.1.0"
RECORD_TYPES = {
    "session_started",
    "iteration_accepted",
    "iteration_rejected",
    "preview_result",
    "checkpoint_completed",
    "rollback",
    "session_closed",
}
SAFE_CHANGE_TYPES = {
    "absolute_transform",
    "visibility",
    "collection_membership",
    "vertex_positions",
}
MAX_TARGETS_PER_EDIT = 6


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def canonical_bytes(record: dict[str, Any]) -> bytes:
    payload = {key: value for key, value in record.items() if key != "record_hash"}
    return json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def calculate_record_hash(record: dict[str, Any]) -> str:
    return hashlib.sha256(canonical_bytes(record)).hexdigest()


def read_records(path: str | Path) -> list[dict[str, Any]]:
    journal = Path(path)
    if not journal.exists():
        return []
    records = []
    for line_number, line in enumerate(journal.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            raise ValueError(f"blank journal line {line_number}")
        value = json.loads(line)
        if not isinstance(value, dict):
            raise ValueError(f"journal line {line_number} is not an object")
        records.append(value)
    return records


def normalize_operations(operations: list[dict[str, Any]]) -> list[dict[str, Any]]:
    def vector(value: Any, label: str) -> list[float]:
        if not isinstance(value, (list, tuple)) or len(value) != 3:
            raise ValueError(f"{label} must contain three numbers")
        normalized_value = [float(item) for item in value]
        if not all(math.isfinite(item) for item in normalized_value):
            raise ValueError(f"{label} must contain finite numbers")
        return normalized_value

    normalized: list[dict[str, Any]] = []
    for raw in operations:
        if not isinstance(raw, dict):
            raise ValueError("each operation must be an object")
        operation = dict(raw)
        kind = operation.get("type")
        target = operation.get("target")
        if kind not in SAFE_CHANGE_TYPES:
            raise ValueError(f"unsupported session operation: {kind}")
        if not isinstance(target, str) or not target:
            raise ValueError("each operation requires one exact target")
        if kind == "absolute_transform":
            keys = [key for key in ("location", "rotation_euler", "scale") if key in operation]
            if not keys or set(operation) - {"type", "target", *keys}:
                raise ValueError("absolute_transform requires only absolute location, rotation_euler, or scale")
            operation = {"type": kind, "target": target, **{key: vector(operation[key], key) for key in keys}}
        elif kind == "visibility":
            keys = [key for key in ("hide_viewport", "hide_render") if key in operation]
            if not keys or set(operation) - {"type", "target", *keys}:
                raise ValueError("visibility requires only hide_viewport or hide_render")
            operation = {"type": kind, "target": target, **{key: bool(operation[key]) for key in keys}}
        elif kind == "collection_membership":
            collections = operation.get("collections")
            if set(operation) != {"type", "target", "collections"} or not isinstance(collections, list) or not collections or any(not isinstance(name, str) or not name for name in collections):
                raise ValueError("collection_membership requires exact collection names")
            operation = {"type": kind, "target": target, "collections": sorted(set(collections))}
        else:
            vertices = operation.get("vertices")
            if set(operation) != {"type", "target", "vertices"} or not isinstance(vertices, list) or not vertices:
                raise ValueError("vertex_positions requires exact vertex updates")
            updates = []
            seen = set()
            for update in vertices:
                if not isinstance(update, dict) or set(update) != {"index", "co"} or not isinstance(update["index"], int) or update["index"] < 0 or update["index"] in seen:
                    raise ValueError("vertex updates require unique non-negative indices and coordinates")
                seen.add(update["index"])
                updates.append({"index": update["index"], "co": vector(update["co"], "co")})
            operation = {"type": kind, "target": target, "vertices": sorted(updates, key=lambda item: item["index"])}
        operation = {key: operation[key] for key in sorted(operation)}
        normalized.append(operation)
    return normalized


def append_record(
    path: str | Path,
    *,
    session_id: str,
    record_type: str,
    targets: list[str] | None = None,
    operations: list[dict[str, Any]] | None = None,
    before_hash: str = "",
    after_hash: str = "",
    drift: dict[str, Any] | None = None,
    durations_ms: dict[str, float] | None = None,
    details: dict[str, Any] | None = None,
    timestamp: str | None = None,
) -> dict[str, Any]:
    """Append exactly one hash-chained record, refusing invalid sequencing."""
    if record_type not in RECORD_TYPES:
        raise ValueError(f"unknown record type: {record_type}")
    journal = Path(path).resolve()
    existing = read_records(journal)
    if existing and existing[-1].get("record_type") == "session_closed":
        raise ValueError("cannot append to a closed session")
    if not existing and record_type != "session_started":
        raise ValueError("the first record must be session_started")
    if existing and record_type == "session_started":
        raise ValueError("session_started may only be the first record")
    if any(item.get("session_id") != session_id for item in existing):
        raise ValueError("session_id does not match existing journal")

    exact_targets = sorted(set(targets or []))
    if len(exact_targets) > MAX_TARGETS_PER_EDIT:
        raise ValueError(f"an edit may target at most {MAX_TARGETS_PER_EDIT} objects")
    normalized = normalize_operations(operations or [])
    operation_targets = {item["target"] for item in normalized}
    if operation_targets - set(exact_targets):
        raise ValueError("operation targets must be included in exact targets")

    previous_hash = existing[-1]["record_hash"] if existing else ""
    record: dict[str, Any] = {
        "schema_version": SCHEMA_VERSION,
        "session_id": session_id,
        "sequence": len(existing) + 1,
        "previous_record_hash": previous_hash,
        "record_type": record_type,
        "timestamp": timestamp or utc_now(),
        "targets": exact_targets,
        "operations": normalized,
        "before_hash": before_hash,
        "after_hash": after_hash,
        "drift": drift or {"status": "not_applicable", "issues": []},
        "durations_ms": durations_ms or {"total": 0.0},
        "details": details or {},
    }
    record["record_hash"] = calculate_record_hash(record)
    journal.parent.mkdir(parents=True, exist_ok=True)
    mode = "a" if existing else "x"
    with journal.open(mode, encoding="utf-8") as handle:
        handle.write(json.dumps(record, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n")
        handle.flush()
        os.fsync(handle.fileno())
    return record


def preflight_cache_key(
    *, server: str, server_version: str, capabilities: list[str], working_file: str | Path, working_sha256: str
) -> dict[str, Any]:
    return {
        "server": server,
        "server_version": server_version,
        "capabilities": sorted(set(capabilities)),
        "working_file": str(Path(working_file).resolve()),
        "working_sha256": working_sha256,
    }


def should_refresh_preflight(
    cached: dict[str, Any] | None,
    current: dict[str, Any],
    *,
    reconnected: bool = False,
    tool_error: bool = False,
) -> bool:
    """Refresh only on reconnect, tool error, or a cache-key mismatch."""
    return not cached or reconnected or tool_error or cached != current


def accepted_operations(path: str | Path) -> list[dict[str, Any]]:
    """Return normalized operations needed to replay all currently accepted edits."""
    operations: list[dict[str, Any]] = []
    for record in read_records(path):
        if record.get("record_type") == "iteration_accepted":
            operations.extend(record.get("operations", []))
        elif record.get("record_type") == "rollback":
            operations = list(record.get("details", {}).get("replayed_operations", []))
    return normalize_operations(operations)


def write_pipeline_state(path: str | Path, **pointers: Any) -> dict[str, Any]:
    """Atomically update the concise authoritative asset workflow pointer."""
    destination = Path(path).resolve()
    destination.parent.mkdir(parents=True, exist_ok=True)
    existing: dict[str, Any] = {}
    if destination.is_file():
        try:
            existing = json.loads(destination.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            existing = {}

    def pointer(name: str, default: Any = None) -> Any:
        return pointers[name] if name in pointers else existing.get(name, default)

    state = {
        "schema_version": "0.1.0",
        "updated_at": utc_now(),
        "current_stage": pointer("current_stage"),
        "task_card": pointer("task_card"),
        "active_session": pointer("active_session"),
        "working_file": pointer("working_file"),
        "last_approved_checkpoint": pointer("last_approved_checkpoint"),
        "handoff": pointer("handoff"),
        "hard_failure_state": pointer("hard_failure_state", "clear"),
    }
    temporary = destination.with_suffix(destination.suffix + ".tmp")
    temporary.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    temporary.replace(destination)
    return state


def open_session(
    *,
    source_file: str | Path,
    asset_root: str | Path,
    asset_id: str,
    stage_id: str,
    task_card: str | Path,
    session_id: str,
    authorized_collections: list[str],
    safe_change_types: list[str],
    server: str,
    server_version: str,
    capabilities: list[str],
) -> dict[str, Any]:
    """Protect files once, cache preflight identity, start the journal, and point state at it."""
    if not authorized_collections:
        raise ValueError("at least one collection must be authorized")
    unknown = sorted(set(safe_change_types) - SAFE_CHANGE_TYPES)
    if not safe_change_types or unknown:
        raise ValueError("unsafe active-session change types: " + ", ".join(unknown))
    root = Path(asset_root).resolve()
    workspace = root / "source" / "mcp_sessions" / session_id
    receipt = workspace / "protection.json"
    prepare_path = Path(__file__).resolve().with_name("prepare_working_copy.py")
    spec = importlib.util.spec_from_file_location("session_prepare_working_copy", prepare_path)
    prepare_module = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(prepare_module)
    protection = prepare_module.prepare(Path(source_file), asset_id, session_id, workspace, receipt)
    cache = preflight_cache_key(
        server=server, server_version=server_version, capabilities=capabilities,
        working_file=protection["working_file"], working_sha256=protection["working_sha256_before"],
    )
    journal = root / "mcp_sessions" / f"{session_id}.jsonl"
    started = append_record(
        journal, session_id=session_id, record_type="session_started",
        before_hash=protection["working_sha256_before"], after_hash=protection["working_sha256_before"],
        durations_ms={"total": 0.0}, details={
            "asset_id": asset_id, "stage_id": stage_id, "task_card": str(Path(task_card).resolve()),
            "authorized_collections": sorted(set(authorized_collections)),
            "safe_change_types": sorted(set(safe_change_types)), "max_targets_per_edit": MAX_TARGETS_PER_EDIT,
            "source_file": protection["source_file"], "backup_file": protection["backup_file"],
            "working_file": protection["working_file"], "source_protection_receipt": str(receipt),
            "capability_preflight": cache,
        },
    )
    state = write_pipeline_state(
        root / "pipeline_state.json", current_stage=stage_id, task_card=str(Path(task_card).resolve()),
        active_session=str(journal), working_file=protection["working_file"],
    )
    return {"protection": protection, "journal": str(journal), "record": started, "pipeline_state": state}
