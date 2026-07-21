# Axial Primary-Forms QA Audit

## Metadata

- `audit_id`: stylized_orc_bruiser-primary-forms-axial-qa-001
- `asset_id`: stylized_orc_bruiser
- `stage_id`: primary_forms
- `created_by`: QA Auditor
- `created_at`: 2026-07-21
- `status`: revise

## Inputs

- `task_card`: `task_cards/primary_forms_axial_masses.md`
- `stage_handoff`: `handoffs/blockout_to_primary_forms.md`
- `review_reports`: `reviews/primary_forms_axial_masses_anatomy_review.md`
- `validation_reports`: `validations/primary_forms_axial_masses_validation.md`
- `screenshots`: `screenshots/primary_forms_axial_masses/stylized_orc_bruiser_primary_forms_screenshot_manifest.json`
- `asset_manifest`: `asset_manifest.md`

## Hard Failure Summary

- `hard_failures_present`: no
- `blocked_stage_progression`: no
- `hard_failures`: none inside this bounded axial pass
- `required_fixes_before_progression`: complete remaining primary forms for limbs, hands, feet, hip transitions, eye sockets/lids, and mouth/jaw construction before secondary anatomy

## Weighted Score

| Category | Weight | Score | Weighted Contribution | Notes |
|---|---:|---:|---:|---|
| Proportions and landmarks | 15 | 7 | 10.5 | Axial depth and named joint landmarks are readable. |
| Silhouette and readability | 10 | 8 | 8.0 | Bruiser read remains strong at gameplay distance. |
| Anatomy or structural logic | 15 | 7 | 10.5 | Axial and facial construction improved; appendicular forms remain primitive. |
| Symmetry and intentional asymmetry | 5 | 8 | 4.0 | Bilateral anatomy remains controlled; user pauldron asymmetry is preserved. |
| Topology and edge flow | 15 | 0 | 0.0 | Deferred. |
| UVs and baking readiness | 10 | 0 | 0.0 | Deferred. |
| Materials and texture logic | 10 | 4 | 4.0 | Placeholder families only. |
| Deformation readiness | 10 | 5 | 5.0 | Eye, mouth, neck, and joint intent exists; no production mesh or tests. |
| Performance and LODs | 5 | 2 | 1.0 | Budgets remain unknown. |
| Godot readiness | 5 | 1 | 0.5 | Target declared; no export work is in scope. |

- `total_score`: 43.5
- `score_band`: structural_rework

## Diagnosis

- `highest_risk_categories`: incomplete limb/hand/foot construction, eye containment, mouth closure and tusk roots, shoulder armor clearance
- `most_important_fixes`: retain axial pass; complete appendicular primary masses; then refine eye sockets/lids and mouth/jaw foundation
- `accepted_limitations`: reversible overlapping primitives and neutral evidence materials
- `deferred_items`: secondary anatomy, costume refinement, retopology, UVs, materials, rigging, deformation, optimization, and Godot validation

## Decision

- `decision`: revise_current_stage
- `decision_reason`: the axial microtask passes, but `primary_forms` is not complete because limbs, hands, feet, and facial containment remain at blockout level
- `next_stage`: primary_forms
- `approval_required_from`: repository user
- `approved_by`: none
- `approved_at`: none
