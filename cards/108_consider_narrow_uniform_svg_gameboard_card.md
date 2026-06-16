# Card 108 — Consider Narrow Uniform SVG Gameboard

## Status
Reference / possible enhancement.

## Observation
The current uniform SVG gameboard is wider than ideal in Game 1 review. The bracket structure works, and the SVG/manifest geometry authority is now useful, but the board may benefit from a narrower geometry pass.

## Possible enhancement
Create a narrower uniform SVG gameboard variant by changing the SVG geometry model and regenerating the SVG, PNG, and manifest together.

## Important boundary
Do not narrow the board with CSS-only scaling. Board width is a geometry authority concern.

A narrower board should be produced by tuning the generator constants that control:

- pick-card slot width
- round column spacing
- outer margins
- connector gutters
- board viewBox width
- manifest bounds

## Suggested first pass
Keep the existing board model and behavior, but try a conservative narrowing:

- reduce R32 slot width by roughly 15–20%
- reduce R16/QF/SF standard slot width by roughly 10–15%
- keep the Final Four center card centered
- preserve the 61-card board model
- regenerate SVG, PNG, JSON manifest, and JS manifest shim together
- keep Game 1 behavior unchanged except for manifest-driven geometry
- do not migrate Game 2 as part of this exploratory pass

## Acceptance signal
The board still reads as a full bracket, but more of it fits in the available browser width without clipping or excessive horizontal scrolling.
