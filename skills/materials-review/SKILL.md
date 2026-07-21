---
name: materials-review
description: Review Godot-targeted character materials, texture sets, texture naming, texture size, channel packing, material slot count, and export texture path readiness. Use when a character has material assignments, texture sources, baked maps, or GLB/glTF export materials that need approval before optimization or Godot import.
---

# Materials Review

The Materials Reviewer checks whether material and texture data can survive the Blender-to-Godot path. It does not approve UV unwrap quality, mesh topology, rigging, or final Godot import by itself.

## Use

Use this skill when:

- Material slots and material names need review.
- Texture sets are ready for naming, size, and path validation.
- Channel packing rules need approval.
- Hair, alpha, skin, metal, cloth, leather, bone, or eye materials need Godot-readiness checks.
- A material issue appears after export or Godot import.

## Inputs

- `templates/review_report.md`
- `templates/material_texture_report.md`
- `blender_scripts/material_report.py`
- `knowledge/materials/godot_character_materials.md`
- `knowledge/engine-standards/godot_import_requirements.md`
- `knowledge/style-library/heroic_stylized.md`

## Required Output

Produce a `templates/review_report.md`-compatible report and, when texture data is available, a `templates/material_texture_report.md`-compatible report with:

- Material slot count and budget findings.
- Material naming findings.
- Texture set coverage by material family.
- Texture naming and size findings.
- Channel packing findings.
- Godot export texture path findings.
- Alpha and hair-card handling when relevant.
- Decision: `approve`, `approve_with_notes`, `revise`, or `block`.

## Review Rules

- Require declared material slot budget before final approval.
- Require stable material names before Godot binding or overrides.
- Require texture naming, size, channel packing, and export path rules before validators can pass.
- Treat missing required texture sets as blockers for material approval.
- Treat Blender-only material appearance as insufficient for Godot readiness.
- Route UV layout, bake cage, padding, and overlap problems to UV Bake Reviewer.

## First Workflow

For `stylized_orc_bruiser`, use `references/materials_review_rules.md` and `references/example_materials_review_report.md`.
