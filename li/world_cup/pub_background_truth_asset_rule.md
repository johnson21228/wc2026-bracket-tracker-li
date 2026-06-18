# Pub background truth asset rule

The clean WC2026 site must render the pub background from the board-truth resource structure, not directly from the legacy playfield path.

## Source discovered from legacy archaeology

- `site/assets/playfield/game1_pub_options_background.jpeg`

## Promoted board-truth path

- `site/assets/board-truth/backgrounds/pub_background.jpeg`

The promoted asset must match the discovered source byte-for-byte until an intentional replacement is captured in LI.

## Rendering rule

The clean site background layer must render from:

- `site/assets/board-truth/backgrounds/pub_background.jpeg`

The legacy-discovered source path may remain for compatibility, but it is not the clean site's render authority.
