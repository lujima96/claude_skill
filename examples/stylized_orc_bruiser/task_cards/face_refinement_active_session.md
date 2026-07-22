# Face Refinement Active Session Task Card

- `schema_version`: 0.3
- `workflow_mode`: active_session
- `task_id`: stylized_orc_bruiser-face-refinement-session-001
- `asset_id`: stylized_orc_bruiser
- `stage_id`: secondary_anatomy
- `revision_of`: secondary_anatomy_refinement_revision
- `status`: approved
- `goal`: Make the face the focal point with stronger eyelids, brow ridge, muzzle integration, organic lip color, embedded tusks, and a readable expression.
- `source_baseline`: `examples/stylized_orc_bruiser/source/mcp_sessions/secondary-anatomy-refinement-revision-session-001/working/stylized_orc_bruiser.secondary-anatomy-refinement-revision-session-001.working.blend`
- `authorized_collections`: `ORC_BLOCKOUT`, `ORC_HIGH_SOURCE_TMP`
- `safe_change_types`: `absolute_transform`, `vertex_positions`, `visibility`, `collection_membership`
- `max_targets_per_edit`: 6
- `viewport_preview_policy`: one current-angle face preview after every accepted batch; black-material face checkpoint
- `checkpoint_triggers`: face geometry completion, structural additions, drift, evidence failure, or scope expansion
- `required_outputs`: face session journal, face checkpoint bundle, updated working file, updated GLB
- `requires_human_approval`: yes
- `execution_authorized_by`: repository user
- `execution_authorized_at`: 2026-07-22
