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

