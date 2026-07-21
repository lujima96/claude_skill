# Appendicular Primary-Forms Validation Report

## Metadata

- `validation_id`: stylized_orc_bruiser-primary-forms-appendicular-validation-001
- `asset_id`: stylized_orc_bruiser
- `stage_id`: primary_forms
- `validator_name`: appendicular evidence validator set
- `validator_version`: repository current
- `created_at`: 2026-07-21
- `status`: pass

## Execution

- `command_or_tool`: validate_stage_task_card; validate_blender_report on five reports; validate_screenshot_manifest
- `input_artifacts`: protected appendicular working `.blend`; appendicular reports and screenshots
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
| hand_foot_construction | Hands and feet remain simplified masses without palm/finger or arch/toe construction. | Five-view screenshots. | Complete one bounded hand/foot primary-form pass before secondary anatomy. |

## Measurements

- `refined_existing_objects`: 22
- `created_primary_form_objects`: 8
- `protected_object_matrices_verified`: 31
- `required_screenshots_captured`: 5 of 5 at 512x512
- `source_sha256_unchanged`: 206ace149aadff49d83e94c9af0bccade755aa3b74788d782fc46c9c761e8818

## Machine-Readable Result

```json
{"status":"pass","hard_failures_present":false,"blocked_stage_progression":false}
```
