# Optimization Review Rules

## Minimum Evidence

- Asset manifest with budgets.
- Mesh report.
- Material report.
- Export package report.
- Declared LOD count and naming convention.
- Declared LOD triangle budgets.
- Texture size and memory policy.
- Required collision, marker, and socket list.

## Hard Failures

- LODs are required but missing.
- LOD names do not follow the declared convention.
- LOD polycounts exceed declared budgets.
- Material slot count exceeds budget.
- Texture sizes exceed budget or are undeclared.
- GLB/glTF package is missing required meshes, materials, textures, skeleton, animations, or blend shapes.
- Export texture paths do not resolve for the target Godot project.

## Escalation

If budgets, LOD policy, or package completeness are unknown at optimization approval time, set `hard_failures_present: yes`, `blocked_stage_progression: yes`, and `decision: block`.
