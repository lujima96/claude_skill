# Good Godot Validation Report

## Metadata

- `report_id`: good-godot-validation
- `asset_id`: stylized_orc_bruiser
- `stage_id`: export_godot_validation
- `created_by`: Godot Export Reviewer
- `created_at`: 2026-07-21
- `status`: pass
- `godot_version`: 4.3

## Inputs

- `asset_manifest`: asset_manifest.md
- `glb_or_gltf`: exports/stylized_orc_bruiser.glb
- `godot_project`: engine/godot/test_project
- `imported_scene`: res://characters/stylized_orc_bruiser.glb
- `preview_scene`: res://preview/stylized_orc_bruiser_preview.tscn
- `export_package_report`: reports/blender/export_package.json

## Import Checks

- `import_succeeded`: yes
- `scene_opens`: yes
- `root_node_name`: StylizedOrcBruiser
- `mesh_count_matches_manifest`: yes
- `material_slots_match_manifest`: yes
- `texture_paths_resolve`: yes
- `lod_policy_documented`: yes

## Rig And Animation Checks

- `skeleton3d_expected`: yes
- `skeleton3d_present`: yes
- `bone_names_stable`: yes
- `skin_weights_present`: yes
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
- `preview_renders`: yes
- `preview_screenshot`: screenshots/godot/preview.png

## Hard Failure Check

- `hard_failures_present`: no
- `hard_failures`: none
- `blocked_stage_progression`: no

## Decision

- `decision`: approve
- `decision_reason`: Godot import and preview checks pass.
- `required_next_actions`: none
- `suggested_next_actions`: archive final package
