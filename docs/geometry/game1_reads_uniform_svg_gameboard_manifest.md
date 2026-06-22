# Game 1 Reads Uniform SVG Gameboard Manifest

This change is a safe migration step. Game 1 learns how to read the new uniform SVG gameboard manifest, but it does not switch the visual gameboard yet.

## What changes

Game 1 now loads a generated local-review shim:

```html
<script src="../data/geometry/uniform_pick_card_gameboard_manifest.js"></script>
```

That shim exposes the manifest JSON as:

```js
window.WC2026_UNIFORM_PICK_CARD_GAMEBOARD_MANIFEST
```

The runtime validates the manifest and records the status on the board element with non-visible data attributes.

## What does not change

Game 1 still uses its existing visible board image. No layer is visually migrated in this card.

The pick-card renderer, tap chooser, R32 card labels, and stored picks are unchanged.

## Why a JavaScript shim exists

The canonical manifest remains:

```text
site/data/geometry/uniform_pick_card_gameboard_manifest.json
```

The generated shim exists so the static `file://` review workflow can read the manifest without relying on browser `fetch()` behavior for local JSON files.

<!-- WC2026_SINGLE_GEOMETRY_TRUTH_START -->
## Single Geometry Truth

WC2026 board geometry has one canonical truth.

The source-truth board geometry artifact is:

- `site/assets/playfield/uniform_pick_card_gameboard.svg`

The app-readable runtime projection is:

- `site/data/geometry/uniform_pick_card_gameboard_manifest.json`

The rendered/review derivative is:

- `site/assets/playfield/uniform_pick_card_gameboard.png`

Canonical rule:

- SVG/source geometry is the source-truth board geometry.
- JSON manifest is a generated/runtime projection of the SVG/source geometry.
- PNG is a rendered derivative for review, fallback, or visual inspection.
- Runtime code may read JSON for convenience, but JSON must not become an independent hand-maintained geometry truth.
- CSS may style rendered surfaces, but CSS must not define canonical slot bounds.
- View/controller/model code must not invent pick-cell geometry that is absent from the source-truth geometry.
- Geometry changes must update the source-truth SVG first, then regenerate or synchronize the JSON projection from that same source.

This prevents SVG, JSON, PNG, CSS, and runtime code from becoming competing geometry authorities.
<!-- WC2026_SINGLE_GEOMETRY_TRUTH_END -->
