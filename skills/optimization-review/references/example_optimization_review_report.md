# Example Optimization Review Report

## Metadata

- `review_id`: stylized_orc_bruiser-optimization_lods-optimization_reviewer-001
- `asset_id`: stylized_orc_bruiser
- `stage_id`: optimization_lods
- `review_type`: optimization
- `reviewer`: Optimization Reviewer
- `created_at`: 2026-07-21
- `status`: blocked

## Inputs Reviewed

- `task_card`: pending
- `artifacts`: `asset_manifest.md`; `reports/blender/mesh_report.sample.json`; `reports/blender/material_report.sample.json`; `reports/blender/export_package.sample.json`
- `screenshots`: none
- `validation_reports`: none
- `references`: `knowledge/engine-standards/godot_import_requirements.md`; `knowledge/materials/godot_character_materials.md`

## Review Scope

- `in_scope`: LOD naming, LOD polycount budgets, material-slot budget, texture size policy, GLB package completeness, Godot texture paths
- `out_of_scope`: final Godot import validation, material art approval, rig deformation approval
- `assumptions`: no production export package exists yet

## Findings

| Severity | Category | Finding | Evidence | Recommendation | Blocking |
|---|---|---|---|---|---|
| critical | lod_policy | LOD count, naming, and budgets are unknown. | Asset manifest lists `lod_count: unknown`; export assets list `lod_files: none`. | Define LOD policy and create LOD assets before optimization approval. | yes |
| critical | package_completeness | GLB/glTF package is not complete. | Export package sample is dry-run only; manifest lists `glb_files: none` and `gltf_files: none`. | Produce export package report from a real package after materials and rigging are ready. | yes |
| high | budgets | Polycount, material slot, and texture budgets are unresolved. | Manifest lists `polycount_lod0: unknown`, `material_slot_count: unknown`, and `texture_sets: unknown`. | Lock budgets before optimization review. | yes |

## Hard Failure Check

- `hard_failures_present`: yes
- `hard_failures`: LOD policy, production package, and performance budgets are missing
- `blocked_stage_progression`: yes

## Score Contribution

- `category_scores`: performance and LODs 0/10; Godot readiness 1/10
- `score_notes`: Review blocks because optimization evidence and export package data do not exist yet.
- `confidence`: high

## Decision

- `decision`: block
- `decision_reason`: Optimization cannot be approved until budgets, LOD policy, and package completeness are validated.
- `required_next_actions`: define platform budgets; create LOD assets if required; run mesh, material, export package, texture readiness, and LOD readiness validators
- `suggested_next_actions`: choose whether LODs are separate `.glb` exports or a single scene hierarchy before Godot adapter work
- `approved_by`: none
- `approved_at`: none
