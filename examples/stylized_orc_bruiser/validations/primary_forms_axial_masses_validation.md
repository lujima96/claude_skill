# Axial Primary-Forms Validation Report

## Metadata

- `validation_id`: stylized_orc_bruiser-primary-forms-axial-validation-001
- `asset_id`: stylized_orc_bruiser
- `stage_id`: primary_forms
- `validator_name`: primary-forms evidence validator set
- `validator_version`: repository current
- `created_at`: 2026-07-21
- `status`: pass

## Execution

- `command_or_tool`: validate_stage_task_card; validate_blender_report on five reports; validate_screenshot_manifest
- `input_artifacts`: protected working `.blend`; `reports/blender/primary_forms_axial_masses/`; `screenshots/primary_forms_axial_masses/`
- `output_artifacts`: validator stdout and this summary
- `environment`: Python standard library; Blender 5.2.0 LTS
- `duration_seconds`: not_measured

## Summary

- `passed_checks`: task card, five Blender reports, five-view screenshot manifest
- `warning_count`: blockout/primary-form warnings only
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
| primary_forms_incomplete | Limbs, hands, and feet remain blockout primitives. | Five-view screenshots. | Continue with a separate bounded primary-forms task after human review. |

## Measurements

- `adjusted_axial_objects`: 9
- `created_primary_form_objects`: 7
- `required_screenshots_captured`: 5 of 5 at 512x512
- `source_sha256_unchanged`: 54a1c5222cc4526d86c65e4783d372aa7a44e07609ef8174bfbeb8fc2f1151c2

## Machine-Readable Result

```json
{"status":"pass","hard_failures_present":false,"blocked_stage_progression":false}
```
