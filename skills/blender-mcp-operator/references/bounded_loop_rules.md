# Bounded Loop Rules

## Minimum Loop

1. Load task card.
2. Validate one microtask, named targets, allowed change types, and execution authorization.
3. Resolve the project root and preflight the exact MCP server capabilities.
4. Create and verify the source-protection receipt, backup, and working copy.
5. Execute the short Blender MCP edit burst against only the working file.
6. Save the working file only.
7. Capture and validate the screenshot set; confirm scene state was restored.
8. Run Blender reports and document validators.
9. Route to specialist review and QA audit.
10. Recheck the source hash and wait for human disposition. Never merge automatically.

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
