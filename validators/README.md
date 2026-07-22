# Validators

Validators produce `templates/validation_report.md`-shaped Markdown output on stdout.

Validators are intentionally local and dependency-free where possible. They check documents, manifests, MCP logs, and production-readiness reports before a stage can advance.

## Current Validators

- `validate_stage_handoff.py`: required handoff fields, valid stage IDs, source/target stage consistency, hard-failure gate state, human-review warning.
- `validate_stage_task_card.py`: required task-card fields, canonical stage consistency, and bounded Blender MCP scope/authorization.
- `validate_mcp_session.py`: active-session JSONL sequencing, hash chain, exact targets, safe operations, timings, previews, and checkpoint bundles.
- `validate_review_report.py`: required review fields, valid review type, valid decision, findings table shape, hard-failure decision consistency.
- `validate_qa_audit.py`: required audit fields, valid stage IDs, hard-failure decision consistency, weighted score math, total score, score band.
- `validate_manifest.py`: required manifest fields, Godot/GLB target sanity, latest stage validity, hard-failure gate state, referenced path existence.
- `validate_mcp_action_log.py`: required MCP log fields, bounded microtask wording, backup checks, screenshot/review evidence, destructive approval, hard-failure decision consistency.
- `validate_mcp_iteration_receipt.py`: quick-iteration target budget, safe change types, scene drift, topology/material protection, hashes, and two-view evidence.
- `validate_blender_report.py`: Blender JSON report schema, source-read-only metadata, summary consistency, and expected asset/stage/source matching.
- `validate_screenshot_manifest.py`: required views, real PNG files, dimensions, source working file, and captured-status consistency.
- `validate_uv_bake_readiness.py`: UV presence, overlap policy, disallowed overlaps, texel density, padding, bake pairing, required maps, and bake artifacts.
- `validate_texture_readiness.py`: material slot budget, material naming, texture set presence, texture naming and size, channel packing, missing textures, and Godot texture paths.
- `validate_lod_readiness.py`: LOD count, LOD naming, LOD polycount budget, material and texture memory status, package completeness, and GLB/glTF presence.
- `validate_godot_validation.py`: Godot import, scene open, texture paths, Skeleton3D, animations, blend shapes, markers, collision, and preview render state.
- `validate_workflow_completion.py`: full workflow stage coverage, final evidence, hard-failure state, and completion decision.

Exit codes:

- `0`: pass or warning
- `1`: validation failure
- `2`: validator runtime or CLI error

## Passing Example

```bash
python3 validators/validate_stage_handoff.py examples/stylized_orc_bruiser/handoffs/anatomy_to_manual_blockout.md
python3 validators/validate_stage_task_card.py examples/stylized_orc_bruiser/task_cards/concept_interpretation.md
python3 validators/validate_review_report.py examples/stylized_orc_bruiser/reviews/anatomy_review.md
python3 validators/validate_qa_audit.py examples/stylized_orc_bruiser/audit.md
python3 validators/validate_manifest.py examples/stylized_orc_bruiser/asset_manifest.md
python3 validators/validate_mcp_action_log.py examples/stylized_orc_bruiser/mcp_logs/accepted_microtask_001.md
python3 validators/validate_mcp_iteration_receipt.py path/to/iteration_receipt.json
python3 validators/validate_uv_bake_readiness.py validators/examples/passing/good_uv_bake_readiness.md
python3 validators/validate_texture_readiness.py validators/examples/passing/good_material_texture_readiness.md
python3 validators/validate_lod_readiness.py validators/examples/passing/good_optimization_readiness.md
python3 validators/validate_godot_validation.py validators/examples/passing/good_godot_validation_report.md
python3 validators/validate_workflow_completion.py examples/stylized_orc_bruiser/workflow/completion_report.md
```

## Failing Examples

These fixtures intentionally fail and should return exit code `1`:

```bash
python3 validators/validate_stage_handoff.py validators/examples/failing/bad_handoff.md
python3 validators/validate_review_report.py validators/examples/failing/bad_review_report.md
python3 validators/validate_qa_audit.py validators/examples/failing/bad_qa_audit.md
python3 validators/validate_manifest.py validators/examples/failing/bad_manifest.md
python3 validators/validate_mcp_action_log.py validators/examples/failing/bad_mcp_action_log.md
python3 validators/validate_uv_bake_readiness.py examples/stylized_orc_bruiser/reports/readiness/uv_bake_readiness.md
python3 validators/validate_texture_readiness.py examples/stylized_orc_bruiser/reports/readiness/material_texture_readiness.md
python3 validators/validate_lod_readiness.py examples/stylized_orc_bruiser/reports/readiness/optimization_readiness.md
python3 validators/validate_godot_validation.py examples/stylized_orc_bruiser/reports/godot_validation_report.md
```

## Notes

- The validators are strict about stage IDs. Phase 5 planning aliases are currently allowed: `style_lock`, `anatomy_blockout_planning`, and `manual_blockout`.
- The QA audit validator checks score math even when the score is low because early-stage audits may approve progression for workflow readiness while asset-quality categories remain deferred.
- Blender JSON reports and screenshot manifests are validated directly before a real MCP action log can pass.
