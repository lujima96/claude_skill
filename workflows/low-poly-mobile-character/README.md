# Low-Poly Mobile Character Workflow

This second workflow proves the framework can generalize without rewriting the core director, templates, handoffs, QA audit format, or validator interfaces.

## Workflow Delta

This workflow reuses the canonical stage list and all core contracts. It changes only the production constraints:

- Lower triangle budgets.
- Stronger material slot limits.
- Smaller texture sizes.
- Simple deformation scope.
- LOD policy decided earlier.
- Stylized readability biased toward mobile camera distance.

## Required Knowledge Additions

- `knowledge/optimization/low_poly_mobile_character_budgets.md`

## Example Project

- `examples/low_poly_mobile_scout/`

## Exit Gate

The workflow is acceptable only if it can use the same Character Director, task cards, handoffs, specialist reviews, QA audit format, and validators as `stylized-biped-godot`.
