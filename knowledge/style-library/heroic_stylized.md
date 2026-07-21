# Heroic Stylized Style Family

```text
domain: style
body_region: full_body
species: humanoid_or_creature_biped
sex_or_body_type: any
age_band: any
style_family: heroic_stylized
deformation_criticality: medium
target_engine: Godot
target_platform: unknown
source_quality: internal_first_pass
last_reviewed: 2026-07-20
linked_docs: knowledge/anatomy/stylized_biped_proportions.md, knowledge/style-library/silhouette_gameplay_readability.md
```

## Style Intent

Heroic stylization prioritizes clear primary shapes, exaggerated role readability, strong silhouettes, simplified but confident anatomy, and material separation that survives gameplay camera distance.

## What Stays Constant

- Skeleton and joint logic.
- Deformation zones.
- Facial construction if expressions are required.
- Gameplay readability.
- Material identity.
- Stage-gated progression.

## What Changes

- Proportion ratios can be pushed.
- Hands, feet, shoulders, jaw, weapons, and gear can be enlarged.
- Planes can be simplified.
- Details can be grouped into larger readable clusters.
- Color and value separation can be stronger than realism.

## Shape Language

- Use large, readable primary forms.
- Use clear taper relationships: shoulders to waist, forearm to wrist, thigh to knee, calf to ankle.
- Keep accessories chunky enough to read but simple enough to rig and export.
- Favor asymmetry only when it supports story or gameplay read.

## Material Treatment

- Skin, leather, cloth, metal, bone, hair, and weapon materials should be separable under neutral Godot lighting.
- Avoid material noise that competes with silhouette and face readability.
- Use detail density to support scale and story, not to hide unresolved form.

## Review Checklist

- Does the character read as the intended role from a small thumbnail?
- Are exaggerated forms consistent across the body?
- Are secondary details subordinate to the primary masses?
- Are colors and materials readable without cinematic lighting?
- Does the style preserve rig and deformation needs?
