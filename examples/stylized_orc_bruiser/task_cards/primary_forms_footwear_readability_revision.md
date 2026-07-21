# Primary Forms Footwear Readability Revision Task Card

## Metadata

- `task_id`: stylized_orc_bruiser-primary-forms-footwear-readability-revision-001
- `asset_id`: stylized_orc_bruiser
- `stage_id`: primary_forms
- `stage_name`: Primary forms revision
- `created_by`: Character Director
- `created_at`: 2026-07-21
- `status`: approved

## Goal

- `goal`: Resolve the mixed shoe-and-bare-foot read by making the existing black footwear base and added construction volumes read as one simple boot, while retaining the hidden anatomical foot plan.
- `current_stage`: primary_forms
- `previous_stage`: primary_forms
- `next_stage`: secondary_anatomy

## Constraints

- `allowed_tools`: protected working-copy script; read-only Blender MCP inspection; one scoped Blender MCP material/transform burst; screenshot and report scripts
- `disallowed_tools`: deletion; changes outside paired foot, heel, instep, and toe objects; changes to stance, ankles, legs, upper body, face, or gear; merge; remesh; topology; UVs; rigging; export
- `known_constraints`: preserve the accepted broad footprint and heel-to-toe construction; footwear should conceal rather than duplicate visible foot anatomy
- `style_constraints`: chunky heroic boot silhouette; simple sole; no individual toe read; no anatomical skin-colored upper sitting on a black shoe
- `technical_constraints`: retain distinct reversible primitives and visible ankle transition
- `godot_constraints`: no engine work; preserve later deformation intent

## Inputs

- `input_refs`: repository-user review identifying the mixed footwear read; extremity anatomy review
- `input_artifacts`: `examples/stylized_orc_bruiser/source/primary_forms/extremities/working/stylized_orc_bruiser.primary-forms-extremity-construction-001.working.blend`
- `input_reports`: extremity validation, anatomy review, and QA audit
- `previous_handoff`: `examples/stylized_orc_bruiser/handoffs/blockout_to_primary_forms.md`
- `assumptions`: the original dark base represents footwear rather than a bare foot; upper foot construction should therefore read as boot volume

## Output Contract

- `required_outputs`: protected backup and revision working `.blend`; clarified paired boot/sole primary forms; five-view screenshots; Blender reports; validation, anatomy review, QA audit, and MCP action log
- `output_paths`: `examples/stylized_orc_bruiser/source/primary_forms/extremities/revisions/working/stylized_orc_bruiser.primary-forms-footwear-readability-revision-001.working.blend`
- `report_paths`: `examples/stylized_orc_bruiser/reports/blender/primary_forms_footwear_readability_revision/`
- `screenshot_requirements`: front; side; back; three_quarter; gameplay_distance targeting `ORC_BLOCKOUT`
- `handoff_format`: `templates/stage_handoff.md`

## Acceptance Tests

- `acceptance_tests`: both feet read as one coherent boot construction; dark material is consistently footwear-only; toe mass reads as a single boot toe, not anatomy; sole remains simple; stance and ankle visibility remain unchanged; all untargeted matrices remain unchanged; source hash remains unchanged; evidence validates
- `required_validators`: validate_stage_task_card; validate_blender_report; validate_screenshot_manifest; validate_mcp_action_log; validate_review_report; validate_qa_audit
- `manual_review_required`: yes
- `hard_failure_checks`: mixed shoe/bare-foot read persists; stance changes; ankle landmark is lost; protected object changes; source or evidence failure

## Stop Conditions

- `stop_conditions`: stop on protection failure, missing target/material, untargeted-object change, stance change, or evidence failure
- `requires_human_approval`: yes
- `rollback_required_if`: any object outside ORC_foot_L/R, ORC_heel_L/R, ORC_instep_L/R, or ORC_toe_block_L/R changes
- `do_not_continue_if`: task, capability, isolation, protection, or target inspection fails

## Execution Notes

- `assigned_specialist`: Blender MCP Operator with Anatomy Reviewer
- `microtasks`: Unify paired sole, heel, instep, and toe masses into a simple footwear read through scoped material assignment and minimal silhouette adjustment if inspection requires it
- `mcp_microtask_id`: primary-forms-footwear-readability-revision-001
- `target_objects`: ORC_foot_L/R; ORC_heel_L/R; ORC_instep_L/R; ORC_toe_block_L/R
- `allowed_change_types`: inspect named targets; assign existing blockout material to named targets; minimally scale or reposition named targets without changing footprint or stance; save only protected revision working copy
- `execution_authorized_by`: repository user
- `execution_authorized_at`: 2026-07-21
- `risks`: over-dark footwear may merge visually; excessive simplification may lose toe-off intent
- `questions_for_director`: none

## Completion

- `completed_outputs`: protected backup and revision working `.blend`; scoped footwear material/form correction; five-view screenshot set; five Blender reports; validation, anatomy review, QA audit, and MCP action log
- `validation_summary`: pass; source and backup hashes match, all five Blender reports and the screenshot manifest validate, and 61 untargeted objects remained unchanged
- `review_summary`: Anatomy Reviewer approves with notes; QA again recommends secondary anatomy after the required human primary-forms gate
- `blocking_issues`: human primary-forms gate remains required after complete evidence and review
- `approved_by`: repository user
- `approved_at`: 2026-07-21
