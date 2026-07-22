# MCP Action Log

## Metadata

- `log_id`:
- `asset_id`:
- `stage_id`:
- `microtask_id`:
- `created_by`:
- `created_at`:
- `status`: draft | executed | approved | rejected | rolled_back | blocked
- `execution_mode`: real_mcp | dry_run | example
- `evidence_tier`: gate_review | quick_iteration
- `iteration_id`: none for gate_review
- `iteration_index`: 0 for gate_review

## Environment Preflight

- `project_root`:
- `blender_version`:
- `mcp_server`:
- `mcp_server_version`:
- `connection_status`: ready | unavailable | incompatible
- `required_capabilities`:
- `available_capabilities`:
- `capability_preflight`: pass | fail
- `isolated_workspace_verified`: yes | no
- `arbitrary_python_requested`: yes | no
- `arbitrary_python_approved_by`:

## Scope

- `task_card`:
- `specialist_owner`:
- `microtask_goal`:
- `allowed_tools`:
- `disallowed_tools`:
- `acceptance_tests`:
- `stop_conditions`:
- `target_objects`:
- `allowed_change_types`:

## Source Protection

- `source_file`:
- `backup_file`:
- `working_file`:
- `source_protection_receipt`:
- `backup_verified`: yes | no
- `source_sha256_before`:
- `backup_sha256`:
- `working_sha256_before`:
- `source_sha256_after`:
- `source_unchanged_verified`: yes | no
- `destructive_operations_requested`: yes | no
- `destructive_operations_approved_by`:
- `destructive_operations_approved_at`:

## Action Trace

| Step | Tool Or Command | Intent | Result | Artifact |
|---:|---|---|---|---|
| 1 |  |  |  |  |

## Evidence

- `session_journal`: none for legacy logs; required for active-session checkpoints
- `screenshots`:
- `iteration_receipt`: none for gate_review
- `blender_reports`:
- `validation_reports`:
- `specialist_review`:
- `qa_audit`:

## Outcome

- `structural_change_made`: yes | no
- `hard_failures_present`: yes | no
- `blocked_stage_progression`: yes | no
- `rollback_required`: yes | no
- `rollback_artifact`:
- `working_copy_disposition`: retained_for_iteration | retained_for_review | discarded | promoted_by_human | not_applicable
- `decision`: continue_iteration | approved | rejected | rolled_back | blocked
- `decision_reason`:
- `human_approval_required`: yes | no
- `approved_by`:
- `approved_at`:
