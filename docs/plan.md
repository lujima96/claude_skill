# Blueprint for an AI Assisted Character Pipeline Framework

## System conclusion

The strongest version of this project is **not** a single “character skill.” It is a **production framework** with five layers: an orchestration agent, specialist subagents or skills, a structured knowledge base, Blender and engine-side validators, and a mandatory review loop that forces the model to stop at explicit gates instead of free-running from prompt to final asset. That direction matches what public studio material repeatedly implies: professional character work is a staged pipeline with separate modeling, texturing, rigging, deformation, optimization, and engine-integration concerns, and it breaks down when topology, rigging, or review are treated as afterthoughts. Naughty Dog’s published Uncharted pipeline explicitly separated sculpt, game mesh, texturing, shader setup, and rigging; standardized skeletons and naming; and identified LODs, optimization, outsourcing, hair, and iteration speed as production-critical issues rather than polish extras. Riot describes character art as the translation of 2D fantasy into readable, believable 3D form, while CD Projekt Red’s character artists describe silhouette, garments, dirt, haircut, and materials as storytelling devices that have to survive production constraints. Blizzard’s Diablo IV team likewise frames the problem as moving concept intent into a PBR production pipeline with dye systems, material tagging, detail mapping, and real-time review. citeturn7view0turn8search0turn25search0turn0search5

That matters because an “AI junior character artist” should be designed to behave like a cautious production worker, not like a one-shot generator. Claude Skills, Claude subagents, Codex skills, AGENTS.md, MCP servers, and scripted validators are useful precisely because they let you encode repeatable procedures, context boundaries, and handoff formats. Anthropic’s docs describe skills as reusable markdown procedures that can be loaded only when needed, and subagents as specialized workers with their own context and tool permissions. OpenAI’s docs describe Codex skills as packages of instructions, resources, and optional scripts, and Codex subagents as delegated agents for bounded tasks inside reviewable workflows. In other words, both toolchains are already steering toward the same architecture: **small, inspectable specialists coordinated by a director**. citeturn33search0turn2search1turn34search2turn34search0turn34search4

My recommendation is therefore straightforward: build this as an **AI Character Pipeline Framework** with a human art director at the approval gates. The model should never be trusted to “finish the character”; it should be trusted to advance the asset **one validated stage at a time**. That is the only architecture that has a serious chance of producing cohesive, anatomically sound, animation-ready, game-ready characters across multiple styles. citeturn7view0turn25search0turn33search8turn34search10

## Production pipeline

The public record does not expose every internal studio SOP in full, but it exposes enough to reconstruct a realistic production model. The common pattern is: story and concept intent first, readable proportion and silhouette second, sculpt and material resolution third, topology and rig fitness fourth, and engine validation last. The pipeline below is the version I would encode into the framework. It is deliberately gate-heavy because that is where most AI-assisted systems fail. citeturn7view0turn8search0turn8search6turn25search0

| Stage | Objective | Inputs | Outputs | Quality gates and automated checks | Review criteria | Basis |
|---|---|---|---|---|---|---|
| Concept interpretation | Turn idea into production brief, not vibes. | Narrative pitch, concept art, game design constraints, target platform, style family. | Character brief with role, silhouette priorities, body type, style constraints, deliverables. | Check for missing target engine, poly budget, rig type, LOD target, texture budget, style tag. | Does the brief define fantasy, gameplay readability, and production targets clearly enough to model against? | citeturn8search0turn25search0turn8search6 |
| Reference gathering | Build a controlled reference set instead of ad hoc scraping. | Brief, anatomy pack, style pack, costume and material refs, pose refs. | Curated reference board with metadata and source quality score. | Reject low-signal or contradictory references; dedupe near-duplicates; require front, side, 3/4, material, and expression refs where relevant. | Are references consistent with silhouette, anatomy, costume logic, and target art style? | citeturn17search0turn17search2turn19search14turn18search2 |
| Proportion planning | Lock landmark proportions before detailed sculpting. | Brief, orthographic overlays, anatomy guides. | Proportion sheet and primitive mannequin. | Symmetry report; limb-length ratios; head-count target; stance and center-of-mass sanity check. | Does the body read correctly in silhouette and match role, age, sex, species, and style intent? | citeturn8search0turn17search1turn17search8 |
| Blockout | Establish big masses only. | Proportion plan, concept, references. | Clean blockout with major masses and accessory placeholders. | No tertiary detail allowed; silhouette snapshots from front/side/3/4/back; intersection and clipping check. | Does it read at thumbnail size and from gameplay camera distance? | citeturn8search6turn8search9turn25search0 |
| Primary forms | Solve torso, pelvis, ribcage, skull, limb volumes. | Blockout, anatomy landmarks. | Primary-form sculpt. | Landmark checklist: ASIS, clavicles, ribcage, scapular plane, patella region, ankle block; symmetry scan. | Do the forms feel structurally true before muscles and cloth noise are added? | citeturn17search0turn32search1turn19search14 |
| Secondary anatomy | Add muscles, fat, tension, and species-specific variation. | Primary sculpt, anatomy pack, style rules. | Secondary-form sculpt. | Muscle insertion and surface landmark checklist; pose stress preview on shoulders, elbows, knees, hips, neck. | Is anatomy believable for the chosen style, not just technically named? | citeturn17search0turn17search2turn19search9turn18search2 |
| Tertiary detail | Add pores, wrinkles, seams, stitch language, wear logic only after big forms hold. | Approved secondary sculpt, material refs. | High-res sculpt and detail layers. | Frequency separation check; detail density map; ban on detail obscuring silhouette or landmarks. | Is detail supporting material story, scale, and camera distance rather than muddying the model? | citeturn0search5turn25search0 |
| Clothing, hard surface, hair | Integrate costume logic and accessories into the body plan. | Costume refs, material callouts, style pack. | Production sculpt of costume, armor, props, hair blockout or cards/groom plan. | Cloth intersection test; attachment plausibility; material ID assignment; hair coverage and scalp breakup check. | Do clothing and props tell story, preserve silhouettes, and still leave riggable deformation zones? | citeturn25search0turn0search5turn16search11 |
| Retopology | Convert sculpt into deformation-ready game mesh. | Approved high-res sculpt. | Clean low or mid poly mesh. | Geometry validation, manifold check, loop density audit, pole placement review, face-loop coverage, triangle hot-spot report. | Are loops placed for motion, not merely for even quads? | citeturn7view0turn30search1turn31search0turn9search11turn9search8 |
| UVs and baking | Create stable texture space and transfer sculpt detail correctly. | Final game mesh, high-res source, material breakdown. | UV sets and baked normal/AO/curvature or equivalent utility maps. | UV overlap and padding check; missing-UV report; cage and skew audit; bake artifact pass. | Are seams hidden intelligently, islands padded for mipmaps, and bakes clean in deformation-heavy zones? | citeturn11search0turn7view0turn11search12 |
| Texturing and materials | Convert form and material story into engine-ready surfaces. | UVs, bakes, material IDs, style rules. | Texture sets and material instances. | Channel packing validation; roughness or metalness legality check; missing map report; naming and size audit. | Do materials stay readable under target engine lighting and match the style family? | citeturn0search5turn8search9 |
| Rigging and skinning | Make the asset deform predictably for gameplay and cinematics. | Game mesh, skeleton spec, facial/morph spec. | Rigged mesh, weights, corrective shapes, facial targets as needed. | Bone naming validation; joint-placement report; max influences per vertex; unweighted verts; morph target presence. | Do shoulders, elbows, knees, hips, neck, jaw, eyelids, lips, and twist zones survive motion? | citeturn16search7turn16search1turn15search11turn10search1turn10search12 |
| Deformation testing | Break the rig on purpose before animation does. | Rigged character and test-pose library. | Deformation report and corrective list. | Automated pose battery: extreme shoulder raise, elbow flexion, wrist pronation, deep squat, hip abduction, neck twist, phoneme and blink set. | Are failures localized and correctable, or do they reveal topology or joint-placement defects? | citeturn16search12turn16search1turn15search17 |
| Optimization and LODs | Hit performance targets without destroying character identity. | Approved LOD0, platform budgets, skeleton spec. | LOD chain, reduced materials where needed, export package. | Polycount report, draw-call and material-slot count, same-skeleton requirement for LODs, naming check. | Do lower LODs preserve primary silhouette and facial read while meeting platform budgets? | citeturn7view0turn9search1turn10search17 |
| Export and engine validation | Prove the asset survives import, retargeting, lighting, and runtime standards. | `glTF`/`GLB` or approved interchange package, textures, material instances, test animations. | Godot import package plus validation log. | Import pass, missing influence report, skeleton and skin validation, animation import, blend-shape import where relevant, material binding, LOD or scene-variant assignment. | Is the asset actually Godot-ready, or only DCC-ready? | citeturn16search2turn16search7turn10search2turn10search7turn15search12 |

A skeptical but important note: most AI-assisted character systems try to collapse too many of these stages into one pass. That is exactly backwards. The published pipelines that do work are the ones that **separate** concept readability, sculpt logic, topology logic, deformation logic, and engine logic. The AI system should preserve that separation rather than erase it. citeturn7view0turn25search0turn34search10

