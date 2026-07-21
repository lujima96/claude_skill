# Primary Forms Facial Readability Revision Task Card

## Metadata

- `task_id`: stylized_orc_bruiser-primary-forms-facial-readability-revision-001
- `asset_id`: stylized_orc_bruiser
- `stage_id`: primary_forms
- `stage_name`: Primary forms revision
- `created_by`: Character Director
- `created_at`: 2026-07-21
- `status`: approved

## Goal

- `goal`: Correct the user-identified brow intersection, eye-material ambiguity, and tusk visibility without changing other approved axial or gear forms.
- `current_stage`: primary_forms
- `previous_stage`: primary_forms
- `next_stage`: primary_forms

## Constraints

- `allowed_tools`: protected working-copy script; Blender MCP scoped Python for transforms on four named brow/tusk objects, eye material creation and assignment on two named eye objects; screenshot and read-only report scripts
- `disallowed_tools`: deletion; new geometry; changes to mouth, jaw, nose, cheeks, torso, limbs, bracers, belt, or pauldron; merge; boolean; remesh; transform application; topology; UVs; rigging; export
- `known_constraints`: preserve all accepted axial construction and the user's prior bracer, belt, and pauldron adjustments
- `style_constraints`: keep the heavy brow and upward orc tusk read while restoring clean separation and visual hierarchy
- `technical_constraints`: brows must not intersect each other; eyes must use a distinct named material; tusk orientation must be preserved while their visible projection increases
- `godot_constraints`: use a simple Principled placeholder eye material that can later map cleanly to Godot; no export work

## Inputs

- `input_refs`: user review note; head/face construction guidance
- `input_artifacts`: `examples/stylized_orc_bruiser/source/primary_forms/working/stylized_orc_bruiser.primary-forms-axial-masses-001.working.blend`
- `input_reports`: axial primary-forms anatomy review and QA audit
- `previous_handoff`: `examples/stylized_orc_bruiser/handoffs/blockout_to_primary_forms.md`
- `assumptions`: “teeth” refers to the paired orc tusks `ORC_tusk_L` and `ORC_tusk_R`

## Output Contract

- `required_outputs`: protected revision backup and working `.blend`; separated brows; distinct eye material; more visible tusks; five-view screenshots; Blender reports; validation, review, QA, and action log
- `output_paths`: `examples/stylized_orc_bruiser/source/primary_forms/revisions/working/stylized_orc_bruiser.primary-forms-facial-readability-revision-001.working.blend`
- `report_paths`: `examples/stylized_orc_bruiser/reports/blender/primary_forms_facial_readability_revision/`
- `screenshot_requirements`: front; side; back; three_quarter; gameplay_distance targeting `ORC_BLOCKOUT`
- `handoff_format`: `templates/stage_handoff.md`

## Acceptance Tests

- `acceptance_tests`: left and right brow world bounds have a visible center gap; eyes no longer use the brow material and share `MAT_ORC_eye_blockout`; both tusks project clearly beyond the mouth mass in front and three-quarter views; all unrelated transforms remain unchanged; source hash remains unchanged; evidence validates
- `required_validators`: validate_stage_task_card; validate_blender_report; validate_screenshot_manifest; validate_mcp_action_log; validate_review_report; validate_qa_audit
- `manual_review_required`: yes
- `hard_failure_checks`: brow intersection remains; eye material remains ambiguous; tusks remain obscured; unrelated object changes; missing protection or evidence

## Stop Conditions

- `stop_conditions`: stop if source protection fails, any target is missing, unrelated object matrices change, tusk orientation changes, or evidence cannot be captured
- `requires_human_approval`: yes
- `rollback_required_if`: any object outside the six named geometry targets changes or the facial read worsens
- `do_not_continue_if`: task card, capability, isolation, or source-protection validation fails

## Execution Notes

- `assigned_specialist`: Blender MCP Operator with Anatomy Reviewer
- `microtasks`: Separate and slightly reduce the paired brows, assign a distinct eye material, and reposition/scale the paired tusks for clearer visibility
- `mcp_microtask_id`: primary-forms-facial-readability-revision-001
- `target_objects`: ORC_brow_L; ORC_brow_R; ORC_eye_L; ORC_eye_R; ORC_tusk_L; ORC_tusk_R; new material MAT_ORC_eye_blockout
- `allowed_change_types`: transform only the paired brows and tusks; create and assign one eye material only to paired eyes; save only the protected revision working copy
- `execution_authorized_by`: repository user
- `execution_authorized_at`: 2026-07-21
- `risks`: excessive separation could weaken the heavy brow; excessive tusk projection could detach them visually from the mouth
- `questions_for_director`: none

## Completion

- `completed_outputs`: protected revision backup and working `.blend`; separated brows; dedicated eye material; repositioned/scaled tusks; five-view evidence; five Blender reports; validation, anatomy review, QA audit, and action log
- `validation_summary`: all required task, report, and screenshot validators pass; source hash and 47 unrelated object matrices remain unchanged
- `review_summary`: Anatomy Reviewer approves with notes; QA remains in `primary_forms`
- `blocking_issues`: none for continued primary forms
- `approved_by`: repository user
- `approved_at`: 2026-07-21
