---
name: blender-mcp-operator
description: Run protected, persistent Blender MCP edit sessions with declarative safe edits, deterministic drift checks, lightweight viewport evidence, replay rollback, and bundled review checkpoints. Use for stage-card-authorized Blender changes, session recovery, checkpoint evidence, or legacy quick-iteration and gate-review evidence.
---

# Blender MCP Operator

Operate only inside the current validated stage task card. Do not choose creative direction, promote source files, approve specialist domains, or advance stages.

The Blender MCP server can execute Python directly inside the active Blender session through `execute_blender_code`. Use it for bounded, deterministic inspection, editing, validation, baking, and viewport synchronization under the active session envelope; recover failed operations by reopening the last saved working file.

## Load the Minimum State

Resolve the nearest ancestor containing `AGENTS.md` as `project_root`. For a routine active-session edit, load only:

- `<asset_root>/pipeline_state.json`
- the referenced stage task card
- the tail of the referenced `mcp_sessions/<session_id>.jsonl`

Load `references/bounded_loop_rules.md` only when opening/recovering a session or running a checkpoint. Defer manifests, old reviews, handoffs, and broad policy documents until those events.

## Use the Active-Session Fast Path

1. Require task-card schema `0.3` and `workflow_mode: active_session`.
2. Reuse its source, backup, working file, protection receipt, and capability preflight. Refresh preflight only after reconnect, server/version/capability change, filepath/hash mismatch, or tool error.
3. Batch related safe changes into one request of at most six exact objects. Allow only `absolute_transform`, `visibility`, `collection_membership`, and topology-preserving `vertex_positions` within authorized collections.
4. Pass normalized absolute operations to `scripts/quick_edit_runner.py` in one MCP execution. Require the expected clean working file and hashes. Save only after deterministic delta checks pass.
5. Append the result with `scripts/mcp_session.py`. Never create a per-edit Markdown log, task card, working copy, report bundle, specialist review, QA audit, validation summary, manifest entry, or persistent multi-view render.
6. Capture one relevant-angle preview with `get_viewport_screenshot`. Journal its tool, view, dimensions, timestamp, and result. If unavailable, render exactly one 512px Eevee preview.
7. Use `scripts/viewer_sync.py` as a clean filepath/hash check. Reload only for explicit recovery.

On an in-memory failure, do not save; reopen the last saved working file. On rejected prior work, reopen the protected session baseline and replay only accepted normalized operations from `accepted_operations()`.

## Escalate

Escalate to `character-director` on scope expansion, stage uncertainty, or stage transition. Escalate to a checkpoint or blocked state on structural/destructive work, visual uncertainty, drift, evidence failure, or tool failure. Edit count alone never triggers a checkpoint.

At a checkpoint, reuse the same task card and session. Run `scripts/checkpoint_bundle.py` once to capture the five persistent views plus the scene, mesh, material, and naming reports. Then create one aggregated action log referencing `session_journal`, one specialist review, one QA audit, and one validation report. Human approval remains required at the gate.

## Compatibility

Legacy `evidence_tier` cards, quick Markdown logs, `scene_delta.py`, and `validate_mcp_iteration_receipt.py` remain supported. When handling them, follow the legacy section in `references/bounded_loop_rules.md` without converting historical evidence.