## Agent architecture and knowledge base

The system should use **multiple skills**, not one massive one. Anthropic explicitly recommends skills for reusable procedures and subagents for specialized workers with their own context windows and tool permissions; OpenAI makes a similar distinction with skills, AGENTS.md, and subagent workflows. That is a strong signal against the monolith. A single giant skill becomes a dumping ground for anatomy notes, topology rules, engine caveats, and review checklists; it bloats context, tangles responsibilities, and makes regressions hard to diagnose. Multiple focused workers are easier to test, version, permission, and replace. citeturn33search0turn33search1turn2search1turn34search2turn34search0turn34search10

My recommended operating model is:

- **Character Director**: owns the stage plan, gate definitions, and handoffs.
- **Reference Librarian**: retrieves anatomy, style, costume, and prior-critiques material.
- **Anatomy Reviewer**: critiques proportions, landmarks, asymmetry, and surface logic.
- **Style Keeper**: enforces style-family rules and silhouette consistency.
- **Topology Assistant**: reviews loops, poles, density, and bake readiness.
- **Rigging Assistant**: reviews joint placement, influences, correctives, and pose tests.
- **Engine Export Assistant**: owns Godot import sanity.
- **Asset QA Auditor**: aggregates validator outputs into a weighted score.

That split mirrors how both Claude and Codex now support delegated and specialized workflows, and it fits the reality of character production better than “one omniscient skill.” citeturn33search5turn34search0turn34search4

A practical division of responsibility looks like this:

| Option | Advantages | Failure mode |
|---|---|---|
| One massive skill | Simpler initial setup; fewer files; easier for a single hobby workflow. | Context sprawl, instruction conflicts, brittle updates, harder debugging, weak permission boundaries. |
| Multiple skills without a director | Better specialization and lower context cost. | Fragmented decisions; inconsistent stage transitions; no single owner for gate logic. |
| Director plus specialist skills | Best balance of specialization, bounded context, and production control. | More setup work up front, but far easier to maintain and scale. |

The knowledge base should also be **a system, not a document**. Anthropic’s docs distinguish between always-on project memory and skills that load only when relevant; OpenAI’s docs position AGENTS.md as durable repository guidance and file search or retrieval as the mechanism for semantic access to larger knowledge stores. The right pattern is therefore: put **stable production law** in always-on repo instructions, put **task procedures** in skills, and put **large domain libraries** in searchable documents. Retrieval-augmented generation helps, but only when it retrieves the right kind of thing. The original RAG paper and current platform retrieval docs both describe retrieval as a way to ground generation in non-parametric memory. For this project, that means RAG is excellent for anatomy references, prior critiques, style exemplars, and engine caveat docs; it is **not** the right place for your non-negotiable pipeline rules, because those must be present without retrieval failure. citeturn33search0turn33search1turn33search12turn3search14turn23search18turn23search1turn23search16turn23search5

The metadata schema should be boring, explicit, and machine-usable. At a minimum, every reference or guide should carry: `domain`, `body_region`, `species`, `sex_or_body_type`, `age_band`, `style_family`, `deformation_criticality`, `target_engine`, `target_platform`, `source_quality`, `last_reviewed`, and `linked_docs`. Cross-references should be many-to-many, not tree-only: a mouth-loop guide should link to topology, phoneme deformation, facial-expression resources, and engine morph-target notes. That is what prevents the AI from “knowing the mouth” in one file and forgetting that the mouth is also a rigging and export problem. citeturn15search11turn15search12turn16search7turn23search16

A repository layout that matches those goals would look like this:

```text
game-character-system/
├── AGENTS.md
├── CLAUDE.md
├── skills/
│   ├── character-director/
│   ├── anatomy-review/
│   ├── style-keeper/
│   ├── topology-review/
│   ├── rigging-review/
│   ├── engine-export/
│   └── qa-audit/
├── prompts/
│   ├── new-character/
│   ├── revision/
│   ├── topology-fix/
│   ├── rigging-fix/
│   └── cleanup/
├── knowledge/
│   ├── anatomy/
│   ├── style-library/
│   ├── topology/
│   ├── rigging/
│   ├── materials/
│   ├── engine-standards/
│   ├── critique-patterns/
│   └── examples/
├── workflows/
│   ├── stylized-biped/
│   ├── realistic-biped/
│   ├── creature-biped/
│   └── quadruped/
├── blender_scripts/
├── validators/
├── engine/
│   └── godot/
├── templates/
└── docs/
```

