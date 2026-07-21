# UV Bake Review Rules

## Minimum Evidence

- Approved retopology mesh.
- UV set report or screenshot evidence.
- UV overlap policy.
- Texel density target.
- Padding target.
- High-poly source and low-poly target.
- Bake cage or ray-distance plan.
- Required baked map list.

## Hard Failures

- Required UV set is missing.
- UV overlaps exist where the task card disallows overlaps.
- Texel density is undefined for final texture work.
- Padding is too low for the target texture size.
- High-poly and low-poly pairing is missing.
- Bake artifacts obscure face, hands, silhouette-critical forms, or deformation-critical zones.

## Escalation

If UVs, overlap policy, or bake source/target pairing are missing at UV/bake approval time, set `hard_failures_present: yes`, `blocked_stage_progression: yes`, and `decision: block`.
