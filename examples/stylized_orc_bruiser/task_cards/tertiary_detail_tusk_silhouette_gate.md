# Tertiary Detail Tusk Silhouette Gate Task Card

## Metadata

- `task_id`: stylized_orc_bruiser-tertiary-detail-tusk-silhouette-gate-001
- `asset_id`: stylized_orc_bruiser
- `stage_id`: tertiary_detail
- `stage_name`: Tertiary detail
- `created_by`: Character Director
- `created_at`: 2026-07-21
- `status`: approved

## Goal

- `goal`: Close the approved paired tusk silhouette refinement with full gate evidence.
- `current_stage`: tertiary_detail
- `previous_stage`: tertiary_detail
- `next_stage`: tertiary_detail

## Constraints

- `allowed_tools`: read-only Blender MCP inspection; full screenshots and Blender reports; validators; anatomy and style review; QA audit
- `disallowed_tools`: additional scene edits; destructive operations; topology changes; transforms; materials; rigging; export
- `known_constraints`: quick iteration 1 changed only paired tusk tip-ring coordinates and passed its delta receipt; the repository user requested the next step
- `style_constraints`: preserve blunt heroic tusks, seated bases, facial hierarchy, and paired symmetry
- `technical_constraints`: reuse the existing protection set and do not resave or modify the scene
- `godot_constraints`: no export or engine-facing change

## Inputs

- `input_refs`: approved secondary-anatomy handoff; tusk quick evidence
- `input_artifacts`: `examples/stylized_orc_bruiser/source/tertiary_detail/tusk_silhouette/working/stylized_orc_bruiser.tertiary-detail-tusk-silhouette-001.working.blend`
- `input_reports`: quick receipt and action log
- `previous_handoff`: `examples/stylized_orc_bruiser/handoffs/secondary_anatomy_to_tertiary_detail.md`
- `assumptions`: final tusk surface polish remains compatible with later production topology

## Output Contract

- `required_outputs`: five-view screenshots; five Blender reports; validation; specialist review; QA audit; approved gate action log
- `output_paths`: existing protected tusk working `.blend` retained without modification
- `report_paths`: `examples/stylized_orc_bruiser/reports/blender/tertiary_detail_tusk_silhouette_gate/`
- `screenshot_requirements`: front; side; back; three_quarter; gameplay_distance targeting ORC_BLOCKOUT
- `handoff_format`: `templates/stage_handoff.md`

## Acceptance Tests

- `acceptance_tests`: paired tusk bases remain seated; sharper flare reads without facial regression; 69 meshes and six retired proxies remain present; source and backup stay unchanged; five views and reports validate; no hard failure exists
- `required_validators`: validate_stage_task_card; validate_blender_report; validate_screenshot_manifest; validate_review_report; validate_qa_audit; validate_mcp_action_log
- `manual_review_required`: yes
- `hard_failure_checks`: detached tusk; broken symmetry; facial regression; topology drift; missing artifact; source or backup change

## Stop Conditions

- `stop_conditions`: stop on filepath, protection, scene, review, evidence, or QA failure
- `requires_human_approval`: yes
- `rollback_required_if`: full evidence contradicts the approved quick result or protected state fails
- `do_not_continue_if`: any required gate check fails

## Execution Notes

- `assigned_specialist`: Anatomy Reviewer and Style Keeper with Blender MCP Operator and QA Auditor
- `microtasks`: Capture and validate full gate evidence for the approved paired tusk refinement without any scene edit
- `mcp_microtask_id`: tertiary-detail-tusk-silhouette-001
- `evidence_tier`: gate_review
- `iteration_budget`: 1
- `iteration_views`: front; side; back; three_quarter; gameplay_distance
- `target_objects`: ORC_tusk_L; ORC_tusk_R
- `allowed_change_types`: evidence capture only; no scene change
- `execution_authorized_by`: repository user
- `execution_authorized_at`: 2026-07-21
- `risks`: full-character views may show the change is too subtle or too sharp
- `questions_for_director`: none

## Completion

- `completed_outputs`: five-view screenshots; five Blender reports; validation; specialist review; QA audit; gate action log
- `validation_summary`: pass; paired tusk delta, protected hashes, 69 meshes, six retired proxies, five views, and all reports validate
- `review_summary`: approved with notes; retain seated blunt bases and defer final production surface to later sculpt/topology work
- `blocking_issues`: none inside this bounded gate
- `approved_by`: repository user
- `approved_at`: 2026-07-21
