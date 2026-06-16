# Card 073 — Restore Game 1 Group Graphic Tap Menu

## Intent

Restore the Game 1 tap menu that lets the user pick teams from a group-oriented chooser.

## Acceptance

- Game 1 uses the shared 32-bit RGBA board PNG.
- Game 1 opens as a scrollable native-size board surface.
- Tapping an R32 slot opens a modal chooser.
- The chooser has visible Group A–L chips.
- Team choices have compact graphic tiles and group metadata.
- Assignments persist in localStorage.
- Game 2 is not changed.
- `make verify` passes.
