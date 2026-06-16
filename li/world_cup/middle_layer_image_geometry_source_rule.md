# Middle Layer Image Geometry Source Rule

## Status
Accepted LI rule for the current WC2026 bracket tracker stage.

## Rule
For the current Game 1 and Game 2 board architecture, the shared middle-layer bracket PNG is geometry-defining.

The image is not merely decorative. It defines the current visible bracket geometry that runtime slot data must align to:

- the visible bracket slot locations
- the visible bracket slot sizes
- the visible bracket connector paths
- the implied topology from Round of 32 through champion
- the presentation locations where bracket items and hit targets must appear

## Shared middle layer
Both games may use the same middle-layer image asset as the visible geometry reference:

- `site/assets/playfield/r32_bracket_geometry_overlay.png`

Game-specific behavior belongs in the DOM/data/runtime layer above the image, not inside the image itself.

## Current-stage source authority
At this stage:

1. The PNG is the visual source of truth for bracket geometry.
2. Slot geometry JSON is a captured/measured representation of that PNG.
3. Bracket items must be placed by slot geometry data that matches the PNG.
4. Runtime logic must not invent independent slot positions that visually contradict the PNG.

## Future-stage source authority
The intended future architecture is:

1. Truth geometry data becomes the source of truth.
2. The PNG/SVG middle-layer geometry is generated from the truth geometry data.
3. Game 1 hit targets and Game 2 bracket item slots are generated from the same truth geometry data.

## Transition rule
Until generated geometry exists, overlays must be honest about the source direction:

`image-defined geometry -> captured slot data -> runtime placement`

After generated geometry exists, overlays should move to:

`truth geometry data -> generated image/SVG -> runtime placement`

## Preservation requirement
Any Capture Back that changes Game 1 or Game 2 board geometry must state whether it is:

- preserving the shared PNG-defined geometry
- capturing more precise geometry from the PNG
- replacing the PNG with generated geometry
- explicitly deprecating the PNG-defined geometry with user approval

A CB must not silently move bracket items, hit targets, or advancement slots away from the accepted middle-layer geometry.
