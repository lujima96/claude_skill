# Biped Deformation Loops

```text
domain: topology
body_region: full_body
species: humanoid
sex_or_body_type: any
age_band: adult
style_family: any
deformation_criticality: critical
target_engine: Godot
target_platform: unknown
source_quality: internal_first_pass
last_reviewed: 2026-07-20
linked_docs: knowledge/anatomy/deformation_landmarks.md, knowledge/rigging/godot_biped_rig_requirements.md
```

## Rule

Topology is approved for deformation, not for still images. Loops must support motion at critical zones.

## Required Loop Areas

| Area | Loop Requirement | Failure Signal |
|---|---|---|
| Eyes | Concentric eyelid loops around eyeball | Blink collapse, flat lids |
| Mouth | Oral loop, mouth corner support, lip volume | Bad closure, broken snarl, phoneme failure |
| Jaw and neck | Jaw hinge and neck compression support | Jaw opens by tearing the neck |
| Shoulder | Shoulder and armpit loops that allow arm raise | Pinching, armor collision, collapsing armpit |
| Elbow | Bend-axis loops with enough span | Candy-wrapper bend or sharp collapse |
| Wrist | Twist-friendly forearm and wrist loops | Bad pronation, hand detaches visually |
| Hip | Groin, glute, and upper-thigh loops | Crouch tearing |
| Knee | Bend-axis loops around patella region | Knee folds like a tube |
| Ankle and foot | Ankle, heel, arch, ball support | Bad toe-off or foot plant |
| Fingers | Curl loops and thumb-base topology | Fist or grip failure |

## Review Checklist

- Are loops placed around motion, not just even quad distribution?
- Are triangles and poles away from high-bend zones?
- Does density increase only where deformation or silhouette needs it?
- Are face loops adequate for required expression scope?
- Does clothing topology respect joint bends?

## Common Failures

- Auto-remesh accepted without manual correction in shoulders or face.
- Even quads everywhere but no deformation logic.
- Poles at mouth corners, eyelids, shoulders, elbows, knees, or groin.
- Cloth mesh ignores the body bend underneath.
- Facial topology built for a neutral pose only.
