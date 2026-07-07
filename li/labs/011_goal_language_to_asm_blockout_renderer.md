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
