# Primary Forms Axial-Mass Task Card

## Metadata

- `task_id`: stylized_orc_bruiser-primary-forms-axial-masses-001
- `asset_id`: stylized_orc_bruiser
- `stage_id`: primary_forms
- `stage_name`: Primary forms
- `created_by`: Character Director
- `created_at`: 2026-07-21
- `status`: review

## Goal

- `goal`: Refine the approved blockout's torso, pelvis, neck, skull, jaw, and facial foundation so the orc reads structurally from front, side, and three-quarter views without changing the approved overall silhouette.
- `current_stage`: primary_forms
- `previous_stage`: blockout
- `next_stage`: secondary_anatomy

## Constraints

- `allowed_tools`: protected working-copy script; Blender MCP scoped Python for transforms on named axial masses and creation of named eye, mouth, cheek, and trapezius primitives; screenshot and read-only report scripts
- `disallowed_tools`: deletion; mesh merge; booleans; remesh; sculpt surface detail; transform application; retopology; UVs; baking; finished materials; rigging; animation; export
- `known_constraints`: preserve the user-approved bracer, belt, and pauldron adjustments; work only on a new protected primary-forms working copy
- `style_constraints`: maintain broad shoulder-to-waist taper, heavy jaw/brow, thick neck, large simple forms, and third-person readability
- `technical_constraints`: refine only axial masses and facial foundation; keep all objects separately named and reversible; preserve shoulder, hip, and neck landmarks
- `godot_constraints`: no Godot work; primary forms must remain suitable for later retopology and deformation planning

## Inputs

- `input_refs`: approved reference board; anatomy primary-form guidance; heroic-stylized style rules
- `input_artifacts`: `examples/stylized_orc_bruiser/source/approved/stylized_orc_bruiser_blockout.approved.blend`
- `input_reports`: adjusted blockout reports; anatomy and style reviews; blockout QA audit
- `previous_handoff`: `examples/stylized_orc_bruiser/handoffs/blockout_to_primary_forms.md`
- `assumptions`: limb and costume refinement will use later primary-form microtasks; facial animation remains unknown

## Output Contract

- `required_outputs`: protected primary-forms backup and working `.blend`; refined axial masses; eye globes, mouth/muzzle, cheek, and trapezius foundation; five-view screenshots; Blender reports; action log; anatomy review; QA audit
- `output_paths`: `examples/stylized_orc_bruiser/source/primary_forms/working/stylized_orc_bruiser.primary-forms-axial-masses-001.working.blend`
- `report_paths`: `examples/stylized_orc_bruiser/reports/blender/primary_forms_axial_masses/`
- `screenshot_requirements`: front; side; back; three_quarter; gameplay_distance targeting `ORC_BLOCKOUT`
- `handoff_format`: `templates/stage_handoff.md`

## Acceptance Tests

- `acceptance_tests`: ribcage and pelvis have readable front-to-back depth; neck joins jaw and torso; eyes sit within a readable brow/cheek foundation; mouth volume and tusk roots are legible; approved silhouette and user-adjusted gear remain intact; source hash remains unchanged; evidence validates
- `required_validators`: validate_stage_task_card; validate_blender_report; validate_screenshot_manifest; validate_mcp_action_log; validate_review_report; validate_qa_audit
- `manual_review_required`: yes
- `hard_failure_checks`: source or approved blockout overwritten; user-adjusted gear changed; scope drift into limbs/detail/topology; side silhouette remains structurally unreadable; eye or mouth construction absent; missing evidence

## Stop Conditions

- `stop_conditions`: stop if source protection fails, any disallowed object changes, the approved silhouette regresses, evidence cannot be captured, or arbitrary Python exceeds named targets
- `requires_human_approval`: yes
- `rollback_required_if`: user-adjusted bracers, belt, pauldron, limb landmarks, or approved blockout artifact change
- `do_not_continue_if`: task card, handoff, capability, isolation, or source-protection validation fails

## Execution Notes

- `assigned_specialist`: Blender MCP Operator with Anatomy Reviewer
- `microtasks`: Refine only the named axial body masses and add the named facial and trapezius primary-form primitives in the protected primary-forms working copy
- `mcp_microtask_id`: primary-forms-axial-masses-001
- `target_objects`: ORC_ribcage; ORC_abdomen; ORC_pelvis; ORC_neck; ORC_head_cranium; ORC_jaw; ORC_nose; ORC_brow_L; ORC_brow_R; ORC_tusk_L; ORC_tusk_R; new ORC_eye_L; ORC_eye_R; ORC_mouth_mass; ORC_cheek_L; ORC_cheek_R; ORC_trapezius_L; ORC_trapezius_R
- `allowed_change_types`: adjust transforms only on named existing axial targets; create and name the seven specified new primitive objects; save only the protected primary-forms working copy
- `execution_authorized_by`: repository user
- `execution_authorized_at`: 2026-07-21
- `risks`: excessive facial primitives could add detail too early; thick neck may obscure jaw/throat construction; pauldron proximity may confuse shoulder silhouette
- `questions_for_director`: facial animation and blend-shape requirements remain open but do not block this reversible foundation pass

## Completion

- `completed_outputs`: protected backup and working `.blend`; nine refined axial targets; seven new primary-form primitives; five-view evidence; five Blender reports; validation, anatomy review, QA audit, and action log
- `validation_summary`: all required task, Blender-report, and screenshot validators pass; source and user-adjusted gear remain protected
- `review_summary`: Anatomy Reviewer approves the axial microtask with notes; QA decision is `revise_current_stage` because appendicular primary forms remain incomplete
- `blocking_issues`: user requested a bounded facial-readability revision for brow intersection, eye material, and tusk visibility before approval
- `approved_by`: none
- `approved_at`: none
