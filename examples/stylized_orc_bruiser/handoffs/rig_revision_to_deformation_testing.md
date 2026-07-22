# Rig Revision Handoff

- `asset_id`: stylized_orc_bruiser
- `from_stage`: rigging_skinning (shoulder and armor revision)
- `to_stage`: deformation_testing
- `status`: pending human approval
- `session_journal`: `examples/stylized_orc_bruiser/mcp_sessions/rig-revision-session-001.jsonl`
- `working_file`: `examples/stylized_orc_bruiser/source/mcp_sessions/rig-revision-session-001/working/stylized_orc_bruiser.rig-revision-session-001.working.blend`
- `checkpoint`: `examples/stylized_orc_bruiser/checkpoints/rig_revision_002`
- `export`: `examples/stylized_orc_bruiser/exports/stylized_orc_bruiser_rig_revision_game_ready.glb`
- `manual_source_baseline_sha256`: `996217400b037da0811fa17a0941cb3b93e412eb51c21b36c8d10bd327d750be`

## Completed

- Preserved the user's current saved model and pose as the protected baseline.
- Confirmed the visible duplicate shoulder came from overlapping outer lobes in `ORC_CHEST_CONTINUOUS` and the authoritative deltoids in `ORC_ARM_RETOPO_L/R`; hidden high-source shoulders were not rendering.
- Trimmed 1,223 outer chest vertices without changing topology.
- Added clavicle influence to the remaining chest transitions and proximal arm vertices.
- Preserved all 18 existing bones and added 11 dedicated clavicle and armor/accessory bones, bringing the exported skin to 29 joints.
- Bound bracers, belt hardware, front/back loincloths, boots, and retained shoulder armor to dedicated bones.
- Removed obsolete vertex groups from rigid bone-parented gear.
- Audited every visible armor/gear object; none remain unbound.
- Passed a raised-left-arm deformation test without the duplicate shoulder shell and restored the exact saved pose afterward.
- Scene, mesh, and material checkpoint reports pass; naming remains a warning only.
- GLB validates with one 29-joint skin and the `ORC_IDLE` animation.
- Blender is synchronized to the accepted file in Pose Mode with all bones visible and `clavicle_L` active.

## Remaining gate

Human visual approval is pending before the broader deformation test matrix. Godot import and preview validation remain blocked because no Godot executable is installed in the current environment.
