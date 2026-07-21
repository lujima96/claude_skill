# Facial Readability Revision Validation Report

## Metadata

- `validation_id`: stylized_orc_bruiser-primary-forms-facial-readability-validation-001
- `asset_id`: stylized_orc_bruiser
- `stage_id`: primary_forms
- `validator_name`: revision evidence validator set
- `validator_version`: repository current
- `created_at`: 2026-07-21
- `status`: pass

## Execution

- `command_or_tool`: validate_stage_task_card; validate_blender_report on five reports; validate_screenshot_manifest
- `input_artifacts`: protected revision working `.blend`; facial revision reports and screenshots
- `output_artifacts`: validator stdout and this summary
- `environment`: Python standard library; Blender 5.2.0 LTS
- `duration_seconds`: not_measured

## Summary

- `passed_checks`: task card, five Blender reports, five-view screenshot manifest
- `warning_count`: primary-form stage warnings only
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
| future_face | Eyelids, mouth corners, jaw hinge, and tusk roots remain schematic. | Revision screenshots. | Address during later primary-form facial construction after animation scope is known. |

## Measurements

- `brow_center_gap_m`: 0.04512
- `eye_material`: MAT_ORC_eye_blockout
- `tusk_scale_factor`: 1.18
- `required_screenshots_captured`: 5 of 5 at 512x512
- `source_sha256_unchanged`: 6f882a0e4e373f31b3e3bf881fbb79ea3bf68791be884533de36c22ae05a7e15

## Machine-Readable Result

```json
{"status":"pass","hard_failures_present":false,"blocked_stage_progression":false}
```
