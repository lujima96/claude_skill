# Stylized Orc Bruiser Topology Review

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
- `artifacts`: `reports/blender/mesh_report.sample.json`; `asset_manifest.md`
- `screenshots`: `screenshots/screenshot_manifest.sample.json`
- `validation_reports`: none
- `references`: `knowledge/topology/biped_deformation_loops.md`; `knowledge/anatomy/deformation_landmarks.md`; `reference_boards/approved_initial_board.md`

## Review Scope

- `in_scope`: retopology readiness, deformation-loop evidence, pole and triangle risk, loop density, bake-readiness blockers
- `out_of_scope`: anatomy approval, skin weights, materials, animation clips, Godot import validation
- `assumptions`: Phase 7 sample reports document expected report shapes only; no production retopology mesh has been submitted

## Findings

| Severity | Category | Finding | Evidence | Recommendation | Blocking |
|---|---|---|---|---|---|
| critical | missing_artifact | No production retopology mesh exists for approval. | `asset_manifest.md` lists `retopo_files: none`; mesh sample is scoped to `manual_blockout`. | Create a retopology task card and submit the production mesh before topology review. | yes |
| critical | deformation_loops | Required loops around face, shoulders, elbows, hips, knees, neck, fingers, and cloth zones are not reviewable. | Mesh sample has object counts and triangles but no loop-zone screenshots or annotated topology evidence. | Capture front, side, back, three-quarter, and close-up topology screenshots for every critical zone. | yes |
| high | pole_triangle_risk | Pole placement and triangle hot spots cannot be evaluated. | Mesh sample reports triangle counts but not pole placement or zone-local triangle placement. | Add annotated topology views and revise any poles or triangles in high-bend regions. | yes |
| medium | bake_readiness | Bake readiness is unproven. | No low-poly/high-poly pair, cage strategy, UV plan, or material ID map is listed. | Add bake target, high-poly source, cage assumptions, and material ID plan before UV/bake work. | no |

## Hard Failure Check

- `hard_failures_present`: yes
- `hard_failures`: production retopology mesh is missing; required deformation-loop evidence is missing; pole and triangle placement are unreviewable
- `blocked_stage_progression`: yes

## Score Contribution

- `category_scores`: topology and edge flow 0/10; UV and baking readiness 1/10; deformation readiness 1/10
- `score_notes`: This review blocks because required retopology artifacts do not exist yet.
- `confidence`: high

## Decision

- `decision`: block
- `decision_reason`: The asset cannot progress through retopology approval until a production mesh and deformation-zone topology evidence are submitted.
- `required_next_actions`: create retopology task card; produce production retopo mesh; run mesh and naming reports; capture annotated topology screenshots for face, shoulder, elbow, wrist, hip, knee, ankle, hand, neck, and cloth/accessory zones
- `suggested_next_actions`: add explicit hand, knee, hip, and facial topology references before the retopology pass
- `approved_by`: none
- `approved_at`: none
