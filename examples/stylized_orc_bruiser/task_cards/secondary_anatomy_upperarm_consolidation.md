# Secondary Anatomy Upper-Arm Consolidation Task Card

## Metadata

- `task_id`: stylized_orc_bruiser-secondary-anatomy-upperarm-consolidation-001
- `asset_id`: stylized_orc_bruiser
- `stage_id`: secondary_anatomy
- `stage_name`: Secondary anatomy consolidation
- `created_by`: Character Director
- `created_at`: 2026-07-21
- `status`: approved

## Goal

- `goal`: Reduce the strongest unnecessary construction overlap by reversibly retiring the paired primary `ORC_upperarm` shells while retaining the more descriptive paired `ORC_bicep` forms and uninterrupted shoulder-to-elbow continuity.
- `current_stage`: secondary_anatomy
- `previous_stage`: secondary_anatomy
- `next_stage`: secondary_anatomy

## Constraints

- `allowed_tools`: protected working-copy script; read-only Blender MCP inspection; one scoped Blender MCP collection/visibility burst; screenshot and report scripts
- `disallowed_tools`: deletion; merge; remesh; mesh edits; transforms; material changes; changes outside ORC_upperarm_L/R; changes to biceps, shoulders, elbows, bracers, pauldron, or any other object; topology; rigging; export
- `known_constraints`: bicep/upperarm pairs overlap 93.1 percent of the smaller bounds with 0.744 IoU; the biceps overlap adjacent shoulder/elbow masses enough to preserve continuity
- `style_constraints`: keep the broad bruiser arm silhouette without double-thick layering
- `technical_constraints`: retirement must be fully reversible by preserving objects and mesh data in a named non-export construction collection
- `godot_constraints`: retired proxies must remain excluded from the active character collection and render evidence

## Inputs

- `input_refs`: read-only overlap audit; deformation landmarks; approved upper-torso anatomy review
- `input_artifacts`: `examples/stylized_orc_bruiser/source/secondary_anatomy/upper_torso/working/stylized_orc_bruiser.secondary-anatomy-upper-torso-transitions-001.working.blend`
- `input_reports`: upper-torso validation, anatomy review, QA audit, and overlap measurements
- `previous_handoff`: `examples/stylized_orc_bruiser/handoffs/primary_forms_to_secondary_anatomy.md`
- `assumptions`: the higher-resolution bicep proxies provide the cleaner retained upper-arm construction

## Output Contract

- `required_outputs`: protected backup and consolidation working `.blend`; hidden reversible retirement collection containing ORC_upperarm_L/R; five-view screenshots; Blender reports; validation, anatomy review, QA audit, and action log
- `output_paths`: `examples/stylized_orc_bruiser/source/secondary_anatomy/consolidation/working/stylized_orc_bruiser.secondary-anatomy-upperarm-consolidation-001.working.blend`
- `report_paths`: `examples/stylized_orc_bruiser/reports/blender/secondary_anatomy_upperarm_consolidation/`
- `screenshot_requirements`: front; side; back; three_quarter; gameplay_distance targeting `ORC_BLOCKOUT`
- `handoff_format`: `templates/stage_handoff.md`

## Acceptance Tests

- `acceptance_tests`: ORC_upperarm_L/R remain present and recoverable but are moved out of ORC_BLOCKOUT into ORC_RETIRED_CONSTRUCTION and hidden from viewport/render; biceps remain unchanged; shoulder-to-elbow silhouette remains continuous; no other object, mesh, transform, material, or collection membership changes; saved source contains all six approved upper-torso guides; source hash and evidence validate
- `required_validators`: validate_stage_task_card; validate_blender_report; validate_screenshot_manifest; validate_mcp_action_log; validate_review_report; validate_qa_audit
- `manual_review_required`: yes
- `hard_failure_checks`: deleted mesh; lost upper-arm continuity; bicep or joint change; missing upper-torso guides; protected-object drift; source or evidence failure

## Stop Conditions

- `stop_conditions`: stop on protection mismatch, missing targets/guides, unexpected object drift, silhouette break, or evidence failure
- `requires_human_approval`: yes
- `rollback_required_if`: any object except ORC_upperarm_L/R changes or either retired object becomes unrecoverable
- `do_not_continue_if`: task, capability, isolation, protection, or restored saved-file inspection fails

## Execution Notes

- `assigned_specialist`: Anatomy Reviewer with Blender MCP Operator
- `microtasks`: Reversibly retire only ORC_upperarm_L/R from the active character collection after restoring the protected 69-mesh working copy
- `mcp_microtask_id`: secondary-anatomy-upperarm-consolidation-001
- `target_objects`: ORC_upperarm_L; ORC_upperarm_R
- `allowed_change_types`: open protected working copy; create ORC_RETIRED_CONSTRUCTION collection; unlink two targets from ORC_BLOCKOUT; link them to retirement collection; set target and retirement collection viewport/render exclusion; save only the consolidation working copy
- `execution_authorized_by`: repository user
- `execution_authorized_at`: 2026-07-21
- `risks`: biceps alone may expose gaps at shoulder or elbow; retirement collection could accidentally be included in evidence or later export
- `questions_for_director`: none

## Completion

- `completed_outputs`: protected backup and consolidation working `.blend`; reversible retirement collection containing paired upperarm shells; five-view screenshots; five Blender reports; validation, anatomy review, QA audit, and MCP action log
- `validation_summary`: pass; 69 total meshes preserved, 67 active character meshes, paired retired shells recoverable, source hash unchanged, and all evidence validates
- `review_summary`: Anatomy Reviewer approves the cleaner upper-arm construction; QA keeps the asset in secondary anatomy for the next bounded consolidation region
- `blocking_issues`: none inside this bounded consolidation task
- `approved_by`: repository user
- `approved_at`: 2026-07-21
