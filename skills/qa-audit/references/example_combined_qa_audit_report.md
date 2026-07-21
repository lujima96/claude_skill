# Example Combined QA Audit Report

## Metadata

- `audit_id`: stylized_orc_bruiser-preproduction-qa-001
- `asset_id`: stylized_orc_bruiser
- `stage_id`: reference_gathering
- `created_by`: QA Auditor
- `created_at`: TBD
- `status`: blocked

## Inputs

- `task_card`: `skills/character-director/references/example_stylized_biped_task_card.md`
- `stage_handoff`: none yet
- `review_reports`: Reference Librarian, Style Keeper, Anatomy Reviewer example reports
- `validation_reports`: none required in Phase 4
- `screenshots`: none
- `asset_manifest`: none yet

## Hard Failure Summary

- `hard_failures_present`: yes
- `blocked_stage_progression`: yes
- `hard_failures`: approved reference set is missing
- `required_fixes_before_progression`: create local reference records or provide references for required categories

## Weighted Score

| Category | Weight | Score | Weighted Contribution | Notes |
|---|---:|---:|---:|---|
| Proportions and landmarks | 15 | pending | pending | Brief identifies proportion intent, but no proportion plan exists. |
| Silhouette and readability | 10 | pending | pending | Silhouette priorities exist but are untested. |
| Anatomy or structural logic | 15 | pending | pending | Anatomy risks are identified but not yet reviewed against refs. |
| Symmetry and intentional asymmetry | 5 | pending | pending | No asset exists. |
| Topology and edge flow | 15 | pending | pending | No mesh exists. |
| UVs and baking readiness | 10 | pending | pending | No mesh or UVs exist. |
| Materials and texture logic | 10 | pending | pending | Material families are named but not referenced. |
| Deformation readiness | 10 | pending | pending | Risks identified only. |
| Performance and LODs | 5 | pending | pending | Budgets unknown. |
| Godot readiness | 5 | pending | pending | Export not started. |

- `total_score`: pending
- `score_band`: structural_rework

## Diagnosis

- `highest_risk_categories`: reference coverage, unknown budgets, unknown Godot version, unknown skeleton and animation requirements
- `most_important_fixes`: gather references; answer target platform and Godot version; define rough technical budgets; clarify facial animation and blend-shape needs
- `accepted_limitations`: later production categories cannot be scored at preproduction stage
- `deferred_items`: topology, UV, materials, rigging, deformation, optimization, and Godot import scoring

## Decision

- `decision`: block_progression
- `decision_reason`: reference gathering cannot pass without approved reference records
- `next_stage`: reference_gathering
- `approval_required_from`: human art director or user
- `approved_by`:
- `approved_at`:
