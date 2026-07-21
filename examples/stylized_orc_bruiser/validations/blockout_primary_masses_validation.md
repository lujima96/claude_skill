# Primary-Mass Blockout Validation Report

## Metadata

- `validation_id`: stylized_orc_bruiser-blockout-primary-masses-validation-001
- `asset_id`: stylized_orc_bruiser
- `stage_id`: blockout
- `validator_name`: blockout evidence validator set
- `validator_version`: repository current
- `created_at`: 2026-07-21
- `status`: pass

## Execution

- `command_or_tool`: validate_stage_task_card; validate_blender_report on scene, mesh, material, naming, and screenshot reports; validate_screenshot_manifest
- `input_artifacts`: `task_cards/blockout_primary_masses.md`; `reports/blender/blockout_primary_masses/`; `screenshots/blockout_primary_masses/stylized_orc_bruiser_blockout_screenshot_manifest.json`
- `output_artifacts`: validator stdout and this summary
- `environment`: Python standard library; Blender 5.2.0 LTS
- `duration_seconds`: not_measured

## Summary

- `passed_checks`: task card; five Blender reports; screenshot manifest
- `warning_count`: 28 report-level warnings
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
| no_armature | No armature exists at blockout. | Scene report warning. | Expected; defer to rigging stage. |
| scale_not_applied | 27 primitive blockout objects retain non-unit scale. | Naming report warnings. | Expected for non-destructive blockout; resolve during production mesh construction, not this MCP task. |

## Measurements

- `mesh_object_count`: 41 including the untouched default cube
- `blockout_collection_object_count`: 44 including review camera and lights
- `vertices`: 2428
- `triangles`: 4692
- `material_count`: 6
- `required_screenshots_captured`: 5 of 5 at 512x512
- `source_sha256_unchanged`: be96690a0369b29ca13dffe085fb0768bc4d48fdbfe014924ae6255639f72f5d

## Machine-Readable Result

```json
{
  "validation_id": "stylized_orc_bruiser-blockout-primary-masses-validation-001",
  "status": "pass",
  "hard_failures_present": false,
  "blocked_stage_progression": false
}
```
