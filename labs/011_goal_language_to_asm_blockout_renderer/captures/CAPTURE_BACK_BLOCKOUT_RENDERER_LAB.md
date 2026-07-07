# Capture Back — Lab 011 Blockout-Style Renderer

## What changed

Seeded Lab 011 for a Workbench-generated C64 projected pit renderer.

## What this proves

```text
renderer_intent.json
  → deterministic projection table
  → deterministic pit line segment table
  → generated ASM data
  → verifier-owned evidence
```

## What this does not prove yet

No runnable PRG yet. The next visual milestone adds C64 bitmap setup and edge drawing.

## Verification

```bash
make -C labs/011_goal_language_to_asm_blockout_renderer verify
```

Expected:

```text
OK: projection table and pit line segment geometry verified.
OK: generated renderer ASM contract verified.
```

## Next move

Draw the generated `pit_line_segments` table onscreen in a C64 emulator.


## Gameboard projection preview

Added an SVG preview generated from the same gameboard definition and pit line segment data:

```text
captures/blockout_gameboard_projection.svg
```

This is not the C64 renderer yet.

It is the first visual proof that the gameboard definition projects into a pit-like board with:

```text
top grid
side/depth rails
z-level projections
```

The next renderer milestone is to make the C64 draw these same line segments.


## Milestone 3 — First runnable PRG

Added a first runnable C64 PRG:

```text
dist/blockout_renderer.prg
```

This first PRG is intentionally crude. It uses a character-screen approximation rather than final bitmap line drawing.

The important Workbench evidence is that the PRG is generated from the same governed line data used by the SVG preview:

```text
renderer_intent.json
  -> pit_line_segments.json
  -> SVG preview
  -> blockout_renderer.prg
```

The PRG therefore shows the governed board, not a separately hand-drawn board.

Next renderer milestone:

```text
replace character-cell approximation with bitmap/pixel line drawing
```


## Projection correction — top-down into the pit

Corrected the Lab 011 gameboard view.

The pit is now rendered as a top-down well:

```text
x/y = visible board opening
z = depth into the well
z guide levels = inset rings
side walls = rails from top perimeter toward deepest ring
```

The SVG preview and the first PRG continue to consume the same generated `pit_line_segments`.

This preserves the Workbench evidence chain while correcting the visual model.


## Perspective projection milestone

Added explicit top-down perspective rings.

The visual model is now:

```text
x/y = visible board opening
z = depth into the well
depth_rings = governed perspective/inset table
```

The SVG and PRG are regenerated from the same governed projection data.

This gets the view right before adding polygon/cube rendering.


## Single cube shaded polygon proof

Added a proof artifact for one cube in the perspective pit:

```text
captures/blockout_single_cube_polygon_preview.svg
dist/single_cube_polygon_faces.json
```

This confirms that the Workbench projection can produce shaded polygon faces for a cube.

The next C64 milestone is not to invent more math. It is to convert the generated face quads into bitmap spans and draw them on the C64.

