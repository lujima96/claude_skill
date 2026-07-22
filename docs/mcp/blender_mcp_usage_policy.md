# Blender MCP Usage Policy

## Authorization

Blender MCP operates only inside a validated current-stage task card. New Blender stages use schema `0.3` with `workflow_mode: active_session`; unchanged `evidence_tier` cards remain valid.

The stage card is the authorization envelope. Each runtime journal record supplies the exact targets and normalized operations, so routine regional requests do not require new cards.

## Active-Session Fast Path

- Protect one source, backup, and working file once per session. Keep paths distinct, non-overwriting, and hash verified.
- Cache the server, version, capabilities, filepath, and working hash. Refresh only after reconnect, identity mismatch, capability/version change, or tool error.
- Batch related work into one execution against no more than six exact objects in authorized collections.
- Allow only absolute transforms, visibility, collection membership, and topology-preserving vertex-position updates.
- Require a clean expected working file before editing. Fingerprint, edit, validate drift and acceptance, then save only on success.
- Reject additions, deletions, renames, topology or material changes, non-target changes, unauthorized target-field changes, and unexpected vertex changes. Reload the last saved working file after in-memory failure.
- Append one hash-chained JSONL iteration record and capture one relevant-angle viewport preview. If viewport capture is unavailable, allow exactly one 512px Eevee preview render.
- Do not create per-edit Markdown logs, report bundles, specialist reviews, QA audits, validation summaries, manifest entries, working copies, or persistent multi-view renders.
- Reopen the protected baseline and replay accepted absolute journal operations for rollback recovery.
- Never promote a working file over source automatically.

## Checkpoints

Trigger a checkpoint on explicit request, stage transition, scope expansion, structural/destructive work, uncertainty, drift, evidence failure, or tool failure. Edit count alone is not a trigger.

Reuse the same task card and session. In one Blender call, capture the persistent front, side, back, three-quarter, and gameplay-distance views plus scene, mesh, material, and naming reports. Then create one aggregated action log referencing the journal, one relevant specialist review, one QA audit, and one validation report. Require human approval for disposition and any stage decision.

## Immediate Blocks

- Missing or invalid stage envelope, runtime receipt, protection, preflight, isolation, preview, or journal chain.
- Wrong or dirty Blender file, or source/backup/working hash mismatch.
- More than six targets, unauthorized collections, unsupported operations, scope expansion, or deterministic drift.
- Arbitrary Blender Python outside the explicitly approved isolated runner context.
- Destructive or structural operations without checkpoint authorization.
- Stage progression without required specialist, QA, validation, handoff, and human approval.

## Legacy Compatibility

Legacy `quick_iteration` and `gate_review` cards keep their existing target and iteration budgets, scene-delta receipts, screenshot manifests, and Markdown action logs. Quick iterations cannot approve or promote a stage. Do not migrate or rewrite historical evidence solely to use active sessions.
