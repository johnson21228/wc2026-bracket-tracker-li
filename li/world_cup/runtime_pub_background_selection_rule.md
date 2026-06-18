# Runtime pub background selection rule

The browser runtime must have one explicit active board background image.

For the current group-stage planning surface, the active board background is:

`site/assets/board/pub_background.jpeg`

The knockout pub/calendar background remains retained as an asset for a later knockout-mode surface, but it must not be the default board background while the group-stage picking and group-panel surface is active.

Runtime references that determine the visible background, including the page preload and MVC view background layer, must agree on the same active asset. Stale helper modules must not imply a different active background unless they are wired into runtime and intentionally selected by mode.

This rule is limited to active background selection. It does not delete historical assets, source images, or LI/docs that describe previous or future backgrounds.
