# Claude Guidance

This repository uses the same production rules for Claude and Codex.

## Core Behavior

- Act as a cautious production assistant, not a one-shot generator.
- Follow `AGENTS.md` as durable project law.
- Use `skills/character-director/` for stage routing and progression decisions.
- Use the templates in `templates/` for all briefs, task cards, handoffs, reviews, validations, QA audits, and manifests.
- Use `docs/pipeline/` as the canonical stage, hard-failure, and scoring reference.

## Stage Gates

- Create a task card before stage work.
- Stop at explicit approval gates.
- Do not proceed when hard failures are present.
- Do not skip retopology, rigging, deformation testing, optimization, or Godot validation.

## Tool Safety

- Treat Blender MCP as unsafe infrastructure unless isolated.
- Prefer read-only reports before edit automation.
- Use deterministic validators where possible.
- Keep Godot validation as the final proof that the asset works outside Blender.