The prompt strategy should follow the same logic. Anthropic’s and OpenAI’s current guidance both favor explicit structure, reusable instructions, and agentic subdivision over vague “do everything” prompting. So every stage prompt should be a **task card** with the same schema: `goal`, `current stage`, `allowed tools`, `known constraints`, `input refs`, `output contract`, `acceptance tests`, `stop conditions`, `handoff format`. That forces iterative refinement by design. A topology-fix prompt should never ask for materials advice. A style-transfer prompt should never silently re-sculpt joint volumes. A rigging-fix prompt should return deformations, joints, weights, and corrective recommendations, not a fresh design pass. citeturn33search7turn3search11turn34search10turn34search2

## Anatomy, construction, style, and topology standards

For anatomy research, the best public resource stack is not one source but a layered combination of **studio-facing anatomy teaching**, **artist-focused construction references**, and **animal or comparative anatomy**. Scott Eaton’s Anatomy for Artists courses are explicitly aimed at digital artists in games, VFX, and animation, including a portrait and facial-anatomy track that breaks the head into skull, landmarks, musculature, fat pads, and expression mechanics. Anatomy for Sculptors publishes resources that focus on the human figure, facial expression, and head-and-neck form through color-coded 3D and live-model references. Proko’s anatomy curriculum is still one of the better structured artist-learning paths for bones and muscles. For quadrupeds and creatures, Eliot Goldfinger’s *Animal Anatomy for Artists* and Gnomon’s animal-anatomy training are the strongest public complements. For hands, feet, folds, and construction simplification, the Morpho series is especially useful. citeturn17search8turn32search1turn19search14turn19search9turn17search2turn18search2turn18search12turn19search16turn19search13

That layered stack suggests a clean rule for the framework: **construction guides should be authored as reusable “build grammars,” not as static notes.** The AI should learn, for each body region, what gets established first, what usually goes wrong, what the style knobs are, and what the downstream topology and deformation consequences are. A compact but production-usable guide looks like this:

