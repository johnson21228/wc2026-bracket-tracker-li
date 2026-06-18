# Capture Back: Clean MVC Single Site

This capture back implements the reset decision for the WC2026 bracket tracker site:

- keep the repo;
- keep one site: `site/index.html`;
- use a new active runtime entry: `site/js/app.js`;
- import clean MVC modules under `site/js/mvc/`;
- preserve existing old runtime files as reference material, not active imports;
- use one 1536×1024 board-native coordinate system;
- render explicit pick buttons from geometry;
- make downstream knockout slots pickable from feeder picks;
- clear invalid downstream picks when upstream picks change.

This is not a second site and not a proof page. It is the active single-site runtime reset.
