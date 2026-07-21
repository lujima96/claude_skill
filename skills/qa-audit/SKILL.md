---
name: qa-audit
description: Aggregate specialist reviews and validation reports into a weighted QA decision for staged character production. Use when deciding whether a character asset can advance, needs revision, must return to an earlier stage, or is blocked by hard failures.
---

# QA Audit

The QA Auditor aggregates reviews, validation reports, hard-failure state, weighted score, and progression decision. It does not override the Character Director; it provides the decision evidence.

## Use

Use this skill when:

- Multiple specialist reviews need one decision.
- A stage handoff needs QA status.
- Hard failures need to be separated from score issues.
- A weighted score is needed.
- The Director needs a progression recommendation.

## Inputs

- `templates/qa_audit_report.md`
- `templates/review_report.md`
- `templates/validation_report.md`
- `docs/pipeline/hard_failures.md`
- `docs/pipeline/scoring_rubric.md`
- `knowledge/critique-patterns/stylized_biped_review_failures.md`

## Required Output

Produce a `templates/qa_audit_report.md`-compatible report with:

- Inputs reviewed.
- Hard-failure summary.
- Weighted score when enough scoreable evidence exists.
- Diagnosis.
- Decision: `approve_next_stage`, `revise_current_stage`, `return_to_previous_stage`, or `block_progression`.

## Audit Rules

- Any hard failure blocks progression.
- Missing required reviews or validations count as blocking when the stage requires them.
- Do not invent scores when evidence is absent. Mark categories as pending.
- Use `structural_rework` when hard failures exist, even if score would be high.
- Record the most important fixes in priority order.
- Do not run or rewrite QA for a Blender MCP `quick_iteration`. Audit the accumulated task only at `gate_review`, rollback, scope escalation, or a stage decision.

## First Workflow

For `stylized_orc_bruiser`, use `references/phase4_preproduction_audit_rules.md` and `references/example_combined_qa_audit_report.md`.
