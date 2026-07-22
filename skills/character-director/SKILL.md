---
name: character-director
description: Orchestrate staged Blender-to-Godot character production, including stage envelopes, active edit sessions, checkpoints, handoffs, specialist routing, and hard-failure decisions. Use when opening or changing a stage, expanding Blender edit scope, resolving uncertainty, reviewing a checkpoint, or blocking skipped topology, deformation, rigging, optimization, and Godot gates.
---

# Character Director

Own stage order, authorization envelopes, handoffs, routing, and blocking decisions. Do not perform specialist or Blender edits.

## Routine Routing

Load `<asset_root>/pipeline_state.json` first. When it points to a validated active session and the request stays within authorized collections and safe change types, route directly to `blender-mcp-operator`. Do not create another task card, working copy, protection receipt, or regional gate.

Invoke the Director for a new asset or stage, scope expansion, uncertainty, checkpoint, safety escalation, rollback requiring a new baseline, or stage transition. Load manifests and historical reviews only when opening a session or reviewing a checkpoint.

## Open a Stage

1. Confirm the preceding handoff and human approval.
2. Load `references/stage_order.md`, `references/hard_failures.md`, and `references/handoff_rules.md`.
3. Create one stage task card from `templates/stage_task_card.md` with schema `0.3` and `workflow_mode: active_session` when Blender editing is expected.
4. Authorize stage collections, safe change types, a six-target per-edit limit, preview policy, and checkpoint triggers. Record one reusable source, backup, working file, protection receipt, and preflight cache key.
5. Create the session journal and update `pipeline_state.json`.

Do not invent unknown production targets. Record them as blocking questions.

## Review a Checkpoint

Require the same task card and session journal, the bundled five-view and Blender-report evidence, one aggregated action log, the relevant specialist review, QA audit, validation report, and human decision. Hard failures override scores. On approval, update `pipeline_state.json`; create a handoff only when changing stages.

Use these decisions: `approve_next_stage`, `revise_current_stage`, `return_to_previous_stage`, or `block_progression`.

## Routing

Route routine safe Blender edits only to `blender-mcp-operator`. At checkpoints, route the smallest relevant domain review: references, style, anatomy, topology, UV/bake, materials, rigging, optimization, or Godot export. Route aggregated scoring to `qa-audit`.

Never skip retopology, rigging, deformation testing, optimization, or Godot validation. `GLB` or `glTF` is the default interchange unless an exception is recorded.

Legacy task cards and evidence tiers remain valid; do not migrate historical artifacts solely to adopt active sessions.
