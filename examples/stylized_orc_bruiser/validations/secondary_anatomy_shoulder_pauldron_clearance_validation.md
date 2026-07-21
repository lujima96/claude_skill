# Secondary Anatomy Shoulder-Pauldron Clearance Validation Report

## Metadata

- `validation_id`: stylized_orc_bruiser-secondary-anatomy-shoulder-pauldron-clearance-validation-001
- `asset_id`: stylized_orc_bruiser
- `stage_id`: secondary_anatomy
- `validator_name`: shoulder-pauldron gate evidence validator set
- `validator_version`: repository current
- `created_at`: 2026-07-21
- `status`: pass

## Execution

- `command_or_tool`: validate_stage_task_card; validate_blender_report on five reports; validate_screenshot_manifest; validate_mcp_iteration_receipt; SHA-256 verification
- `input_artifacts`: protected shoulder-pauldron working `.blend`; quick delta receipt; gate reports and screenshots
- `output_artifacts`: validator stdout and this summary
- `environment`: Python standard library; Blender 5.2.0 LTS
- `duration_seconds`: not_measured

## Summary

- `passed_checks`: task cards, quick delta receipt, five Blender reports, five-view screenshot manifest, source protection, mesh preservation, and protected-object verification
- `warning_count`: 68 stage-expected report warnings
- `failure_count`: 0
- `hard_failure_count`: 0
- `blocked_stage_progression`: no

## Hard Failures

| Rule ID | Rule | Evidence | Required Fix |
|---|---|---|---|
| none | none | all required validators exited 0 | none |

## Warnings

| Rule ID | Rule | Evidence | Suggested Fix |
|---|---|---|---|
| non_applied_scale | Reversible construction primitives retain non-applied scale. | Naming report records 67 warnings with zero invalid names or negative scales. | Resolve during later production mesh construction. |
| no_armature | No armature exists during secondary anatomy. | Scene report. | Defer to mandatory rigging. |

## Measurements

- `total_mesh_objects_preserved`: 69
- `active_character_meshes`: 63
- `retired_recoverable_meshes`: 6
- `quick_changed_objects`: 1
- `quick_protected_objects_verified`: 74
- `required_screenshots_captured`: 5 of 5 at 512x512
- `source_sha256_unchanged`: c8ff9a2e61ed5e737bea21e2fa4d4c498275bcbb0735e073c481cdc02004c02b
- `backup_sha256_unchanged`: c8ff9a2e61ed5e737bea21e2fa4d4c498275bcbb0735e073c481cdc02004c02b
- `working_sha256`: 4403c6f7e771c48097ccb6e49fce57f37fcc2accf0300c3daeab7d9b3c949e82

## Machine-Readable Result

```json
{"status":"pass","hard_failures_present":false,"blocked_stage_progression":false}
```
