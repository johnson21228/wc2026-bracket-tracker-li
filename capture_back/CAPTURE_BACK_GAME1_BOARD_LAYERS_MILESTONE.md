# Capture Back — Game 1 Board Layers Milestone

## Summary
This milestone captures the Game 1 board architecture after the transition from a single opaque board image to a layered game surface.

## Board Layer Contract

- **Back layer:** pub/background image, decorative only.
- **Middle layer:** transparent bracket geometry PNG, decorative only.
- **Top layer:** runtime DOM hit targets, visible and clickable.
- **Chooser layer:** modal team picker filtered by the clicked slot rule.

## Key Decision
Do not bake hit testing, slot numbers, team names, or chooser eligibility into the PNG. The PNG is only a visual bracket overlay. The slot rectangles and click behavior are runtime DOM elements so they can be tuned, debugged, and connected to game state.

## Current Acceptance Target
The Game 1 page should create 32 visible clickable targets and constrain the chooser as follows:

- `1A` shows only Group A teams.
- `2F` shows only Group F teams.
- `3 A/B/C/D/F` shows only teams from Groups A, B, C, D, and F.

## Milestone Note
If the board appears visually correct but the buttons are not visible/clickable, inspect the browser console first. A duplicate top-level `const STORAGE_KEY` declaration prevents all Game 1 JavaScript from parsing.
