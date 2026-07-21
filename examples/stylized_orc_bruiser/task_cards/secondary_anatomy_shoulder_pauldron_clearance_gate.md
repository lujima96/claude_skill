# Secondary Anatomy Shoulder-Pauldron Clearance Gate Task Card

## Metadata

- `task_id`: stylized_orc_bruiser-secondary-anatomy-shoulder-pauldron-clearance-gate-001
- `asset_id`: stylized_orc_bruiser
- `stage_id`: secondary_anatomy
- `stage_name`: Secondary anatomy consolidation
- `created_by`: Character Director
- `created_at`: 2026-07-21
- `status`: approved

## Goal

- `goal`: Close the completed left shoulder-pauldron clearance region with full evidence and the repository user's explicit visual approval.
- `current_stage`: secondary_anatomy
- `previous_stage`: secondary_anatomy
- `next_stage`: secondary_anatomy

## Constraints

- `allowed_tools`: read-only Blender MCP inspection; full screenshot and Blender report scripts; repository validators; anatomy review; QA audit
- `disallowed_tools`: additional scene edits; deletion; addition; rename; merge; remesh; topology; transforms; materials; rigging; export
- `known_constraints`: quick iteration 1 changed only ORC_shoulder_pad_L and passed its delta receipt; the repository user approved the visible result
- `style_constraints`: preserve the oversized asymmetric bruiser pauldron and the user's manual shaping
- `technical_constraints`: reuse and verify the existing source, backup, working copy, and protection receipt; do not resave or modify the scene
- `godot_constraints`: no export or engine-facing change in this gate

## Inputs

- `input_refs`: approved quick iteration 1 screenshots and scene-delta receipt
- `input_artifacts`: `examples/stylized_orc_bruiser/source/secondary_anatomy/shoulder_pauldron/working/stylized_orc_bruiser.secondary-anatomy-shoulder-pauldron-clearance-001.working.blend`
- `input_reports`: quick iteration action log and user visual approval
- `previous_handoff`: `examples/stylized_orc_bruiser/handoffs/primary_forms_to_secondary_anatomy.md`
- `assumptions`: the approved seated overlap is adequate for the current secondary-anatomy blockout and will be revisited during clothing/hardsurface and deformation stages

## Output Contract

- `required_outputs`: five-view screenshots; scene, mesh, material, naming, and screenshot reports; validation summary; anatomy review; QA audit; gate MCP action log
- `output_paths`: existing protected shoulder-pauldron working `.blend` retained without modification
- `report_paths`: `examples/stylized_orc_bruiser/reports/blender/secondary_anatomy_shoulder_pauldron_clearance_gate/`
- `screenshot_requirements`: front; side; back; three_quarter; gameplay_distance targeting ORC_BLOCKOUT
- `handoff_format`: `templates/stage_handoff.md`

## Acceptance Tests

- `acceptance_tests`: pauldron remains seated with improved clearance; only the approved target differs from the source; all 69 meshes remain present; six retired construction meshes remain recoverable; source and backup remain unchanged; five views and all reports validate; no hard failure exists
- `required_validators`: validate_stage_task_card; validate_blender_report; validate_screenshot_manifest; validate_mcp_action_log; validate_review_report; validate_qa_audit
- `manual_review_required`: yes
- `hard_failure_checks`: missing artifact; unexpected scene drift; floating pauldron; lost shoulder coverage; source or backup change; failed evidence

## Stop Conditions

- `stop_conditions`: stop on filepath mismatch, protection mismatch, missing objects, visual seating failure, source drift, or validator failure
- `requires_human_approval`: yes
- `rollback_required_if`: the full evidence contradicts the approved quick iteration or any protected state fails
- `do_not_continue_if`: task, capability, isolation, protection, saved-file inspection, review, or QA fails

## Execution Notes

- `assigned_specialist`: Anatomy Reviewer with Blender MCP Operator and QA Auditor
- `microtasks`: Capture and validate full gate evidence for the completed shoulder-pauldron quick iteration without any additional scene edit
- `mcp_microtask_id`: secondary-anatomy-shoulder-pauldron-clearance-001
- `evidence_tier`: gate_review
- `iteration_budget`: 1
- `iteration_views`: front; side; back; three_quarter; gameplay_distance
- `target_objects`: ORC_shoulder_pad_L
- `allowed_change_types`: evidence capture only; no scene change
- `execution_authorized_by`: repository user
- `execution_authorized_at`: 2026-07-21
- `risks`: full-body evidence may reveal a clearance or silhouette issue missed in the close view
- `questions_for_director`: none

## Completion

- `completed_outputs`: five-view screenshots; five Blender reports; validation summary; anatomy review; QA audit; approved gate action log
- `validation_summary`: pass; 69 meshes preserved, six retired construction meshes recoverable, five views captured, source and backup unchanged, and all deterministic evidence validators pass
- `review_summary`: Anatomy review approves the pauldron clearance with a non-blocking downstream armor-contour note; QA keeps the asset in secondary anatomy for facial mechanics
- `blocking_issues`: none inside this bounded gate
- `approved_by`: repository user
- `approved_at`: 2026-07-21
