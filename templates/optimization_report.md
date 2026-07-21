# Optimization Report

## Metadata

- `report_id`:
- `asset_id`:
- `stage_id`: optimization_lods
- `created_by`:
- `created_at`:
- `status`: draft | pass | warning | blocked

## Inputs

- `asset_manifest`:
- `mesh_report`:
- `material_report`:
- `export_package_report`:
- `related_task_card`:

## Budget Checks

- `target_platform`:
- `lod_count`:
- `lod_naming_status`: pass | warning | fail | unknown
- `lod_polycount_status`: pass | warning | fail | unknown
- `lod0_triangle_budget`:
- `lod1_triangle_budget`:
- `lod2_triangle_budget`:
- `material_slot_status`: pass | warning | fail | unknown
- `texture_memory_status`: pass | warning | fail | unknown

## Package Checks

- `glb_or_gltf_present`: yes | no
- `package_completeness_status`: pass | warning | fail | unknown
- `required_meshes_present`: yes | no | unknown
- `required_materials_present`: yes | no | unknown
- `required_textures_present`: yes | no | unknown
- `required_skeleton_present`: yes | no | unknown
- `required_animations_present`: yes | no | not_required | unknown
- `godot_texture_paths_status`: pass | warning | fail | unknown

## Hard Failure Check

- `hard_failures_present`: yes | no
- `hard_failures`:
- `blocked_stage_progression`: yes | no

## Decision

- `decision`: approve | approve_with_notes | revise | block
- `decision_reason`:
- `required_next_actions`:
- `suggested_next_actions`:
