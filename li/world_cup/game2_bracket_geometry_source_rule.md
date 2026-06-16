# Game 2 Bracket Geometry Source Rule

## Living intent

Game 2 is a bracket gameboard. The bracket is not merely decoration. Its geometry defines where teams appear, where user choices happen, and how winners advance.

## Current authority posture

At the current stage, the transparent bracket geometry image is the visual source of truth for the bracket layout. The image defines the visible boxes, connector paths, round grouping, and overall board shape.

The matching geometry data model must therefore be treated as a captured representation of the image-defined geometry, not as an invented independent layout.

## Future authority posture

The intended mature architecture is the reverse:

1. bracket geometry data model defines the board;
2. generated SVG/PNG geometry is produced from that data model;
3. runtime bracket items and hit targets are rendered from the same data model;
4. game logic uses the same slot topology for advancement.

Until generation exists, the WB must be honest: the image defines the geometry and the JSON captures it.

## Required notions

A Game 2 bracket geometry contract must distinguish these notions:

- `boardAsset`: the visible bracket geometry image currently in use.
- `coordinateSystem`: the coordinate system used to place items, preferably percentages relative to the board frame.
- `bracketSlot`: a logical/presentational slot on the board.
- `bracketItem`: a team/player pick item placed into a slot.
- `round`: R32, R16, QF, SF, Final, Champion.
- `feedsTo`: the next slot or match node reached by the winner.
- `source`: whether a slot is seeded, user-picked, official-result-derived, or computed by advancement.
- `geometryStatus`: whether the slot geometry is captured-from-image or generated-from-data.

## Rule

Any CB that seeds or renders Game 2 bracket items must render them into bracket slots aligned to the bracket geometry layer. A CB must not replace bracket-slot rendering with an unrelated card list unless it explicitly states that it is only a temporary diagnostic surface.

Any CB that changes the bracket geometry image must either update the matching slot data or explicitly mark the slot data as stale.

Any future generator that creates the geometry image must use the same bracket-slot model consumed by the runtime.
