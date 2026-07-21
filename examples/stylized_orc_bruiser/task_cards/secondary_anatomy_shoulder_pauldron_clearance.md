# Secondary Anatomy Shoulder-Pauldron Clearance Task Card

## Metadata

- `task_id`: stylized_orc_bruiser-secondary-anatomy-shoulder-pauldron-clearance-001
- `asset_id`: stylized_orc_bruiser
- `stage_id`: secondary_anatomy
- `stage_name`: Secondary anatomy consolidation
- `created_by`: Character Director
- `created_at`: 2026-07-21
- `status`: approved

## Goal

- `goal`: Improve the left shoulder-pauldron clearance and silhouette with a small reversible transform of the existing pauldron while preserving the user's manual shaping and all anatomical masses.
- `current_stage`: secondary_anatomy
- `previous_stage`: secondary_anatomy
- `next_stage`: secondary_anatomy

## Constraints

- `allowed_tools`: protected working-copy script; read-only Blender MCP inspection; one scoped Blender MCP transform burst; quick front and three-quarter screenshots; scene-delta and MCP-log validators
- `disallowed_tools`: deletion; addition; rename; merge; remesh; topology edits; transform application; material changes; changes outside ORC_shoulder_pad_L; changes to shoulder, clavicle, ribcage, arm, bracer, or retired construction; rigging; export
- `known_constraints`: ORC_shoulder_pad_L is the only pauldron object and currently overlaps the left shoulder mass; the user manually adjusted its placement earlier
- `style_constraints`: retain the asymmetrical heavy bruiser silhouette and the user's chosen pauldron scale and shape
- `technical_constraints`: preserve mesh counts, vertex positions, scale, materials, and collection membership; transform only the named object
- `godot_constraints`: no export or engine-facing change in this task

## Inputs

- `input_refs`: current protected shin-calf working scene; prior anatomy reviews; user visual feedback
- `input_artifacts`: `examples/stylized_orc_bruiser/source/secondary_anatomy/consolidation/working/stylized_orc_bruiser.secondary-anatomy-shin-calf-consolidation-001.working.blend`
- `input_reports`: approved shin-calf consolidation evidence and read-only shoulder object preflight
- `previous_handoff`: `examples/stylized_orc_bruiser/handoffs/primary_forms_to_secondary_anatomy.md`
- `assumptions`: a modest outward and upward pauldron translation can improve clearance without weakening the intended overlap

## Output Contract

- `required_outputs`: protected backup and working `.blend`; quick-iteration scene-delta receipt; front and three-quarter screenshots; compact MCP action log
- `output_paths`: `examples/stylized_orc_bruiser/source/secondary_anatomy/shoulder_pauldron/working/stylized_orc_bruiser.secondary-anatomy-shoulder-pauldron-clearance-001.working.blend`
- `report_paths`: `examples/stylized_orc_bruiser/reports/blender/secondary_anatomy_shoulder_pauldron_clearance/quick_iteration_001/`
- `screenshot_requirements`: front; three_quarter targeting ORC_BLOCKOUT at 512 pixels or greater
- `handoff_format`: `templates/stage_handoff.md`

## Acceptance Tests

- `acceptance_tests`: only ORC_shoulder_pad_L changes; pauldron scale, mesh topology, materials, and collection membership remain unchanged; shoulder armor remains seated on the shoulder with visibly improved separation; anatomy and all other objects remain unchanged; source and backup hashes validate
- `required_validators`: validate_stage_task_card; validate_mcp_iteration_receipt; validate_mcp_action_log
- `manual_review_required`: no
- `hard_failure_checks`: missing or added object; unexpected object drift; topology or material change; pauldron floating or losing shoulder coverage; source or protection failure

## Stop Conditions

- `stop_conditions`: stop on protection mismatch, unrelated change, topology drift, material drift, unclear visual result, excessive clearance, screenshot failure, or validator failure
- `requires_human_approval`: yes
- `rollback_required_if`: any object except ORC_shoulder_pad_L changes or the pauldron no longer reads as seated armor
- `do_not_continue_if`: task, capability, isolation, protection, filepath, or scene-delta preflight fails

## Execution Notes

- `assigned_specialist`: Anatomy Reviewer with Blender MCP Operator
- `microtasks`: Translate only ORC_shoulder_pad_L slightly outward and upward without changing scale, mesh data, materials, or collection membership
- `mcp_microtask_id`: secondary-anatomy-shoulder-pauldron-clearance-001
- `evidence_tier`: quick_iteration
- `iteration_budget`: 3
- `iteration_views`: front; three_quarter
- `target_objects`: ORC_shoulder_pad_L
- `allowed_change_types`: transform
- `execution_authorized_by`: repository user
- `execution_authorized_at`: 2026-07-21
- `risks`: too much separation could make the pauldron float; too little would not improve clearance
- `questions_for_director`: none

## Completion

- `completed_outputs`: protected backup and working `.blend`; quick iteration 1 front and three-quarter screenshots; passing scene-delta receipt; compact MCP action log
- `validation_summary`: quick iteration 1 changed only ORC_shoulder_pad_L by a 4 cm outward and 2.5 cm upward translation; 74 non-target objects, topology, materials, scale, rotation, and source protection remain unchanged
- `review_summary`: Full gate review approves the seated clearance with a non-blocking note to revisit final armor contour during clothing and hardsurface work.
- `blocking_issues`: none inside this bounded shoulder-pauldron task
- `approved_by`: repository user
- `approved_at`: 2026-07-21
