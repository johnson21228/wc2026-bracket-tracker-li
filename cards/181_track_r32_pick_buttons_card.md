# Card 181 — Track R32 pick buttons and show pre-select highlighting

## Intent

Make Game 1 R32 pickability observable before a user clicks.

The site should track which R32 pick button the user is hovering/focusing/clicking and render an obvious pre-select highlight on the button itself.

## Behavior

- Every rendered R32 pick slot button exposes pickability metadata.
- Pickable buttons get a visible pre-selectable state.
- Hover/focus gives a stronger pre-select highlight.
- Click marks the active slot and opens the controller-governed menu.
- The layer exposes tracking data for the developer console and browser inspection.

## Boundary

This does not change pick legality. `Game1R32PickController` remains the authority for menu availability, candidates, validation, duplicate prevention, and persistence.
