# Stylized Orc Bruiser Asset Manifest

## Metadata

- `asset_id`: stylized_orc_bruiser
- `asset_name`: Stylized Orc Bruiser
- `character_name`: Stylized Orc Bruiser
- `created_by`: Character Director
- `created_at`: 2026-07-21
- `last_updated`: 2026-07-21
- `status`: in_progress

## Project Paths

- `project_root`: .
- `brief`: brief.md
- `references_dir`: references
- `task_cards_dir`: task_cards
- `handoffs_dir`: handoffs
- `reviews_dir`: reviews
- `validations_dir`: validations
- `screenshots_dir`: screenshots
- `exports_dir`: none
- `godot_project_dir`: none

## Source Assets

- `source_blend_files`: source/stylized_orc_bruiser_blockout_source.blend; source/backups/stylized_orc_bruiser.blockout-primary-masses-001.before.blend; source/working/stylized_orc_bruiser.blockout-primary-masses-001.working.blend; source/approved/stylized_orc_bruiser_blockout.approved.blend; source/primary_forms/backups/stylized_orc_bruiser.primary-forms-axial-masses-001.before.blend; source/primary_forms/working/stylized_orc_bruiser.primary-forms-axial-masses-001.working.blend; source/primary_forms/revisions/backups/stylized_orc_bruiser.primary-forms-facial-readability-revision-001.before.blend; source/primary_forms/revisions/working/stylized_orc_bruiser.primary-forms-facial-readability-revision-001.working.blend; source/primary_forms/appendicular/backups/stylized_orc_bruiser.primary-forms-appendicular-masses-001.before.blend; source/primary_forms/appendicular/working/stylized_orc_bruiser.primary-forms-appendicular-masses-001.working.blend; source/primary_forms/extremities/backups/stylized_orc_bruiser.primary-forms-extremity-construction-001.before.blend; source/primary_forms/extremities/working/stylized_orc_bruiser.primary-forms-extremity-construction-001.working.blend; source/primary_forms/extremities/revisions/backups/stylized_orc_bruiser.primary-forms-footwear-readability-revision-001.before.blend; source/primary_forms/extremities/revisions/working/stylized_orc_bruiser.primary-forms-footwear-readability-revision-001.working.blend; source/secondary_anatomy/upper_torso/backups/stylized_orc_bruiser.secondary-anatomy-upper-torso-transitions-001.before.blend; source/secondary_anatomy/upper_torso/working/stylized_orc_bruiser.secondary-anatomy-upper-torso-transitions-001.working.blend; source/secondary_anatomy/consolidation/backups/stylized_orc_bruiser.secondary-anatomy-upperarm-consolidation-001.before.blend; source/secondary_anatomy/consolidation/working/stylized_orc_bruiser.secondary-anatomy-upperarm-consolidation-001.working.blend; source/secondary_anatomy/consolidation/backups/stylized_orc_bruiser.secondary-anatomy-pelvis-hip-consolidation-001.before.blend; source/secondary_anatomy/consolidation/working/stylized_orc_bruiser.secondary-anatomy-pelvis-hip-consolidation-001.working.blend; source/secondary_anatomy/consolidation/backups/stylized_orc_bruiser.secondary-anatomy-shin-calf-consolidation-001.before.blend; source/secondary_anatomy/consolidation/working/stylized_orc_bruiser.secondary-anatomy-shin-calf-consolidation-001.working.blend; source/secondary_anatomy/shoulder_pauldron/working/stylized_orc_bruiser.secondary-anatomy-shoulder-pauldron-clearance-001.working.blend; source/secondary_anatomy/facial_mechanics/working/stylized_orc_bruiser.secondary-anatomy-facial-mechanics-001.working.blend
- `sculpt_files`: none
- `retopo_files`: none
- `rig_files`: none
- `texture_source_files`: none
- `external_dependencies`: none

## Export Assets

- `glb_files`: none
- `gltf_files`: none
- `texture_files`: none
- `animation_files`: none
- `lod_files`: none
- `collision_files`: none

## Godot Assets

