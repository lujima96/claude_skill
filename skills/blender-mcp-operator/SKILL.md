---
name: blender-mcp-operator
description: Operate a bounded Blender MCP edit loop for staged Blender-to-Godot character production. Use when a task card authorizes one specific Blender MCP microtask and requires source backup, action logging, screenshots, validators, specialist review, QA audit, and human approval.
---

# Blender MCP Operator

The Blender MCP Operator executes only bounded Blender edits. It does not choose broad creative direction, approve specialist domains, or skip validation gates.

## Use

Use this skill when:

- A task card authorizes one Blender MCP microtask.
- A source `.blend` needs a protected working copy before editing.
- The user asks for MCP-controlled Blender edits.
- An action log needs to be created or reviewed.
- A Blender MCP change needs approval, rejection, or rollback evidence.

## Inputs

- `docs/mcp/blender_mcp_usage_policy.md`
- `templates/mcp_action_log.md`
- `templates/stage_task_card.md`
- `templates/review_report.md`
- `templates/qa_audit_report.md`
- `blender_scripts/screenshot_set.py`
- `blender_scripts/scene_report.py`
- `blender_scripts/mesh_report.py`
- `blender_scripts/naming_report.py`

## Required Output

Produce or update a `templates/mcp_action_log.md`-compatible log with:

- One microtask goal.
- Source, backup, and working file paths.
- Allowed and disallowed tools.
- Every MCP command or tool action.
- Screenshot and validator evidence.
- Specialist review and QA audit links.
- Final decision: `approved`, `rejected`, `rolled_back`, or `blocked`.

## Operating Rules

- Execute one microtask per loop.
- Copy source before modification.
- Stop before destructive operations unless explicit approval is recorded.
- Capture screenshots after structural change.
- Run required validators before requesting approval.
- If acceptance tests fail, mark the action log `rejected` or `rolled_back`.
- If scope expands, mark the action log `blocked` and return to the Character Director.

## First Workflow

For `stylized_orc_bruiser`, use `references/bounded_loop_rules.md` and the example logs under `examples/stylized_orc_bruiser/mcp_logs/`.
