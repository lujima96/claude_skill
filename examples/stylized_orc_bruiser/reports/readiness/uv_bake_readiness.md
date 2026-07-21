# Stylized Orc Bruiser UV Bake Readiness

## Metadata

- `report_id`: stylized_orc_bruiser-uv-bake-readiness-001
- `asset_id`: stylized_orc_bruiser
- `stage_id`: uvs_and_baking
- `created_by`: UV Bake Reviewer
- `created_at`: 2026-07-21
- `status`: blocked

## Inputs

- `retopo_mesh`: none
- `high_poly_source`: none
- `uv_screenshots`: none
- `bake_outputs`: none
- `related_task_card`: pending

## UV Checks

- `uv_sets_present`: no
- `required_uv_sets`: UV0 for base textures
- `overlap_policy`: unknown
- `disallowed_overlaps_present`: unknown
- `texel_density_target`: unknown
- `texel_density_status`: unknown
- `padding_target_pixels`: unknown
- `padding_status`: unknown

## Bake Checks

- `bake_pairing_defined`: no
- `cage_strategy`: unknown
- `required_maps`: normal; ambient_occlusion; material_id
- `baked_maps_present`: none
- `bake_artifacts_present`: unknown
- `artifact_notes`: no bake exists

## Hard Failure Check

- `hard_failures_present`: yes
- `hard_failures`: UV sets are missing; overlap policy is unknown; bake source/target pairing is missing
- `blocked_stage_progression`: yes

## Decision

- `decision`: block
- `decision_reason`: UV and bake readiness cannot pass until real retopology, UV, overlap, and bake evidence exists.
- `required_next_actions`: approve retopology; create UVs; define overlap policy; define texel density and padding; create bake source/target plan
- `suggested_next_actions`: produce UV screenshots and bake report from Blender during the next production pass
