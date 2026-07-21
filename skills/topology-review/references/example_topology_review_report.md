# Example Topology Review Report

## Metadata

- `review_id`: stylized_orc_bruiser-retopology-topology_reviewer-001
- `asset_id`: stylized_orc_bruiser
- `stage_id`: retopology
- `review_type`: topology
- `reviewer`: Topology Reviewer
- `created_at`: 2026-07-21
- `status`: blocked

## Inputs Reviewed

- `task_card`: pending
- `artifacts`: `reports/blender/mesh_report.sample.json`
- `screenshots`: `screenshots/screenshot_manifest.sample.json`
- `validation_reports`: none
- `references`: `knowledge/topology/biped_deformation_loops.md`

## Review Scope

- `in_scope`: retopology readiness, edge-flow evidence, pole and triangle risk, loop density, bake-readiness blockers
- `out_of_scope`: anatomy approval, skin weights, materials, Godot import
- `assumptions`: sample report shape represents the expected evidence format, not a real production retopo mesh

## Findings

| Severity | Category | Finding | Evidence | Recommendation | Blocking |
|---|---|---|---|---|---|
| critical | missing_artifact | No production retopology mesh is available for approval. | Asset manifest lists `retopo_files: none`; sample mesh report is marked `stage_id: manual_blockout`. | Create a retopology task card and submit the production mesh plus deformation-zone screenshots. | yes |
| high | deformation_loops | Critical loops around face, shoulder, elbow, hip, knee, neck, fingers, and cloth zones are not reviewable. | Mesh report contains object metrics but no loop-zone evidence. | Capture topology screenshots and annotate loop direction for each deformation zone. | yes |
| medium | bake_readiness | Bake readiness cannot be evaluated without low-poly/high-poly pairing and cage notes. | Export and mesh samples do not name bake source assets. | Add bake target, high-poly source, cage strategy, and material ID assumptions before UV/bake review. | no |

## Hard Failure Check

- `hard_failures_present`: yes
- `hard_failures`: production retopology mesh and critical loop evidence are missing
- `blocked_stage_progression`: yes

## Score Contribution

- `category_scores`: topology and edge flow 0/10; deformation readiness 1/10; UV and baking readiness 1/10
- `score_notes`: The score reflects missing required artifacts, not a failed mesh implementation.
- `confidence`: high

## Decision

- `decision`: block
- `decision_reason`: Retopology approval cannot proceed until a production mesh and deformation-zone evidence exist.
- `required_next_actions`: create retopology task card; produce retopo mesh; run mesh and naming reports; capture topology screenshots for face, shoulder, elbow, hip, knee, neck, hands, and cloth zones
- `suggested_next_actions`: add topology-specific references before the retopology pass
- `approved_by`: none
- `approved_at`: none
