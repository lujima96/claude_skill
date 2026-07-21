# Blender MCP Usage Policy

## Purpose

Blender MCP is allowed only after the pipeline has a task card, approval gate, specialist acceptance tests, and validator path. It is not a replacement for the Character Director or specialist reviews.

## Operating Rules

- One MCP task may contain up to three quick iterations inside one bounded regional microtask, followed by one full gate review.
- Do not issue broad instructions such as "finish the character", "fix the model", "make it better", or "complete the rig".
- Every microtask must have a task card, acceptance tests, and stop conditions before MCP execution.
- Source `.blend` files must be copied before modification.
- Source, backup, and working files must be distinct, hash-verified, and created without overwriting existing files.
- Resolve the project root from `AGENTS.md` before loading contracts or evidence paths.
- Record the Blender version, MCP server/version, exact tool names, required capabilities, and available capabilities before execution.
- Block real MCP work when capability preflight fails or the workspace is not isolated.
- Every meaningful structural change must be followed by screenshots. Quick iterations require front and three-quarter previews; gate reviews require the full task-card set.
- Relevant validators must run before the next modeling pass.
- Every MCP command, tool result, warning, and decision must be recorded in an action log. Quick iterations may use a compact log plus a validated scene-delta receipt.
- Destructive operations require explicit human approval before execution.
- If an MCP command changes scope, stop the loop and request Director review.
- If reports or screenshots are missing, the loop cannot be approved.
- Example or dry-run logs cannot satisfy a live approval gate.
- Never promote a working file over source automatically; record human-controlled disposition separately.

## Allowed MCP Work

- Rename or organize objects when the naming contract is clear.
- Move, scale, or adjust a small set of blockout forms for a specific accepted proportion issue.
- Add a simple marker, camera, light, or collection required for review.
- Apply one local topology, rigging, or material correction when a specialist has defined exact acceptance tests.
- Export or screenshot only when the export or screenshot command is explicitly allowed by the task card.

## Quick Iteration Mode

Quick iteration exists to reduce repeated evidence work without weakening rollback or drift detection.

- Reuse one verified working copy and backup for no more than three iterations in one task.
- Limit the task to one anatomical region and at most six exact target objects.
- Allow only transforms, visibility, collection membership, and vertex-position changes with unchanged topology counts.
- Capture a deterministic before/after scene fingerprint and reject missing, added, renamed, topology-changed, or unexpected objects.
- Capture front and three-quarter previews and validate their manifest.
- Defer Blender report bundles, specialist review, QA audit, asset-manifest updates, and human approval to the gate review.
- Never use quick iteration to approve progression or promote a working file.

## Disallowed MCP Work

- Broad sculpting, retopology, rigging, texturing, or animation without a bounded task card.
- Any hidden destructive cleanup.
- Deleting source assets without explicit approval.
- Applying transforms, merging meshes, decimating, remeshing, baking, or exporting over source files unless the task card specifically allows it.
- Adding, deleting, renaming, changing topology counts, editing materials, rigging, exporting, or performing destructive work in quick iteration mode.
- Advancing a stage without specialist review, QA audit, and human approval.

## Required Loop

1. Character Director selects one bounded regional microtask and its evidence tier.
2. Specialist defines acceptance tests and hard-failure checks.
3. MCP connection and capabilities pass preflight.
4. Source, backup, and working files are created with a verified hash receipt.
5. Blender MCP executes a short edit burst against named targets.
6. Quick iterations capture two views plus a scene-delta receipt; the gate captures the full screenshot set and restores scene state.
7. Required validators run for the selected tier.
8. At the gate, Blender reports run and the specialist reviews output.
9. At the gate, QA Auditor scores result.
10. Human approves, rejects, or requests revision at the gate.
11. Source hash is rechecked and the action log is closed.

## Approval Rules

- `approved`: all required artifacts exist, validators pass, no hard failures, human approval recorded.
- `rejected`: output is reviewable but fails acceptance or style/anatomy/topology/rigging requirements.
- `rolled_back`: output is discarded and source backup is retained.
- `blocked`: required evidence is missing or MCP attempted to exceed scope.

## Server Policy

Use the approved Blender MCP server for the workspace. The policy is server-agnostic: official or community servers must both obey the same task-card, backup, screenshot, validation, review, audit, and approval gates.
