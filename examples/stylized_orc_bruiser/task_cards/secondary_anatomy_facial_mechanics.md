# Secondary Anatomy Facial Mechanics Task Card

## Metadata

- `task_id`: stylized_orc_bruiser-secondary-anatomy-facial-mechanics-001
- `asset_id`: stylized_orc_bruiser
- `stage_id`: secondary_anatomy
- `stage_name`: Secondary anatomy consolidation
- `created_by`: Character Director
- `created_at`: 2026-07-21
- `status`: approved

## Goal

- `goal`: Clarify the stylized mouth, cheek, and tusk relationships so the face reads as an expressive orc rather than one merged muzzle band.
- `current_stage`: secondary_anatomy
- `previous_stage`: secondary_anatomy
- `next_stage`: secondary_anatomy

## Constraints

- `allowed_tools`: protected working-copy script; read-only Blender MCP inspection; one scoped transform burst; quick front and three-quarter screenshots; scene-delta and MCP-log validators
- `disallowed_tools`: deletion; addition; rename; merge; remesh; vertex edits; topology changes; transform application; material changes; changes outside the five named targets; changes to jaw, cranium, eyes, brows, nose, ears, body, gear, or retired construction; rigging; export
- `known_constraints`: eyes and brows already read after the approved facial revision; tusks are visible but partially merge into the cheeks and mouth mass; the skin-colored mouth mass has weak separation from the surrounding face
- `style_constraints`: preserve the compact heavy jaw, blunt muzzle, visible paired tusks, and stern stylized expression
- `technical_constraints`: preserve mesh counts, mesh coordinates, materials, rotations, and collection membership; use only small location and mouth-mass scale adjustments
- `godot_constraints`: no export or engine-facing change in this task

## Inputs

- `input_refs`: approved facial readability revision; current close face inspection; stylized biped head and face construction rules
- `input_artifacts`: `examples/stylized_orc_bruiser/source/secondary_anatomy/shoulder_pauldron/working/stylized_orc_bruiser.secondary-anatomy-shoulder-pauldron-clearance-001.working.blend`
- `input_reports`: approved shoulder-pauldron gate and current read-only facial inventory
- `previous_handoff`: `examples/stylized_orc_bruiser/handoffs/primary_forms_to_secondary_anatomy.md`
- `assumptions`: modest separation and vertical compression can improve mouth mechanics without introducing new geometry or overriding the established expression

## Output Contract

- `required_outputs`: protected backup and working `.blend`; quick iteration scene-delta receipt; front and three-quarter screenshots; compact MCP action log
- `output_paths`: `examples/stylized_orc_bruiser/source/secondary_anatomy/facial_mechanics/working/stylized_orc_bruiser.secondary-anatomy-facial-mechanics-001.working.blend`
- `report_paths`: `examples/stylized_orc_bruiser/reports/blender/secondary_anatomy_facial_mechanics/quick_iteration_001/`
- `screenshot_requirements`: front; three_quarter targeting the facial composition at 512 pixels or greater
- `handoff_format`: `templates/stage_handoff.md`

## Acceptance Tests

- `acceptance_tests`: only ORC_mouth_mass, ORC_cheek_L/R, and ORC_tusk_L/R change; mouth band gains visible separation; tusks remain paired, visible, and seated; cheek symmetry remains controlled; jaw, head, eyes, brows, nose, ears, all other objects, topology, materials, rotations, and collections remain unchanged; source and backup hashes validate
- `required_validators`: validate_stage_task_card; validate_mcp_iteration_receipt; validate_mcp_action_log
- `manual_review_required`: no
- `hard_failure_checks`: unexpected object drift; topology or material change; floating tusk; broken symmetry; lost stern expression; source or evidence failure

## Stop Conditions

- `stop_conditions`: stop on protection mismatch, unrelated change, topology or material drift, tusk detachment, excessive cheek gap, expression loss, screenshot failure, or validator failure
- `requires_human_approval`: yes
- `rollback_required_if`: any non-target changes or the face reads less clearly than the protected source
- `do_not_continue_if`: task, capability, isolation, protection, filepath, or scene-delta preflight fails

## Execution Notes

- `assigned_specialist`: Anatomy Reviewer with Blender MCP Operator
- `microtasks`: Improve mouth-cheek-tusk separation using transform-only adjustments on five named targets
- `mcp_microtask_id`: secondary-anatomy-facial-mechanics-001
- `evidence_tier`: quick_iteration
- `iteration_budget`: 3
- `iteration_views`: front; three_quarter
- `target_objects`: ORC_mouth_mass; ORC_cheek_L; ORC_cheek_R; ORC_tusk_L; ORC_tusk_R
- `allowed_change_types`: transform
- `execution_authorized_by`: repository user
- `execution_authorized_at`: 2026-07-21
- `risks`: over-separation could create floating facial pieces or a cartoon moustache read
- `questions_for_director`: none

## Completion

- `completed_outputs`: protected backup and working `.blend`; quick iteration 1 facial front and three-quarter screenshots; passing scene-delta receipt; compact MCP action log
- `validation_summary`: quick iteration 1 changed only the five authorized mouth, cheek, and tusk objects; 70 non-target objects, topology, materials, rotations, collections, source, and backup remain unchanged
- `review_summary`: Full gate review approves the clearer mouth, cheek, and tusk relationships; deformable mouth construction remains downstream work.
- `blocking_issues`: none inside this bounded facial task
- `approved_by`: repository user
- `approved_at`: 2026-07-21
