# Disposable Blender MCP Live-Test Task Card

## Metadata

- `task_id`: disposable_blender_fixture-blockout-review-marker-001
- `asset_id`: disposable_blender_fixture
- `stage_id`: blockout
- `stage_name`: Blockout
- `created_by`: Character Director
- `created_at`: 2026-07-20
- `status`: draft

## Goal

- `goal`: Add one non-rendering empty named `MCP_REVIEW_height_marker` beside the disposable fixture without changing its character mesh.
- `current_stage`: blockout
- `previous_stage`: proportion_planning
- `next_stage`: blockout

## Constraints

- `allowed_tools`: Blender MCP object creation; Blender MCP object rename; Blender save working file; screenshot and read-only report scripts
- `disallowed_tools`: arbitrary Python; mesh edits; transforms on existing objects; deletion; apply transforms; export; source-file save
- `known_constraints`: use a generated disposable fixture and protected working copy only
- `style_constraints`: none; this test validates operations and evidence, not character aesthetics
- `technical_constraints`: Blender 4.3.2 baseline; target collection is `CHARACTER`
- `godot_constraints`: no Godot work is authorized in this microtask

## Inputs

- `input_refs`: `docs/mcp/blender_mcp_usage_policy.md`
- `input_artifacts`: disposable source `.blend` generated for the smoke test
- `input_reports`: source-protection receipt
- `previous_handoff`: none; infrastructure smoke test
- `assumptions`: a compatible Blender MCP server will be connected before this card becomes ready

## Output Contract

- `required_outputs`: working `.blend` containing one new empty; MCP action log; five screenshots; scene and naming reports; validation reports
- `output_paths`: isolated temporary workspace only
- `report_paths`: isolated temporary workspace only
- `screenshot_requirements`: front; side; back; three_quarter; gameplay_distance targeting collection `CHARACTER`
- `handoff_format`: `templates/stage_handoff.md`

## Acceptance Tests

- `acceptance_tests`: marker exists with the exact name; marker is an empty; no pre-existing object data or transforms changed; source hash remains unchanged; required evidence validates
- `required_validators`: validate_stage_task_card; validate_blender_report; validate_screenshot_manifest; validate_mcp_action_log
- `manual_review_required`: yes
- `hard_failure_checks`: missing capability; source hash change; missing evidence; mesh or unrelated object change; scope drift

## Stop Conditions

- `stop_conditions`: stop if capability preflight fails, source protection fails, the server requires arbitrary Python, or any unrelated object would change
- `requires_human_approval`: yes
- `rollback_required_if`: the working copy changes anything beyond the new review empty
- `do_not_continue_if`: the task card is not ready and authorized or the MCP server is unavailable

## Execution Notes

- `assigned_specialist`: Blender MCP Operator
- `microtasks`: Add and name one non-rendering review empty beside the disposable fixture
- `mcp_microtask_id`: blockout-review-marker-001
- `target_objects`: new empty `MCP_REVIEW_height_marker`; existing collection `CHARACTER` must remain unchanged
- `allowed_change_types`: create one empty; rename the new empty; save the working copy
- `execution_authorized_by`: none
- `execution_authorized_at`: none
- `risks`: an overly broad creation or save tool could alter unrelated scene state
- `questions_for_director`: none

## Completion

- `completed_outputs`: pending
- `validation_summary`: pending
- `review_summary`: pending
- `blocking_issues`: keep draft until a compatible Blender MCP server is connected and execution is explicitly authorized
- `approved_by`: none
- `approved_at`: none
