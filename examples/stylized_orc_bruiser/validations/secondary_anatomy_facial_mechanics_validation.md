# Secondary Anatomy Facial Mechanics Validation Report

## Metadata

- `validation_id`: stylized_orc_bruiser-secondary-anatomy-facial-mechanics-validation-001
- `asset_id`: stylized_orc_bruiser
- `stage_id`: secondary_anatomy
- `validator_name`: facial-mechanics gate evidence validator set
- `validator_version`: repository current
- `created_at`: 2026-07-21
- `status`: pass

## Execution

- `command_or_tool`: task, screenshot, Blender-report, scene-delta, review, QA, action-log, and SHA-256 validators
- `input_artifacts`: protected facial working `.blend`; quick receipt; gate reports and screenshots
- `output_artifacts`: validator stdout and this summary
- `environment`: Python standard library; Blender 5.2.0 LTS
- `duration_seconds`: not_measured

## Summary

- `passed_checks`: task cards, quick delta, five Blender reports, five-view manifest, source protection, mesh preservation, and protected-object verification
- `warning_count`: 68 stage-expected report warnings
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
| non_applied_scale | Construction primitives retain non-applied scale. | Naming report records 67 warnings. | Resolve during production mesh construction. |
| no_armature | No armature exists during secondary anatomy. | Scene report. | Defer to mandatory rigging. |

## Measurements

- `total_mesh_objects_preserved`: 69
- `active_character_meshes`: 63
- `retired_recoverable_meshes`: 6
- `quick_changed_objects`: 5
- `quick_protected_objects_verified`: 70
- `required_screenshots_captured`: 5 of 5 at 512x512
- `source_sha256_unchanged`: 4403c6f7e771c48097ccb6e49fce57f37fcc2accf0300c3daeab7d9b3c949e82
- `working_sha256`: 7c7608bcf9b0f1966a96aae2966d7dd8a475bb9829c1401483acf369f672c041

## Machine-Readable Result

```json
{"status":"pass","hard_failures_present":false,"blocked_stage_progression":false}
```
