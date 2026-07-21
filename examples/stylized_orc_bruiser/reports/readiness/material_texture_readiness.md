# Stylized Orc Bruiser Material Texture Readiness

## Metadata

- `report_id`: stylized_orc_bruiser-material-texture-readiness-001
- `asset_id`: stylized_orc_bruiser
- `stage_id`: texturing_materials
- `created_by`: Materials Reviewer
- `created_at`: 2026-07-21
- `status`: blocked

## Inputs

- `material_report`: `reports/blender/material_report.sample.json`
- `texture_manifest`: none
- `export_package_report`: `reports/blender/export_package.sample.json`
- `related_task_card`: pending

## Material Checks

- `material_slot_count`: 4
- `max_material_slots`: 4
- `material_slot_status`: pass
- `material_naming_status`: warning
- `required_material_families`: skin; cloth; leather; metal; bone; eyes; weapon_or_gear
- `missing_material_families`: cloth; leather; metal; bone; eyes; weapon_or_gear

## Texture Checks

- `texture_sets_present`: no
- `texture_naming_status`: unknown
- `texture_size_status`: unknown
- `max_texture_size`: unknown
- `missing_textures`: base_color; normal; roughness_or_orm; ambient_occlusion; material_id
- `channel_packing_policy`: unknown
- `channel_packing_status`: unknown
- `godot_texture_paths_status`: unknown
- `alpha_policy`: unknown

## Hard Failure Check

- `hard_failures_present`: yes
- `hard_failures`: required material families are missing; texture sets are missing; channel packing and Godot texture paths are unknown
- `blocked_stage_progression`: yes

## Decision

- `decision`: block
- `decision_reason`: Texture readiness cannot pass without production textures, naming, size, channel packing, and Godot path policy.
- `required_next_actions`: create texture package; declare map naming; declare max texture size; declare channel packing; declare Godot texture paths
- `suggested_next_actions`: decide material override policy before Godot adapter work
