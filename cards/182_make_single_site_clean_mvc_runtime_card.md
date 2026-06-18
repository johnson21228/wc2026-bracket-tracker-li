# Card 182: Make the single site a clean MVC runtime

## Purpose

Reset the active `site/index.html` runtime to a clean single-site MVC implementation while preserving the repo, source data, geometry assets, and historical files as reference material.

## Boundary

There is one site: `site/index.html`.

The active runtime starts at `site/js/app.js`. Imported modules are part of the one site only when they have a declared role: Model, View, Controller, data, or pure utility.

Existing old runtime files remain in the repo as source material unless explicitly removed later. They are not active if they are not imported by `site/js/app.js`.

## MVC governance

- Model owns tournament state, slot bounds, R32 eligibility choices, knockout feeder relationships, pick validity, storage, and downstream clearing.
- View owns DOM rendering only: board layers, pick buttons, menus, selected teams, and status text.
- Controller owns user actions only: slot click, team choice, clear pick, clear all, redraw request.
- Visual layers must be inert.
- Only declared pick buttons and menu controls may receive pointer events.

## Geometry governance

The board uses one native coordinate plane:

- width: 1536 px
- height: 1024 px
- origin: top-left
- x increases left to right
- y increases top to bottom

Every rendered visual layer and every hit target must use this same board-native coordinate system.

## Pickability governance

- R32 slots are pickable from their FIFA/group eligibility rules.
- R16 slots become pickable when both feeder R32 slots are non-empty.
- QF/R8 slots become pickable when both feeder R16 slots are non-empty.
- SF/R4 slots become pickable when both feeder QF slots are non-empty.
- The center Final Four/champion card becomes pickable when the semifinal/final-four feeder picks are non-empty.

## Cascade invariant

No downstream pick may survive if its feeder path no longer supplies that team as a valid choice. When an upstream pick changes or becomes empty, the Model clears all invalid downstream picks.

## Acceptance

- `site/index.html` remains the only site entry point.
- `site/js/app.js` imports clean MVC modules, not the old board patch runtime.
- The board renders in the 1536×1024 native coordinate plane.
- R32 buttons render from geometry and logical slot data.
- Later-round buttons render from geometry and become pickable only when feeder picks are complete.
- Changing or clearing an upstream pick clears invalid downstream picks.
- `make verify` checks the clean MVC runtime boundary.