| Region | Construction order | Common mistakes | Stylized shifts | Topology and deformation notes | Evaluation checklist |
|---|---|---|---|---|---|
| Head | Cranial mass → jaw wedge → brow ridge/cheek plane → eye sockets → muzzle or mouth cylinder → nose cartilage block → ear placement. | Eye sockets too shallow, jaw too small, facial planes over-smoothed, ear height drift. | Realistic styles keep plane transitions and fat pads; anime compresses nasal and lip structure; Blizzard-like and League-like styles exaggerate primary read while keeping eye and mouth function. | Orbital loop first, oral loop second, then nasolabial bridge; preserve eyelid thickness and lip roll; facial rig needs clean blink and lip closure paths. | Front, side, 3/4 likeness; plane clarity; eye closure; lip seal; jaw rotation; ear alignment. |
| Neck | Cylinder is not enough: build throat column, SCM paths, trapezius wedge, clavicle relationship. | Neck peg effect, no sternum-to-neck transition, overthick stylization that kills head turn. | Stylized characters may thicken the neck, but head support and clavicle relation still have to read. | Neck loops must support twist and compression; keep density where the jaw, clavicles, and traps meet. | Natural head support, sternocleidomastoid read, clean neck twist, no collar collapse. |
| Torso | Ribcage egg → pelvis block → abdominal bridge → scapular plane → pectoral and lat masses. | “Ab pack” thinking without ribcage and pelvis structure; too straight side profile. | Stylized bodies often widen ribcage or narrow pelvis, but ribcage and pelvis still need distinct masses. | Shoulder and spine deformation begin here; preserve scapula and armpit loop logic. | Ribcage-pelvis relation, center of mass, side profile rhythm, armpit construction. |
| Arms | Deltoid cap → upper-arm cylinder split by biceps/triceps logic → forearm wedge and twist groups. | Tube arms, missing brachioradialis/ulna rhythm, elbow placed too low or high. | Heroic styles enlarge deltoid, forearm, and hand rhythm; cartoony styles simplify tendon breakup. | Elbow loops should follow bend axis; forearm twist needs either twist bones or corrective logic. | Elbow flexion, pronation-supination read, silhouette from side, wrist taper. |
| Hands | Palm block → finger fan → thumb saddle → proximal-to-distal finger segmentation. | Tiny palms, identical fingers, thumb attached like extra finger, no metacarpal fan. | Stylized hands can enlarge palm or fingertips, but thumb opposition mechanics cannot disappear. | Finger loops must support curl and spread; thumb base needs its own topology logic. | Open hand, fist, pinch, point, grasp all read cleanly. |
| Pelvis | Iliac crest block → sacrum and glute mass → femur insertion landmarks. | Flat pelvis, no ASIS landmarks, glutes treated as spheres, hip joint ambiguity. | Stylization can push width and tilt, but pelvis still anchors legs and spine. | Hip loops matter for crouch, kick, and spread; keep density around groin and glute fold. | Crouch and leg raise hold; pelvis tilt reads; groin does not tear. |
| Legs | Upper-leg cylinders with adductor and quad logic → knee block → lower-leg wedge with tibia and calf rhythm. | Symmetrical legs, knees as bumps, no tibial plane, calf placement wrong from side view. | Stylized legs often simplify knee and ankle detail but exaggerate silhouette taper. | Knee loops align to bend axis; ankle and calf density should support walk-cycle compression. | Deep knee bend, side silhouette, ankle taper, planted-foot stability. |
| Feet | Heel block → arch wedge → forefoot fan → toe grouping. | Slipper feet, no arch, ankle merged into foot, toe box unspecified. | Many styles simplify toes, but heel, ball, and arch still drive believable stance. | Foot topology must support dorsiflexion and toe-off if animated. | Standing plant, tiptoe, dorsiflex, shoe fit or barefoot logic. |
| Ears | Helix shell → antihelix → concha bowl → lobe. | Ears pasted on flatly, wrong height, no inner bowl structure. | Stylized ears can sharpen, lengthen, or simplify, especially for elves and goblins. | Usually low deformation, but silhouette-critical. | Height from brow-to-nose band, side silhouette, species read. |
| Mouth and nose | Oral cylinder and lip pillows → philtrum and corners → nasal bridge, ball, wings, septum. | Lips as outlines, no mouth bag logic, nostrils pasted on. | Anime simplifies nose and lip planes; realistic and Arcane-like approaches keep stronger plane hierarchy. | Mouth loops are non-negotiable for phonemes; nose can be lighter unless facial closeups matter. | Closed-mouth neutral, smile, frown, O and F/V shapes, nostril and alar form. |
| Eyes | Eyeball first → lids wrapping the globe → canthi and lid thickness → brow support. | Flat lids, almond cutouts, no lower-lid volume, lashes replacing anatomy. | Stylized eyes can grow dramatically, but lids still need to wrap a sphere. | Blink quality depends on concentric loops and lid thickness. | Neutral stare, blink, squint, upward glance, side view. |
| Hair | Hairline and scalp masses → primary clumps → secondary breakup → cards or groom strategy. | Sculpting random strands before mass, helmet hair, no root logic. | Stylized hair exaggerates clump design; realistic hair needs flow and layering. | Cards require directional UV and alpha planning; Godot export needs clear material, alpha, texture, and scene-node conventions. | Primary read, hairline logic, silhouette breakup, head turn readability. |
| Clothing folds | Tension points first, compression second, material thickness third. | Random wrinkles, no gravity logic, same fold language on leather and knit. | Stylized folds reduce frequency and amplify major tension lines. | Cloth topology should align with bend zones and keep enough span for skinning. | Material-specific fold logic, clean silhouettes, deformation under poses. |

The style-library question is where many teams get fuzzy. The rules that remain constant across styles are the **structural rules**: joints still need to bend, landmarks still need to anchor proportion, silhouettes still need to read at gameplay distance, and face loops still need to support expressions. The rules that change are mainly **proportion ratios, plane simplification, feature emphasis, material treatment, and detail frequency**. Riot’s clarity guidance is explicit that silhouette is the most important recognition tool in League; Riot’s VALORANT rendering notes make the same point from the opposite direction, emphasizing depth and readability against the environment. Blizzard’s art-positioning language still emphasizes recognizable silhouettes and strong color. Fortiche and Netflix openly describe Arcane through watercolor-like visuals and high-touch character design. Taken together, those sources point to a useful style taxonomy for the framework: treat style as a controlled set of dials, not as a full replacement of anatomy. citeturn8search6turn8search9turn0search3turn20search3turn22search2turn22search12

A practical style map for the system is:

