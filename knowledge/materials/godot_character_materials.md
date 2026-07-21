# Godot Character Materials

```text
domain: materials
body_region: full_body
species: any
sex_or_body_type: any
age_band: any
style_family: heroic_stylized
deformation_criticality: medium
target_engine: Godot
target_platform: unknown
source_quality: internal_first_pass
last_reviewed: 2026-07-20
linked_docs: knowledge/engine-standards/godot_import_requirements.md, knowledge/style-library/heroic_stylized.md
```

## Purpose

Use this when reviewing texture and material readiness for Godot-targeted character assets.

## Material Families

- Skin.
- Cloth.
- Leather.
- Metal.
- Bone, teeth, tusks, claws.
- Hair.
- Eyes.
- Weapon or gear materials.

## Review Rules

- Material slots should stay within the declared budget.
- Material names should be stable and descriptive.
- Texture paths should be export-friendly.
- Alpha materials, especially hair cards, need explicit handling.
- Materials should read under neutral Godot lighting, not only Blender preview lighting.
- Texture detail should not hide unresolved form or deformation issues.

## Godot Export Concerns

- Some material features may need Godot-side material overrides.
- Texture references must survive the export/import path.
- Channel packing rules must be documented before validators enforce them.
- Hair cards need consistent alpha, sorting, and normal expectations.
- Stylized materials should be tested in a preview scene, not judged only in Blender.

## Common Failures

- Materials named casually in Blender and difficult to bind in Godot.
- Too many material slots for the platform.
- Hair alpha works in Blender but fails visually in Godot.
- Roughness, metallic, or normal maps are inconsistent across texture sets.
- Textures exported to paths that the Godot project does not expect.

## Research Needed

Before engine-adapter implementation, decide project material conventions for Godot: imported materials only, Godot-side overrides, custom shaders, channel packing, and hair alpha policy.
