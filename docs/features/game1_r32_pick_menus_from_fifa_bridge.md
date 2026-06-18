# Game 1 R32 pick menus from FIFA bridge

## Overview

Card 179 makes the FIFA arrangement playable.

The board already has:

```text
FIFA logic:
  site/data/model/fifa_r32_logical_slot_order.json

Geometry bridge:
  site/data/geometry/game1_fifa_slot_geometry_map.json

Board geometry:
  site/data/geometry/gameboard_manifest.json
```

This card adds:

```text
site/js/board/R32PickMenuLayer.js
```

## Pre-lock pick rule

For prediction mode, the player is allowed to choose any team that can possibly occupy the slot:

```text
group-winner:
  all teams from that group

group-runner-up:
  all teams from that group

third-place-candidate-set:
  all teams from all listed candidate groups
```

## Lifecycle enablement

Menus are enabled in:

```text
GROUP_STAGE_OPEN
R32_PROJECTION_LIVE
```

If lifecycle data is unavailable, menus fail open for local development.

## Storage

The first implementation stores locally:

```text
wc2026.game1.r32ProjectionPicks.v1
```

Each pick records:

```text
fifaSlotId
fifaLabel
qualifierKind
eligibleGroups
teamId
abbr
name
group
pickedAt
```
