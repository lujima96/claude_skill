# Session and Gate Rules

## Open or Recover an Active Session

1. Validate the schema-0.3 stage card and confirm explicit authorization.
2. Create non-overwriting backup and working copies once with `prepare_working_copy.py`.
3. Confirm source, backup, and working hashes; cache MCP server, version, capabilities, filepath, and working hash.
4. Start `<asset_root>/mcp_sessions/<session_id>.jsonl` and update `pipeline_state.json`.
5. Never refresh protection or preflight during routine edits unless their recorded identity changes, the MCP reconnects, or a tool errors.

Recover a failed in-memory edit by reopening the last saved working file. Recover a rejected saved iteration by reopening the protected baseline and replaying journaled accepted absolute operations. Append a `rollback` record; never rewrite earlier records.

## Checkpoint

Trigger a checkpoint on explicit request, scope expansion, structural/destructive work, uncertainty, drift, evidence failure, stage transition, or closure. Do not trigger one from edit count.

Use the existing card and session. In one bundled Blender execution, capture five persistent views and the scene, mesh, material, and naming reports. Validate the journal and artifacts, then write one aggregated action log, specialist review, QA audit, and validation report. Require human approval at the gate. Update state and create a handoff only for stage transition.

## Immediate Stops

- Wrong or dirty Blender file before editing.
- Source, backup, working, receipt, filepath, or hash mismatch.
- More than six exact targets or a target outside authorized collections.
- Addition, deletion, rename, topology/material change, non-target drift, or unsupported operation.
- Missing preview, failed journal chain, unavailable recovery baseline, or failed validator.
- Destructive or structural work without explicit checkpoint authorization.

## Legacy Evidence-Tier Path

For an unchanged legacy card, preserve `gate_review` and `quick_iteration` behavior, `scene_delta.py`, `validate_mcp_iteration_receipt.py`, and Markdown action logs. Do not rewrite historical evidence. A legacy quick iteration remains limited to its card's target and iteration budgets and cannot approve or promote a stage.
