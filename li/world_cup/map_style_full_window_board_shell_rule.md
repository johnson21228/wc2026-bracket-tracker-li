# Map-style full-window board shell rule

Bracketeering Hub should present the gameboard as the primary player-facing surface.

The page shell may keep semantic header, identity, rules, clear-pick, stage-selector, zoom, status, and board hooks, but the player-facing layout should behave like a browser map surface:

- the board scroll surface fills the browser viewport
- hero/banner text is not part of normal visible document flow
- controls are lightweight overlay chrome above the board
- status is compact overlay chrome
- rules remain an overlay dialog
- board pan, scroll, zoom, double-click zoom, pick menus, group panels, and pick rendering remain View-owned and unchanged

This is a View/CSS shell rule only. It must not alter pick models, controllers, slot geometry, SVG truth, manifests, lifecycle semantics, scoring data, or storage/Supabase seams.
