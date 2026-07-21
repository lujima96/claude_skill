---
name: blender-mcp-operator
description: Operate protected Blender MCP character edits using quick iterations inside one bounded task and full evidence at review gates. Use when a ready task card authorizes named Blender targets, source/backup/working copies need protection, minor reversible edits need fast delta validation, or screenshots, reports, specialist review, QA, and human approval must gate a checkpoint.
---

# Blender MCP Operator

Execute only edits authorized by one ready task card. Do not choose creative direction, approve specialist domains, promote a working file over source, or advance a pipeline stage.

## Resolve Contracts

Find the nearest ancestor containing `AGENTS.md` and treat it as `project_root`. Stop if these repository-root-relative contracts are absent:

- `docs/mcp/blender_mcp_usage_policy.md`
- `templates/mcp_action_log.md`
- `templates/stage_task_card.md`
- `validators/validate_stage_task_card.py`
- `validators/validate_mcp_action_log.py`

Load `references/bounded_loop_rules.md` before any real MCP action. Read only the section for the selected evidence tier.

## Select One Evidence Tier

- Use `quick_iteration` for a minor, reversible edit inside an already approved regional task. Limit the task to six named objects and three iterations. Allow transforms, visibility or collection changes, and vertex-position edits that preserve topology. Prohibit add, delete, rename, merge, remesh, topology-count changes, transform application, material edits, bake, export, rigging, and stage progression.
- Use `gate_review` for the first edit in an unprotected task, the final checkpoint, user review, scope changes, uncertain visual results, destructive or topology-changing work, and every stage decision.
- Escalate immediately from quick to gate when a delta receipt reports unexpected drift, topology-count changes, missing objects, evidence failure, or scope expansion.

## Execute the Loop

1. Validate the task card. Require one `mcp_microtask_id`, explicit target objects, allowed change types, acceptance tests, stop conditions, execution authorization, and `evidence_tier`. Require `status: ready` for the first execution and allow `in_progress` for later quick iterations.
2. Enumerate the connected Blender MCP server, version, exact tool names, and capabilities. Record required and available capabilities in the action log. Block when the server is absent, incompatible, or broader than the approved scope.
3. Require an isolated workspace. Treat arbitrary Blender Python as disallowed unless the task card and action log record explicit approval.
4. For a new task, run `scripts/prepare_working_copy.py` once. Reuse that protected working copy for later quick iterations in the same task; never fork from or overwrite the source.
5. Before each quick edit, use `scripts/scene_delta.py` to capture a scene fingerprint. Execute one short MCP action burst, save only the working file, then finalize and validate the delta receipt.
6. For `quick_iteration`, capture `front` and `three_quarter` views, validate them with the delta receipt and compact action log, keep the task `in_progress`, and continue only within the iteration budget.
7. For `gate_review`, capture the full task-card view set, generate required Blender reports, validate all evidence, and route it to the specialist and `qa-audit`.
8. Stop on scope drift, failed validation, missing evidence, or any hard failure.
9. Record human approval, rejection, or rollback only at a gate. Verify the source hash again. Never promote the working file automatically.
10. End every completed quick iteration, gate, rollback, or recovery with `scripts/viewer_sync.py`. Reload only when Blender already has the expected working filepath, then require that exact validated file to be open with `bpy.data.is_dirty == false`. Report the synced filepath to the user.

## Required Action-Log State

Use `templates/mcp_action_log.md`. Always record:

- Project root, Blender/MCP versions, connection state, capabilities, isolation, and Python approval state.
- One microtask, target objects, allowed change types, and exact action trace.
- Source, backup, working copy, protection receipt, and before/after hashes.
- `evidence_tier`, iteration identity, screenshot manifest, and exact action trace.
- Source-unchanged verification, working-copy disposition, final decision, and human approval state.

For `quick_iteration`, also record and validate the scene-delta receipt. Set specialist review and QA to `deferred_to_gate_review`; never mark the iteration approved or promote it. For `gate_review`, record Blender reports, validation reports, specialist review, and QA audit as before.

Use `continue_iteration` only for a passing quick iteration. Use `approved`, `rejected`, `rolled_back`, or `blocked` at gates. Example and dry-run approval never satisfies a live gate.

## Stop Immediately

- Stop when source, backup, and working paths are not distinct or hash verification fails.
- Stop quick iteration when its task exceeds six targets or three iterations.
- Stop quick iteration on object addition, deletion, rename, topology-count change, material edit, or an operation outside its safe allowlist.
- Stop before deletion, merge, transform application, remesh, decimation, bake, export, or arbitrary Python unless explicitly authorized.
- Stop when an MCP tool cannot be bounded to the named targets.
- Stop when screenshots or validators fail, a specialist reports a hard failure, or scope expands.
- Stop end-of-step sync when Blender has a different filepath than the expected working file. Never discard or replace an unrelated dirty scene to satisfy viewer sync.
- Return scope changes to `character-director` as a new or revision task card.
