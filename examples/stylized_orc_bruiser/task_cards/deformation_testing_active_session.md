# Deformation Testing Active Session Task Card

- `schema_version`: 0.3
- `task_id`: stylized_orc_bruiser-deformation-testing-session-001
- `asset_id`: stylized_orc_bruiser
- `stage_id`: deformation_testing
- `stage_name`: Deformation testing
- `status`: approved
- `goal`: Run a pose battery against the rigged character and record corrective deformation issues.
- `previous_stage`: rigging_skinning
- `next_stage`: optimization_lods
- `allowed_tools`: Blender MCP Python; pose test scripts; validators
- `disallowed_tools`: export before deformation approval; unreviewed redesign
- `required_outputs`: pose battery renders; corrective issue list; checkpoint bundle
- `input_checkpoint`: `examples/stylized_orc_bruiser/checkpoints/rigging_skinning_001`
- `requires_human_approval`: yes
- `execution_authorized_by`: repository user
- `execution_authorized_at`: 2026-07-22