- `imported_scenes`: none
- `material_resources`: none
- `preview_scene`: none
- `animation_player_or_library`: none
- `skeleton_node`: none
- `marker_nodes`: none
- `collision_nodes`: none

## Technical Summary

- `target_engine`: Godot
- `target_godot_version`: unknown
- `interchange_format`: GLB
- `polycount_lod0`: not_applicable_to_primary_forms; primitive working file reports 9408 triangles
- `lod_count`: unknown
- `material_slot_count`: unknown
- `texture_sets`: unknown
- `max_skin_influences`: unknown
- `blend_shapes`: unknown
- `animation_clips`: unknown

## Validation State

- `latest_stage`: tertiary_detail
- `latest_handoff`: handoffs/secondary_anatomy_to_tertiary_detail.md
- `latest_qa_audit`: audit_secondary_anatomy_completion.md
- `hard_failures_present`: no
- `approved_for_next_stage`: yes

## Change Log

| Date | Change | Author | Related Stage |
|---|---|---|---|
| 2026-07-21 | Approved the completed secondary-anatomy stage and handed the validated facial-mechanics working file to tertiary detail. | Character Director | tertiary_detail |
| 2026-07-21 | Reversibly retired the paired redundant shin shells, reducing the active character from 65 to 63 meshes without deleting data. | Blender MCP Operator | secondary_anatomy |
| 2026-07-21 | Reversibly retired the paired redundant hip shells, reducing the active character from 67 to 65 meshes without deleting data. | Blender MCP Operator | secondary_anatomy |
| 2026-07-21 | Reversibly retired the paired redundant upperarm shells, reducing the active character from 69 to 67 meshes without deleting data. | Blender MCP Operator | secondary_anatomy |
| 2026-07-21 | Completed first protected secondary-anatomy upper-torso transition pass and retained it for human review. | Blender MCP Operator | secondary_anatomy |
| 2026-07-21 | User approved completed primary forms; created approved secondary-anatomy handoff and opened upper-torso transition task. | Character Director | secondary_anatomy |
| 2026-07-21 | Resolved mixed footwear/anatomy readability, recovered the saved revision after Blender exited, and completed all evidence. | Blender MCP Operator | primary_forms |
| 2026-07-21 | Completed protected hand-and-foot primary construction; QA recommends secondary anatomy pending the human stage gate. | Blender MCP Operator | primary_forms |
| 2026-07-21 | Completed protected appendicular primary-form pass and retained it for human review. | Blender MCP Operator | primary_forms |
| 2026-07-21 | Corrected user-reported brow intersection, eye-material ambiguity, and tusk visibility in a protected primary-forms revision. | Blender MCP Operator | primary_forms |
| 2026-07-21 | Completed protected axial primary-form microtask and retained it for human review; QA keeps the asset in primary forms. | Blender MCP Operator | primary_forms |
| 2026-07-21 | Recorded user-adjusted approved blockout, refreshed evidence, approved blockout handoff, and opened the first bounded primary-forms task. | Character Director | primary_forms |
| 2026-07-21 | Created protected live Blender blockout working copy, five-view evidence, specialist reviews, and passing blockout QA recommendation; retained for human review. | Blender MCP Operator | blockout |
| 2026-07-21 | Added Phase 11 Godot validation report, Phase 12 workflow completion gate, and final blocked QA audit. | Character Director | export_godot_validation |
| 2026-07-21 | Added Phase 10 UV/bake, material/texture, and optimization readiness reports and blocking QA audit. | Character Director | uvs_and_baking |
| 2026-07-21 | Added Phase 9 bounded Blender MCP action-log examples and operating policy links. | Character Director | blockout |
| 2026-07-21 | Added Phase 8 topology and rigging reviews plus blocking QA audit. | Character Director | retopology |
| 2026-07-21 | Added Phase 7 sample Blender report and screenshot manifest paths. | Character Director | manual_blockout |
| 2026-07-21 | Created preproduction manifest for Phase 6 validator testing. | Character Director | anatomy_blockout_planning |
