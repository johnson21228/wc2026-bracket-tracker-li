# Card 191 — Define and Implement Gameboard Group Button Rail

## Intent

Add Language Infrastructure and first runtime implementation for a persistent group-button rail along the bottom of the gameboard.

## Behavior

- Render one group tile for each group A through L.
- Each tile shows the group label above a 2×2 square grid of the four flags in that group.
- The whole tile is one button.
- Individual flags are not team-pick controls.
- Activating a tile opens the shared group panel for that group.
- The rail does not mutate bracket picks or advancement state.
- The rail is centered and spread along the bottom of the gameboard.

## Runtime boundary

Use local checked-in group/team data only. Do not scrape ESPN at runtime.
