# Bad QA Audit Example

## Metadata

- `audit_id`: bad-qa-001
- `asset_id`: stylized_orc_bruiser
- `stage_id`: anatomy_blockout_planning
- `created_by`: Test
- `created_at`: 2026-07-21
- `status`: pass

## Inputs

- `task_card`: task_cards/anatomy_blockout_planning.md
- `stage_handoff`: handoffs/anatomy_to_manual_blockout.md
- `review_reports`: reviews/anatomy_review.md
- `validation_reports`: validations/phase5_manual_validation.md

## Hard Failure Summary

- `hard_failures_present`: yes
- `blocked_stage_progression`: yes
- `hard_failures`: deliberate example
- `required_fixes_before_progression`: fix deliberate example

## Weighted Score

| Category | Weight | Score | Weighted Contribution | Notes |
|---|---:|---:|---:|---|
| Proportions and landmarks | 15 | 8 | 1.0 | Wrong contribution on purpose. |
| Silhouette and readability | 10 | 8 | 8.0 | Correct row. |

- `total_score`: 99
- `score_band`: ship_candidate

## Decision

- `decision`: approve_next_stage
- `decision_reason`: wrong on purpose
- `next_stage`: manual_blockout
- `approval_required_from`: Test
