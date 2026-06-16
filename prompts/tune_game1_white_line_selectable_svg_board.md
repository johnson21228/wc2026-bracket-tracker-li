# Prompt — Tune Game 1 White-Line Selectable SVG Board

Use this prompt to continue tuning the Game 1 uniform SVG middle layer.

Preserve these invariants:

- SVG/generator/manifest remains the geometry authority.
- SVG is transparent except for connector strokes, slot outlines, and intentional target fills.
- R32 slots may use stronger translucent fill to signal selectability in Game 1.
- Pick cards and hit targets remain above the SVG layer.
- Game 2 is not migrated unless explicitly requested.

Tune only presentation values such as stroke color, stroke opacity, fill opacity, and selectable-target emphasis.
