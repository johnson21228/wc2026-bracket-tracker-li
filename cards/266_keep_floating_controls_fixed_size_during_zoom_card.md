# Card 266: Keep floating controls fixed-size during board zoom

## Intent

Preserve map-style browser chrome while the gameboard zooms.

## Problem

Some floating/browser overlay controls can visually scale if they are placed inside or styled like board geometry.

## Rule

Floating controls are viewport chrome, not board geometry.

They must remain fixed-size while board content zooms and pans.

## Controls covered

- zoom + / − controls
- info panel button
- lifecycle/stage selector if visible as browser chrome
- login/auth identity surface
- any fixed map-style overlay controls attached to the browser viewport

## Implementation

- Keep board zoom scoped to `.pixel-native-board-plane`.
- Keep `.board-scale-frame` as the render-size wrapper, not the transform owner.
- Keep browser chrome outside `[data-board-scroll]` / `[data-board-plane]`.
- Add fixed-size CSS isolation for map icon controls and identity/status surfaces.
- Verify fixed controls are not inside the board zoom surface.

## Acceptance

- Floating controls appear same size at 50%, 100%, 125%, and future zoom levels.
- Board content zooms normally.
- Pick slots and geometry remain aligned.
- Pick menus and group panels still appear above bottom controls.
- `make verify` and `make pack` pass.
