#!/usr/bin/env python3
"""Capture the five persistent Blender checkpoint artifacts in one process."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
from typing import Any


REPORT_NAMES = ("scene_report", "mesh_report", "material_report", "naming_report")
VIEWS = ["front", "side", "back", "three_quarter", "gameplay_distance"]


def _load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(module)
    return module


def run_checkpoint_bundle(
    *,
    project_root: str | Path,
    asset_id: str,
    stage_id: str,
    output_dir: str | Path,
    target_collection: str | None = None,
    target_objects: list[str] | None = None,
) -> dict[str, Any]:
    root = Path(project_root).resolve()
    output = Path(output_dir).resolve()
    output.mkdir(parents=True, exist_ok=True)
    scripts = root / "blender_scripts"
    screenshot_module = _load(scripts / "screenshot_set.py", "checkpoint_screenshot_set")
    screenshot_report = screenshot_module.collect_report(
        asset_id, stage_id, output / "screenshots", VIEWS, False,
        target_collection=target_collection, target_names=target_objects or [], overwrite=False,
    )
    if screenshot_report.get("hard_failures"):
        raise RuntimeError("checkpoint screenshot bundle failed")
    artifacts = [Path(screenshot_report["summary"]["manifest_path"])]
    report_statuses = {}
    for name in REPORT_NAMES:
        module = _load(scripts / f"{name}.py", f"checkpoint_{name}")
        report = module.collect_report(asset_id, stage_id)
        destination = output / f"{asset_id}_{stage_id}_{name}.json"
        with destination.open("x", encoding="utf-8") as handle:
            json.dump(report, handle, indent=2, sort_keys=True)
            handle.write("\n")
        artifacts.append(destination)
        report_statuses[name] = report["summary"]["status"]
    return {
        "bundle_version": "0.1.0",
        "artifacts": [str(path.resolve()) for path in artifacts],
        "report_statuses": report_statuses,
        "blender_call_count": 1,
    }
