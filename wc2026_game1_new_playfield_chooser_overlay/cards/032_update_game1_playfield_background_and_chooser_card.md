# Card 032 — Update Game 1 Playfield Background And Chooser

## Intent

Use the new USA-themed playfield image and add tap/click chooser behavior for each Round-of-32 slot.

## Acceptance

- New image is stored at `assets/playfield/r32_usa_single_frame_playfield.jpeg`.
- `game1_playfield.html` uses the new background.
- R32 cells are hit-testable.
- Tap/click opens a choice list for the relevant group set.
- Player choice writes the flag into the slot.
- Export/import JSON still works.
- New release is created.
