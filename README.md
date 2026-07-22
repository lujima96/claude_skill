# AI Assisted Character Pipeline Framework

This project is a staged production framework for AI-assisted character creation. The target path is Blender source assets exported through `GLB` or `glTF` and validated in Godot.

The framework is intentionally not a one-shot character generator. It is built around a Character Director, specialist skills, structured artifact templates, validators, Blender automation, and Godot validation gates.

## Current Status

- Phase 0: repository foundation backfilled.
- Phase 1: pipeline contracts implemented.
- Phase 2: Character Director skill implemented.
- Phase 3: knowledge base skeleton implemented.
- Phase 4: first specialist skills implemented.
- Phase 5: manual vertical slice implemented for `examples/stylized_orc_bruiser/`.
- Phase 6: core document validators implemented.
- Phase 7: read-only Blender script pack implemented.
- Phase 8: topology and rigging review specialists implemented.
- Phase 9: bounded Blender MCP loop policy, hash-verified working copies, capability preflight, action logs, and evidence validators implemented.
- Phase 10: materials, UV/bake, optimization skills and readiness validators implemented.
- Phase 11: Godot adapter contracts, import probe, review skill, and validator implemented.
- Phase 12: full stylized biped workflow completion gate implemented; the example has real Blender artifacts through tertiary detail and remains blocked on downstream mesh, rig, texture, export, and Godot evidence.
- Phase 14: persistent Blender MCP edit sessions, declarative safe edits, hash-chained JSONL evidence, and bundled checkpoints implemented.
- Phase 13: second workflow profile added for low-poly mobile character.

## First Supported Workflow

`workflows/stylized-biped-godot/`

The first workflow is a stylized biped character authored in Blender and validated in Godot. The acceptance example is expected to be `examples/stylized_orc_bruiser/`.

## Key Files

- `AGENTS.md`: durable project rules.
- `CLAUDE.md`: equivalent durable guidance for Claude use.
- `docs/plan.md`: research-backed blueprint.
- `docs/implementation_order.md`: build sequence.
- `docs/pipeline/`: stage list, hard failures, and QA scoring.
- `docs/mcp/`: bounded Blender MCP operating policy and action-log rules.
- `templates/`: artifact contracts.
- `templates/pipeline_state.json`: concise current-stage and active-session pointer.
- `skills/character-director/`: orchestration skill.
- `skills/reference-librarian/`: reference coverage and metadata review.
- `skills/style-keeper/`: style-family and readability review.
- `skills/anatomy-review/`: proportion, construction, landmark, and pose-risk review.
- `skills/topology-review/`: deformation-ready mesh topology review.
- `skills/rigging-review/`: skeleton, skinning, pose-battery, and deformation review.
- `skills/uv-bake-review/`: UV layout, overlap, padding, and bake-readiness review.
- `skills/materials-review/`: material, texture, channel packing, and Godot texture path review.
- `skills/optimization-review/`: LOD, budget, package completeness, and performance review.
- `skills/godot-export-review/`: Godot import, preview scene, package, skeleton, animation, and material validation review.
- `skills/blender-mcp-operator/`: bounded Blender MCP edit-loop operation.
- `skills/qa-audit/`: aggregate QA and progression decision support.
- `validators/`: local document validators for handoffs, reviews, QA audits, and manifests.
- `blender_scripts/`: read-only Blender report scripts and guarded export readiness tooling.
- `engine/godot/`: Godot adapter contracts and import probe.
- `workflows/low-poly-mobile-character/`: second workflow profile.

## Build Order

Follow `docs/implementation_order.md`.

The short version:

1. Define contracts.
2. Create director workflow.
3. Build knowledge base.
4. Add specialist skills.
5. Prove one manual vertical slice.
6. Add validators.
7. Add read-only Blender reports.
8. Add topology and rigging specialists.
9. Add bounded Blender MCP edits.
10. Add materials, UV, baking, and optimization specialists.
11. Add Godot validation.
12. Add full workflow completion gates.
13. Add second workflow profile.

## Definition of Done

An asset is complete only when every stage has an artifact, every handoff is explicit, hard failures are absent, and the final package imports and previews correctly in Godot.
