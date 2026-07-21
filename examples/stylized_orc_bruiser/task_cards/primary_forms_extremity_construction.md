# Primary Forms Extremity Construction Task Card

## Metadata

- `task_id`: stylized_orc_bruiser-primary-forms-extremity-construction-001
- `asset_id`: stylized_orc_bruiser
- `stage_id`: primary_forms
- `stage_name`: Primary forms
- `created_by`: Character Director
- `created_at`: 2026-07-21
- `status`: review

## Goal

- `goal`: Complete primary-form hand and foot construction with readable palms, finger direction, thumbs, insteps, arches, and toe blocks before the secondary-anatomy gate.
- `current_stage`: primary_forms
- `previous_stage`: primary_forms
- `next_stage`: secondary_anatomy

## Constraints

- `allowed_tools`: protected working-copy script; scoped Blender MCP Python for transforms on paired hands, feet, heels, and ankles plus eight named extremity primitives; screenshot and read-only report scripts
- `disallowed_tools`: deletion; changes above wrists or ankles; changes to face, torso, limbs, or gear; individual fingers/toes; merge; remesh; detail; topology; UVs; rigging; export
- `known_constraints`: preserve every accepted prior form; construction must remain low-detail, reversible, and suitable for later deformation planning
- `style_constraints`: large functional hands, grounded feet, simple chunky planes, clear third-person silhouette
- `technical_constraints`: palm and finger blocks must remain distinct at the wrist; thumb wedges must establish later opposition; instep, toe block, heel, and ankle must remain legible
- `godot_constraints`: no engine work; preserve hand and foot deformation intent for retopology

## Inputs

- `input_refs`: stylized biped proportions; deformation landmarks; appendicular anatomy review
- `input_artifacts`: `examples/stylized_orc_bruiser/source/primary_forms/appendicular/working/stylized_orc_bruiser.primary-forms-appendicular-masses-001.working.blend`
- `input_reports`: appendicular validation, anatomy review, and QA audit
- `previous_handoff`: `examples/stylized_orc_bruiser/handoffs/blockout_to_primary_forms.md`
- `assumptions`: mitten and boot primary construction is appropriate; individual digits belong to later production work

## Output Contract

- `required_outputs`: protected extremity backup and working `.blend`; refined hands/feet/heels/ankles; paired finger, thumb, instep, and toe primitives; five-view screenshots; Blender reports; validation, anatomy review, QA audit, and action log
- `output_paths`: `examples/stylized_orc_bruiser/source/primary_forms/extremities/working/stylized_orc_bruiser.primary-forms-extremity-construction-001.working.blend`
- `report_paths`: `examples/stylized_orc_bruiser/reports/blender/primary_forms_extremity_construction/`
- `screenshot_requirements`: front; side; back; three_quarter; gameplay_distance targeting `ORC_BLOCKOUT`
- `handoff_format`: `templates/stage_handoff.md`

## Acceptance Tests

- `acceptance_tests`: each hand has distinct palm, finger direction, and thumb wedge; each foot has readable heel, instep/arch, and toe block; wrists and ankles stay visible; stance remains stable; all prior forms and gear remain unchanged; source hash remains unchanged; evidence validates
- `required_validators`: validate_stage_task_card; validate_blender_report; validate_screenshot_manifest; validate_mcp_action_log; validate_review_report; validate_qa_audit
- `manual_review_required`: yes
- `hard_failure_checks`: missing hand/foot construction; lost wrist or ankle landmark; unstable feet; protected-form change; source or evidence failure

## Stop Conditions

- `stop_conditions`: stop on protection failure, protected-object change, missing target, silhouette regression, or evidence failure
- `requires_human_approval`: yes
- `rollback_required_if`: any object outside hands, feet, heels, ankles, or eight named new primitives changes
- `do_not_continue_if`: task, capability, isolation, or protection validation fails

## Execution Notes

- `assigned_specialist`: Blender MCP Operator with Anatomy Reviewer
- `microtasks`: Refine paired hand and foot base masses and add paired finger, thumb, instep, and toe primary-form primitives
- `mcp_microtask_id`: primary-forms-extremity-construction-001
- `target_objects`: ORC_hand_L/R; ORC_ankle_L/R; ORC_foot_L/R; ORC_heel_L/R; new ORC_finger_mass_L/R; ORC_thumb_L/R; ORC_instep_L/R; ORC_toe_block_L/R
- `allowed_change_types`: transform only eight named existing extremity targets; create and name eight specified primitives; save only the protected extremity working copy
- `execution_authorized_by`: repository user
- `execution_authorized_at`: 2026-07-21
- `risks`: digit blocks may become visually noisy; feet may become too long; thumb wedges may merge into forearms
- `questions_for_director`: none

## Completion

- `completed_outputs`: protected backup and working `.blend`; eight refined extremity masses; eight new paired construction primitives; five-view screenshots; five Blender reports; validation, anatomy review, QA audit, and MCP action log
- `validation_summary`: pass; source and backup hashes match, five Blender reports and the screenshot manifest validate, and 53 protected object matrices remained unchanged
- `review_summary`: Anatomy Reviewer approves with notes; QA recommends secondary anatomy after the required human primary-forms gate
- `blocking_issues`: human primary-forms gate approval required afterward
- `approved_by`: none
- `approved_at`: none
