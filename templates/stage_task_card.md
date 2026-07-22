# Stage Task Card

- `schema_version`: 0.3 for active sessions; omit or retain the existing value for legacy cards

## Metadata

- `task_id`:
- `asset_id`:
- `stage_id`:
- `stage_name`:
- `created_by`:
- `created_at`:
- `status`: draft | ready | in_progress | review | approved | blocked

## Goal

- `goal`:
- `current_stage`:
- `previous_stage`:
- `next_stage`:

## Constraints

- `allowed_tools`:
- `disallowed_tools`:
- `known_constraints`:
- `style_constraints`:
- `technical_constraints`:
- `godot_constraints`:

## Inputs

- `input_refs`:
- `input_artifacts`:
- `input_reports`:
- `previous_handoff`:
- `assumptions`:

## Output Contract

- `required_outputs`:
- `output_paths`:
- `report_paths`:
- `screenshot_requirements`:
- `handoff_format`:

## Acceptance Tests

- `acceptance_tests`:
- `required_validators`:
- `manual_review_required`:
- `hard_failure_checks`:

## Stop Conditions

- `stop_conditions`:
- `requires_human_approval`: yes
- `rollback_required_if`:
- `do_not_continue_if`:

## Execution Notes

- `assigned_specialist`:
- `microtasks`:
- `mcp_microtask_id`: none unless Blender MCP is allowed
- `evidence_tier`: gate_review | quick_iteration
- `iteration_budget`: 1 for gate_review; 1-3 for quick_iteration
- `iteration_views`: front; three_quarter for quick_iteration, or the full required view set for gate_review
- `target_objects`: none unless Blender MCP is allowed
- `allowed_change_types`: none unless Blender MCP is allowed
- `execution_authorized_by`: none until authorized
- `execution_authorized_at`: none until authorized
- `risks`:
- `questions_for_director`:

## Active Edit Session (Schema 0.3)

- `workflow_mode`: active_session | legacy_evidence_tier
- `session_id`: none until a session is opened
- `authorized_collections`: none unless `workflow_mode` is active_session
- `safe_change_types`: absolute_transform; visibility; collection_membership; vertex_positions
- `max_targets_per_edit`: 6
- `viewport_preview_policy`: one relevant-angle get_viewport_screenshot; fallback one 512px Eevee render
- `checkpoint_triggers`: explicit checkpoint; stage transition; scope expansion; structural or destructive work; uncertainty; drift; evidence failure
- `pipeline_state`: <asset_root>/pipeline_state.json
- `session_journal`: <asset_root>/mcp_sessions/<session_id>.jsonl
- `source_file`:
- `backup_file`:
- `working_file`:
- `source_protection_receipt`:
- `preflight_cache_key`:

## Completion

- `completed_outputs`:
- `validation_summary`:
- `review_summary`:
- `blocking_issues`:
- `approved_by`:
- `approved_at`:
