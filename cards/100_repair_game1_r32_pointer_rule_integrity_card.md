# Card 100 — Repair Game 1 R32 Pointer Rule Integrity

## Intent

Fix an observed Game 1 chooser mismatch where a visible third-place R32 target could open the adjacent `Winner Group I` chooser.

## Rule

The chooser must resolve from the manifest slot under the pointer, not only from a DOM button that may be adjacent or stale after SVG geometry migration.

## Done when

- Game 1 includes a pointer-to-manifest rule resolver.
- R32 hit target clicks and pick-card clicks route through that resolver.
- Debug attributes expose the active chooser slot/rule.
- Verification passes.
