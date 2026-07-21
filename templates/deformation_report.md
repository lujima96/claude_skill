# Deformation Report

## Metadata

- `report_id`:
- `asset_id`:
- `stage_id`: rigging_skinning | deformation_testing
- `created_by`:
- `created_at`:
- `status`: draft | pass | warning | blocked

## Inputs

- `source_blend`:
- `scene_report`:
- `pose_battery_report`:
- `mesh_report`:
- `screenshots`:
- `approved_rig_contract`:
- `related_task_card`:

## Rig Summary

- `armature_count`:
- `skeleton_root`:
- `naming_convention`:
- `rest_pose`:
- `scale_policy`:
- `skinned_mesh_count`:
- `max_skin_influences`:
- `unweighted_vertices`:
- `blend_shapes`:
- `animation_clips`:

## Pose Battery

| Pose | Required | Result | Evidence | Corrective Needed |
|---|---|---|---|---|
| bind_pose | yes | pending |  |  |
| shoulder_raise | yes | pending |  |  |
| elbow_bend | yes | pending |  |  |
| wrist_twist | yes | pending |  |  |
| hip_flex | yes | pending |  |  |
| knee_bend | yes | pending |  |  |
| ankle_bend | yes | pending |  |  |
| neck_turn | yes | pending |  |  |
| jaw_open | depends | pending |  |  |
| blink | depends | pending |  |  |

## Godot Import Risks

- `target_godot_version`:
- `skeleton3d_expected`:
- `bone_name_stability`:
- `skin_weight_import_risk`:
- `animation_import_risk`:
- `blend_shape_import_risk`:

## Hard Failure Check

- `hard_failures_present`: yes | no
- `hard_failures`:
- `blocked_stage_progression`: yes | no

## Decision

- `decision`: approve | approve_with_notes | revise | block
- `decision_reason`:
- `required_next_actions`:
- `suggested_next_actions`:
