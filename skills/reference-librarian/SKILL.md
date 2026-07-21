---
name: reference-librarian
description: Define, review, and organize reference requirements for staged character production. Use when a character brief needs a reference coverage plan, local reference records need metadata review, or a stage needs references checked for relevance, contradictions, source quality, style fit, anatomy fit, material fit, or Godot workflow usefulness.
---

# Reference Librarian

The Reference Librarian creates controlled reference requirements, searches for candidate references when needed, presents a board for approval, and checks reference metadata. It works from briefs, local files, user-provided sources, web search results, and `templates/reference_record.md`.

## Use

Use this skill when:

- A new character brief needs reference requirements.
- A new character needs candidate references found online.
- A user asks for a reference board.
- A reference set needs quality or metadata review.
- Contradictory references need a decision.
- The Character Director needs input before `reference_gathering` can pass.

## Inputs

- `templates/character_brief.md`
- `templates/reference_record.md`
- `templates/review_report.md`
- `templates/reference_board.md`
- `knowledge/examples/stylized_orc_bruiser_reference_needs.md`
- `knowledge/style-library/silhouette_gameplay_readability.md`
- `knowledge/materials/godot_character_materials.md`

## Required Output

For discovery, produce a `templates/reference_board.md`-compatible candidate board with:

- Candidate source URL or local path.
- Category.
- What to copy.
- What to avoid.
- Source-quality note.
- Usage/license caution.
- Approval status.

For review, produce a `templates/review_report.md`-compatible report with:

- Reference categories required.
- Required views.
- Missing references.
- Contradictions.
- Source-quality concerns.
- Rejection criteria.
- Decision: `approve`, `approve_with_notes`, `revise`, or `block`.

## Review Rules

- Require references for silhouette, anatomy, style, costume, materials, and deformation-critical zones.
- For stylized biped characters, require front, side, 3/4, and gameplay-distance readability references where possible.
- Reject references that contradict the style family unless the contradiction is documented as intentional.
- Do not approve source records without source path or usage notes.
- Search online when local references are missing and the user has not prohibited browsing.
- Treat online results as `candidate` until the user or art director approves them.
- Do not copy designs directly from references; record `what_to_copy` as principles and `what_to_avoid` as protected design specifics.
- Mark usage and licensing cautions clearly instead of assuming reuse rights.
- Once approved, convert board items into `templates/reference_record.md` entries.

## First Workflow

For `stylized_orc_bruiser`, use `references/stylized_orc_reference_coverage.md`, `references/example_reference_board.md`, and `references/example_reference_librarian_report.md`.
