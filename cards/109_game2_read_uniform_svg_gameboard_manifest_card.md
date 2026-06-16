# Card 109 — Game 2 Read Uniform SVG Gameboard Manifest

## Intent

Let Game 2 load and validate the uniform SVG gameboard manifest before changing any visible Game 2 geometry.

## Scope

- Add Game 2 read-only manifest load.
- Add Game 2 manifest validation probe.
- Expose probe result on `window.WC2026_GAME2_UNIFORM_SVG_MANIFEST_PROBE`.
- Add board data attributes for review/debug.

## Non-scope

- Do not switch Game 2 board image.
- Do not move Game 2 bracket cards.
- Do not change Game 2 advancement logic.
- Do not change Game 1.

## Verification

Run:

```bash
python3 tools/verify_wc2026_game2_uniform_svg_manifest_read_patch.py
```
