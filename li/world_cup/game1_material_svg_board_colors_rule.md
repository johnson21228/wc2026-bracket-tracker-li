# Game 1 Material SVG Board Colors Rule

Game 1 uses the uniform SVG gameboard as a transparent middle-layer board stencil and geometry authority.

The SVG must remain transparent outside bracket strokes, slot outlines, and intentional pick-card slot fills. The bottom image/pub layer must remain visible beneath it.

Game 1 board presentation uses sampled warm material colors:

- pick-card slot fill: `#816A51` sampled from the lighter reference image;
- bracket connector and slot outline stroke: `#542C23` sampled from the darker reference image;
- standard non-R32 slot fill is lower opacity so the bracket reads as a full board without hiding the bottom layer;
- R32 selectable target fill is stronger opacity so Game 1 users can see which slots are selectable;
- selected pick cards render above the SVG and may use their own fill/flag/abbreviation styling.

The SVG is still the geometry truth. The manifest is still the app-readable projection. Color and fill classes are presentation annotations on the same geometry, not separate geometry sources.

Game 2 is not migrated by this rule.