| Style family | What stays constant | What changes most |
|---|---|---|
| Realistic | Landmark placement, muscle insertions, believable material response, deformation priorities. | Detail density rises; asymmetry increases; secondary fat and material nuance matter more. |
| Semi-realistic | Same skeletal logic and deformation zones. | Cleaner planes, slightly larger features, moderated detail. |
| Overwatch or WoW-like heroic stylization | Landmark and bend logic, strong readability. | Exaggerated silhouettes, chunkier hands or armor, simplified forms, stronger color separation. |
| League or Fortnite-like gameplay stylization | Silhouette primacy and gameplay readability. | More aggressive shape language, larger read-from-distance features, simplified small forms. |
| Valorant-like tactical stylization | Readability, material separation, pose clarity. | Cleaner and tighter features, reduced noise, strong depth separation. |
| Arcane-like painterly stylization | Real head and body construction still matters. | Plane design, painterly texture treatment, selective exaggeration, more illustrative color decisions. |
| Anime | Joint function, skull-to-face attachment, lid-to-eyeball relationship. | Radically simplified noses and mouths, enlarged eyes, shorter lower faces, stylized hair grammar. |
| Disney or Pixar family | Construction, appeal through clear masses, deformation cleanliness. | Strong simplification, softer transitions, large eyes and appealing proportions, expressive surface compression. |
| Low poly or mobile | Core silhouette and rig functionality remain. | Loop count, material count, texture strategy, facial loop density, microdetail removal. |
| Hand-painted | Construction still governs forms. | Normal reliance may drop; painted value breakup and color design carry more form. |

Topology standards should be encoded as **deformation standards first**. Polycount’s long-running topology guidance defines topology as the layout of vertices and edges that creates the surface and directly affects performance and function, while current topology guides keep repeating the same point in plainer language: edge loops should generally align to the axis of animation, especially at elbows, knees, shoulders, and facial loops. Naughty Dog’s published pipeline reinforces that same priority by distinguishing sculpt topology from game-resolution topology and by showing how standardization, fixers, and helper joints mattered once assets had to animate consistently. Blender’s current retopology tools, RetopoFlow, and Quad Remesher are valuable, but Blender’s own docs already hint at the right caution: Quadriflow and other remeshers are tools, not replacements for animation-focused edge flow. Use automatic remesh for exploration, assisted retopo for speed, and manual correction wherever deformation matters. citeturn30search1turn31search0turn7view0turn9search0turn9search11turn9search8

Rigging standards then follow from could-this-actually-bend. For a Godot-targeted workflow, the important engine-side questions are whether the exported character imports as a usable scene, preserves `Skeleton3D` hierarchy and bone names, keeps skin weights intact, brings in animation clips, preserves blend shapes where required, and can run through a preview pose or animation test inside the Godot project. Unreal and Unity examples are still useful as broader production references, but they should not drive the first implementation. So the framework should encode a blunt rule: **if topology cannot survive the pose tests and import cleanly into Godot, it is not finished topology**. citeturn16search7turn15search11turn16search1turn16search12turn10search2turn10search7

## Blender MCP workflow, automation, and QA

Blender automation is powerful enough to be central to this framework, but the MCP layer has to be treated as dangerous infrastructure, not as a toy. The ahujasid `blender-mcp` project exposes Blender control through MCP, Anthropic describes MCP as a standard for connecting AI systems to external tools, and Blender’s own experimental MCP server page explicitly warns that LLM-generated code can execute in Blender without safeguards and can remove data or send it elsewhere. That warning should shape the system design from day one. Run the pipeline in isolated project directories, keep references read-only, separate source assets from generated assets, require approval for destructive operations, and log every tool action. If you skip that, the system may be productive for a week and catastrophic the week after. citeturn1search0turn1search3turn1search4

The right MCP operating loop is therefore **bounded, multimodal, and reversible**. Because Claude and Codex both now support skills, subagents, tool use, and image understanding, the most reliable working pattern is: assign one bounded task, execute a short burst of edits, capture screenshots, run validators, score the result, and either continue or roll back. I would not let the agent “wander” across the body. I would force a single region or single concern per cycle: “adjust clavicle and shoulder blockout,” “repair upper-eyelid loops,” “rename materials and validate origin,” “fix LOD1 material slot count.” That matches current multi-agent guidance much better than an open-ended edit spree. citeturn33search10turn33search11turn34search0turn34search10turn33search15

My recommended cadence is a policy, not a published standard: **take screenshots after any structurally meaningful change, and at minimum after every 3–5 edit actions or one completed microtask**. Each screenshot set should include front, side, back, 3/4, and a gameplay-distance camera, plus a face close-up when facial work is involved. After that, run validators before allowing another modeling pass. That recommendation is an inference from the available agent-tooling and vision capabilities rather than a direct studio rule, but it is the safest way to prevent silent regressions. citeturn33search10turn33search11turn34search0

The automatable Blender tasks are substantial:

| Automation target | What to script | Why it belongs in the framework | Basis |
|---|---|---|---|
| Mesh validation | Run mesh validation and emit geometry warnings. | Catch invalid geometry before export or bake. | citeturn13search13turn13search0 |
| Non-manifold and topology scanning | Use BMesh inspection for manifold state, loose components, and abnormal edge conditions. | Flag export-breaking or bake-breaking geometry early. | citeturn13search12turn13search11 |
| Cleanup ops | Merge by distance, delete loose, remove unused data-blocks under controlled conditions. | Prevent dirty scenes and duplicate geometry from poisoning later stages. | citeturn14search0turn29search8 |
| Normal checks | Detect and optionally repair flipped face normals; generate face-orientation snapshots. | Bad normals wreck shading, bakes, and engine import. | citeturn14search9turn14search7 |
| UV validation | Check for missing UVs, overlaps where disallowed, tiny islands, and insufficient padding. | UV defects often surface too late if unscripted. | citeturn11search0turn12search1 |
| Polycount and density reports | Count verts, faces, tris, material slots, and density by region or LOD. | Makes budgets testable instead of aspirational. | citeturn7view0turn9search1 |
| Naming and origin checks | Enforce object, material, armature, and export naming; verify origins and transforms. | Prevent broken downstream import and inconsistent scene hygiene. | citeturn16search2turn12search8 |
| Pose testing | Apply a pose battery and render problem zones. | Turns rigging quality into an observable test. | citeturn16search12turn16search1 |
| Turntables and screenshots | Use Blender render operators or viewport rendering to generate review imagery. | Makes every stage reviewable by the model and by humans. | citeturn28search0turn28search13 |
| Scene cleanup and batch execution | Run Blender as a Python-capable pipeline tool, not only a GUI app. | Enables repeatable CI-style checks and batch audits. | citeturn29search15turn29search3 |

The automated character audit should produce both a score and a diagnosis. A weighted rubric that matches your goals could look like this:

| Category | Weight | What the score should represent |
|---|---:|---|
| Proportions and landmarks | 15 | Skeletal plausibility, age or species fit, center of mass, major landmark placement. |
| Silhouette and readability | 10 | Recognition at distance, camera readability, pose clarity, negative-space strength. |
| Anatomy or structural logic | 15 | Primary and secondary forms, believable attachments, facial construction, creature logic where applicable. |
| Symmetry and intentional asymmetry | 5 | Accidental asymmetry caught; intentional asymmetry documented. |
| Topology and edge flow | 15 | Loops for eyes, mouth, shoulders, elbows, knees, hips, neck, fingers, cloth. |
| UVs and baking readiness | 10 | UV legality, seam placement, texel strategy, bake cleanliness. |
| Materials and texture logic | 10 | PBR or stylized consistency, channel validity, material separation, storytelling. |
| Deformation readiness | 10 | Weight distribution, twist zones, correctives, pose-test performance. |
| Performance and LODs | 5 | Budgets, material-slot discipline, LOD chain integrity. |
| Engine readiness | 5 | Godot import success, `Skeleton3D` and skin preservation, blend shapes where required, animation clips, material binding, texture references, naming. |

I would define **85+** as ship candidate, **70–84** as needs targeted revision, and **below 70** as structural rework. More important than the score, though, is the fail-fast rule: any hard failure in topology legality, skinning, import, or deformation blocks progression regardless of total score. citeturn16search7turn10search2turn15search11turn9search1turn23search5

Godot validation should be a first-class step, not an optional export. That means the framework should ship with a **Godot adapter** that does at least three things: validate the exported package before import, validate the imported Godot scene and resources after import, and run a standard preview scene with known lighting and test motions. The default interchange target should be `glTF` or `GLB` from Blender unless the project proves another format is necessary. If the system only says “file exported successfully,” that is not validation. citeturn16search7turn15search11turn9search1turn16search2turn10search1turn10search2turn10search7turn15search12

## Example workflow, repository blueprint, and future expansion

A stylized orc is a good stress test because it forces the framework to combine heroic stylization, creature or hybrid anatomy, costuming, silhouette clarity, and deformation-heavy shoulders and jaws. CD Projekt Red’s character artists talk about telling story through silhouette, garments, and surface treatment; Blizzard’s public language still ties character work to strong silhouettes and recognizable color; Riot’s clarity work says the silhouette stays primary even when skins or style changes are layered on top. That combination makes the orc example a better systems test than a generic “realistic male.” citeturn25search0turn0search3turn8search6

The production path should look like this:

**Idea and brief.** The Character Director converts “stylized orc bruiser” into a brief: role, camera distance, target engine, poly and texture budgets, animation needs, style family, and gameplay priorities. The Style Keeper tags the build as “heroic stylized fantasy,” not “fully realistic,” which changes proportion and detail rules without relaxing topology or deformation rules. citeturn25search0turn8search6

**References.** The Reference Librarian pulls orc and heroic-fantasy silhouette cues, tusk and jaw references, trapezius and neck anatomy, heavy cloth and leather references, and prior approved stylized-fantasy examples. Human and facial anatomy packs still remain in play because a stylized orc is usually a structured exaggeration of the human figure, not an excuse to skip construction. citeturn17search0turn19search14turn32search1turn18search2

**Proportion plan and blockout.** The Anatomy Reviewer and Style Keeper agree on the proportions before sculpt detail begins: broader ribcage, heavier jaw, thicker neck, longer forearms or enlarged hands if the style wants it, but stable landmarks and a readable center of mass. The first gate is silhouette only. If the orc does not read at thumbnail distance, nothing else matters. citeturn8search6turn8search9turn25search0

**Primary and secondary sculpt.** The Sculpt Assistant builds skull, ribcage, pelvis, shoulder girdle, limb masses, tusk base, and hand blocks. Only after that does it resolve muscle, fat, and surface logic. The gate here is “does this still feel like a structured body under the exaggeration?” The system should explicitly reject the common AI failure mode of piling skin pores and armor scratches onto a body whose clavicles and knees do not make sense. citeturn17search0turn17search2turn19search9

**Clothing and gear.** The costume pass adds shoulder armor, straps, bracers, belt kit, and a simplified hair or topknot solution. Everything gets material IDs early, because Diablo IV’s public production notes make clear that material tagging and detail layering are part of the character system, not just painterly decoration. The gear must not destroy shoulder deformation lanes or neck rotation. citeturn0search5turn25search0

**Topology.** The Topology Assistant creates a clean game mesh with strong shoulder, elbow, hip, jaw, eyelid, and mouth loops. The jaw and tusk area need special care because stylized mouths often look fine in stills and fail immediately once phonemes or aggressive expressions are tested. Auto-remeshing may be acceptable for a first pass, but final facial and shoulder loops should be manually corrected. citeturn30search1turn31search0turn9search8turn9search11

**UVs, baking, and materials.** The system unwraps with hidden seams, validates padding, bakes the utility maps, and pushes materials toward the intended fantasy style. The review gate is not “pretty textures”; it is “material families are legible under default engine lighting and from gameplay distance.” citeturn11search0turn0search5turn8search9

**Rigging and deformation.** The Rigging Assistant binds to the project skeleton, applies shoulder, neck, jaw, and wrist tests, and adds corrective strategies where needed. For Godot, the export gate should verify that the skeleton hierarchy, skin weights, animation clips, and blend shapes where relevant survive the Blender-to-Godot path. This is where the orc either becomes a production asset or gets sent backward. citeturn16search7turn16search1turn15search11turn10search1turn10search2

**QA and engine handoff.** The Asset QA Auditor runs the rubric, reports a weighted score, and blocks handoff on any hard failures. The Engine Export Assistant then imports into Godot, verifies scene structure, skeleton and skin data, material slots, texture references, animation clips, blend shapes where relevant, LOD or scene-variant policy, and preview-scene rendering. Only after the Godot pass succeeds should the asset be treated as “done.” citeturn9search1turn16search2turn10search7turn15search12

The framework is also positioned well for future expansion, but only if it stays adapter-driven. Anthropic’s MCP framing and OpenAI’s MCP and multi-agent workflow docs are useful here because they push toward standardized external-tool connections instead of hardcoding one monolithic behavior. That means the same architecture can later add specialized adapters for NPC batching, modular armor assembly, concept ingestion, scan cleanup, Unreal, Unity, MetaHuman-style workflows, or downstream DCCs. Those should remain extensions. The first production target should stay Godot so the export and validation rules can be tested deeply instead of spread thinly across multiple engines. citeturn1search3turn34search4turn0search14turn1search18

The safest way to think about future tools such as Marvelous Designer, Substance Painter, Houdini, photogrammetry cleanup, or modular armor is not “replace the pipeline,” but “plug into the same pipeline contracts.” Each new tool should register the same things the current Blender-centered system already demands: clear stage ownership, imported and exported data contracts, validator hooks, artifact screenshots, and human approval gates. If you preserve those contracts, the framework can grow; if you tie correctness to one giant prompt, it will collapse the moment the workflow gets broader than a single character sculpt. citeturn33search8turn33search11turn34search2turn34search4

The bottom line is blunt. If the goal is consistency, the framework should encode **pipeline law** more aggressively than it encodes “creative prompting.” Public studio material keeps pointing to the same truth: high-end character work is the accumulation of many disciplined passes, each with its own failure modes. So the right deliverable is a **director-led, validator-backed, knowledge-grounded, stage-gated character pipeline framework** that uses Claude or Codex as bounded specialists inside a production system, not as magical one-shot artists. citeturn7view0turn25search0turn33search0turn34search2
