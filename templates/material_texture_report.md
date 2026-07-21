# Material Texture Report

## Metadata

- `report_id`:
- `asset_id`:
- `stage_id`: texturing_materials
- `created_by`:
- `created_at`:
- `status`: draft | pass | warning | blocked

## Inputs

- `material_report`:
- `texture_manifest`:
- `export_package_report`:
- `related_task_card`:

## Material Checks

- `material_slot_count`:
- `max_material_slots`:
- `material_slot_status`: pass | warning | fail | unknown
- `material_naming_status`: pass | warning | fail | unknown
- `required_material_families`:
- `missing_material_families`:

## Texture Checks

- `texture_sets_present`: yes | no
- `texture_naming_status`: pass | warning | fail | unknown
- `texture_size_status`: pass | warning | fail | unknown
- `max_texture_size`:
- `missing_textures`:
- `channel_packing_policy`: declared | not_required | unknown
- `channel_packing_status`: pass | warning | fail | unknown
- `godot_texture_paths_status`: pass | warning | fail | unknown
- `alpha_policy`:

## Hard Failure Check

- `hard_failures_present`: yes | no
- `hard_failures`:
- `blocked_stage_progression`: yes | no

## Decision

- `decision`: approve | approve_with_notes | revise | block
- `decision_reason`:
- `required_next_actions`:
- `suggested_next_actions`:
