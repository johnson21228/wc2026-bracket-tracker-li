# Game 2 Bracket Geometry Slots Rule

Game 2 MUST render bracket items into named bracket slots.

At the current stage, the shared middle-layer PNG is the geometry-defining visual source. The slot JSON is a captured representation of that image. Game 2 logic MUST use the captured slot data for placement rather than freehand or near-board item positioning.

Future geometry work may invert authority so the slot data becomes truth geometry and generates the PNG/SVG. Until that migration is completed, the JSON must be treated as measured-from-image geometry and preserved with the image asset.
