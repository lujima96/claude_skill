# Blockout To Primary Forms Handoff

## Metadata

- `handoff_id`: stylized_orc_bruiser-blockout-to-primary-forms-001
- `asset_id`: stylized_orc_bruiser
- `from_stage`: blockout
- `to_stage`: primary_forms
- `created_by`: Character Director
- `created_at`: 2026-07-21
- `status`: approved

## Stage Result

- `stage_goal`: establish an approved heroic-stylized orc bruiser silhouette and visible deformation landmarks
- `completed_work`: created and validated the primitive blockout; user enlarged both bracers and belt and repositioned the left pauldron; saved the adjusted state as a separate approved artifact
- `changed_artifacts`: bracer scale; belt scale; left pauldron location; user removed the default cube from the approved scene
- `new_artifacts`: approved blockout `.blend`; adjusted five-view screenshots and Blender reports; validation summary
- `removed_or_superseded_artifacts`: earlier MCP screenshots remain historical evidence and are superseded for visual review by `screenshots/blockout_manual_approved/`

## Required Artifacts

- `source_files`: `examples/stylized_orc_bruiser/source/approved/stylized_orc_bruiser_blockout.approved.blend`
- `export_files`: none
- `screenshots`: `examples/stylized_orc_bruiser/screenshots/blockout_manual_approved/stylized_orc_bruiser_blockout_screenshot_manifest.json`
- `reports`: `examples/stylized_orc_bruiser/reports/blender/blockout_manual_approved/`; `examples/stylized_orc_bruiser/validations/blockout_manual_approved_validation.md`
- `references_used`: approved reference board; style lock; anatomy plan

## Validation

- `validators_run`: validate_blender_report on scene, mesh, material, naming, and screenshot reports; validate_screenshot_manifest
- `validation_reports`: `examples/stylized_orc_bruiser/validations/blockout_manual_approved_validation.md`
- `hard_failures_present`: no
- `hard_failure_summary`: none in blockout scope
- `warning_summary`: no armature and unapplied primitive scales are expected and deferred

## Review

- `specialist_reviews`: `reviews/blockout_primary_masses_anatomy_review.md`; `reviews/blockout_primary_masses_style_review.md`
- `qa_audit`: `audit_blockout_primary_masses.md`
- `human_review_required`: yes
- `approval_decision`: approved
- `approval_notes`: user approved progression after light manual bracer, pauldron, and belt adjustments

## Known Issues

- `accepted_limitations`: intersecting primitives, neutral evidence shading, simple hands/feet, and blockout-only gear
- `deferred_work`: facial-animation decision, topology, UVs, materials, rigging, deformation, optimization, and Godot validation
- `risks_for_next_stage`: side depth is weak; left pauldron must preserve shoulder-raise clearance; eyes and mouth lack constructed primary forms
- `must_not_change_next_stage`: overall bruiser silhouette, user-adjusted bracer/belt/pauldron intent, named joint landmarks, source protection

## Next Stage Instructions

- `next_stage_inputs`: approved adjusted blockout, five-view evidence, anatomy/style reviews, QA audit
- `next_stage_focus`: refine axial body and facial foundation before limbs, costume, or detail
- `next_stage_stop_conditions`: stop on silhouette regression, hidden joint landmarks, pauldron collision with shoulder clearance, or detail added before primary forms
- `next_stage_owner`: Blender MCP Operator with Anatomy Reviewer

## Signoff

- `prepared_by`: Character Director
- `approved_by`: repository user
- `approved_at`: 2026-07-21
