# Card 098 — Game 1 Material SVG Board Colors

## Intent

Tune the uniform SVG middle-layer board so it reads as a warm material gameboard over the bottom image layer while preserving SVG/manifest geometry authority.

## Change

- Regenerate the uniform SVG with transparent background.
- Render bracket connector linework and slot outlines in sampled dark brown `#542C23`.
- Render pick-card slot fills in sampled tan `#816A51`.
- Use stronger fill opacity for R32 selectable Game 1 targets.
- Preserve manifest-derived R32 hit/pick-card placement in Game 1.
- Keep Game 2 unmigrated.

## Acceptance

- Game 1 behavior remains restored.
- Bottom layer remains visible through the SVG.
- Full bracket is visible as warm material linework and slot surfaces.
- Empty R32 targets read as selectable.
- Selected R32 pick cards remain above the board linework.
