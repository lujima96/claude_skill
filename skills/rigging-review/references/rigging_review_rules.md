# Rigging Review Rules

## Minimum Evidence

- Current rigged `.blend` path or exported rig artifact.
- Blender pose battery report.
- Scene report showing armature and mesh counts.
- Skeleton naming convention.
- Maximum skin influence policy.
- Required animation and facial deformation scope.
- Godot version or declared unknown that remains a tracked risk.

## Hard Failures

- No armature exists for a stage that requires rigging approval.
- No skinned mesh exists for deformation testing.
- Required pose battery cannot run.
- Unweighted vertices exist on a required skinned mesh.
- Max influences exceed the Godot target policy.
- Skeleton naming is unstable or not declared.
- Corrective-shape or twist-zone needs are ignored after visible deformation failure.

## Scoring Guidance

- High score: all required pose tests pass, naming is stable, weights are complete, influence limits are respected, and corrective needs are explicitly accepted or resolved.
- Medium score: rig is usable but has localized deformation issues with clear revision tasks.
- Low score: rig data is missing, pose tests cannot run, or Godot import expectations are unresolved.

## Escalation

If deformation cannot be tested, set `hard_failures_present: yes`, `blocked_stage_progression: yes`, and `decision: block`.
