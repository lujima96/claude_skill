# Deformation Landmarks

```text
domain: anatomy
body_region: full_body
species: humanoid
sex_or_body_type: any
age_band: adult
style_family: engine_agnostic
deformation_criticality: critical
target_engine: Godot
target_platform: unknown
source_quality: internal_first_pass
last_reviewed: 2026-07-20
linked_docs: knowledge/topology/biped_deformation_loops.md, knowledge/rigging/godot_biped_rig_requirements.md
```

## Purpose

Use this when checking whether a biped design can survive rigging, skinning, and pose tests.

## Critical Zones

| Zone | What Must Be Clear | Pose Risk |
|---|---|---|
| Neck | Jaw, throat column, clavicle, trapezius, head support | Head twist, head tilt, jaw open |
| Shoulder | Clavicle, deltoid cap, scapular plane, armpit | Arm raise, reach, weapon swing |
| Elbow | Bend axis, upper-arm mass, forearm wedge | Flexion, extension |
| Wrist | Forearm taper, hand block, twist path | Pronation, grip, weapon hold |
| Hip | Pelvis block, femur insertion, groin, glute fold | Crouch, kick, strafe |
| Knee | Patella block, quad insertion, calf relation | Deep bend, run cycle |
| Ankle | Tibia plane, heel block, foot arch | Plant, toe-off, crouch |
| Mouth | Mouth bag, lip closure, corners, jaw hinge | Phonemes, snarl, jaw open |
| Eyes | Eyeball, lids, canthi, brow support | Blink, squint, look direction |

## Minimum Pose Battery

- Shoulder raise.
- Elbow flexion.
- Wrist pronation and supination.
- Neck twist and tilt.
- Jaw open and close.
- Blink and squint if eyelids exist.
- Deep squat.
- Hip abduction.
- Knee bend.
- Toe-off or planted-foot check.

## Review Checklist

- Are bend axes visible in the sculpt or mesh plan?
- Do forms compress and stretch in plausible directions?
- Are accessories clear of deformation lanes?
- Does clothing cross joints in a way that can be weighted?
- Are stylized exaggerations making pose tests easier or harder?

## Common Failures

- Shoulder armor blocks arm raise with no rigging strategy.
- Thick neck prevents head turn.
- Elbow and knee loops are placed for visual symmetry, not bend direction.
- Hip area is obscured by belts or cloth without deformation planning.
- Mouth detail is sculpted before mouth mechanics are solved.
