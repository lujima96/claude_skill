# Primary Forms Appendicular-Mass Task Card

## Metadata

- `task_id`: stylized_orc_bruiser-primary-forms-appendicular-masses-001
- `asset_id`: stylized_orc_bruiser
- `stage_id`: primary_forms
- `stage_name`: Primary forms
- `created_by`: Character Director
- `created_at`: 2026-07-21
- `status`: approved

## Goal

- `goal`: Refine the approved arm, hand, hip, leg, and foot blockout into clearer heroic-stylized appendicular primary masses while preserving the accepted face, torso, silhouette, and gear.
- `current_stage`: primary_forms
- `previous_stage`: primary_forms
- `next_stage`: secondary_anatomy

## Constraints

- `allowed_tools`: protected working-copy script; scoped Blender MCP Python for transforms on named limb masses and creation of paired bicep, glute, calf, and heel primitives; screenshot and read-only report scripts
- `disallowed_tools`: deletion; changes to head, face, torso, bracers, belt, or pauldron; merge; boolean; remesh; detail sculpt; transform application; topology; UVs; materials; rigging; export
- `known_constraints`: accepted facial revision is the immutable source; left pauldron must retain shoulder-raise clearance; user gear adjustments must remain unchanged
- `style_constraints`: oversized forearms and hands, grounded feet, strong upper-to-lower taper, compact bruiser stance
- `technical_constraints`: keep elbows, wrists, hips, knees, and ankles separately readable; all new forms remain reversible and named
- `godot_constraints`: no engine work; preserve future deformation zones for retopology

## Inputs

- `input_refs`: approved anatomy plan; appendicular deformation landmarks; heroic-stylized proportions
- `input_artifacts`: `examples/stylized_orc_bruiser/source/primary_forms/revisions/working/stylized_orc_bruiser.primary-forms-facial-readability-revision-001.working.blend`
- `input_reports`: current primary-forms anatomy reviews and QA audits
- `previous_handoff`: `examples/stylized_orc_bruiser/handoffs/blockout_to_primary_forms.md`
- `assumptions`: this pass establishes large limb volumes only; fingers, toes, joint mechanics, and secondary muscles remain later work

## Output Contract

- `required_outputs`: protected appendicular backup and working `.blend`; refined named limb masses; paired bicep, glute, calf, and heel forms; five-view screenshots; Blender reports; validation, anatomy review, QA audit, and action log
- `output_paths`: `examples/stylized_orc_bruiser/source/primary_forms/appendicular/working/stylized_orc_bruiser.primary-forms-appendicular-masses-001.working.blend`
- `report_paths`: `examples/stylized_orc_bruiser/reports/blender/primary_forms_appendicular_masses/`
- `screenshot_requirements`: front; side; back; three_quarter; gameplay_distance targeting `ORC_BLOCKOUT`
- `handoff_format`: `templates/stage_handoff.md`

## Acceptance Tests

- `acceptance_tests`: upper arms taper into readable elbows; forearms and hands remain powerful but separated at wrists; pelvis/glute/thigh transitions support the stance; knees and calves read from side and 3/4; feet gain heel and planted mass; accepted face, torso, gear, and overall silhouette remain intact; source unchanged; evidence validates
- `required_validators`: validate_stage_task_card; validate_blender_report; validate_screenshot_manifest; validate_mcp_action_log; validate_review_report; validate_qa_audit
- `manual_review_required`: yes
- `hard_failure_checks`: protected facial/torso/gear change; lost joint landmark; shoulder armor collision; unstable stance; missing hand or foot mass; source or evidence failure

## Stop Conditions

- `stop_conditions`: stop on source-protection failure, protected-object change, missing named target, silhouette regression, or evidence failure
- `requires_human_approval`: yes
- `rollback_required_if`: accepted face, torso, bracers, belt, pauldron, or source changes
- `do_not_continue_if`: task, capability, isolation, or protection validation fails

## Execution Notes

- `assigned_specialist`: Blender MCP Operator with Anatomy Reviewer
- `microtasks`: Refine the paired appendicular blockout masses and add paired bicep, glute, calf, and heel primary-form primitives
- `mcp_microtask_id`: primary-forms-appendicular-masses-001
- `target_objects`: ORC_shoulder_L/R; ORC_upperarm_L/R; ORC_elbow_L/R; ORC_forearm_L/R; ORC_hand_L/R; ORC_hip_L/R; ORC_thigh_L/R; ORC_knee_L/R; ORC_shin_L/R; ORC_ankle_L/R; ORC_foot_L/R; new ORC_bicep_L/R; ORC_glute_L/R; ORC_calf_L/R; ORC_heel_L/R
- `allowed_change_types`: transform only named existing appendicular targets; create and name eight specified paired primitives; save only the protected appendicular working copy
- `execution_authorized_by`: repository user
- `execution_authorized_at`: 2026-07-21
- `risks`: excess volume could erase elbow/knee negative space; pauldron may crowd the left shoulder; feet may become comically large
- `questions_for_director`: none

## Completion

- `completed_outputs`: protected appendicular backup and working `.blend`; 22 refined masses; eight new volumes; five-view evidence; five reports; validation, anatomy review, QA audit, and action log
- `validation_summary`: all task, report, and screenshot validators pass; source hash and 31 protected matrices remain unchanged
- `review_summary`: Anatomy Reviewer approves with notes; QA remains in `primary_forms` for hand/foot construction
- `blocking_issues`: none for the final extremity primary-form pass
- `approved_by`: repository user
- `approved_at`: 2026-07-21
