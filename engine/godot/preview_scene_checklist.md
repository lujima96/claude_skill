# Godot Preview Scene Checklist

The preview scene proves the asset works outside Blender.

## Required Scene Setup

- Known camera distance.
- Neutral key/fill lighting.
- Ground plane or origin marker when useful.
- Imported character instance.
- Optional pose or animation player.
- Debug labels or markers kept out of final game scenes.

## Required Checks

- Scene opens without errors.
- Asset scale is correct.
- Materials are visible and assigned.
- Texture references resolve.
- Skeleton is present when expected.
- Test animation or pose plays when expected.
- Blend shapes are available when expected.
- Collision, hitbox, socket, or marker nodes are present when required.
- Screenshot or render evidence exists.

## Blocking Conditions

- Preview scene cannot open.
- Imported character is invisible.
- Required textures are missing.
- Required skeleton is missing.
- Required animation cannot play.
- Required blend shapes are missing.
- Required marker, hitbox, socket, or collision nodes are missing.
