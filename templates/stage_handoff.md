# Stage Handoff

## Metadata

- `handoff_id`:
- `asset_id`:
- `from_stage`:
- `to_stage`:
- `created_by`:
- `created_at`:
- `status`: draft | ready_for_review | approved | blocked

## Stage Result

- `stage_goal`:
- `completed_work`:
- `changed_artifacts`:
- `new_artifacts`:
- `removed_or_superseded_artifacts`:

## Required Artifacts

- `source_files`:
- `export_files`:
- `screenshots`:
- `reports`:
- `references_used`:

## Validation

- `validators_run`:
- `validation_reports`:
- `hard_failures_present`: yes | no
- `hard_failure_summary`:
- `warning_summary`:

## Review

- `specialist_reviews`:
- `qa_audit`:
- `human_review_required`: yes
- `approval_decision`: approved | revise | blocked
- `approval_notes`:

## Known Issues

- `accepted_limitations`:
- `deferred_work`:
- `risks_for_next_stage`:
- `must_not_change_next_stage`:

## Next Stage Instructions

- `next_stage_inputs`:
- `next_stage_focus`:
- `next_stage_stop_conditions`:
- `next_stage_owner`:

## Signoff

- `prepared_by`:
- `approved_by`:
- `approved_at`:
