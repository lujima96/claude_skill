# Knowledge Base

This folder contains retrieval-ready domain knowledge for anatomy, style, topology, rigging, materials, Godot standards, critique patterns, and examples.

Every knowledge file should include metadata when practical:

```text
domain:
body_region:
species:
sex_or_body_type:
age_band:
style_family:
deformation_criticality:
target_engine:
target_platform:
source_quality:
last_reviewed:
linked_docs:
```

Stable production law belongs in `AGENTS.md` and `docs/pipeline/`, not only in retrieval documents.

## First Workflow Seed Docs

These are the initial high-signal documents for the stylized biped to Godot workflow:

- `anatomy/stylized_biped_proportions.md`
- `anatomy/head_face_construction.md`
- `anatomy/deformation_landmarks.md`
- `style-library/heroic_stylized.md`
- `style-library/silhouette_gameplay_readability.md`
- `topology/biped_deformation_loops.md`
- `rigging/godot_biped_rig_requirements.md`
- `materials/godot_character_materials.md`
- `optimization/low_poly_mobile_character_budgets.md`
- `engine-standards/godot_import_requirements.md`
- `critique-patterns/stylized_biped_review_failures.md`

## Research Needed Later

The current files are deliberately first-pass production heuristics. Before finalizing validators or engine adapters, verify against the target Godot version and the actual game project's import, animation, material, and performance constraints.
