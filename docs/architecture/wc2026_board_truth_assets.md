# WC2026 board truth assets

The clean WC2026 site owns board truth resources under `site/assets/board-truth/`.

## Background truth

| Role | Path |
| --- | --- |
| Promoted pub background | `site/assets/board-truth/backgrounds/pub_background.jpeg` |
| Legacy-discovered source | `site/assets/playfield/game1_pub_options_background.jpeg` |

The promoted pub background is currently expected to match the discovered source byte-for-byte.

## Gameboard SVG truth

| Role | Path |
| --- | --- |
| SVG definition | `site/assets/playfield/uniform_pick_card_gameboard.svg` |

The SVG can later be promoted into `site/assets/board-truth/` as a separate captured change. For this card, only the pub background is promoted.

## Render checkpoint

`site/new/` renders the pub background layer from the promoted board-truth path.

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
