# Stylized Orc Bruiser UV Bake Review

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

- `in_scope`: UV presence, overlap policy, texel density, padding, bake source/target pairing, bake artifact blockers
- `out_of_scope`: material art approval, texture painting, rigging, Godot import
- `assumptions`: no approved retopology mesh, UV layout, or bake package exists yet

## Findings

| Severity | Category | Finding | Evidence | Recommendation | Blocking |
|---|---|---|---|---|---|
| critical | missing_uvs | Required UV sets are missing or unreviewable. | `asset_manifest.md` lists `retopo_files: none`; no UV report or UV screenshots exist. | Approve retopology first, then submit a UV report with required UV sets. | yes |
| critical | overlap_policy | UV overlap policy is not declared. | No task card or report defines whether mirrored, stacked, or unique UVs are required. | Define allowed overlaps by material family and baked map type. | yes |
| high | bake_pairing | Bake source and target pairing is missing. | Manifest lists `sculpt_files: none`, `retopo_files: none`, and `texture_source_files: none`. | Identify high-poly source, low-poly target, cage strategy, and required baked maps. | yes |
| medium | texel_density | Texel density and padding targets are unknown. | No UV/bake task card exists. | Set target texture size, texel density, and padding before bake validation. | no |

## Hard Failure Check

- `hard_failures_present`: yes
- `hard_failures`: UV sets, UV overlap policy, and bake source/target pairing are missing
- `blocked_stage_progression`: yes

## Score Contribution

- `category_scores`: UVs and baking readiness 0/10; materials dependency unresolved
- `score_notes`: The review blocks because UV and bake artifacts do not exist yet.
- `confidence`: high

## Decision

- `decision`: block
- `decision_reason`: UV and bake approval cannot proceed without approved retopology, UV evidence, overlap policy, and bake source/target planning.
- `required_next_actions`: approve retopology; create UV/bake task card; produce UV report; define overlap policy, texel density, padding, cage strategy, and required baked maps
- `suggested_next_actions`: decide whether mirrored UVs are allowed for skin, armor, cloth, and weapons before baking
- `approved_by`: none
- `approved_at`: none
