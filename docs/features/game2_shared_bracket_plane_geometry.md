# Game 2 Shared Bracket Plane Geometry

This feature repairs the coordinate mismatch between the visible bracket PNG and the logical bracket item placement.

Before this feature, the geometry image and item layer were placed using different insets, so the item coordinate system could not agree with the image coordinate system.

The page now uses a shared `bracketPlane`:

- the PNG geometry layer is inside it
- slot guides are inside it
- bracket items are inside it

All `x`, `y`, `w`, and `h` values in `site/data/game2_bracket_geometry_slots.json` are percentages of the same plane.

This does not claim the slot measurements are final. It establishes the correct coordinate authority so the slots can now be tuned against the PNG honestly.
