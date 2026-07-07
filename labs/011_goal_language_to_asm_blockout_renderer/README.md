# Lab 011 — Goal Language to ASM: Blockout-Style Polygon Renderer

This lab explores a constrained C64 renderer inspired by classic 3D falling-block pit games.

The goal is not to build a general 3D engine. The goal is to prove a Workbench path:

```text
geometry intent
  → deterministic projection tables
  → generated 6502 assembly
  → verifier-owned evidence
  → runnable C64 visual artifact
```

## Current milestone

This seed creates:

```text
intent JSON
generator
projection table
pit line segment table
renderer ASM contract stub
verifiers
```

It does not yet build a runnable PRG.

## Commands

```bash
make generate
make verify
make build
make run
make clean
```


## Milestone 3 — First runnable PRG

The first runnable PRG uses a character-screen approximation.

It reads the generated `dist/pit_line_segments.json`, maps projected C64 coordinates into 40x25 screen cells, and emits:

```text
dist/blockout_renderer.prg
```

This is intentionally not the final bitmap renderer.

It proves:

```text
governed gameboard definition
  -> generated pit_line_segments
  -> runnable C64 artifact
```


## Top-down pit projection

The board is rendered as a top-down well.

`x` and `y` define the 5x5 board opening. `z` is depth into the pit. Deeper guide levels are inset toward the center.

This corrects the first crude side/oblique view and better matches the intended Blockout-style view.


## Explicit perspective depth rings

The perspective pit is now controlled by explicit ring dimensions in `goal/renderer_intent.json`.

This makes the view inspectable and verifiable before adding cube or polygon rendering.


## Single cube polygon proof

`make polygon-proof` creates a shaded SVG proof of one cube inside the perspective pit.

This confirms the polygon math before C64 bitmap/span rendering.


## Solid red shaded cube faces

The single-cube polygon proof now renders with solid red shaded faces.

Open:

```text
captures/blockout_single_cube_red_shaded_faces.svg
```

