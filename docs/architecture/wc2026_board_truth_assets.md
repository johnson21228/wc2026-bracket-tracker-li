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
