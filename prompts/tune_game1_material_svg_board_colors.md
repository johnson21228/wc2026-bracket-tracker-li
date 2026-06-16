# Prompt — Tune Game 1 Material SVG Board Colors

Use this prompt to continue tuning the Game 1 uniform SVG middle layer.

Preserve these invariants:

- SVG/generator/manifest remains the geometry authority.
- SVG is transparent except for connector strokes, slot outlines, and intentional target fills.
- R32 slots may use stronger translucent fill to signal selectability in Game 1.
- Pick cards and hit targets remain above the SVG layer.
- Game 2 is not migrated unless explicitly requested.

Current sampled palette:

```text
Pick-card fill: #816A51
Bracket linework / outlines: #542C23
```

Tune only presentation values such as stroke color, stroke opacity, fill color, fill opacity, selectable-target emphasis, and hover/active affordance.
