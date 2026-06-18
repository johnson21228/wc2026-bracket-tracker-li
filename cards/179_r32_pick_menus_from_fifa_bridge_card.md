# Card 179 — Drive R32 pick menus from FIFA bridge map

## Intent

Make Game 1 playable R32 slot menus follow the FIFA-shaped slot arrangement captured in Card 178.

## Behavior

Before FIFA locks the Round of 32:

```text
1X slot:
  all teams from Group X are valid menu choices

2X slot:
  all teams from Group X are valid menu choices

3 ABCDF slot:
  all teams from Groups A/B/C/D/F are valid menu choices
```

## Enablement

A menu is enabled only when:

- Game 1 is in `GROUP_STAGE_OPEN` or `R32_PROJECTION_LIVE`, or lifecycle data is unavailable.
- The slot has at least one candidate team.
- The slot has a valid FIFA logic entry and board geometry slot.

## Storage

Picks are stored locally under:

```text
wc2026.game1.r32ProjectionPicks.v1
```

This storage is intentionally simple and local for the first playable surface. It can be routed into the repository/store model later.

## Acceptance

- `site/js/board/R32PickMenuLayer.js` exists.
- `BoardShell` appends the R32 pick menu layer.
- R32 slot menus are generated from `fifa_r32_logical_slot_order.json`.
- Geometry is resolved through `game1_fifa_slot_geometry_map.json`.
- Choices come from group/team data.
- `make verify` and `make pack` pass.
