# Stylized Orc Bruiser Godot Validation Report

## Metadata

- `report_id`: stylized_orc_bruiser-godot-validation-001
- `asset_id`: stylized_orc_bruiser
- `stage_id`: export_godot_validation
- `created_by`: Godot Export Reviewer
- `created_at`: 2026-07-21
- `status`: blocked
- `godot_version`: unknown

## Inputs

- `asset_manifest`: `asset_manifest.md`
- `glb_or_gltf`: none
- `godot_project`: none
- `imported_scene`: none
- `preview_scene`: none
- `export_package_report`: `reports/blender/export_package.sample.json`

## Import Checks

- `import_succeeded`: no
- `scene_opens`: no
- `root_node_name`: none
- `mesh_count_matches_manifest`: unknown
- `material_slots_match_manifest`: unknown
- `texture_paths_resolve`: unknown
- `lod_policy_documented`: no

## Rig And Animation Checks

- `skeleton3d_expected`: yes
- `skeleton3d_present`: no
- `bone_names_stable`: unknown
- `skin_weights_present`: unknown
- `animations_expected`: no
- `animations_imported`: not_required
- `animations_play_in_preview`: not_required
- `blend_shapes_expected`: no
- `blend_shapes_imported`: not_required

## Scene Requirements

- `markers_expected`: no
- `markers_present`: not_required
- `collision_expected`: no
- `collision_present`: not_required
- `preview_renders`: no
- `preview_screenshot`: none

## Hard Failure Check

- `hard_failures_present`: yes
- `hard_failures`: no export package; no Godot project; no imported scene; no preview render; expected Skeleton3D is missing
- `blocked_stage_progression`: yes

## Decision

- `decision`: block
- `decision_reason`: Godot readiness cannot pass because no real GLB/glTF package has been imported and previewed in Godot.
- `required_next_actions`: export production GLB/glTF; import into target Godot project; run import probe; create preview scene; capture preview screenshot; rerun validation
- `suggested_next_actions`: lock Godot version before testing
