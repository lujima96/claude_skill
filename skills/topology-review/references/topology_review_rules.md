# Topology Review Rules

## Minimum Evidence

- Current source `.blend` path or exported mesh artifact.
- Blender mesh report.
- Naming report when mesh object names are part of the production contract.
- Screenshots or turntable views that show face, shoulder, elbow, hip, knee, hand, neck, and cloth zones.
- Deformation requirements from the brief or Character Director.

## Hard Failures

- Critical deformation loops are missing around eyes, mouth, shoulders, elbows, hips, knees, neck, fingers, or cloth bend zones.
- Poles or triangles sit in predictable high-bend zones.
- The mesh is approved only because it looks clean in a neutral pose.
- Retopology data is missing for a stage that requires topology approval.
- Cloth or accessories hide unresolved topology around joints.

## Scoring Guidance

- High score: loops visibly follow motion, density is concentrated where needed, poles are parked in low-motion areas, bake cage risks are named, and screenshots cover all critical zones.
- Medium score: mostly workable topology with localized density or pole issues that can be corrected before rigging.
- Low score: topology is missing, generated, or unreviewable; mesh may be acceptable only for blockout or still-image use.

## Escalation

If a finding blocks deformation or bake readiness, set `hard_failures_present: yes`, `blocked_stage_progression: yes`, and `decision: block`.
