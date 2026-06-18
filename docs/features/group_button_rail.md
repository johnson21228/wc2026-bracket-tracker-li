# Gameboard Group Button Rail

This feature adds a bottom gameboard rail of group tile buttons.

Each tile represents one full World Cup group. It shows the group label above a 2×2 square grid of the four flags in that group. The tile is an inspection entry point, not a pick control.

## User behavior

- The rail shows Group A through Group L in order.
- All group tiles are centered and spread along the bottom of the gameboard.
- Clicking a tile opens the same group panel used by pick-menu group labels.
- Clicking a tile does not select a team, clear a pick, or change bracket advancement.
- Flags inside a tile are visual evidence only; the entire tile is one button.

## MVC boundary

Model:

- Provides `getGroupRail()`.
- Returns group IDs, labels, four teams, flags, team names, and an accessible label.

View:

- Provides `renderGroupRail()`.
- Renders one button per group.
- Renders the group label above a 2×2 square flag grid.
- Keeps the rail along the bottom of the gameboard.

Controller:

- Routes group tile activation through the same `onGroupPanelOpen(groupId)` path used by pick-menu group labels.

## Data boundary

The rail uses local checked-in group/team data already loaded by the site. It does not scrape ESPN or any external site at runtime.

## Visual emphasis and anchored panel refinement

The bottom group rail should be subtle at rest. Each group tile uses a partially translucent treatment so it stays present without competing with the bracket board. On hover, focus, touch, or tracking-over interaction, the tile becomes fully opaque.

The group panel opens over or immediately above the launching group control when space permits. This applies to both bottom rail group tiles and pick-menu group labels. The panel is board-attached and is clamped inside the visible gameboard viewport when possible. If there is not enough height, the panel can scroll internally while remaining part of the scrollable board plane.
