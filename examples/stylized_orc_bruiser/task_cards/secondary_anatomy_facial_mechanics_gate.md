# Secondary Anatomy Facial Mechanics Gate Task Card

## Metadata

- `task_id`: stylized_orc_bruiser-secondary-anatomy-facial-mechanics-gate-001
- `asset_id`: stylized_orc_bruiser
- `stage_id`: secondary_anatomy
- `stage_name`: Secondary anatomy consolidation
- `created_by`: Character Director
- `created_at`: 2026-07-21
- `status`: approved

## Goal

- `goal`: Close the approved mouth-cheek-tusk facial region with full evidence before opening the next secondary-anatomy task.
- `current_stage`: secondary_anatomy
- `previous_stage`: secondary_anatomy
- `next_stage`: secondary_anatomy

## Constraints

- `allowed_tools`: read-only Blender MCP inspection; full screenshot and Blender report scripts; repository validators; anatomy review; QA audit
- `disallowed_tools`: additional scene edits; deletion; addition; rename; merge; remesh; topology; transforms; materials; rigging; export
- `known_constraints`: quick iteration 1 changed only five authorized facial objects and passed its scene-delta receipt; the repository user approved the visible result
- `style_constraints`: preserve the heavy jaw, stern expression, paired tusks, readable eyes, and compact heroic proportions
- `technical_constraints`: reuse and verify the existing protected source, backup, working copy, and receipt without resaving or modifying the scene
- `godot_constraints`: no export or engine-facing change in this gate

## Inputs

- `input_refs`: approved facial quick screenshots; stylized biped head and face rules
- `input_artifacts`: `examples/stylized_orc_bruiser/source/secondary_anatomy/facial_mechanics/working/stylized_orc_bruiser.secondary-anatomy-facial-mechanics-001.working.blend`
- `input_reports`: facial quick iteration receipt and action log
- `previous_handoff`: `examples/stylized_orc_bruiser/handoffs/primary_forms_to_secondary_anatomy.md`
- `assumptions`: final facial loops and deformable mouth construction remain deferred to retopology and rigging

## Output Contract

- `required_outputs`: five-view screenshots; five Blender reports; validation summary; anatomy review; QA audit; approved gate MCP action log
- `output_paths`: existing protected facial-mechanics working `.blend` retained without modification
- `report_paths`: `examples/stylized_orc_bruiser/reports/blender/secondary_anatomy_facial_mechanics_gate/`
- `screenshot_requirements`: front; side; back; three_quarter; gameplay_distance targeting ORC_BLOCKOUT
- `handoff_format`: `templates/stage_handoff.md`

## Acceptance Tests

- `acceptance_tests`: facial separation remains readable in full-character context; all 69 meshes remain present; six retired meshes remain recoverable; source and backup stay unchanged; five views and reports validate; no hard failure exists
- `required_validators`: validate_stage_task_card; validate_blender_report; validate_screenshot_manifest; validate_mcp_action_log; validate_review_report; validate_qa_audit
- `manual_review_required`: yes
- `hard_failure_checks`: missing artifact; unexpected scene drift; floating tusks; broken symmetry; lost expression; source or backup change; failed evidence

## Stop Conditions

- `stop_conditions`: stop on filepath mismatch, protection mismatch, missing object, visual regression, source drift, or validator failure
- `requires_human_approval`: yes
- `rollback_required_if`: full evidence contradicts the approved facial quick iteration or any protected state fails
- `do_not_continue_if`: task, capability, isolation, protection, saved-file inspection, review, or QA fails

## Execution Notes

- `assigned_specialist`: Anatomy Reviewer with Blender MCP Operator and QA Auditor
- `microtasks`: Capture and validate full gate evidence for the approved facial-mechanics quick iteration without any additional scene edit
- `mcp_microtask_id`: secondary-anatomy-facial-mechanics-001
- `evidence_tier`: gate_review
- `iteration_budget`: 1
- `iteration_views`: front; side; back; three_quarter; gameplay_distance
- `target_objects`: ORC_mouth_mass; ORC_cheek_L; ORC_cheek_R; ORC_tusk_L; ORC_tusk_R
- `allowed_change_types`: evidence capture only; no scene change
- `execution_authorized_by`: repository user
- `execution_authorized_at`: 2026-07-21
- `risks`: full-character evidence may expose a facial proportion issue missed in close framing
- `questions_for_director`: none

## Completion

- `completed_outputs`: five-view screenshots; five Blender reports; validation summary; anatomy review; QA audit; approved gate action log
- `validation_summary`: pass; 69 meshes preserved, six retired meshes recoverable, source and backup unchanged, five views captured, and all evidence validators pass
- `review_summary`: Anatomy review approves the facial separation; QA retains secondary anatomy for one final transition audit
- `blocking_issues`: none inside this bounded gate
- `approved_by`: repository user
- `approved_at`: 2026-07-21
