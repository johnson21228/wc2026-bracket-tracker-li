# Clean MVC Single Site Runtime

The WC2026 bracket tracker has one deployable site: `site/index.html`.

`site/js/app.js` is the startup file. It wires Model, View, and Controller modules. It should stay small.

The clean runtime uses:

- `site/js/mvc/model.js` for data loading, pick state, slot eligibility, feeder dependencies, validation, and downstream clearing;
- `site/js/mvc/view.js` for DOM creation and rendering;
- `site/js/mvc/controller.js` for user-action routing.

Old board/runtime files may remain in the repo, but they are source material only unless deliberately imported into `app.js` after being assigned a clean MVC role.

## Geometry

The board-native coordinate system is 1536×1024 pixels with top-left origin. Slot rectangles from `site/data/geometry/gameboard_manifest.json` become absolute-positioned buttons in that same coordinate plane.

## Knockout pickability

Later-round slots are not always active. They become pickable only when their immediate feeder slots are non-empty. Their choices are the teams currently selected in those feeder slots.

## Downstream clearing

A pick is valid only if it is one of the current choices for its slot. After any pick change, the Model checks R16, QF, SF, and the center Final Four/champion card in order and clears any pick that is no longer valid.
