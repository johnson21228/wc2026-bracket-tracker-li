# Game 1 Transparent SVG Middle-Layer Rule

The uniform SVG gameboard is a middle presentation layer, not an opaque background replacement.

Required layer order:

1. Bottom background/pub/image layer.
2. Transparent SVG gameboard linework layer.
3. Manifest-driven hit-target layer.
4. Manifest-driven pick-card layer.
5. Menu, tooltip, and chooser layer.

The SVG must be transparent except for connector strokes and pick-card slot outlines. It must not carry proof titles, checkerboard fills, opaque page rectangles, or any decorative background that hides the bottom layer.

For Game 1, the R32 hit targets and rendered R32 pick cards must use the R32 slot bounds from `site/data/geometry/uniform_pick_card_gameboard_manifest.json`. The slot qualification/menu rules may still come from the Game 1 data bundle, but their visual/hit geometry is projected from the uniform SVG manifest.

Game 2 is not migrated by this rule.
