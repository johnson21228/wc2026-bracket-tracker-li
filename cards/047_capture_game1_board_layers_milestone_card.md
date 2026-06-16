# Card 047 — Capture Game 1 Board Layers Milestone

## Intent
Capture the Game 1 Round-of-32 board as a milestone now that the visual layer model and chooser behavior are understood.

## Milestone
Game 1 now has a clarified layered architecture:

1. Pub/background atmosphere layer.
2. Transparent bracket geometry PNG layer.
3. Explicit DOM hit-target layer with visible opaque pick slots.
4. Modal chooser filtered to only the group or groups named by the selected slot rule.

## Governance
The bracket geometry image is visual only. It must not carry interaction state, slot numbers, team choices, or hit testing. Hit testing and pick state belong to the DOM/runtime layer.

## Acceptance
- `site/game1/index.html` references `r32_bracket_geometry_overlay.png`.
- Game 1 has an explicit hit layer.
- The browser creates 32 clickable slot targets.
- The chooser menu is filtered by the selected slot rule.
- Duplicate top-level JavaScript state declarations are not present.
