# Stylized Biped Review Failure Patterns

```text
domain: critique_pattern
body_region: full_body
species: humanoid_or_creature_biped
sex_or_body_type: any
age_band: any
style_family: heroic_stylized
deformation_criticality: high
target_engine: Godot
target_platform: unknown
source_quality: internal_first_pass
last_reviewed: 2026-07-20
linked_docs: knowledge/anatomy/stylized_biped_proportions.md, knowledge/topology/biped_deformation_loops.md, knowledge/style-library/silhouette_gameplay_readability.md
```

## Purpose

Use this to make reviews sharper and less generic.

## Failure Patterns

| Pattern | Symptom | Likely Fix |
|---|---|---|
| Detail before structure | Pores, scratches, wrinkles, or gear noise on weak forms | Return to primary or secondary forms |
| Strong front, weak side | Character looks good only from front | Recheck ribcage, pelvis, skull, and limb depth |
| Big shoulders, broken arm raise | Heroic silhouette blocks deformation | Redesign shoulder mass, armor clearance, and topology |
| Monster face, human topology forgotten | Creature face cannot blink, snarl, or close mouth | Rebuild eye and mouth construction |
| Equal noise everywhere | No clear focal hierarchy | Reduce detail frequency and group forms |
| Costume hides rig problems | Belts, cloth, or armor cover unclear joints | Expose or define joint/deformation strategy |
| Blender-only approval | Asset looks acceptable before engine import | Require Godot preview and validation |
| Still-image topology | Mesh looks clean but fails pose tests | Review loops around deformation zones |

## Review Questions

- What stage owns this problem?
- Is this a hard failure or a weighted score issue?
- Does fixing it require returning to an earlier stage?
- Is the issue visible in silhouette, deformation, material read, or Godot import?
- Can the next stage proceed safely with this issue documented?

## Escalation

If the issue affects topology legality, skinning, deformation, Godot import, or missing required artifacts, treat it as a hard-failure candidate and route through the Character Director.
