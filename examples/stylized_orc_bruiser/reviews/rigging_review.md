# Stylized Orc Bruiser Rigging Review

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
- `artifacts`: `reports/blender/pose_battery.sample.json`; `reports/blender/mesh_report.sample.json`; `asset_manifest.md`
- `screenshots`: none
- `validation_reports`: none
- `references`: `knowledge/rigging/godot_biped_rig_requirements.md`; `knowledge/engine-standards/godot_import_requirements.md`; `knowledge/anatomy/deformation_landmarks.md`

## Review Scope

- `in_scope`: skeleton presence, skeleton naming readiness, skinning readiness, max influence policy, unweighted vertex checks, twist zones, corrective-shape needs, pose-battery evidence
- `out_of_scope`: topology approval, texture/material approval, final Godot import validation
- `assumptions`: no production rig exists; Phase 7 pose battery sample shows the expected report format

## Findings

| Severity | Category | Finding | Evidence | Recommendation | Blocking |
|---|---|---|---|---|---|
| critical | missing_armature | No armature exists for rigging approval. | Pose battery sample reports `armature_count: 0`; asset manifest lists `rig_files: none`. | Build the biped skeleton after retopology approval and declare naming, rest pose, and scale policy. | yes |
| critical | missing_skinning | No skinned mesh exists and no weights can be reviewed. | Pose battery sample reports `skinned_mesh_count: 0`; mesh sample reports `vertex_groups: 0`. | Skin the approved retopo mesh and run checks for unweighted vertices and influence limits. | yes |
| critical | pose_battery | Required deformation poses have not run. | Pose battery status is `readiness_only` and includes no pose-result items. | Run shoulder raise, elbow bend, wrist twist, hip flex, knee bend, ankle bend, neck turn, and jaw tests after rigging. | yes |
| medium | godot_contract | Godot rig policy is not locked. | Asset manifest lists `target_godot_version: unknown` and `max_skin_influences: unknown`. | Declare target Godot version, max skin influences, facial deformation scope, and required animation clips before final skinning. | no |

## Hard Failure Check

- `hard_failures_present`: yes
- `hard_failures`: armature is missing; skinned mesh is missing; pose-battery results are missing
- `blocked_stage_progression`: yes

## Score Contribution

- `category_scores`: deformation readiness 0/10; Godot readiness 1/10; performance and LODs pending
- `score_notes`: This review blocks because rigging artifacts and pose evidence do not exist yet.
- `confidence`: high

## Decision

- `decision`: block
- `decision_reason`: The asset cannot progress through rigging or deformation testing without an armature, skinned mesh, influence policy, and pose-battery results.
- `required_next_actions`: approve retopology first; create rigging task card; build skeleton; skin mesh; run pose battery; define Godot version, max influences, required clips, and facial deformation scope
- `suggested_next_actions`: decide whether the jaw, tusks, eyelids, and brow need animation before finalizing head rig controls
- `approved_by`: none
- `approved_at`: none
