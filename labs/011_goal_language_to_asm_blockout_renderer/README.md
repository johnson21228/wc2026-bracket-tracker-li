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
