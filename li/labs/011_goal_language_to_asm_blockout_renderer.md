# Lab 011 — Goal Language to ASM: Blockout-Style Polygon Renderer

## Status

Seed LI.

This lab explores whether Workbench can turn declarative geometric intent into deterministic Commodore 64 6502 assembly that renders a constrained 3D-ish game surface.

The visual inspiration is a historical falling-block 3D pit game style. The lab must not copy protected assets, names, exact screen layouts, sprites, logos, game code, or proprietary implementation details.

## Thesis

Lab 010 proves:

```text
goal language → deterministic 6502 movement behavior
```

Lab 011 tests:

```text
geometry intent → projection tables → generated ASM → visual C64 artifact
```

The target is not a general 3D engine.

The target is a constrained renderer:

```text
fixed 3D grid
fixed camera
fixed projection
table-driven coordinates
wireframe pit
projected cuboids
optional filled convex faces later
precomputed piece orientations later
deterministic ASM output
verifier-owned geometry evidence
```

## Boundary

Workbench owns:

```text
intent
generation
generated ASM
verification
capture
```

The C64 runtime consumes generated tables and routines. It should not silently own high-level geometry.

## First milestones

1. Lab shell.
2. Intent JSON.
3. Generated projection table.
4. Generated pit line segment table.
5. Verifiers.
6. Later: bitmap setup and visible wireframe pit.

## Working mantra

```text
Do not make the C64 think harder than necessary.

Make Workbench precompute the geometry.
Make assembly draw the geometry.
Make the verifier prove the contract.
Make the emulator show the artifact.
```


---

## Projection correction — top-down into the pit

Lab 011 uses a top-down pit view.

The player is looking down into the gameboard, not at the pit from the side.

This means:

```text
x/y define the visible board opening
z represents depth into the well
deeper z levels are drawn as inset rings toward the center
side walls are implied by rails connecting corresponding perimeter points
```

The projection source of truth is still:

```text
labs/011_goal_language_to_asm_blockout_renderer/goal/renderer_intent.json
```

The SVG and the C64 PRG are both derived from the generated `pit_line_segments`.

The current SVG/PRG view is intentionally a top-down wireframe proof, not final Blockout-quality bitmap graphics.


---

## Explicit perspective ring projection

The top-down pit projection is governed by an explicit perspective ring table.

This replaces vague perspective math with inspectable data:

```text
z=0   largest opening ring
z=3   smaller guide ring
z=6   smaller guide ring
z=9   smaller guide ring
z=12  deepest visible guide ring
```

The intent carries ring dimensions directly. The generator interpolates between rings when it needs intermediate z coordinates.

The C64 does not calculate perspective.

Workbench precomputes:

```text
depth_rings
  -> projection_table
  -> pit_line_segments
  -> SVG preview
  -> first PRG character-rendering approximation
```

This is the projection boundary before polygon/cuboid rendering begins.


---

## Single cube polygon proof

Before implementing C64 bitmap/span fill, Lab 011 confirms that a single cube in the perspective pit can be decomposed into shaded polygon faces.

The proof artifact is:

```text
captures/blockout_single_cube_polygon_preview.svg
```

The generated polygon data is:

```text
dist/single_cube_polygon_faces.json
```

This confirms:

```text
cube cell + z depth
  -> projected vertices
  -> face quads
  -> shaded polygon preview
```

The C64 does not yet fill these polygons. The next renderer milestone is to convert these face quads into C64 bitmap spans.


---

## Solid red shaded cube proof

Lab 011 now includes a deliberately visible single-cube proof using solid red shaded faces.

Artifacts:

```text
captures/blockout_single_cube_polygon_preview.svg
captures/blockout_single_cube_red_shaded_faces.svg
dist/single_cube_polygon_faces.json
```

The red cube proof confirms:

```text
perspective pit projection
  -> projected cube vertices
  -> five face quads
  -> solid shaded visual faces
```

This is still an SVG/polygon proof, not final C64 bitmap span fill.


---

## C64-facing cube span generation

Lab 011 now generates horizontal span rows from the solid red cube face quads.

Artifacts:

```text
dist/single_cube_polygon_spans.json
src/generated_single_cube_spans.s
```

This is the bridge from polygon proof to C64 bitmap fill:

```text
projected face quads
  -> horizontal spans
  -> C64 fill rows
```

The C64 should not calculate polygon intersections. Workbench generates the span data; the C64 renderer consumes it.

