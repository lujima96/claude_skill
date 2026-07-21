# Secondary Anatomy Pelvis-Hip Consolidation Task Card

## Metadata

- `task_id`: stylized_orc_bruiser-secondary-anatomy-pelvis-hip-consolidation-001
- `asset_id`: stylized_orc_bruiser
- `stage_id`: secondary_anatomy
- `stage_name`: Secondary anatomy consolidation
- `created_by`: Character Director
- `created_at`: 2026-07-21
- `status`: approved

## Goal

- `goal`: Reduce redundant pelvis-region layering by reversibly retiring the paired `ORC_hip` shells while preserving the central pelvis, rear glute silhouette, thigh connections, abdomen transition, and user-adjusted belt.
- `current_stage`: secondary_anatomy
- `previous_stage`: secondary_anatomy
- `next_stage`: secondary_anatomy

## Constraints

- `allowed_tools`: protected working-copy script; read-only Blender MCP inspection; one scoped Blender MCP collection and visibility burst; screenshot and report scripts
- `disallowed_tools`: deletion; merge; remesh; mesh edits; transforms; material changes; belt changes; changes outside ORC_hip_L/R; changes to pelvis, glutes, thighs, abdomen, or lower legs; topology; rigging; export
- `known_constraints`: each hip shell overlaps 83.7 percent with the central pelvis and 76.9 percent with its corresponding glute by smaller AABB fraction; pelvis and glutes provide the retained front and rear silhouette
- `style_constraints`: preserve the broad bruiser pelvis and readable glute mass without triple-layer construction
- `technical_constraints`: retirement must remain fully reversible by preserving both objects and their mesh data in the existing named non-export construction collection
- `godot_constraints`: retired proxies must remain excluded from the active character collection and render evidence

## Inputs

- `input_refs`: read-only pelvis overlap audit; deformation landmarks; approved upper-arm consolidation review
- `input_artifacts`: `examples/stylized_orc_bruiser/source/secondary_anatomy/consolidation/working/stylized_orc_bruiser.secondary-anatomy-upperarm-consolidation-001.working.blend`
- `input_reports`: upper-arm consolidation validation, anatomy review, QA audit, and live pelvis overlap measurements
- `previous_handoff`: `examples/stylized_orc_bruiser/handoffs/primary_forms_to_secondary_anatomy.md`
- `assumptions`: the central pelvis plus paired glutes and thighs preserve continuous hip structure after the redundant side shells are hidden

## Output Contract

- `required_outputs`: protected backup and pelvis-hip consolidation working `.blend`; existing hidden reversible retirement collection containing ORC_hip_L/R and prior retired objects; five-view screenshots; Blender reports; validation, anatomy review, QA audit, and action log
- `output_paths`: `examples/stylized_orc_bruiser/source/secondary_anatomy/consolidation/working/stylized_orc_bruiser.secondary-anatomy-pelvis-hip-consolidation-001.working.blend`
- `report_paths`: `examples/stylized_orc_bruiser/reports/blender/secondary_anatomy_pelvis_hip_consolidation/`
- `screenshot_requirements`: front; side; back; three_quarter; gameplay_distance targeting `ORC_BLOCKOUT`
- `handoff_format`: `templates/stage_handoff.md`

## Acceptance Tests

- `acceptance_tests`: ORC_hip_L/R remain present and recoverable but move out of ORC_BLOCKOUT into ORC_RETIRED_CONSTRUCTION and are hidden from viewport and render; pelvis, glutes, thighs, abdomen, belt, and all other objects remain unchanged; front-to-back pelvis silhouette and thigh continuity remain intact; all six approved upper-torso guides and prior retired upperarms remain present; source hash and evidence validate
- `required_validators`: validate_stage_task_card; validate_blender_report; validate_screenshot_manifest; validate_mcp_action_log; validate_review_report; validate_qa_audit
- `manual_review_required`: yes
- `hard_failure_checks`: deleted mesh; lost pelvis or thigh continuity; flattened rear silhouette; belt or non-target change; missing upper-torso guides; missing prior retired upperarms; protected-object drift; source or evidence failure

## Stop Conditions

- `stop_conditions`: stop on protection mismatch, missing targets or retained structures, unexpected object drift, silhouette break, or evidence failure
- `requires_human_approval`: yes
- `rollback_required_if`: any object except ORC_hip_L/R changes or either retired hip becomes unrecoverable
- `do_not_continue_if`: task, capability, isolation, protection, saved-file inspection, or reversible-retirement preflight fails

## Execution Notes

- `assigned_specialist`: Anatomy Reviewer with Blender MCP Operator
- `microtasks`: Reversibly retire only ORC_hip_L/R from the active character collection after opening the protected 69-mesh consolidation copy
- `mcp_microtask_id`: secondary-anatomy-pelvis-hip-consolidation-001
- `target_objects`: ORC_hip_L; ORC_hip_R
- `allowed_change_types`: open protected working copy; unlink two targets from ORC_BLOCKOUT; link them to ORC_RETIRED_CONSTRUCTION; set target viewport and render exclusion; save only the pelvis-hip consolidation working copy
- `execution_authorized_by`: repository user
- `execution_authorized_at`: 2026-07-21
- `risks`: removing the side shells could narrow the pelvis too far or expose a gap between pelvis, glutes, and thighs
- `questions_for_director`: none

## Completion

- `completed_outputs`: protected backup and pelvis-hip consolidation working `.blend`; reversible retirement collection containing paired hip and upperarm shells; five-view screenshots; five Blender reports; validation, anatomy review, QA audit, and MCP action log
- `validation_summary`: pass; 69 total meshes preserved, 65 active character meshes, paired hip shells recoverable, 73 protected objects unchanged, source hash unchanged, and all evidence validates
- `review_summary`: Anatomy Reviewer approves with a note that the cleaner front pelvis is slightly straighter under the belt; QA keeps the asset in secondary anatomy
- `blocking_issues`: none inside this bounded consolidation task
- `approved_by`: repository user
- `approved_at`: 2026-07-21
