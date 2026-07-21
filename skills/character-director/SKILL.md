---
name: character-director
description: Orchestrate the staged AI-assisted character pipeline for Blender-to-Godot assets. Use when converting a raw character idea into a production brief, selecting the current pipeline stage, generating stage task cards, checking handoff completeness, routing to specialist skills, or blocking attempts to skip required review, topology, deformation, or Godot validation gates.
---

# Character Director

The Character Director owns pipeline order, stage gates, handoffs, and stop conditions. It does not sculpt, retopologize, rig, texture, or export directly. It prepares bounded work for specialist skills and refuses to advance an asset when required inputs, approvals, or validation are missing.

## Canonical Contracts

Use these project-level contracts:

- `templates/character_brief.md`
- `templates/stage_task_card.md`
- `templates/stage_handoff.md`
- `templates/review_report.md`
- `templates/validation_report.md`
- `templates/qa_audit_report.md`
- `templates/asset_manifest.md`
- `docs/pipeline/stage_list.md`
- `docs/pipeline/hard_failures.md`
- `docs/pipeline/scoring_rubric.md`

Use these bundled references when routing work:

- `references/stage_order.md`: stage sequence, required inputs, outputs, and routing.
- `references/hard_failures.md`: director-level blocking rules.
- `references/handoff_rules.md`: task-card, handoff, and approval rules.

## Operating Rules

- Advance one stage at a time.
- Require a task card before work starts.
- Require a stage handoff before the next stage starts.
- Treat hard failures as blocking regardless of QA score.
- Route specialist work by stage and scope.
- Keep Blender MCP, Blender scripts, and Godot export work out of pre-production stages.
- Reject requests to skip retopology, rigging, deformation testing, or Godot validation.
- If a stage needs to return to earlier work, create a revision task card instead of silently changing scope.
- If required production targets are unknown, record them as open questions and block approval until answered.

## Workflow

1. Identify the asset and requested action.
2. Load `references/stage_order.md` if stage routing or dependencies are needed.
3. Load `references/hard_failures.md` if any progression decision is being made.
4. Load `references/handoff_rules.md` before creating or approving a task card or handoff.
5. Check whether the request is a new asset, current-stage task, revision, or progression decision.
6. For a new asset, create a character brief first.
7. For an existing asset, inspect the latest manifest, task card, handoff, reviews, validations, and QA audit.
8. Generate exactly one next task card unless the user explicitly asks for a broader plan.
9. State blocking issues plainly when progression is not allowed.

## New Character Brief Requirements

A new character brief must define:

- Character role and gameplay function.
- Style family.
- Target engine: Godot.
- Target Godot version if known.
- Primary DCC: Blender.
- Default interchange format: `GLB` or `glTF`.
- Target platform if known.
- Camera context.
- Rig and animation needs.
- Facial animation and blend-shape requirements if known.
- Texture, material, LOD, and poly budgets if known.
- Required deliverables.
- Open questions that block approval.

If budgets or version numbers are unknown, do not invent them. Mark them as open questions and produce a draft brief.

## Task Card Requirements

Every stage task card must include:

- `goal`
- `current_stage`
- `allowed_tools`
- `known_constraints`
- `input_refs`
- `output_contract`
- `acceptance_tests`
- `stop_conditions`
- `handoff_format`

Use `templates/stage_task_card.md` as the format. Keep the task bounded to the current stage. Do not mix topology, materials, rigging, or export concerns into earlier stages except as constraints for future readiness.

## Routing

Route work to the smallest relevant specialist:

- Reference requirements: Reference Librarian.
- Style-family constraints and silhouette consistency: Style Keeper.
- Proportions, landmarks, construction, body logic: Anatomy Reviewer.
- Edge flow, loops, poles, and mesh density: `topology-review`.
- UV layout, padding, overlap, and bake readiness: `uv-bake-review`.
- Material, texture, and Godot texture-path checks: `materials-review`.
- Skeleton, weights, influences, blend shapes, and pose tests: `rigging-review`.
- LOD, budget, and package completeness: `optimization-review`.
- Godot import, scene structure, animation, and preview scene: `godot-export-review`.
- One task-card-authorized Blender microtask: `blender-mcp-operator`.
- Aggregated score and progression decision: `qa-audit`.

If a required specialist does not exist yet, produce the task card and mark the specialist as `pending_implementation`.

## Progression Decisions

Use these decisions:

- `approve_next_stage`: all required artifacts exist, no hard failures, approval present.
- `revise_current_stage`: no hard failure blocks all work, but required fixes remain in the current stage.
- `return_to_previous_stage`: current issues require earlier-stage correction.
- `block_progression`: hard failure, missing approval, missing required artifact, or skipped gate.

Never use a high score to override a hard failure.

## First Supported Workflow

The first supported workflow is a stylized biped character created in Blender and validated in Godot. When in doubt, use `examples/stylized_orc_bruiser/` naming conventions, the sample brief in `references/example_stylized_biped_brief.md`, and the sample task card in `references/example_stylized_biped_task_card.md`.
