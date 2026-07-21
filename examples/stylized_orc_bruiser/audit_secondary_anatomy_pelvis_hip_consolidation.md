# Secondary Anatomy Pelvis-Hip Consolidation QA Audit

## Metadata

- `audit_id`: stylized_orc_bruiser-secondary-anatomy-pelvis-hip-consolidation-qa-001
- `asset_id`: stylized_orc_bruiser
- `stage_id`: secondary_anatomy
- `created_by`: QA Auditor
- `created_at`: 2026-07-21
- `status`: revise

## Inputs

- `task_card`: `task_cards/secondary_anatomy_pelvis_hip_consolidation.md`
- `stage_handoff`: `handoffs/primary_forms_to_secondary_anatomy.md`
- `review_reports`: `reviews/secondary_anatomy_pelvis_hip_consolidation_anatomy_review.md`
- `validation_reports`: `validations/secondary_anatomy_pelvis_hip_consolidation_validation.md`
- `screenshots`: `screenshots/secondary_anatomy_pelvis_hip_consolidation/stylized_orc_bruiser_secondary_anatomy_screenshot_manifest.json`
- `asset_manifest`: `asset_manifest.md`

## Hard Failure Summary

- `hard_failures_present`: no
- `blocked_stage_progression`: no
- `hard_failures`: none inside pelvis-hip consolidation scope
- `required_fixes_before_progression`: human review; continue remaining secondary-anatomy cleanup and construction tasks

## Weighted Score

| Category | Weight | Score | Weighted Contribution | Notes |
|---|---:|---:|---:|---|
| Proportions and landmarks | 15 | 8 | 12.0 | Pelvis, glute, and thigh continuity remains. |
| Silhouette and readability | 10 | 8 | 8.0 | Cleaner front pelvis retains the bruiser read. |
| Anatomy or structural logic | 15 | 8 | 12.0 | Duplicate active hip layers are reduced. |
| Symmetry and intentional asymmetry | 5 | 8 | 4.0 | Paired retirement is controlled. |
| Topology and edge flow | 15 | 0 | 0.0 | Deferred to mandatory retopology. |
| UVs and baking readiness | 10 | 0 | 0.0 | Deferred. |
| Materials and texture logic | 10 | 6 | 6.0 | Placeholder identities remain coherent. |
| Deformation readiness | 10 | 6 | 6.0 | Hip landmarks remain; pose tests are pending. |
| Performance and LODs | 5 | 4 | 2.0 | Active construction count improves again, but budgets remain unknown. |
| Godot readiness | 5 | 1 | 0.5 | Target declared; export remains out of scope. |

- `total_score`: 50.5
- `score_band`: structural_rework

## Diagnosis

- `highest_risk_categories`: shin/calf layering, shoulder/pauldron clearance, facial mechanics, and downstream production work
- `most_important_fixes`: approve or revise this cleanup; audit shin/calf separately; continue required secondary anatomy afterward
- `accepted_limitations`: hidden recoverable proxies, overlapping guide construction, placeholder materials, and stage-relative score depressed by deferred work
- `deferred_items`: remaining secondary anatomy and all downstream stages

## Decision

- `decision`: revise_current_stage
- `decision_reason`: the pelvis-hip consolidation passes, but human review and other secondary-anatomy requirements remain
- `next_stage`: secondary_anatomy
- `approval_required_from`: repository user
- `approved_by`: repository user
- `approved_at`: 2026-07-21
