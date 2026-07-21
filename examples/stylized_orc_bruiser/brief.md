# Stylized Orc Bruiser Brief

## Metadata

- `brief_id`: stylized_orc_bruiser-brief-001
- `character_name`: Stylized Orc Bruiser
- `created_by`: Character Director
- `created_at`: 2026-07-21
- `last_updated`: 2026-07-21
- `status`: approved
- `current_stage`: blockout_planning

## Source Request

- `raw_prompt`: stylized orc bruiser for a third-person game
- `user_goals`: create a Godot-targeted stylized biped character pipeline example with visible stage gates and approved references
- `non_goals`: no Blender MCP edits, sculpting, retopology, rigging, texturing, Godot import, or automation in Phase 5
- `open_questions`: target Godot version; target platform; exact poly budget; material slot budget; texture resolution; skeleton spec; animation list; facial animation needs; collision and attachment marker requirements

## Production Target

- `target_engine`: Godot
- `target_godot_version`: unknown
- `primary_dcc`: Blender
- `default_interchange_format`: GLB
- `target_platform`: unknown
- `camera_context`: third_person
- `expected_screen_size`: gameplay-distance readability required; exact screen size unknown

## Character Intent

- `role`: bruiser enemy or playable heavy archetype
- `narrative_function`: imposing fantasy combatant with readable strength, aggression, and battle wear
- `gameplay_function`: close-range melee threat with clear attack-readiness and durable silhouette
- `species`: orc
- `age_band`: adult
- `sex_or_body_type`: broad muscular humanoid body type
- `body_type`: heroic stylized heavy build
- `personality_keywords`: intimidating, durable, blunt, aggressive, battle-worn
- `silhouette_priorities`: broad shoulders, thick neck, heavy jaw, large hands, strong forearms, readable tusks, simple gear massing

## Style Contract

- `style_family`: heroic_stylized
- `style_references`: `reference_boards/approved_initial_board.md`; `references/ref-001_dmitry_sokolovsky_orcish_orc.md`; `references/ref-002_daniel_zuleta_orc_and_bison.md`; `references/ref-003_tozi_stylized_warrior.md`; `references/ref-005_andrus_zapata_orc_warrior.md`; `references/ref-007_diana_pancorbo_stylized_orc.md`
- `proportion_rules`: exaggerate upper body mass while preserving ribcage, pelvis, shoulder, elbow, wrist, hip, knee, neck, jaw, eyelid, and mouth construction logic
- `shape_language`: large simple primary masses, angular jaw and brow, powerful shoulder-to-waist taper, chunky hands, compact heavy gear
- `detail_frequency`: primary and secondary forms first; tertiary scars, pores, stitches, scratches, and surface noise deferred until forms read cleanly
- `material_treatment`: Godot-readable skin, leather, metal, cloth, bone, hair, and eye material families with value separation
- `color_readability_rules`: skin, armor, cloth, and gear must separate by value and silhouette at third-person distance

## Asset Scope

- `required_body_regions`: full biped body, head, neck, torso, arms, hands, pelvis, legs, feet, eyes, mouth, nose, ears or orc ear variant
- `clothing_and_gear`: shoulder armor, bracers, belt kit, simple cloth or leather elements; exact design remains original and must not copy approved references
- `hair_strategy`: sculpted or cards, pending platform and style constraints
- `facial_animation_required`: unknown
- `blend_shapes_required`: unknown
- `animation_requirements`: idle, locomotion, attack, hit reaction, and pose tests likely required; exact list unknown
- `collision_or_marker_requirements`: unknown

## Technical Budgets

- `poly_budget_lod0`: unknown
- `lod_count_target`: unknown
- `texture_sets`: unknown
- `texture_resolution_target`: unknown
- `material_slot_budget`: unknown
- `max_skin_influences`: unknown
- `skeleton_spec`: unknown

## Required Deliverables

- `source_blend`: required later
- `export_package`: GLB package required later
- `godot_import_package`: required later
- `screenshots`: required from blockout onward
- `validation_reports`: required once validators exist
- `qa_audit`: `audit.md`

## Acceptance Criteria

- `brief_completeness`: approved for manual vertical slice and blockout planning; technical unknowns are tracked as risks
- `style_readability`: heroic stylized fantasy direction is defined and supported by approved references
- `production_constraints_defined`: Blender-to-GLB-to-Godot path defined; exact budgets still open
- `godot_target_defined`: yes
- `approval_required_from`: Lucas

## Handoff

- `next_stage`: blockout_planning
- `handoff_summary`: use the approved board to plan a heroic stylized orc blockout focused on silhouette, shoulder/neck massing, jaw/tusk construction, hands, and simple Godot-readable material families
- `blocking_issues`: no Phase 5 blocker; target platform, Godot version, budgets, skeleton spec, facial animation needs, and animation list must be answered before production mesh approval
- `approved_by`: Lucas
- `approved_at`: 2026-07-21
