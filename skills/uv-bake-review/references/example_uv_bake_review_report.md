# Example UV Bake Review Report

## Metadata

- `review_id`: stylized_orc_bruiser-uvs_and_baking-uv_bake_reviewer-001
- `asset_id`: stylized_orc_bruiser
- `stage_id`: uvs_and_baking
- `review_type`: uv_bake
- `reviewer`: UV Bake Reviewer
- `created_at`: 2026-07-21
- `status`: blocked

## Inputs Reviewed

- `task_card`: pending
- `artifacts`: `asset_manifest.md`; `reports/blender/mesh_report.sample.json`
- `screenshots`: none
- `validation_reports`: none
- `references`: `knowledge/topology/biped_deformation_loops.md`; `knowledge/materials/godot_character_materials.md`

## Review Scope

- `in_scope`: UV presence, UV overlap policy, texel density, padding, bake source/target pairing, bake artifact blockers
- `out_of_scope`: material art approval, rigging, Godot import
- `assumptions`: no approved retopology mesh or UV report exists yet

## Findings

| Severity | Category | Finding | Evidence | Recommendation | Blocking |
|---|---|---|---|---|---|
| critical | missing_uvs | UV sets cannot be confirmed. | Asset manifest lists `retopo_files: none`; no UV report exists. | Produce approved retopology mesh and UV report before bake review. | yes |
| critical | overlap_policy | UV overlap policy is not declared. | No task card or UV report defines allowed mirrored or stacked overlaps. | Define which materials may overlap and which baked maps require unique UVs. | yes |
| high | bake_pairing | Bake source and target pairing is missing. | Manifest lists `sculpt_files: none` and `retopo_files: none`. | Identify high-poly source, low-poly target, cage strategy, and required map list. | yes |

## Hard Failure Check

- `hard_failures_present`: yes
- `hard_failures`: UV evidence, overlap policy, and bake source/target pairing are missing
- `blocked_stage_progression`: yes

## Score Contribution

- `category_scores`: UVs and baking readiness 0/10; topology dependency unresolved
- `score_notes`: Review blocks because UV and bake artifacts do not exist yet.
- `confidence`: high

## Decision

- `decision`: block
- `decision_reason`: UV and bake approval cannot proceed without an approved retopo mesh, UV report, overlap policy, and bake source/target plan.
- `required_next_actions`: approve retopology first; create UV/bake task card; produce UV report; define overlap policy, texel density, padding, cage, and required maps
- `suggested_next_actions`: decide whether mirrored UVs are allowed for armor, cloth, and skin detail before baking
- `approved_by`: none
- `approved_at`: none
