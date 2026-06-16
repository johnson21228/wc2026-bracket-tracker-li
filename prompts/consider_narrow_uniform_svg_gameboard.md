# Prompt — Consider Narrow Uniform SVG Gameboard

Review the current Game 1 uniform SVG board in browser.

If the board is too wide, propose a conservative geometry-only narrowing pass.

Use the SVG/generator/manifest chain as the authority. Do not propose CSS-only scaling as the main solution.

Preserve:

- transparent SVG middle-layer board presentation
- bottom image/background layer visibility
- manifest-driven hit targets
- manifest-driven pick-card placement
- 61-card board model unless a later card explicitly changes it
- Game 1 behavior
- Game 2 unmigrated until separately requested

Suggest exact generator constants to tune and verifier checks that prevent geometry drift.
