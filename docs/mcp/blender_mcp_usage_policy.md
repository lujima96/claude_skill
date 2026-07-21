# Blender MCP Usage Policy

## Purpose

Blender MCP is allowed only after the pipeline has a task card, approval gate, specialist acceptance tests, and validator path. It is not a replacement for the Character Director or specialist reviews.

## Operating Rules

- One MCP loop may execute one bounded microtask only.
- Do not issue broad instructions such as "finish the character", "fix the model", "make it better", or "complete the rig".
- Every microtask must have a task card, acceptance tests, and stop conditions before MCP execution.
- Source `.blend` files must be copied before modification.
- Every meaningful structural change must be followed by screenshots.
- Relevant validators must run before the next modeling pass.
- Every MCP command, tool result, warning, and decision must be recorded in an action log.
- Destructive operations require explicit human approval before execution.
- If an MCP command changes scope, stop the loop and request Director review.
- If reports or screenshots are missing, the loop cannot be approved.

## Allowed MCP Work

- Rename or organize objects when the naming contract is clear.
- Move, scale, or adjust a small set of blockout forms for a specific accepted proportion issue.
- Add a simple marker, camera, light, or collection required for review.
- Apply one local topology, rigging, or material correction when a specialist has defined exact acceptance tests.
- Export or screenshot only when the export or screenshot command is explicitly allowed by the task card.

## Disallowed MCP Work

- Broad sculpting, retopology, rigging, texturing, or animation without a bounded task card.
- Any hidden destructive cleanup.
- Deleting source assets without explicit approval.
- Applying transforms, merging meshes, decimating, remeshing, baking, or exporting over source files unless the task card specifically allows it.
- Advancing a stage without specialist review, QA audit, and human approval.

## Required Loop

1. Character Director selects one microtask.
2. Specialist defines acceptance tests and hard-failure checks.
3. Source file is copied to a working file.
4. Blender MCP executes a short edit burst.
5. Screenshot set is captured.
6. Required Blender reports and document validators run.
7. Specialist reviews output.
8. QA Auditor scores result.
9. Human approves, rejects, or requests revision.
10. Action log is closed with the final decision.

## Approval Rules

- `approved`: all required artifacts exist, validators pass, no hard failures, human approval recorded.
- `rejected`: output is reviewable but fails acceptance or style/anatomy/topology/rigging requirements.
- `rolled_back`: output is discarded and source backup is retained.
- `blocked`: required evidence is missing or MCP attempted to exceed scope.

## Server Policy

Use the approved Blender MCP server for the workspace. The policy is server-agnostic: official or community servers must both obey the same task-card, backup, screenshot, validation, review, audit, and approval gates.
