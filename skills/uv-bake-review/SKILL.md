---
name: uv-bake-review
description: Review UV layout, UV overlap policy, texel density, padding, bake cage, high-poly to low-poly pairing, baked map completeness, and bake artifact risks for staged Blender-to-Godot character production. Use when a retopo mesh is prepared for texture baking or when UV/bake validation is required before materials.
---

# UV Bake Review

The UV Bake Reviewer checks whether the approved mesh can receive clean texture data. It does not approve material art direction, rigging, or Godot import by itself.

## Use

Use this skill when:

- A retopology mesh needs UV and bake readiness review.
- UV sets, UDIM policy, padding, texel density, or overlap rules need approval.
- Bake cages, high-poly sources, or normal/AO/ID maps need review.
- Bake artifacts appear in high-visibility or deformation-critical areas.

## Inputs

- `templates/review_report.md`
- `templates/uv_bake_report.md`
- `templates/topology_report.md`
- `knowledge/topology/biped_deformation_loops.md`
- `knowledge/materials/godot_character_materials.md`
- `knowledge/engine-standards/godot_import_requirements.md`

## Required Output

Produce a `templates/review_report.md`-compatible report and, when UV/bake data is available, a `templates/uv_bake_report.md`-compatible report with:

- UV set presence.
- Overlap policy and overlap findings.
- Texel density and padding findings.
- Bake source/target pairing.
- Cage and ray-distance notes.
- Required baked map list and artifact findings.
- Decision: `approve`, `approve_with_notes`, `revise`, or `block`.

## Review Rules

- Missing UVs block bake and texture progression.
- Disallowed UV overlaps block bake approval.
- Bake artifacts in face, hands, shoulders, joints, or focal costume areas block progression.
- Texture work cannot begin until required map outputs and naming expectations are declared.
- Route material naming, channel packing, and Godot texture path issues to Materials Reviewer.

## First Workflow

For `stylized_orc_bruiser`, use `references/uv_bake_review_rules.md` and `references/example_uv_bake_review_report.md`.
