---
name: style-keeper
description: Enforce style-family rules for AI-assisted character production. Use when a brief, reference set, proportion plan, blockout, sculpt, material plan, or review needs style constraints checked for silhouette, proportion dials, plane simplification, feature emphasis, material treatment, detail frequency, and gameplay readability.
---

# Style Keeper

The Style Keeper protects the chosen style family without overriding anatomy, topology, deformation, or Godot readiness. Style is treated as controlled dials, not permission to ignore structure.

## Use

Use this skill when:

- A brief needs a style contract.
- References need style-fit review.
- A proportion plan or blockout needs silhouette review.
- Materials or detail density need style-family constraints.
- A specialist review risks drifting into vague taste comments.

## Inputs

- `templates/character_brief.md`
- `templates/review_report.md`
- `knowledge/style-library/heroic_stylized.md`
- `knowledge/style-library/silhouette_gameplay_readability.md`
- `knowledge/materials/godot_character_materials.md`
- `knowledge/critique-patterns/stylized_biped_review_failures.md`

## Required Output

Produce a `templates/review_report.md`-compatible report with:

- Style-family decision.
- Proportion dials.
- Shape-language rules.
- Detail-frequency rules.
- Material-readability rules.
- Silhouette and gameplay readability concerns.
- Decision: `approve`, `approve_with_notes`, `revise`, or `block`.

## Review Rules

- Style cannot override deformation.
- Preserve gameplay-distance readability.
- Keep detail subordinate to primary masses.
- Require material separation under neutral Godot lighting.
- Record which style dials can move and which structural rules cannot.

## First Workflow

For `stylized_orc_bruiser`, use `references/heroic_stylized_style_rules.md` and `references/example_style_keeper_report.md`.
