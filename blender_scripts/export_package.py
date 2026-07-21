#!/usr/bin/env python3
"""Generate a GLB/glTF export readiness report, with optional explicit export."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.reporting import add_hard_failure, add_warning, base_report, blender_args, build_parser, finalize, write_report


def collect_report(asset_id: str, stage_id: str, export_path: Path | None, execute_export: bool) -> dict:
    import bpy

    source_file = bpy.data.filepath or "unsaved_blender_file"
    report = base_report(
        report_type="export_package",
        asset_id=asset_id,
        stage_id=stage_id,
        source_file=source_file,
    )
    meshes = [obj for obj in bpy.data.objects if obj.type == "MESH"]
    armatures = [obj for obj in bpy.data.objects if obj.type == "ARMATURE"]
    animations = list(bpy.data.actions)

    report["summary"].update(
        {
            "mesh_count": len(meshes),
            "armature_count": len(armatures),
            "animation_count": len(animations),
            "execute_export": execute_export,
            "export_path": str(export_path) if export_path else "not_requested",
        }
    )
    report["items"] = {
        "meshes": [obj.name for obj in meshes],
        "armatures": [obj.name for obj in armatures],
        "animations": [action.name for action in animations],
    }
    if not meshes:
        add_hard_failure(report, "no_meshes", "Cannot export a character package without mesh objects.")
    if not armatures:
        add_warning(report, "no_armature", "No armature exists; export may not be animation-ready.")
    if execute_export:
        if export_path is None:
            add_hard_failure(report, "missing_export_path", "`--execute-export` requires `--export-path`.")
        elif report["hard_failures"]:
            add_hard_failure(report, "export_blocked", "Export blocked because readiness hard failures exist.")
        else:
            export_path.parent.mkdir(parents=True, exist_ok=True)
            bpy.ops.export_scene.gltf(
                filepath=str(export_path),
                export_format="GLB" if export_path.suffix.lower() == ".glb" else "GLTF_SEPARATE",
                export_apply=True,
            )
            report["measurements"]["export_status"] = "written"
    else:
        report["measurements"]["export_status"] = "dry_run"
    return finalize(report)


def main() -> int:
    parser = build_parser(__doc__ or "")
    parser.add_argument("--export-path", type=Path)
    parser.add_argument(
        "--execute-export",
        action="store_true",
        help="Actually write GLB/glTF. Omitted by default for read-only readiness reporting.",
    )
    args = parser.parse_args(blender_args(sys.argv))
    report = collect_report(args.asset_id, args.stage_id, args.export_path, args.execute_export)
    write_report(report, args.out, args.format)
    return 0 if not report["hard_failures"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
