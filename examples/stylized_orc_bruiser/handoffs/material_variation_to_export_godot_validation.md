# Material Variation Handoff

- `asset_id`: stylized_orc_bruiser
- `from_stage`: texturing_materials
- `to_stage`: export_godot_validation
- `status`: pending human approval
- `session_journal`: `examples/stylized_orc_bruiser/mcp_sessions/material-variation-session-001.jsonl`
- `working_file`: `examples/stylized_orc_bruiser/source/mcp_sessions/material-variation-session-001/working/stylized_orc_bruiser.material-variation-session-001.working.blend`
- `checkpoint`: `examples/stylized_orc_bruiser/checkpoints/material_variation_001`
- `export`: `examples/stylized_orc_bruiser/exports/stylized_orc_bruiser_material_variation_game_ready.glb`
- `manual_source_baseline_sha256`: `30ec9f2c15697b489a8a4447047442ee12e5fb577c1ebed4341d274f64d3d172`

## Completed

- Preserved the approved belt working file as the protected material-stage baseline.
- Added restrained warmer greens to the nose, ears, eyelids, elbows, palms, fingers, thumbs, and lips.
- Added cooler, darker generated gradients beneath the chest and belly.
- Added compact pupils and transparent specular corneal shells; all four new eye layers follow the head bone and passed pose testing.
- Kept tusks on `ORC_TUSK_IVORY` and assigned finger/thumb tip faces to the separate `ORC_NAIL_KERATIN` material.
- Darkened leather and added subtle procedural color/roughness variation.
- Assigned the belt's rolled edges a lighter worn-edge leather response.
- Set buckle hardware to 0.92 metallic with restrained 0.18-0.32 roughness variation.
- Scene, mesh, and material checkpoint reports pass; naming remains a warning only.
- GLB structure validates with one skin and the `ORC_IDLE` animation.
- Blender is synchronized to the accepted working file in Material Preview.

## Remaining gate

Human visual approval is pending. Godot import and preview validation remain blocked because no Godot executable is installed in the current environment.
