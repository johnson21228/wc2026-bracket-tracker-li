# Card 037 — Repair Game 1 Hit Testing

## Intent

Repair the Game 1 shared board page so Round-of-32 hotspots reliably open the chooser modal.

## Acceptance

- `game1_playfield.html` is rebuilt as the canonical Game 1 page.
- R32 hotspots are created explicitly at runtime.
- Hotspots sit above the board image with `z-index: 10`.
- Board template has `pointer-events: none`.
- Page displays `32 hotspots active`.
- Clicking/tapping an R32 slot opens the chooser modal.
- Picks save and render back onto the matching slot.
- Release copy is created.
