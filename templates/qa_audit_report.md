# QA Audit Report

## Metadata

- `audit_id`:
- `asset_id`:
- `stage_id`:
- `created_by`:
- `created_at`:
- `status`: draft | pass | revise | blocked

## Inputs

- `task_card`:
- `stage_handoff`:
- `review_reports`:
- `validation_reports`:
- `screenshots`:
- `asset_manifest`:

## Hard Failure Summary

- `hard_failures_present`: yes | no
- `blocked_stage_progression`: yes | no
- `hard_failures`:
- `required_fixes_before_progression`:

## Weighted Score

| Category | Weight | Score | Weighted Contribution | Notes |
|---|---:|---:|---:|---|
| Proportions and landmarks | 15 |  |  |  |
| Silhouette and readability | 10 |  |  |  |
| Anatomy or structural logic | 15 |  |  |  |
| Symmetry and intentional asymmetry | 5 |  |  |  |
| Topology and edge flow | 15 |  |  |  |
| UVs and baking readiness | 10 |  |  |  |
| Materials and texture logic | 10 |  |  |  |
| Deformation readiness | 10 |  |  |  |
| Performance and LODs | 5 |  |  |  |
| Godot readiness | 5 |  |  |  |

- `total_score`:
- `score_band`: ship_candidate | targeted_revision | structural_rework

Score bands:

- `ship_candidate`: 85 or higher, with no hard failures.
- `targeted_revision`: 70 to 84, with no hard failures.
- `structural_rework`: below 70, or any hard failure.

## Diagnosis

- `highest_risk_categories`:
- `most_important_fixes`:
- `accepted_limitations`:
- `deferred_items`:

## Decision

- `decision`: approve_next_stage | revise_current_stage | block_progression
- `decision_reason`:
- `next_stage`:
- `approval_required_from`:
- `approved_by`:
- `approved_at`:
