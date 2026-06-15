# Card 033 — Game 1 Modal Chooser Runtime Storage

## Intent

Use the provided playfield image as the background and implement click-to-choose behavior in an external modal/window.

## Acceptance

- `game1_playfield.html` uses `assets/playfield/r32_usa_single_frame_playfield.jpeg`.
- Clicking/tapping an R32 slot opens a chooser modal.
- The chooser is populated from group/flag data and official slot rule.
- Picks are saved in browser runtime storage.
- Picked flags render over the background at the hotspot.
- The chooser allows deleting a pick.
- Export/import JSON remains available.
