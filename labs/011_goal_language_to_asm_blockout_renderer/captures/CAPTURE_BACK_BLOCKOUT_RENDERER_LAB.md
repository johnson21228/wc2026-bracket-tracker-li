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
