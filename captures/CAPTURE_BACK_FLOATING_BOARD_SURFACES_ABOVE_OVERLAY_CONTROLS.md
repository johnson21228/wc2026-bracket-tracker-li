# Capture Back: Floating board surfaces above overlay controls

## Intent

Make sure pick menus and group panels render in front of fixed overlay controls, including the Supabase login control in the upper right and map controls in the upper left.

## Change

- Added a CSS rule that promotes `.board-scroll` above app overlay controls whenever a pick menu or group panel is open.
- Kept pick menu and group panel z-index values above the promoted host layer.
- Captured the rule as View/CSS-owned LI.

## Boundary

This does not change:
- match data
- group standings
- pick validity
- Supabase auth behavior
- storage or save/load behavior
