# Low-Poly Mobile Character Delta Notes

## Reused Core

- Character Director.
- Stage task cards.
- Stage handoffs.
- Review reports.
- QA audits.
- Asset manifests.
- MCP action logs.
- Blender report scripts.
- Godot adapter.
- Phase 10 readiness validators.

## Changed Constraints

- Target platform defaults to mobile.
- LOD policy is required before optimization approval.
- Material slot count should be lower than desktop stylized biped assumptions.
- Texture size caps are stricter.
- Deformation scope should avoid expensive facial systems unless explicitly required.
- Silhouette readability should be judged at smaller screen size and lower pixel density.

## No Core Rewrite

No director rewrite is needed. The second workflow is a constraint/profile variation, not a different pipeline architecture.
