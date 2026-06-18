# Clean MVC Single Site Runtime Rule

The WC2026 bracket tracker has one site entry point: `site/index.html`.

The active runtime starts at `site/js/app.js`. `app.js` may import modules only when those modules have a declared role: Model, View, Controller, data, or pure utility.

Existing pre-reset site runtime files are source material, not automatically active runtime. Do not import old board/menu/layer patch modules into the clean runtime unless they are deliberately refactored into an MVC-clean role.

Model owns data loading, slot identity, native geometry, R32 eligibility, knockout feeder dependencies, pick state, validation, persistence, and downstream clearing.

View owns rendering and pointer-event surfaces. Visual layers are inert. Only explicit pick buttons and menu controls may receive pointer events.

Controller owns user actions and redraw coordination.

The board coordinate system is 1536×1024 native pixels, top-left origin. All visual layers and hit targets must use that same coordinate system.

A downstream pick may not survive if its feeder path no longer provides that team as a valid choice. Upstream changes must clear invalid downstream picks.
