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
