# Game 2 Shared Bracket Plane Geometry Rule

Game 2 must use one shared coordinate frame for the middle-layer bracket geometry image, slot guides, and rendered bracket items.

Current stage:
- The shared middle-layer PNG defines visible bracket geometry.
- `site/data/game2_bracket_geometry_slots.json` is a captured representation of that PNG.
- Slot coordinates are expressed as percentages of `.bracketPlane`.

Required runtime structure:

```html
<div class="bracketPlane">
  <div class="geometryLayer"></div>
  <div id="slotGuideLayer"></div>
  <div id="itemLayer"></div>
</div>
```

The geometry layer, slot-guide layer, and item layer must all use `inset: 0` inside `.bracketPlane`.

A Capture Back that changes Game 2 bracket layout must preserve this shared coordinate frame unless it explicitly replaces it with a stronger truth-geometry model.
