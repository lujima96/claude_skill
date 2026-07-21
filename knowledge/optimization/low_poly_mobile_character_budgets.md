# Low-Poly Mobile Character Budgets

```text
domain: optimization
body_region: full_body
species: humanoid
sex_or_body_type: any
age_band: any
style_family: low_poly_mobile
deformation_criticality: medium
target_engine: Godot
target_platform: mobile
source_quality: internal_first_pass
last_reviewed: 2026-07-21
linked_docs: knowledge/materials/godot_character_materials.md, knowledge/engine-standards/godot_import_requirements.md
```

## Default Budget Profile

These are starter constraints, not universal targets.

| Item | Starter Budget |
|---|---:|
| LOD0 triangles | 6000 |
| LOD1 triangles | 3000 |
| LOD2 triangles | 1200 |
| Material slots | 2 |
| Texture sets | 1-2 |
| Max texture size | 1024 |
| Skin influences | 4 |

## Review Rules

- Prioritize silhouette over micro-detail.
- Use fewer materials before using smaller unreadable details.
- Avoid facial rigs unless gameplay requires them.
- Require LOD naming and package policy before export validation.
- Test in Godot preview under mobile-like camera distance.
