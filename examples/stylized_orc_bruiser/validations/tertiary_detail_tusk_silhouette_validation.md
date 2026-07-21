# Tertiary Detail Tusk Silhouette Validation Report

## Metadata

- `validation_id`: stylized_orc_bruiser-tertiary-detail-tusk-silhouette-validation-001
- `asset_id`: stylized_orc_bruiser
- `stage_id`: tertiary_detail
- `validator_name`: tusk silhouette gate validator set
- `validator_version`: repository current
- `created_at`: 2026-07-21
- `status`: pass

## Execution

- `command_or_tool`: task, screenshot, Blender-report, scene-delta, review, QA, action-log, and hash validators
- `input_artifacts`: protected tusk working `.blend`; quick receipt; gate evidence
- `output_artifacts`: validator stdout and this summary
- `environment`: Python standard library; Blender 5.2.0 LTS
- `duration_seconds`: not_measured

## Summary

- `passed_checks`: all required tusk quick and gate checks
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
- `source_sha256_unchanged`: 7c7608bcf9b0f1966a96aae2966d7dd8a475bb9829c1401483acf369f672c041
- `working_sha256`: 15d9fff637507873da2370d262c7a87c4084e8c3889715d009eb0bc4c70eb446

## Machine-Readable Result

```json
{"status":"pass","hard_failures_present":false,"blocked_stage_progression":false}
```
