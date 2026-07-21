# Example Rigging Review Report

## Metadata

- `review_id`: stylized_orc_bruiser-rigging_skinning-rigging_reviewer-001
- `asset_id`: stylized_orc_bruiser
- `stage_id`: rigging_skinning
- `review_type`: rigging
- `reviewer`: Rigging Reviewer
- `created_at`: 2026-07-21
- `status`: blocked

## Inputs Reviewed

- `task_card`: pending
- `artifacts`: `reports/blender/pose_battery.sample.json`; `reports/blender/scene_report.sample.json`
- `screenshots`: none
- `validation_reports`: none
- `references`: `knowledge/rigging/godot_biped_rig_requirements.md`; `knowledge/engine-standards/godot_import_requirements.md`

## Review Scope

- `in_scope`: skeleton presence, skinning readiness, pose-battery evidence, Godot rig risks
- `out_of_scope`: retopology approval, material validation, final Godot import
- `assumptions`: sample reports show evidence format only; no real rig has been authored yet

## Findings

| Severity | Category | Finding | Evidence | Recommendation | Blocking |
|---|---|---|---|---|---|
| critical | missing_armature | No armature exists, so rigging approval and pose testing cannot proceed. | Pose battery sample reports `armature_count: 0`. | Create the biped skeleton with declared naming, scale, rest pose, and Godot import assumptions. | yes |
| critical | missing_skinning | No mesh has an armature modifier or skinning data. | Pose battery sample reports `skinned_mesh_count: 0`; mesh report shows `vertex_groups: 0`. | Skin the approved retopo mesh and run unweighted-vertex and max-influence checks. | yes |
| high | pose_battery | Required deformation poses have not run. | Pose battery status is `readiness_only` and reports no pose items. | Run shoulder, elbow, wrist, hip, knee, ankle, neck, and jaw tests after rigging. | yes |
| medium | godot_contract | Target Godot version and max influence policy remain unknown. | Asset manifest lists `target_godot_version: unknown` and `max_skin_influences: unknown`. | Lock Godot version and influence budget before final skinning approval. | no |

## Hard Failure Check

- `hard_failures_present`: yes
- `hard_failures`: armature, skinning data, and pose-battery evidence are missing
- `blocked_stage_progression`: yes

## Score Contribution

- `category_scores`: deformation readiness 0/10; Godot readiness 1/10; topology dependency unresolved
- `score_notes`: The review blocks because required rig artifacts are absent.
- `confidence`: high

## Decision

- `decision`: block
- `decision_reason`: Rigging and deformation approval cannot proceed without an armature, skinned mesh, influence policy, and pose-battery results.
- `required_next_actions`: approve retopology first; create rigging task card; build skeleton; skin mesh; run pose battery; declare Godot version and max skin influence policy
- `suggested_next_actions`: decide facial deformation scope before head and jaw controls are finalized
- `approved_by`: none
- `approved_at`: none
