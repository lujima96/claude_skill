# Example Godot Export Review

## Metadata

- `review_id`: stylized_orc_bruiser-export_godot_validation-godot_export_reviewer-001
- `asset_id`: stylized_orc_bruiser
- `stage_id`: export_godot_validation
- `review_type`: godot_export
- `reviewer`: Godot Export Reviewer
- `created_at`: 2026-07-21
- `status`: blocked

## Inputs Reviewed

- `task_card`: pending
- `artifacts`: `reports/godot/godot_validation_report.md`; `asset_manifest.md`
- `screenshots`: none
- `validation_reports`: none
- `references`: `engine/godot/import_checklist.md`; `engine/godot/preview_scene_checklist.md`

## Review Scope

- `in_scope`: Godot import, scene opening, Skeleton3D, materials, textures, animations, blend shapes, markers, collision, preview render
- `out_of_scope`: Blender modeling fixes, texture authoring, rig authoring
- `assumptions`: no real Godot import has been performed for the orc asset yet

## Findings

| Severity | Category | Finding | Evidence | Recommendation | Blocking |
|---|---|---|---|---|---|
| critical | missing_import | No Godot import package exists. | Manifest lists `glb_files: none`, `gltf_files: none`, and `imported_scenes: none`. | Export a production GLB/glTF and import it into the Godot project. | yes |
| critical | missing_preview | No Godot preview scene or screenshot exists. | Manifest lists `preview_scene: none`. | Create preview scene and capture render evidence. | yes |

## Hard Failure Check

- `hard_failures_present`: yes
- `hard_failures`: no Godot import package; no preview scene
- `blocked_stage_progression`: yes

## Score Contribution

- `category_scores`: Godot readiness 0/10
- `score_notes`: The review blocks because engine evidence does not exist yet.
- `confidence`: high

## Decision

- `decision`: block
- `decision_reason`: Final Godot readiness cannot be approved without import and preview evidence.
- `required_next_actions`: create export package; import into Godot; run import probe; fill Godot validation report; capture preview screenshot
- `suggested_next_actions`: lock target Godot version before the import pass
- `approved_by`: none
- `approved_at`: none
