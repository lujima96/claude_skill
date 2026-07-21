# Validator Examples

## Passing Inputs

Use the Phase 5 vertical slice as the primary passing input set:

```bash
python3 validators/validate_stage_handoff.py examples/stylized_orc_bruiser/handoffs/anatomy_to_manual_blockout.md
python3 validators/validate_review_report.py examples/stylized_orc_bruiser/reviews/anatomy_review.md
python3 validators/validate_qa_audit.py examples/stylized_orc_bruiser/audit.md
python3 validators/validate_manifest.py examples/stylized_orc_bruiser/asset_manifest.md
python3 validators/validate_mcp_action_log.py examples/stylized_orc_bruiser/mcp_logs/accepted_microtask_001.md
python3 validators/validate_uv_bake_readiness.py validators/examples/passing/good_uv_bake_readiness.md
python3 validators/validate_texture_readiness.py validators/examples/passing/good_material_texture_readiness.md
python3 validators/validate_lod_readiness.py validators/examples/passing/good_optimization_readiness.md
python3 validators/validate_godot_validation.py validators/examples/passing/good_godot_validation_report.md
python3 validators/validate_workflow_completion.py examples/stylized_orc_bruiser/workflow/completion_report.md
```

## Failing Inputs

These files intentionally fail and should return exit code `1`:

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
