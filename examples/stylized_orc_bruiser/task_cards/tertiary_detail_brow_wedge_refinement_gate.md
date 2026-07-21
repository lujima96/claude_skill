# Tertiary Detail Brow Wedge Refinement Gate Task Card

## Metadata

- `task_id`: stylized_orc_bruiser-tertiary-detail-brow-wedge-refinement-gate-001
- `asset_id`: stylized_orc_bruiser
- `stage_id`: tertiary_detail
- `stage_name`: Tertiary detail
- `created_by`: Character Director
- `created_at`: 2026-07-21
- `status`: approved

## Goal

- `goal`: Close the approved paired brow wedge refinement with full evidence.
- `current_stage`: tertiary_detail
- `previous_stage`: tertiary_detail
- `next_stage`: tertiary_detail

## Constraints

- `allowed_tools`: read-only Blender MCP evidence capture; full screenshot and report scripts; validators; specialist review; QA audit
- `disallowed_tools`: additional scene edits; destructive operations; topology changes; transforms; materials; rigging; export
- `known_constraints`: quick iteration 1 changed only paired brow outer-end coordinates and passed its receipt; the repository user approved progression
- `style_constraints`: preserve stern expression, visible eyes, center separation, and mirrored wedge shape
- `technical_constraints`: reuse existing protection and do not resave or alter the scene
- `godot_constraints`: no engine-facing change

## Inputs

- `input_refs`: approved tusk gate and brow quick evidence
- `input_artifacts`: `examples/stylized_orc_bruiser/source/tertiary_detail/brow_wedge/working/stylized_orc_bruiser.tertiary-detail-brow-wedge-refinement-001.working.blend`
- `input_reports`: quick receipt and action log
- `previous_handoff`: `examples/stylized_orc_bruiser/handoffs/secondary_anatomy_to_tertiary_detail.md`
- `assumptions`: final production brow topology remains downstream

## Output Contract

- `required_outputs`: five-view screenshots; five Blender reports; validation; specialist review; QA audit; gate action log
- `output_paths`: existing protected brow working `.blend` retained
- `report_paths`: `examples/stylized_orc_bruiser/reports/blender/tertiary_detail_brow_wedge_refinement_gate/`
- `screenshot_requirements`: front; side; back; three_quarter; gameplay_distance targeting ORC_BLOCKOUT
- `handoff_format`: `templates/stage_handoff.md`

## Acceptance Tests

- `acceptance_tests`: brows remain separated and eyes visible; wedge taper reads without expression loss; 69 meshes and six retired proxies remain; source and backup stay unchanged; five views and reports pass
- `required_validators`: validate_stage_task_card; validate_blender_report; validate_screenshot_manifest; validate_review_report; validate_qa_audit; validate_mcp_action_log
- `manual_review_required`: yes
- `hard_failure_checks`: center overlap; eye occlusion; expression regression; topology drift; missing evidence; source or backup change

## Stop Conditions

- `stop_conditions`: stop on filepath, protection, visual, evidence, review, or QA failure
- `requires_human_approval`: yes
- `rollback_required_if`: full evidence contradicts the approved quick result
- `do_not_continue_if`: any gate check fails

## Execution Notes

- `assigned_specialist`: Anatomy Reviewer and Style Keeper with Blender MCP Operator and QA Auditor
- `microtasks`: Capture and validate full gate evidence for the approved paired brow wedge refinement without scene edits
- `mcp_microtask_id`: tertiary-detail-brow-wedge-refinement-001
- `evidence_tier`: gate_review
- `iteration_budget`: 1
- `iteration_views`: front; side; back; three_quarter; gameplay_distance
- `target_objects`: ORC_brow_L; ORC_brow_R
- `allowed_change_types`: evidence capture only; no scene change
- `execution_authorized_by`: repository user
- `execution_authorized_at`: 2026-07-21
- `risks`: full-character framing could expose lost brow readability
- `questions_for_director`: none

## Completion

- `completed_outputs`: five-view screenshots; five Blender reports; validation; specialist review; QA audit; gate action log
- `validation_summary`: pass; paired-brow delta, protected hashes, 69 meshes, six retired proxies, five views, and all reports validate
- `review_summary`: approved with notes; preserve the separated inner ends and tapered outer wedges during later production reconstruction
- `blocking_issues`: none inside this bounded gate
- `approved_by`: repository user
- `approved_at`: 2026-07-21
