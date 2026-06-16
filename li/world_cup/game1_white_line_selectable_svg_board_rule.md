# Game 1 White-Line Selectable SVG Board Rule

Game 1 uses the uniform SVG gameboard as a transparent middle-layer board stencil, not as an opaque replacement picture.

The SVG must remain the geometry authority for the board coordinate system, pick-card rectangles, and connector linework. The manifest is the app-readable projection of the same geometry. The PNG is only a derived review/fallback artifact.

For Game 1 presentation, the middle SVG board layer must:

- be transparent outside bracket strokes, slot outlines, and intentional target fills;
- render connector linework and all pick-card slot outlines in white/light strokes so the whole bracket remains visible over the bottom image layer;
- preserve all non-R32 bracket slots as visible board structure;
- give R32 selectable pick-card targets an intentional translucent fill so users can see where they may pick teams;
- keep R32 selected pick cards rendered above this SVG layer;
- keep hit targets above the SVG layer and tied to the manifest, not to hand-coded geometry.

The SVG may contain presentation classes such as `slot-r32-selectable`, but those classes are not a second geometry source. They are visual annotations on the SVG geometry source.

Game 2 is not migrated by this rule.
