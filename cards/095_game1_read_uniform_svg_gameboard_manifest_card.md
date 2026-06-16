# Card 095 — Let Game 1 Read Uniform SVG Gameboard Manifest

## Intent

Let Game 1 consume the uniform SVG gameboard manifest as a non-visible runtime contract probe before switching the visible board layer.

## Scope

- Add a Game 1 LI rule for reading the uniform SVG gameboard manifest.
- Add documentation for the manifest-read-only migration step.
- Generate a JavaScript shim from the JSON manifest for local static review.
- Patch Game 1 to load and validate the manifest.
- Do not switch Game 1's visible board image.
- Do not switch Game 2.

## Acceptance

- `make verify` passes.
- `python3 tools/verify_wc2026_game1_uniform_svg_manifest_read_patch.py` passes.
- Game 1 still references the previous visible board image.
- Game 1 references `uniform_pick_card_gameboard_manifest.js` only as a manifest-read dependency.
