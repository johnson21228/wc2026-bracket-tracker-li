# CAPTURE BACK: Runtime Single Geometry SVG Truth

## Intent
Ensure the runtime board linework is rendered from the same source-truth SVG used to derive the geometry manifests.

## Problem
The approved final-stack geometry updated `site/assets/playfield/uniform_pick_card_gameboard.svg` and the derived manifests, but runtime linework still fetched the stale `assets/board/gameboard.svg` asset.

## Change
`site/js/services/assetPaths.js` now points `svgGameboardDefinition` at:

```text
assets/playfield/uniform_pick_card_gameboard.svg
```

This aligns runtime linework with the source-truth SVG and prevents the browser-rendered gameboard outline from drifting from the derived geometry manifests.

## Verification
Added `tools/verify_wc2026_runtime_uses_single_geometry_svg_truth.py` and wired it into `make verify`.

The verifier confirms:
- runtime `svgGameboardDefinition` uses the playfield source-truth SVG
- stale `assets/board/gameboard.svg` is not used as runtime linework truth
- `BoardShell` passes the configured SVG truth into `SvgGameboardLayer`
- `SvgGameboardLayer` fetches the configured SVG
- geometry manifests still point to the same playfield SVG authority
