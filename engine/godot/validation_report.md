# Godot Validation Report

## Metadata

- `report_id`:
- `asset_id`:
- `stage_id`: export_godot_validation
- `created_by`:
- `created_at`:
- `status`: draft | pass | warning | blocked
- `godot_version`:

## Inputs

- `asset_manifest`:
- `glb_or_gltf`:
- `godot_project`:
- `imported_scene`:
- `preview_scene`:
- `export_package_report`:

## Import Checks

- `import_succeeded`: yes | no
- `scene_opens`: yes | no
- `root_node_name`:
- `mesh_count_matches_manifest`: yes | no | unknown
- `material_slots_match_manifest`: yes | no | unknown
- `texture_paths_resolve`: yes | no | unknown
- `lod_policy_documented`: yes | no

## Rig And Animation Checks

- `skeleton3d_expected`: yes | no
- `skeleton3d_present`: yes | no | not_required
- `bone_names_stable`: yes | no | not_required | unknown
- `skin_weights_present`: yes | no | not_required | unknown
- `animations_expected`: yes | no
- `animations_imported`: yes | no | not_required
- `animations_play_in_preview`: yes | no | not_required
- `blend_shapes_expected`: yes | no
- `blend_shapes_imported`: yes | no | not_required

## Scene Requirements

- `markers_expected`: yes | no
- `markers_present`: yes | no | not_required
- `collision_expected`: yes | no
- `collision_present`: yes | no | not_required
- `preview_renders`: yes | no
- `preview_screenshot`:

## Hard Failure Check

- `hard_failures_present`: yes | no
- `hard_failures`:
- `blocked_stage_progression`: yes | no

## Decision

- `decision`: approve | approve_with_notes | revise | block
- `decision_reason`:
- `required_next_actions`:
- `suggested_next_actions`:
