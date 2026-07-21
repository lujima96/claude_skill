# Primary-Mass Blockout QA Audit

## Metadata

- `audit_id`: stylized_orc_bruiser-blockout-qa-001
- `asset_id`: stylized_orc_bruiser
- `stage_id`: blockout
- `created_by`: QA Auditor
- `created_at`: 2026-07-21
- `status`: pass

## Inputs

- `task_card`: `task_cards/blockout_primary_masses.md`
- `stage_handoff`: `handoffs/anatomy_to_manual_blockout.md`; blockout-to-primary-forms handoff pending human approval
- `review_reports`: `reviews/blockout_primary_masses_anatomy_review.md`; `reviews/blockout_primary_masses_style_review.md`
- `validation_reports`: `validations/blockout_primary_masses_validation.md`
- `screenshots`: `screenshots/blockout_primary_masses/stylized_orc_bruiser_blockout_screenshot_manifest.json`
- `asset_manifest`: `asset_manifest.md`

## Hard Failure Summary

- `hard_failures_present`: no
- `blocked_stage_progression`: no
- `hard_failures`: none within primary-mass blockout scope
- `required_fixes_before_progression`: human stage-gate approval; then carry side-depth, shoulder-clearance, and facial-construction notes into primary forms

## Weighted Score

| Category | Weight | Score | Weighted Contribution | Notes |
|---|---:|---:|---:|---|
| Proportions and landmarks | 15 | 7 | 10.5 | Major masses and joints are separately visible. |
| Silhouette and readability | 10 | 8 | 8.0 | Strong front, back, 3/4, and gameplay read; side needs depth. |
| Anatomy or structural logic | 15 | 6 | 9.0 | Primary hierarchy works; facial and torso construction remain primitive. |
| Symmetry and intentional asymmetry | 5 | 8 | 4.0 | Bilateral body massing plus one intentional shoulder pad. |
| Topology and edge flow | 15 | 0 | 0.0 | Out of scope; primitive intersections are not retopology. |
| UVs and baking readiness | 10 | 0 | 0.0 | Deferred. |
| Materials and texture logic | 10 | 4 | 4.0 | Named placeholder families exist; visual separation is not proven. |
| Deformation readiness | 10 | 4 | 4.0 | Landmarks are visible, but no production mesh or pose tests exist. |
| Performance and LODs | 5 | 2 | 1.0 | Blockout report exists; production budget remains unknown. |
| Godot readiness | 5 | 1 | 0.5 | Godot is the declared target; no export or import work is in scope yet. |

- `total_score`: 41.0
- `score_band`: structural_rework

Score note: the total is intentionally low because most production stages are not yet in scope; it does not override the passing blockout-stage evidence.

## Diagnosis

- `highest_risk_categories`: side-view structure, shoulder clearance, facial construction, unknown production budgets and facial-animation requirements
- `most_important_fixes`: obtain human blockout approval; clarify torso/pelvis depth; build eye and mouth construction; preserve deformation lanes in primary forms
- `accepted_limitations`: primitive intersections, unapplied primitive scales, neutral-white evidence renders, no armature
- `deferred_items`: sculpt refinement, costume development, retopology, UVs, materials, rigging, deformation tests, optimization, export, and Godot validation

## Decision

- `decision`: approve_next_stage
- `decision_reason`: all required blockout evidence validates, both specialist reviews approve with notes, and no blockout hard failure is present
- `next_stage`: primary_forms
- `approval_required_from`: repository user or designated human art director
- `approved_by`: repository user
- `approved_at`: 2026-07-21
