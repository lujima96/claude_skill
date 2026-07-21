# Secondary Anatomy Upper-Torso Transitions Validation Report

## Metadata

- `validation_id`: stylized_orc_bruiser-secondary-anatomy-upper-torso-validation-001
- `asset_id`: stylized_orc_bruiser
- `stage_id`: secondary_anatomy
- `validator_name`: upper-torso transition evidence validator set
- `validator_version`: repository current
- `created_at`: 2026-07-21
- `status`: pass

## Execution

- `command_or_tool`: validate_stage_task_card; validate_blender_report on five reports; validate_screenshot_manifest; SHA-256 verification
- `input_artifacts`: protected secondary-anatomy working `.blend`; upper-torso reports and screenshots
- `output_artifacts`: validator stdout and this summary
- `environment`: Python standard library; Blender 5.2.0 LTS
- `duration_seconds`: not_measured

## Summary

- `passed_checks`: task card, five Blender reports, five-view screenshot manifest, source protection, and protected-object verification
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
| non_applied_scale | Reversible construction primitives retain non-applied scale. | Naming report records 67 warnings with zero invalid names or negative scales. | Resolve during later mesh construction, before topology approval. |
| no_armature | No armature exists during secondary anatomy. | Scene report. | Defer to mandatory rigging. |

## Measurements

- `created_secondary_form_objects`: 6
- `approved_preexisting_objects_verified`: 69
- `required_screenshots_captured`: 5 of 5 at 512x512
- `mesh_objects`: 69
- `triangles`: 10752
- `source_sha256_unchanged`: 69813e68c1ccad5cf7a56afba8a14a3853d1f73828e97a8c856019deae1e9559
- `working_sha256`: 1c1b3e63292a2f2045aa6bbb3a2bd5f4e58bcb7a3a3516b8a6f17750919c9701

## Machine-Readable Result

```json
{"status":"pass","hard_failures_present":false,"blocked_stage_progression":false}
```
