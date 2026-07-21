# Tertiary Detail Brow Wedge Refinement Validation Report

## Metadata

- `validation_id`: stylized_orc_bruiser-tertiary-detail-brow-wedge-refinement-validation-001
- `asset_id`: stylized_orc_bruiser
- `stage_id`: tertiary_detail
- `validator_name`: brow wedge refinement gate validator set
- `validator_version`: repository current
- `created_at`: 2026-07-21
- `status`: pass

## Execution

- `command_or_tool`: task, screenshot, Blender-report, scene-delta, review, QA, action-log, and hash validators
- `input_artifacts`: protected brow working `.blend`; quick receipt; gate evidence
- `output_artifacts`: validator stdout and this summary
- `environment`: Python standard library; Blender 5.2.0 LTS
- `duration_seconds`: not_measured

## Summary

- `passed_checks`: all required brow quick and gate checks
- `warning_count`: 68 stage-expected report warnings
- `failure_count`: 0
- `hard_failure_count`: 0
- `blocked_stage_progression`: no

## Hard Failures

| Rule ID | Rule | Evidence | Required Fix |
|---|---|---|---|
| none | none | all validators exited 0 | none |

## Warnings

| Rule ID | Rule | Evidence | Suggested Fix |
|---|---|---|---|
| construction_scales | Construction objects retain non-applied scale. | Naming report. | Resolve during production mesh work. |

## Measurements

- `changed_objects`: 2
- `protected_objects_verified`: 73
- `topology_count_changes`: 0
- `required_screenshots_captured`: 5 of 5
- `source_sha256_unchanged`: 15d9fff637507873da2370d262c7a87c4084e8c3889715d009eb0bc4c70eb446
- `working_sha256`: 4035e74fc6a1cf6842717c71e96c5766382525de399924e6431ff5eb923817d0

## Machine-Readable Result

```json
{"status":"pass","hard_failures_present":false,"blocked_stage_progression":false}
```
