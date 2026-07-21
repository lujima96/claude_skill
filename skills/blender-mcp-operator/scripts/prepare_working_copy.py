#!/usr/bin/env python3
"""Create hash-verified, non-overwriting Blender backup and working copies."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path


SAFE_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_-]*$")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def exclusive_copy(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    with source.open("rb") as src, destination.open("xb") as dst:
        shutil.copyfileobj(src, dst)
    shutil.copystat(source, destination)


def prepare(source: Path, asset_id: str, microtask_id: str, workspace: Path, receipt: Path) -> dict:
    source = source.resolve(strict=True)
    workspace = workspace.resolve()
    receipt = receipt.resolve()
    if not source.is_file() or source.suffix.lower() != ".blend":
        raise ValueError("source must be an existing .blend file")
    for label, value in (("asset_id", asset_id), ("microtask_id", microtask_id)):
        if not SAFE_ID.fullmatch(value):
            raise ValueError(f"{label} must contain only letters, numbers, underscores, and hyphens")

    base = f"{asset_id}.{microtask_id}"
    backup = workspace / "backups" / f"{base}.before.blend"
    working = workspace / "working" / f"{base}.working.blend"
    protected_paths = [backup, working, receipt]
    existing = [str(path) for path in protected_paths if path.exists()]
    if existing:
        raise FileExistsError("refusing to overwrite existing protection artifacts: " + ", ".join(existing))
    if source in {backup, working} or backup == working:
        raise ValueError("source, backup, and working paths must be distinct")

    created: list[Path] = []
    try:
        exclusive_copy(source, backup)
        created.append(backup)
        exclusive_copy(source, working)
        created.append(working)
        source_hash = sha256(source)
        backup_hash = sha256(backup)
        working_hash = sha256(working)
        if len({source_hash, backup_hash, working_hash}) != 1:
            raise RuntimeError("source protection hashes do not match")
        payload = {
            "receipt_version": "0.1.0",
            "created_at": datetime.now(timezone.utc).isoformat(),
            "asset_id": asset_id,
            "microtask_id": microtask_id,
            "source_file": str(source),
            "backup_file": str(backup),
            "working_file": str(working),
            "source_sha256_before": source_hash,
            "backup_sha256": backup_hash,
            "working_sha256_before": working_hash,
            "source_size_bytes": source.stat().st_size,
            "backup_verified": True,
            "working_copy_verified": True,
        }
        receipt.parent.mkdir(parents=True, exist_ok=True)
        with receipt.open("x", encoding="utf-8") as handle:
            json.dump(payload, handle, indent=2)
            handle.write("\n")
        created.append(receipt)
        return payload
    except Exception:
        for path in reversed(created):
            path.unlink(missing_ok=True)
        raise


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("--asset-id", required=True)
    parser.add_argument("--microtask-id", required=True)
    parser.add_argument("--workspace", type=Path, required=True)
    parser.add_argument("--receipt", type=Path, required=True)
    args = parser.parse_args()
    try:
        print(json.dumps(prepare(args.source, args.asset_id, args.microtask_id, args.workspace, args.receipt), indent=2))
        return 0
    except Exception as exc:
        print(f"prepare working copy error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
