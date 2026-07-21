# Pipeline Contracts

This folder contains the canonical Phase 1 contracts that govern stage order, blocking failures, and QA scoring.

## Files

- `stage_list.md`: canonical stage order for the first Blender-to-Godot stylized biped workflow.
- `hard_failures.md`: blocking conditions that override weighted score.
- `scoring_rubric.md`: weighted QA categories, score bands, and calculation rules.

## Contract Rules

- Stage IDs in reports and task cards must match `stage_list.md`.
- Hard failures in `hard_failures.md` block progression regardless of score.
- QA score bands in `scoring_rubric.md` are advisory unless no hard failures are present.
- Godot validation is required before an asset is considered complete.
