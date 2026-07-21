# Good UV Bake Readiness

## Metadata

- `report_id`: good-uv-bake-readiness
- `asset_id`: stylized_orc_bruiser
- `stage_id`: uvs_and_baking
- `created_by`: UV Bake Reviewer
- `created_at`: 2026-07-21
- `status`: pass

## Inputs

- `retopo_mesh`: source/retopo/example.blend
- `high_poly_source`: source/sculpt/example.blend
- `uv_screenshots`: screenshots/uv/example_manifest.json
- `bake_outputs`: textures/bakes/example
- `related_task_card`: task_cards/uv_bake.example.md

## UV Checks

- `uv_sets_present`: yes
- `required_uv_sets`: UV0
- `overlap_policy`: partial
- `disallowed_overlaps_present`: no
- `texel_density_target`: 512 px/m
- `texel_density_status`: pass
- `padding_target_pixels`: 16
- `padding_status`: pass

## Bake Checks

- `bake_pairing_defined`: yes
- `cage_strategy`: cage mesh per body and gear
- `required_maps`: normal; ambient_occlusion; material_id
- `baked_maps_present`: normal; ambient_occlusion; material_id
- `bake_artifacts_present`: no
- `artifact_notes`: none

## Hard Failure Check

- `hard_failures_present`: no
- `hard_failures`: none
- `blocked_stage_progression`: no

## Decision

- `decision`: approve
- `decision_reason`: UV and bake readiness checks pass for the declared scope.
- `required_next_actions`: none
- `suggested_next_actions`: continue to material texture review
