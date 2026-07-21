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

## Scope

- `task_card`:
- `specialist_owner`:
- `microtask_goal`:
- `allowed_tools`:
- `disallowed_tools`:
- `acceptance_tests`:
- `stop_conditions`:

## Source Protection

- `source_file`:
- `backup_file`:
- `working_file`:
- `backup_verified`: yes | no
- `destructive_operations_requested`: yes | no
- `destructive_operations_approved_by`:
- `destructive_operations_approved_at`:

## Action Trace

| Step | Tool Or Command | Intent | Result | Artifact |
|---:|---|---|---|---|
| 1 |  |  |  |  |

## Evidence

- `screenshots`:
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
- `decision`: approved | rejected | rolled_back | blocked
- `decision_reason`:
- `human_approval_required`: yes | no
- `approved_by`:
- `approved_at`:
