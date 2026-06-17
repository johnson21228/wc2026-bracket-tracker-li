# Card 168 — Vivid gameboard line controls

## Intent

Make the gameboard SVG outline easier to see over the pub background.

## Change

Add developer controls for:

- Gameboard opacity
- Gameboard line color
- Gameboard line width
- Gameboard glow

## Acceptance

- Gameboard can be made more vivid without changing source SVG authority.
- Controls are developer-only visual diagnostics.
- Board source assets remain unchanged.
- `make verify` and `make pack` pass.
