# Floating board surfaces above overlay controls

The board now treats open pick menus and group panels as the top interactive layer.

When either `.r32-pick-menu-popover`, `.pick-menu-popover`, or `.group-panel-popover` exists inside `.board-scroll`, CSS promotes `.board-scroll` above fixed app overlay controls. This prevents the login control in the upper right, or the map controls in the upper left, from visually covering the pick menu or group panel.

This keeps overlay controls visible during normal play while making the active floating board surface dominant during inspection/picking.
