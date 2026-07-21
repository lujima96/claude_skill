# Materials Review Rules

## Minimum Evidence

- Blender material report.
- Declared material slot budget.
- Texture set list with paths.
- Texture naming convention.
- Texture size policy.
- Channel packing policy.
- Godot export texture path policy.
- Material screenshots under neutral lighting when visual review is needed.

## Hard Failures

- Required material families are missing.
- Texture files are missing or referenced outside the export package.
- Texture names do not identify asset, material family, map type, and resolution.
- Channel packing is unknown when packed maps are required.
- Material slot count exceeds the declared budget.
- Alpha material behavior is unknown for required hair cards or transparent surfaces.

## Escalation

If texture paths, material budget, or channel packing are unknown at material approval time, set `hard_failures_present: yes`, `blocked_stage_progression: yes`, and `decision: block`.
