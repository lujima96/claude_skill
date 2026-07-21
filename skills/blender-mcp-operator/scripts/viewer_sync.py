#!/usr/bin/env python3
"""Leave Blender cleanly displaying the exact validated working file."""

from __future__ import annotations

import hashlib
from pathlib import Path


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def sync_viewer(expected_working_file: str | Path) -> dict:
    import bpy

    expected = Path(expected_working_file).resolve(strict=True)
    if not expected.is_file() or expected.suffix.lower() != ".blend":
        raise ValueError("expected working file must be an existing .blend file")
    if not bpy.data.filepath:
        raise ValueError("Blender has no current filepath; refusing to discard an unknown scene")

    current = Path(bpy.data.filepath).resolve()
    if current != expected:
        raise ValueError(
            "Blender is displaying a different file; refusing to discard or replace it during viewer sync"
        )

    expected_hash = sha256(expected)
    bpy.ops.wm.open_mainfile(filepath=str(expected))
    reloaded = Path(bpy.data.filepath).resolve()
    if reloaded != expected:
        raise RuntimeError("Blender did not reload the expected working file")
    if bpy.data.is_dirty:
        raise RuntimeError("Blender remained dirty after reloading the validated working file")
    actual_hash = sha256(expected)
    if actual_hash != expected_hash:
        raise RuntimeError("working file changed during viewer sync")

    return {
        "viewer_sync": "pass",
        "working_file": str(expected),
        "working_sha256": actual_hash,
        "blender_filepath": bpy.data.filepath,
        "is_dirty": bool(bpy.data.is_dirty),
    }
