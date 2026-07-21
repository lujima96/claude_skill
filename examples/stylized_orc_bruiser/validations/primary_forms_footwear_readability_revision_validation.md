# Footwear Readability Revision Validation Report

## Metadata

- `validation_id`: stylized_orc_bruiser-primary-forms-footwear-readability-validation-001
- `asset_id`: stylized_orc_bruiser
- `stage_id`: primary_forms
- `validator_name`: footwear revision evidence validator set
- `validator_version`: repository current
- `created_at`: 2026-07-21
- `status`: pass

## Execution

- `command_or_tool`: validate_stage_task_card; validate_blender_report on five reports; validate_screenshot_manifest; SHA-256 verification
- `input_artifacts`: protected footwear revision working `.blend`; revision reports and screenshots
- `output_artifacts`: validator stdout and this summary
- `environment`: Python standard library; Blender 5.2.0 LTS
- `duration_seconds`: not_measured

## Summary

- `passed_checks`: task card, five Blender reports, five-view screenshot manifest, source protection, and scoped-object verification
- `warning_count`: 62 report warnings expected for reversible primitive construction
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
| non_applied_scale | Reversible construction primitives retain non-applied scale. | Naming report records 61 warnings with zero invalid names or negative scales. | Resolve during later mesh construction, before topology approval. |
| no_armature | No armature exists at primary-forms stage. | Scene report contains no armature. | Defer to the required rigging stage. |

## Measurements

- `target_objects_changed`: 8
- `untargeted_objects_verified`: 61
- `required_screenshots_captured`: 5 of 5 at 512x512
- `mesh_objects`: 63
- `triangles`: 9408
- `source_sha256_unchanged`: 015ce877fae2f6947245ab343e460b0e7d4a3e3b39e9f5e625921ed0ef6452c1
- `working_sha256`: 69813e68c1ccad5cf7a56afba8a14a3853d1f73828e97a8c856019deae1e9559

## Machine-Readable Result

```json
{"status":"pass","hard_failures_present":false,"blocked_stage_progression":false}
```
