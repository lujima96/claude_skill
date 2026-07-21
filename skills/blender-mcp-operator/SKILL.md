---
name: blender-mcp-operator
description: Operate and validate one bounded Blender MCP microtask for a staged Blender-to-Godot character asset. Use when a ready task card authorizes a specific Blender edit, when source/backup/working copies must be protected, when MCP capabilities need preflight, or when screenshots, Blender reports, action logs, rollback evidence, specialist review, QA audit, and human approval must gate a Blender change.
---

# Blender MCP Operator

Execute only the Blender edit authorized by one ready task card. Do not choose creative direction, approve specialist domains, promote a working file over source, or advance a pipeline stage.

## Resolve Contracts

Find the nearest ancestor containing `AGENTS.md` and treat it as `project_root`. Stop if these repository-root-relative contracts are absent:

- `docs/mcp/blender_mcp_usage_policy.md`
- `templates/mcp_action_log.md`
- `templates/stage_task_card.md`
- `validators/validate_stage_task_card.py`
- `validators/validate_mcp_action_log.py`

Load `references/bounded_loop_rules.md` before any real MCP action.

## Execute the Loop

1. Validate the task card. Require `status: ready`, one `mcp_microtask_id`, explicit target objects, allowed change types, acceptance tests, stop conditions, and execution authorization.
2. Enumerate the connected Blender MCP server, version, exact tool names, and capabilities. Record required and available capabilities in the action log. Block when the server is absent, incompatible, or broader than the approved scope.
3. Require an isolated workspace. Treat arbitrary Blender Python as disallowed unless the task card and action log record explicit approval.
4. Run `scripts/prepare_working_copy.py` to create distinct backup and working `.blend` files plus a hash receipt. Open and edit only the working file.
5. Execute one short MCP action burst against only the named targets and allowed change types. Record every tool call and result verbatim enough to reproduce the action.
6. Capture the task-card-required views with `blender_scripts/screenshot_set.py`, naming the target collection or objects explicitly.
7. Generate the required Blender JSON reports. Validate the task card, every Blender report, the screenshot manifest, and the final action log.
8. Route evidence to the named specialist and `qa-audit`. Stop on scope drift, failed validation, missing evidence, or any hard failure.
9. Record human approval, rejection, or rollback. Verify the source hash again. Never promote the working file automatically.

## Required Action-Log State

Use `templates/mcp_action_log.md`. For `real_mcp`, record:

- Project root, Blender/MCP versions, connection state, capabilities, isolation, and Python approval state.
- One microtask, target objects, allowed change types, and exact action trace.
- Source, backup, working copy, protection receipt, and before/after hashes.
- Screenshot manifest, Blender reports, validation reports, specialist review, and QA audit.
- Source-unchanged verification, working-copy disposition, final decision, and human approval state.

Use only `approved`, `rejected`, `rolled_back`, or `blocked` as final decisions. Example and dry-run approval never satisfies a live gate.

## Stop Immediately

- Stop when source, backup, and working paths are not distinct or hash verification fails.
- Stop before deletion, merge, transform application, remesh, decimation, bake, export, or arbitrary Python unless explicitly authorized.
- Stop when an MCP tool cannot be bounded to the named targets.
- Stop when screenshots or validators fail, a specialist reports a hard failure, or scope expands.
- Return scope changes to `character-director` as a new or revision task card.
