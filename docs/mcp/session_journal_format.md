# MCP Session Journal 0.1.0

Store one append-only journal at `<asset_root>/mcp_sessions/<session_id>.jsonl`. Write records with `skills/blender-mcp-operator/scripts/mcp_session.py` and validate them with `validators/validate_mcp_session.py`.

Every line is one canonical JSON object with:

- `schema_version`, `session_id`, contiguous `sequence`, `previous_record_hash`, and `record_hash`
- `record_type` and timezone-aware `timestamp`
- exact `targets` and normalized absolute `operations`
- `before_hash`, `after_hash`, deterministic `drift`, and phase/total `durations_ms`
- type-specific `details`

Record types are `session_started`, `iteration_accepted`, `iteration_rejected`, `preview_result`, `checkpoint_completed`, `rollback`, and `session_closed`. An accepted iteration must have a following successful viewport or Eevee-fallback preview record. A checkpoint must reference the screenshot manifest and four Blender reports. Never edit or delete prior lines; append recovery and rollback facts.
