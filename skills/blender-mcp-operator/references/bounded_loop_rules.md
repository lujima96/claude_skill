# Bounded Loop Rules

## Tier Selection

Choose `quick_iteration` only when all conditions hold:

- A validated task card already names one anatomical region and no more than six target objects.
- A verified source, backup, working copy, and protection receipt already exist.
- The edit is reversible and limited to transforms, visibility, collection membership, or vertex positions with unchanged topology counts.
- No stage decision or human approval is requested yet.
- The task has completed fewer than three quick iterations since its last gate.

Otherwise choose `gate_review`.

## Quick Iteration Loop

1. Verify the current Blender filepath equals the protected working file and the file is not an unrelated dirty scene.
2. Validate the task card with `evidence_tier: quick_iteration` and `status: ready` or `in_progress`.
3. Capture a pre-edit fingerprint with `scripts/scene_delta.py`.
4. Execute one short MCP burst against only the named targets and safe change types.
5. Save only the working file and finalize the scene-delta receipt.
6. Require no missing, added, renamed, or unexpectedly changed objects and no target topology-count changes.
7. Capture `front` and `three_quarter` screenshots at 512 pixels or greater.
8. Validate the screenshot manifest, iteration receipt, and compact MCP action log.
9. Keep the working copy and task `in_progress`; do not write specialist review, QA audit, manifest promotion, or human approval records.
10. After all iteration evidence validates, run `scripts/viewer_sync.py` against the validated working file. Require the exact filepath, its current disk hash, and a clean Blender state before returning control to the user.
11. Run `gate_review` after the third iteration, at a region boundary, on user review, or on any uncertainty.

## Gate Review Loop

1. Load task card.
2. Validate one microtask, named targets, allowed change types, and execution authorization.
3. Resolve the project root and preflight the exact MCP server capabilities.
4. For a new task, create and verify the source-protection receipt, backup, and working copy. When closing quick iterations, verify and retain the task's existing protected files.
5. Execute the short Blender MCP edit burst against only the working file.
6. Save the working file only.
7. Capture and validate the screenshot set; confirm scene state was restored.
8. Run Blender reports and document validators.
9. Route to specialist review and QA audit.
10. Recheck the source hash and wait for human disposition. Never merge automatically.
11. After gate evidence and disposition records validate, run `scripts/viewer_sync.py` against the retained validated working file and leave Blender clean on that exact file.

## Immediate Stop Conditions

- The command would delete or overwrite the only source file.
- The command affects unrelated model regions.
- The output cannot be screenshotted.
- A validator fails.
- The specialist review marks a hard failure.
- The user has not approved a destructive operation.
- The MCP server or required capability is absent.
- The workspace is not isolated or arbitrary Python lacks explicit approval.
- Source, backup, working-copy, or receipt hashes do not match.
- A quick iteration adds, deletes, renames, or changes topology counts.
- A quick iteration changes an object outside its target allowlist.
- A quick iteration requests materials, destructive work, export, rigging, or stage progression.
- Blender's current filepath differs from the expected validated working file at end-of-step sync.
