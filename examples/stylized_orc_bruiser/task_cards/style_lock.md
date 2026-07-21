# Style Lock Task Card

## Metadata

- `task_id`: stylized_orc_bruiser-style_lock-001
- `asset_id`: stylized_orc_bruiser
- `stage_id`: style_lock
- `stage_name`: Style lock
- `created_by`: Character Director
- `created_at`: 2026-07-21
- `status`: approved

## Goal

- `goal`: Convert the approved brief and reference board into explicit style constraints for blockout planning.
- `current_stage`: style_lock
- `previous_stage`: reference_gathering
- `next_stage`: anatomy_blockout_planning

## Constraints

- `allowed_tools`: approved reference board, reference records, style knowledge notes, review report template
- `disallowed_tools`: creating final sculpt details, copying reference designs, topology or rigging decisions
- `known_constraints`: heroic stylized orc bruiser for third-person Godot gameplay
- `style_constraints`: broad shoulder-to-waist taper, thick neck, heavy jaw, tusks, large hands, chunky readable gear
- `technical_constraints`: tertiary detail must not be planned before primary/secondary forms read clearly
- `godot_constraints`: silhouette and materials must remain readable under Godot lighting

## Inputs

- `input_refs`: `examples/stylized_orc_bruiser/reference_boards/approved_initial_board.md`
- `input_artifacts`: `examples/stylized_orc_bruiser/brief.md`
- `input_reports`: `examples/stylized_orc_bruiser/reviews/reference_librarian.md`
- `previous_handoff`: `examples/stylized_orc_bruiser/handoffs/reference_to_style.md`
- `assumptions`: blockout will prioritize form language over costume detail

## Output Contract

- `required_outputs`: style review with approved style dials and constraints
- `output_paths`: `examples/stylized_orc_bruiser/reviews/style_keeper.md`
- `report_paths`: `examples/stylized_orc_bruiser/reviews/style_keeper.md`
- `screenshot_requirements`: none
- `handoff_format`: `examples/stylized_orc_bruiser/handoffs/style_to_anatomy.md`

## Acceptance Tests

- `acceptance_tests`: style report defines shape language, silhouette priorities, detail frequency, material readability, and copy-avoidance rules
- `required_validators`: none in Phase 5
- `manual_review_required`: yes
- `hard_failure_checks`: vague style family; no silhouette rule; no copy-avoidance rule

## Stop Conditions

- `stop_conditions`: stop if style rules cannot be traced to brief and approved board
- `requires_human_approval`: yes
- `rollback_required_if`: approved references change style family
- `do_not_continue_if`: style lock contradicts the brief or approved reference board

## Execution Notes

- `assigned_specialist`: Style Keeper
- `microtasks`: map references to style dials; define blockout-readable form rules; flag risks for next stage
- `risks`: gear complexity may overwhelm silhouette if added too early
- `questions_for_director`: none

## Completion

- `completed_outputs`: `examples/stylized_orc_bruiser/reviews/style_keeper.md`
- `validation_summary`: no validators required
- `review_summary`: style lock approved with notes
- `blocking_issues`: none for anatomy blockout planning
- `approved_by`: Lucas
- `approved_at`: 2026-07-21
