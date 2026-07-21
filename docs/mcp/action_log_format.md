# MCP Action Log Format

MCP action logs record what was allowed, what happened, what changed, and how the result was reviewed.

Use `templates/mcp_action_log.md` for every Blender MCP loop.

## Required Evidence

- The task card that bounded the work.
- Project-root resolution and MCP capability preflight.
- The source file and backup copy.
- The working-copy protection receipt and matching hashes.
- The working file changed by MCP.
- The exact allowed tools or commands.
- A chronological action table.
- Screenshot manifest after structural change.
- Blender reports and document validator output.
- Specialist review.
- QA audit or QA decision.
- Human approval state.
- Source-unchanged verification and working-copy disposition.

## Blocking Conditions

- Missing backup.
- Missing or failed capability preflight.
- Missing protection receipt, hash mismatch, or changed source file.
- Missing action rows.
- Missing screenshot manifest after structural change.
- Missing validator output.
- Missing specialist review.
- Destructive operation without explicit approval.
- Final decision says approved while hard failures are present.
- Example or dry-run evidence is presented as live approval.
- Loop changes more than one microtask.
