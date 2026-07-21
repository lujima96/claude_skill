# UV Bake Report

## Metadata

- `report_id`:
- `asset_id`:
- `stage_id`: uvs_and_baking
- `created_by`:
- `created_at`:
- `status`: draft | pass | warning | blocked

## Inputs

- `retopo_mesh`:
- `high_poly_source`:
- `uv_screenshots`:
- `bake_outputs`:
- `related_task_card`:

## UV Checks

- `uv_sets_present`: yes | no
- `required_uv_sets`:
- `overlap_policy`: allowed | disallowed | partial | unknown
- `disallowed_overlaps_present`: yes | no | unknown
- `texel_density_target`:
- `texel_density_status`: pass | warning | fail | unknown
- `padding_target_pixels`:
- `padding_status`: pass | warning | fail | unknown

## Bake Checks

- `bake_pairing_defined`: yes | no
- `cage_strategy`:
- `required_maps`:
- `baked_maps_present`:
- `bake_artifacts_present`: yes | no | unknown
- `artifact_notes`:

## Hard Failure Check

- `hard_failures_present`: yes | no
- `hard_failures`:
- `blocked_stage_progression`: yes | no

## Decision

- `decision`: approve | approve_with_notes | revise | block
- `decision_reason`:
- `required_next_actions`:
- `suggested_next_actions`:
