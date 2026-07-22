# Tertiary Detail Session Checkpoint Validation Report

## Metadata

- `validation_id`: stylized_orc_bruiser-tertiary-detail-session-checkpoint-validation-001
- `asset_id`: stylized_orc_bruiser
- `stage_id`: tertiary_detail
- `validator_name`: active-session checkpoint validator set
- `validator_version`: repository current
- `created_at`: 2026-07-22
- `status`: warning

## Execution

- `command_or_tool`: bundled Blender checkpoint capture; session-journal, task-card, screenshot-manifest, Blender-report, review, QA, and action-log validators
- `input_artifacts`: protected active-session working `.blend`; append-only session journal
- `output_artifacts`: five-view screenshot manifest; scene, mesh, material, and naming reports; this validation summary
- `environment`: Blender 5.2.0 LTS; Python standard library
- `duration_seconds`: 1.719596 for bundled Blender checkpoint capture

## Summary

- `passed_checks`: protected source and backup unchanged; working file clean; journal chain valid; five required views captured; mesh and material reports pass; no invalid names or negative scales
- `warning_count`: 68 stage-expected report warnings
- `failure_count`: 0
- `hard_failure_count`: 0
- `blocked_stage_progression`: no

## Hard Failures

| Rule ID | Rule | Evidence | Required Fix |
|---|---|---|---|
| none | none | all hard-failure checks clear | none |

## Warnings

| Rule ID | Rule | Evidence | Suggested Fix |
|---|---|---|---|
| construction_scales | Construction objects retain non-applied scale. | Naming report records 67 objects; no negative scales. | Resolve deliberately during production-mesh reconstruction, before rigging. |
| no_armature | The scene has no armature at this stage. | Scene report. | Add and validate the armature in the rigging stage. |

## Measurements

- `polycount`: 5,514 vertices; 6,000 faces; 10,752 triangles across 69 mesh objects
- `material_slots`: 69 slots across 6 materials
- `texture_sets`: 2 referenced images; 0 missing
- `skin_influences`: 0; rigging deferred
- `missing_files`: none reported
- `godot_import_status`: deferred to downstream export validation
- `screenshot_manifest_status`: pass; front, side, back, three-quarter, and gameplay-distance views captured at 768 by 768

## Machine-Readable Result

```json
{
  "validation_id": "stylized_orc_bruiser-tertiary-detail-session-checkpoint-validation-001",
  "status": "warning",
  "hard_failures_present": false,
  "blocked_stage_progression": false,
  "rules": [
    {"rule_id": "construction_scales", "status": "warning", "count": 67},
    {"rule_id": "no_armature", "status": "warning", "count": 1}
  ]
}
```
