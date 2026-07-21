# Anatomy To Manual Blockout Handoff

## Metadata

- `handoff_id`: stylized_orc_bruiser-anatomy_to_manual_blockout-001
- `asset_id`: stylized_orc_bruiser
- `from_stage`: anatomy_blockout_planning
- `to_stage`: manual_blockout
- `created_by`: Anatomy Reviewer
- `created_at`: 2026-07-21
- `status`: approved

## Stage Result

- `stage_goal`: approve the anatomical plan for the first manual Blender blockout
- `completed_work`: identified primary masses, landmark checks, deformation risk zones, face/tusk construction requirements, and blockout screenshot expectations
- `changed_artifacts`: none
- `new_artifacts`: `examples/stylized_orc_bruiser/task_cards/anatomy_blockout_planning.md`; `examples/stylized_orc_bruiser/reviews/anatomy_review.md`
- `removed_or_superseded_artifacts`: none

## Required Artifacts

- `source_files`: `examples/stylized_orc_bruiser/brief.md`
- `export_files`: none
- `screenshots`: none in Phase 5; required in manual blockout
- `reports`: `examples/stylized_orc_bruiser/reviews/anatomy_review.md`
- `references_used`: `ref-007`, `ref-008`, `ref-009`, `ref-010`, `ref-011`

## Validation

- `validators_run`: none
- `validation_reports`: `examples/stylized_orc_bruiser/validations/phase5_manual_validation.md`
- `hard_failures_present`: no
- `hard_failure_summary`: no Phase 5 hard failures
- `warning_summary`: unknown animation and facial requirements may affect later topology and rig planning

## Review

- `specialist_reviews`: `examples/stylized_orc_bruiser/reviews/anatomy_review.md`
- `qa_audit`: `examples/stylized_orc_bruiser/audit.md`
- `human_review_required`: yes
- `approval_decision`: approved
- `approval_notes`: proceed to manual blockout; do not progress beyond blockout review without screenshots and validation artifacts

## Known Issues

- `accepted_limitations`: anatomy plan is preproduction guidance, not mesh validation
- `deferred_work`: topology, UVs, materials, skinning, LODs, Godot import checks
- `risks_for_next_stage`: silhouette could hide shoulder/neck landmarks; tusks could obstruct mouth deformation if facial animation is later required
- `must_not_change_next_stage`: landmark plan, screenshot requirements, Godot target

## Next Stage Instructions

- `next_stage_inputs`: brief, approved references, style review, anatomy review, Phase 5 audit
- `next_stage_focus`: create a simple Blender blockout that proves silhouette and landmark placement before detail
- `next_stage_stop_conditions`: stop if screenshots are missing, proportions contradict style lock, or deformation-critical landmarks are not visible
- `next_stage_owner`: human artist or bounded Blender automation after validators exist

## Signoff

- `prepared_by`: Anatomy Reviewer
- `approved_by`: Lucas
- `approved_at`: 2026-07-21
