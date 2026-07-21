# AI Assisted Character Pipeline Framework

This repository defines a staged AI-assisted production framework for creating Blender character assets and validating them for Godot.

## Non-Negotiable Rules

- Advance one validated stage at a time.
- Do not treat the system as a one-shot character generator.
- Every stage must have a task card before work starts.
- Every completed stage must produce a handoff before the next stage begins.
- Hard failures block progression regardless of QA score.
- Human approval is required at stage gates.
- Do not skip retopology, rigging, deformation testing, optimization, or Godot validation.
- Do not use Blender MCP for broad unsupervised edits.
- Prefer deterministic scripts and validators for trusted checks.
- Treat MCP servers as adapter layers, not as the source of truth.
- Godot is the first supported engine target.
- Blender is the first supported DCC.
- `GLB` or `glTF` is the default Blender-to-Godot interchange path unless the project records an exception.

## Canonical Contracts

- `docs/pipeline/stage_list.md`
- `docs/pipeline/hard_failures.md`
- `docs/pipeline/scoring_rubric.md`
- `templates/character_brief.md`
- `templates/reference_record.md`
- `templates/stage_task_card.md`
- `templates/stage_handoff.md`
- `templates/review_report.md`
- `templates/validation_report.md`
- `templates/qa_audit_report.md`
- `templates/asset_manifest.md`

## First Supported Workflow

The first workflow is `workflows/stylized-biped-godot/`: a stylized biped character authored in Blender and validated in Godot.

The first example asset is `examples/stylized_orc_bruiser/`.

## Skill Responsibilities

- `skills/character-director/`: stage order, task cards, handoffs, routing, and blocking decisions.
- Future specialist skills should stay inside their domains and report back through the standard templates.

## Safety Rules

- Do not run destructive Blender, filesystem, or project-modification commands without explicit approval.
- Keep source assets separate from generated or exported assets.
- Preserve source files before MCP-controlled edits.
- Capture screenshots and validation reports after meaningful asset changes.
- If a tool can execute arbitrary Python in Blender, treat it as unsafe and run it only in isolated project contexts.

## Godot Readiness

An asset is not done until Godot validation passes. Validation must prove that the imported asset opens and previews correctly in Godot, including expected scene structure, `Skeleton3D`, skin weights, material bindings, texture references, animation clips, blend shapes where required, collision or marker nodes where required, and preview-scene rendering.
