# Accepted Behavior Preservation Contract

This Workbench now treats accepted runtime behavior as durable source material.

## Problem observed

During the Game 1 layered-board work, later overlays replaced or patched `site/game1/index.html` and accidentally dropped prior behavior, including group-filtered tap menus and working hit-target behavior.

The regression occurred because the behavior was known in conversation but not sufficiently represented as a repo-level contract.

## Contract

Once a behavior is accepted by the user, it must be recorded as a behavior contract and future CB overlays must preserve it unless explicitly changed.

## Current accepted WC2026 behaviors

- Game 1 Round-of-32 slots are visible/clickable DOM targets, not baked into the PNG.
- Game 1 slot chooser is filtered by slot rule.
- Game 1 visual board layers are decorative and do not intercept input.
- Game 2 starts from fixed seed truth and progresses bracket picks forward.
- Game 1 picks can be compared against official Game 2 seed truth as tiebreaker metadata.

## Future verification direction

The repo should eventually add a behavior verifier that can check:

- exactly 32 Game 1 hotspot definitions are created;
- `1A` opens a Group A-only chooser;
- third-place slots open only the referenced groups;
- duplicate top-level JavaScript state declarations are rejected;
- Game 2 seed truth remains separate from Game 1 comparison metadata.
