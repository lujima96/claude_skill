# Example Style Keeper Report

## Metadata

- `review_id`: stylized_orc_bruiser-concept_interpretation-style_keeper-001
- `asset_id`: stylized_orc_bruiser
- `stage_id`: concept_interpretation
- `review_type`: style
- `reviewer`: Style Keeper
- `created_at`: TBD
- `status`: complete

## Inputs Reviewed

- `task_card`: `skills/character-director/references/example_stylized_biped_task_card.md`
- `artifacts`: `skills/character-director/references/example_stylized_biped_brief.md`
- `screenshots`: none
- `validation_reports`: none
- `references`: none yet

## Review Scope

- `in_scope`: style-family contract for first brief
- `out_of_scope`: anatomy approval, reference approval, sculpting, topology, rigging
- `assumptions`: third-person Godot game, heroic stylized orc bruiser

## Findings

| Severity | Category | Finding | Evidence | Recommendation | Blocking |
|---|---|---|---|---|---|
| low | style_family | Heroic stylized is a suitable style family. | Brief calls for stylized orc bruiser with heavy silhouette. | Keep heroic stylized as the default unless user provides another style target. | no |
| medium | silhouette | Silhouette priorities are defined but not yet proven. | Broad shoulders, thick neck, heavy jaw, hands, and tusks are listed. | Require silhouette checks during proportion planning and blockout. | no |
| medium | materials | Material treatment is directionally defined but needs references. | Skin, leather, metal, cloth, bone, hair, and eyes are not yet sourced. | Reference Librarian should gather material examples. | no |

## Hard Failure Check

- `hard_failures_present`: no
- `hard_failures`: none in style scope
- `blocked_stage_progression`: no

## Score Contribution

- `category_scores`: silhouette/readability pending; materials pending
- `score_notes`: style direction is usable for reference gathering
- `confidence`: medium

## Decision

- `decision`: approve_with_notes
- `decision_reason`: style contract is strong enough for reference gathering but needs reference support
- `required_next_actions`: gather heroic stylized proportion, silhouette, and material references
- `suggested_next_actions`: ask user for preferred games or art examples if they have a taste target
- `approved_by`:
- `approved_at`:
