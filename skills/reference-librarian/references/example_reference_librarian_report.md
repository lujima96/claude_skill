# Example Reference Librarian Report

## Metadata

- `review_id`: stylized_orc_bruiser-reference_gathering-reference_librarian-001
- `asset_id`: stylized_orc_bruiser
- `stage_id`: reference_gathering
- `review_type`: reference
- `reviewer`: Reference Librarian
- `created_at`: TBD
- `status`: complete

## Inputs Reviewed

- `task_card`: pending
- `artifacts`: `skills/character-director/references/example_stylized_biped_brief.md`
- `screenshots`: none
- `validation_reports`: none
- `references`: none yet

## Review Scope

- `in_scope`: define reference coverage for stylized orc bruiser pre-production
- `out_of_scope`: web search, source licensing decisions, sculpting, topology, rigging
- `assumptions`: heroic stylized fantasy, third-person camera, Godot target

## Findings

| Severity | Category | Finding | Evidence | Recommendation | Blocking |
|---|---|---|---|---|---|
| low | coverage | Initial approved reference board exists in the example project. | `examples/stylized_orc_bruiser/reference_boards/approved_initial_board.md` and reference records exist. | Continue to add hand, hip, knee, topology, and Godot import references before later stages. | no |
| medium | production | Target platform and budgets are unknown. | Brief lists these as open questions. | Keep references platform-flexible until target constraints are known. | no |
| medium | deformation | Shoulder, jaw, neck, hip, knee, and hand references are required before blockout approval. | Orc bruiser design depends on heavy upper-body and melee deformation zones. | Require references for these zones. | no |

## Hard Failure Check

- `hard_failures_present`: no
- `hard_failures`: none for initial reference coverage
- `blocked_stage_progression`: no

## Score Contribution

- `category_scores`: reference coverage is not scored in the global QA rubric yet
- `score_notes`: initial reference coverage is sufficient for concept and early proportion planning
- `confidence`: high

## Decision

- `decision`: approve_with_notes
- `decision_reason`: initial approved reference board is sufficient for early pre-production
- `required_next_actions`: add more specific hand, hip, knee, topology, and Godot import references before those stages
- `suggested_next_actions`: ask user for preferred taste targets and target Godot/platform constraints
- `approved_by`:
- `approved_at`:
