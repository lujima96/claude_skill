#!/usr/bin/env python3
"""Generate a read-only armature pose-battery readiness report."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.reporting import add_warning, base_report, blender_args, build_parser, finalize, write_report

REQUIRED_POSE_TESTS = [
    "bind_pose",
    "shoulder_raise",
    "elbow_bend",
    "wrist_twist",
    "hip_flex",
    "knee_bend",
    "ankle_bend",
    "neck_turn",
    "jaw_open_if_required",
]


def collect_report(asset_id: str, stage_id: str) -> dict:
    import bpy

    source_file = bpy.data.filepath or "unsaved_blender_file"
    report = base_report(
        report_type="pose_battery",
        asset_id=asset_id,
        stage_id=stage_id,
        source_file=source_file,
        blender_version=bpy.app.version_string,
    )
    armatures = [obj for obj in bpy.data.objects if obj.type == "ARMATURE"]
    meshes = [obj for obj in bpy.data.objects if obj.type == "MESH"]
    skinned_meshes = [
        obj for obj in meshes if any(modifier.type == "ARMATURE" for modifier in obj.modifiers)
    ]

    report["summary"].update(
        {
            "armature_count": len(armatures),
            "mesh_count": len(meshes),
            "skinned_mesh_count": len(skinned_meshes),
            "required_pose_tests": REQUIRED_POSE_TESTS,
        }
    )
    report["items"] = [
        {
            "armature": armature.name,
            "bone_count": len(armature.data.bones),
            "pose_bone_count": len(armature.pose.bones) if armature.pose else 0,
        }
        for armature in armatures
    ]
    if not armatures:
        add_warning(report, "no_armature", "No armature exists; pose battery cannot run yet.")
    if not skinned_meshes:
        add_warning(report, "no_skinned_meshes", "No mesh has an armature modifier yet.")
    report["measurements"]["pose_battery_status"] = "readiness_only"
    return finalize(report)


def main() -> int:
    parser = build_parser(__doc__ or "")
    args = parser.parse_args(blender_args(sys.argv))
    report = collect_report(args.asset_id, args.stage_id)
    write_report(report, args.out, args.format, overwrite=args.overwrite)
    return 0 if not report["hard_failures"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
