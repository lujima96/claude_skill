# Example Materials Review Report

## Metadata

- `review_id`: stylized_orc_bruiser-texturing_materials-materials_reviewer-001
- `asset_id`: stylized_orc_bruiser
- `stage_id`: texturing_materials
- `review_type`: materials
- `reviewer`: Materials Reviewer
- `created_at`: 2026-07-21
- `status`: blocked

## Inputs Reviewed

- `task_card`: pending
- `artifacts`: `reports/blender/material_report.sample.json`; `asset_manifest.md`
- `screenshots`: none
- `validation_reports`: none
- `references`: `knowledge/materials/godot_character_materials.md`

## Review Scope

- `in_scope`: material slots, material naming, texture set coverage, texture naming, texture size, channel packing, Godot texture paths
- `out_of_scope`: UV unwrap approval, topology approval, rigging, final Godot import
- `assumptions`: sample material report documents expected shape only; no final texture package exists

## Findings

| Severity | Category | Finding | Evidence | Recommendation | Blocking |
|---|---|---|---|---|---|
| critical | missing_textures | No production texture files exist. | Asset manifest lists `texture_source_files: none` and `texture_files: none`. | Create texture sets for approved material families before material approval. | yes |
| critical | channel_packing | Channel packing policy is unknown. | Material knowledge note lists channel packing as unresolved. | Define map channels before validating texture package completeness. | yes |
| high | godot_paths | Godot texture path policy is not set. | Asset manifest lists `godot_project_dir: none`; export assets are empty. | Define export folder and Godot import texture path convention. | yes |

## Hard Failure Check

- `hard_failures_present`: yes
- `hard_failures`: production textures, channel packing policy, and Godot texture paths are missing
- `blocked_stage_progression`: yes

## Score Contribution

- `category_scores`: materials and texture logic 0/10; Godot readiness 1/10
- `score_notes`: Review blocks because required texture package evidence does not exist.
- `confidence`: high

## Decision

- `decision`: block
- `decision_reason`: Materials cannot be approved until texture sets, naming, sizes, channel packing, and Godot export paths are declared and validated.
- `required_next_actions`: approve UV/bake readiness first; define material budget; create texture package; run material and texture readiness validators
- `suggested_next_actions`: decide whether Godot-side material overrides or imported materials are the default
- `approved_by`: none
- `approved_at`: none
