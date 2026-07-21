# Secondary Anatomy Shin-Calf Consolidation Task Card

## Metadata

- `task_id`: stylized_orc_bruiser-secondary-anatomy-shin-calf-consolidation-001
- `asset_id`: stylized_orc_bruiser
- `stage_id`: secondary_anatomy
- `stage_name`: Secondary anatomy consolidation
- `created_by`: Character Director
- `created_at`: 2026-07-21
- `status`: approved

## Goal

- `goal`: Reduce redundant lower-leg layering by reversibly retiring the paired low-resolution `ORC_shin` shells while preserving the more descriptive calf masses and continuous knee-to-ankle construction.
- `current_stage`: secondary_anatomy
- `previous_stage`: secondary_anatomy
- `next_stage`: secondary_anatomy

## Constraints

- `allowed_tools`: protected working-copy script; read-only Blender MCP inspection; one scoped Blender MCP collection and visibility burst; screenshot and report scripts
- `disallowed_tools`: deletion; merge; remesh; mesh edits; transforms; material changes; changes outside ORC_shin_L/R; changes to calves, knees, ankles, feet, toe blocks, thighs, or gear; topology; rigging; export
- `known_constraints`: each shin shell overlaps 69.7 percent with its corresponding calf by smaller AABB fraction; retained calves overlap the ankles and knees enough to preserve continuity
- `style_constraints`: keep the compact powerful lower-leg silhouette without double-layer construction
- `technical_constraints`: retirement must remain fully reversible by preserving both objects and mesh data in the existing named non-export construction collection
- `godot_constraints`: retired proxies must remain excluded from the active character collection and render evidence

## Inputs

- `input_refs`: read-only lower-leg overlap audit; deformation landmarks; approved pelvis-hip consolidation review
- `input_artifacts`: `examples/stylized_orc_bruiser/source/secondary_anatomy/consolidation/working/stylized_orc_bruiser.secondary-anatomy-pelvis-hip-consolidation-001.working.blend`
- `input_reports`: pelvis-hip consolidation validation, anatomy review, QA audit, and lower-leg overlap measurements
- `previous_handoff`: `examples/stylized_orc_bruiser/handoffs/primary_forms_to_secondary_anatomy.md`
- `assumptions`: the higher-resolution calf proxies preserve a clearer anatomical lower-leg read and sufficient knee-to-ankle continuity

## Output Contract

- `required_outputs`: protected backup and shin-calf consolidation working `.blend`; existing hidden reversible retirement collection containing ORC_shin_L/R and prior retired objects; five-view screenshots; Blender reports; validation, anatomy review, QA audit, and action log
- `output_paths`: `examples/stylized_orc_bruiser/source/secondary_anatomy/consolidation/working/stylized_orc_bruiser.secondary-anatomy-shin-calf-consolidation-001.working.blend`
- `report_paths`: `examples/stylized_orc_bruiser/reports/blender/secondary_anatomy_shin_calf_consolidation/`
- `screenshot_requirements`: front; side; back; three_quarter; gameplay_distance targeting `ORC_BLOCKOUT`
- `handoff_format`: `templates/stage_handoff.md`

## Acceptance Tests

- `acceptance_tests`: ORC_shin_L/R remain present and recoverable but move out of ORC_BLOCKOUT into ORC_RETIRED_CONSTRUCTION and are hidden from viewport and render; calves, knees, ankles, feet, toe blocks, and all other objects remain unchanged; knee-to-ankle silhouette remains continuous; prior retired upperarms and hips remain present; source hash and evidence validate
- `required_validators`: validate_stage_task_card; validate_blender_report; validate_screenshot_manifest; validate_mcp_action_log; validate_review_report; validate_qa_audit
- `manual_review_required`: yes
- `hard_failure_checks`: deleted mesh; lost lower-leg continuity; calf, knee, ankle, foot, toe, or non-target change; missing prior retired objects; protected-object drift; source or evidence failure

## Stop Conditions

- `stop_conditions`: stop on protection mismatch, missing targets or retained structures, unexpected object drift, lower-leg silhouette break, or evidence failure
- `requires_human_approval`: yes
- `rollback_required_if`: any object except ORC_shin_L/R changes or either retired shin becomes unrecoverable
- `do_not_continue_if`: task, capability, isolation, protection, saved-file inspection, or reversible-retirement preflight fails

## Execution Notes

- `assigned_specialist`: Anatomy Reviewer with Blender MCP Operator
- `microtasks`: Reversibly retire only ORC_shin_L/R from the active character collection after opening the protected 69-mesh consolidation copy
- `mcp_microtask_id`: secondary-anatomy-shin-calf-consolidation-001
- `target_objects`: ORC_shin_L; ORC_shin_R
- `allowed_change_types`: open protected working copy; unlink two targets from ORC_BLOCKOUT; link them to ORC_RETIRED_CONSTRUCTION; set target viewport and render exclusion; save only the shin-calf consolidation working copy
- `execution_authorized_by`: repository user
- `execution_authorized_at`: 2026-07-21
- `risks`: removing the shin shells could expose a narrow transition between knee, calf, and ankle
- `questions_for_director`: none

## Completion

- `completed_outputs`: protected backup and shin-calf consolidation working `.blend`; reversible retirement collection containing paired shins and prior retired objects; five-view screenshots; five Blender reports; validation, anatomy review, QA audit, and MCP action log
- `validation_summary`: pass; 69 total meshes preserved, 63 active character meshes, paired shin shells recoverable, 73 protected objects unchanged, source hash unchanged, and all evidence validates
- `review_summary`: Anatomy Reviewer approves the cleaner lower-leg construction with continuous knee-to-ankle structure; QA keeps the asset in secondary anatomy
- `blocking_issues`: none inside this bounded consolidation task
- `approved_by`: repository user
- `approved_at`: 2026-07-21
