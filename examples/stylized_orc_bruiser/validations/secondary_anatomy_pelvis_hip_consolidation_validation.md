# Secondary Anatomy Pelvis-Hip Consolidation Validation Report

## Metadata

- `validation_id`: stylized_orc_bruiser-secondary-anatomy-pelvis-hip-consolidation-validation-001
- `asset_id`: stylized_orc_bruiser
- `stage_id`: secondary_anatomy
- `validator_name`: pelvis-hip consolidation evidence validator set
- `validator_version`: repository current
- `created_at`: 2026-07-21
- `status`: pass

## Execution

- `command_or_tool`: validate_stage_task_card; validate_blender_report on five reports; validate_screenshot_manifest; SHA-256 verification
- `input_artifacts`: protected pelvis-hip consolidation working `.blend`; reports and screenshots
- `output_artifacts`: validator stdout and this summary
- `environment`: Python standard library; Blender 5.2.0 LTS
- `duration_seconds`: not_measured

## Summary

- `passed_checks`: task card, five Blender reports, five-view screenshot manifest, source protection, mesh preservation, target mesh preservation, and protected-object verification
- `warning_count`: 68 report warnings expected for reversible construction
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
| non_applied_scale | Reversible construction primitives retain non-applied scale. | Naming report records 67 warnings with zero invalid names or negative scales. | Resolve during later mesh construction. |
| no_armature | No armature exists during secondary anatomy. | Scene report. | Defer to mandatory rigging. |

## Measurements

- `total_mesh_objects_preserved`: 69
- `active_character_meshes`: 65
- `retired_recoverable_meshes`: 4
- `newly_retired_meshes`: 2
- `protected_objects_verified`: 73
- `required_screenshots_captured`: 5 of 5 at 512x512
- `triangles_preserved`: 10752
- `source_sha256_unchanged`: 240f9dc66264b80f1681e5f9326bba8a636117f9719c8257f6e5167d47eea1d6
- `working_sha256`: fb8547d699b8d6d98e12ad9edff90610f13e814a576f7fefb14cae4f7bf3064a

## Machine-Readable Result

```json
{"status":"pass","hard_failures_present":false,"blocked_stage_progression":false}
```
