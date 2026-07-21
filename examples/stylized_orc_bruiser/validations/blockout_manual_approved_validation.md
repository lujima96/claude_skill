# Human-Adjusted Blockout Validation Report

## Metadata

- `validation_id`: stylized_orc_bruiser-blockout-manual-approved-validation-001
- `asset_id`: stylized_orc_bruiser
- `stage_id`: blockout
- `validator_name`: blockout evidence validator set
- `validator_version`: repository current
- `created_at`: 2026-07-21
- `status`: pass

## Execution

- `command_or_tool`: validate_blender_report on five reports; validate_screenshot_manifest
- `input_artifacts`: `source/approved/stylized_orc_bruiser_blockout.approved.blend`; `reports/blender/blockout_manual_approved/`; `screenshots/blockout_manual_approved/`
- `output_artifacts`: validator stdout and this summary
- `environment`: Python standard library; Blender 5.2.0 LTS
- `duration_seconds`: not_measured

## Summary

- `passed_checks`: five Blender reports and five-view screenshot manifest
- `warning_count`: report-level blockout warnings only
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
| blockout_only | No armature and unapplied primitive scales remain. | Scene and naming reports. | Expected; do not apply transforms until a later authorized production task. |

## Measurements

- `adjusted_objects`: ORC_bracer_L; ORC_bracer_R; ORC_shoulder_pad_L; ORC_belt
- `required_screenshots_captured`: 5 of 5 at 512x512
- `approved_blockout`: `source/approved/stylized_orc_bruiser_blockout.approved.blend`

## Machine-Readable Result

```json
{"status":"pass","hard_failures_present":false,"blocked_stage_progression":false}
```
