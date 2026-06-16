# Card 098 — Game 1 White-Line Selectable SVG Board

## Intent

Make the uniform SVG middle-layer board read as a visible gameboard over the bottom image layer while preserving SVG/manifest geometry authority.

## Change

- Regenerate the uniform SVG with transparent background.
- Render full bracket linework and slot outlines in white/light strokes.
- Add translucent fill to R32 selectable targets.
- Preserve manifest-derived R32 hit/pick-card placement in Game 1.
- Keep Game 2 unmigrated.

## Acceptance

- Game 1 behavior remains back/restored.
- Bottom layer remains visible through the SVG.
- Full bracket is visible as white linework.
- Empty R32 targets read as selectable.
- Selected R32 pick cards remain above the board linework.
