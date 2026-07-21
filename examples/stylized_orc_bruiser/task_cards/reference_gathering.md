# Reference Gathering Task Card

## Metadata

- `task_id`: stylized_orc_bruiser-reference_gathering-001
- `asset_id`: stylized_orc_bruiser
- `stage_id`: reference_gathering
- `stage_name`: Reference gathering
- `created_by`: Character Director
- `created_at`: 2026-07-21
- `status`: approved

## Goal

- `goal`: Gather and approve references that cover style, anatomy, silhouette, materials, head/tusks, and production benchmarks before blockout planning.
- `current_stage`: reference_gathering
- `previous_stage`: concept_interpretation
- `next_stage`: style_lock

## Constraints

- `allowed_tools`: online search, local templates, reference board template, reference record template
- `disallowed_tools`: direct copying of character designs, downloading marketplace assets without license, Blender MCP, mesh generation, Godot import
- `known_constraints`: references must support an original heroic stylized orc bruiser for Godot
- `style_constraints`: large readable forms, simple heroic masses, low-to-medium detail frequency before blockout approval
- `technical_constraints`: references may inform budgets, but cannot define final budgets without project constraints
- `godot_constraints`: prefer examples and technical benchmarks compatible with GLB/glTF game-character thinking

## Inputs

- `input_refs`: online candidate sources
- `input_artifacts`: `examples/stylized_orc_bruiser/brief.md`
- `input_reports`: none
- `previous_handoff`: `examples/stylized_orc_bruiser/handoffs/concept_to_reference.md`
- `assumptions`: approved references are inspiration, not source art to reproduce

## Output Contract

- `required_outputs`: approved reference board and individual reference records
- `output_paths`: `examples/stylized_orc_bruiser/reference_boards/approved_initial_board.md`; `examples/stylized_orc_bruiser/references/`
- `report_paths`: `examples/stylized_orc_bruiser/reviews/reference_librarian.md`
- `screenshot_requirements`: none
- `handoff_format`: `examples/stylized_orc_bruiser/handoffs/reference_to_style.md`

## Acceptance Tests

- `acceptance_tests`: board includes style/full-body, anatomy, face/tusk, material, production, and readability coverage; each approved source has usage guidance and avoidance notes
- `required_validators`: none in Phase 5
- `manual_review_required`: yes
- `hard_failure_checks`: no approved references; missing source URLs; missing usage restrictions; all references from one category only

## Stop Conditions

- `stop_conditions`: stop for approval before treating candidate references as approved production inputs
- `requires_human_approval`: yes
- `rollback_required_if`: reference source is later rejected or licensing makes it unusable
- `do_not_continue_if`: no approved references exist

## Execution Notes

- `assigned_specialist`: Reference Librarian
- `microtasks`: search online; create candidate board; request approval; convert approved items to reference records; summarize coverage gaps
- `risks`: hand, hip, knee, topology, and Godot import references are still light and may need expansion later
- `questions_for_director`: none

## Completion

- `completed_outputs`: approved board plus 11 reference records
- `validation_summary`: no validators required
- `review_summary`: reference coverage approved with notes
- `blocking_issues`: none for style lock or anatomy planning
- `approved_by`: Lucas
- `approved_at`: 2026-07-21
