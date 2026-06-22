# Floating controls fixed-size during board zoom rule

Browser/player floating controls are viewport chrome, not board geometry.

The board content may zoom and pan, including:

- board image / SVG linework
- pick slots
- bracket geometry
- board-attached menus when intentionally board-relative

The following controls must remain fixed-size in viewport coordinates:

- map zoom + / − controls
- info panel button
- lifecycle/stage selector if visible as browser chrome
- login/auth identity surface
- status/info overlay surfaces
- other fixed map-style browser controls

Implementation rule:

- Board zoom transforms must stay scoped to the board plane.
- Fixed controls must not be descendants of the zoom-transformed board plane.
- Fixed controls must use fixed viewport positioning or an equivalent fixed-control layer.
- Fixed controls must not scale with `--board-render-scale`.
- Pick menus and group panels may remain board-attached, but must continue to render above overlay controls when open.

Acceptance:

At 50%, 100%, 125%, and future larger board zoom levels, floating browser controls should appear the same size while the board content zooms normally.
