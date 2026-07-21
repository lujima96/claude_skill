# Concept To Reference Handoff

## Metadata

- `handoff_id`: stylized_orc_bruiser-concept_to_reference-001
- `asset_id`: stylized_orc_bruiser
- `from_stage`: concept_interpretation
- `to_stage`: reference_gathering
- `created_by`: Character Director
- `created_at`: 2026-07-21
- `status`: approved

## Stage Result

- `stage_goal`: turn the raw character idea into a brief suitable for reference gathering
- `completed_work`: defined character role, style family, Godot target, Blender source path, scope, open questions, and first-stage acceptance criteria
- `changed_artifacts`: none
- `new_artifacts`: `examples/stylized_orc_bruiser/brief.md`; `examples/stylized_orc_bruiser/task_cards/concept_interpretation.md`
- `removed_or_superseded_artifacts`: none

## Required Artifacts

- `source_files`: `examples/stylized_orc_bruiser/brief.md`
- `export_files`: none
- `screenshots`: none
- `reports`: none
- `references_used`: none

## Validation

- `validators_run`: none
- `validation_reports`: none
- `hard_failures_present`: no
- `hard_failure_summary`: none
- `warning_summary`: target Godot version, platform, budgets, skeleton, animation list, facial animation, and markers are unknown

## Review

- `specialist_reviews`: none
- `qa_audit`: none
- `human_review_required`: yes
- `approval_decision`: approved
- `approval_notes`: proceed to reference gathering; keep technical unknowns visible

## Known Issues

- `accepted_limitations`: concept stage can approve reference gathering without final production budgets
- `deferred_work`: technical budgets, animation requirements, skeleton spec, facial requirements, marker requirements
- `risks_for_next_stage`: references may skew too cinematic or too detailed for a Godot gameplay asset
- `must_not_change_next_stage`: Godot target, third-person camera context, heroic stylized style family

## Next Stage Instructions

- `next_stage_inputs`: brief, raw prompt, style family, open questions
- `next_stage_focus`: gather approved references for style, silhouette, anatomy, face/tusks, materials, and production benchmark
- `next_stage_stop_conditions`: stop if references are only candidates and have not been approved
- `next_stage_owner`: Reference Librarian

## Signoff

- `prepared_by`: Character Director
- `approved_by`: Lucas
- `approved_at`: 2026-07-21
