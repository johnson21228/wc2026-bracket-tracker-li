# Card 180 — Game 1 R32 pick controller

## Intent

Move Game 1 R32 pick rules out of the view layer and into a controller.

The controller is responsible for:

- menu availability
- menu contents
- pick validation
- duplicate-team prevention
- selection persistence back to the Game 1 R32 projection data model

## Controller

```text
site/js/controllers/Game1R32PickController.js
```

## View

```text
site/js/board/R32PickMenuLayer.js
```

The view renders only slot buttons and menus. It asks the controller what can be shown and sends selections back through the controller.

## Rules

```text
1X slot:
  all teams from Group X

2X slot:
  all teams from Group X

3 ABCDF slot:
  all teams from Groups A/B/C/D/F
```

A menu is enabled only while Game 1 is in projection-picking mode:

```text
GROUP_STAGE_OPEN
R32_PROJECTION_LIVE
```

If lifecycle data is absent during local development, the controller fails open so the board can still be tested.

## Persistence

The controller writes picks to:

```text
wc2026.game1.r32ProjectionPicks.v1
```

## Acceptance

- Controller exists.
- R32 pick menu layer imports controller.
- Pick validation is centralized.
- Duplicate teams are blocked across the projected R32 board.
- `make verify` and `make pack` pass.
