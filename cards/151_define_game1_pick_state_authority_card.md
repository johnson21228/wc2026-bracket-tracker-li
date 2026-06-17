# Card 151 — Define Game 1 Pick State Authority

## Intent
Prevent stale R16/QF/SF/Final/Champion picks from rendering when their feeder picks do not exist.

## Problem
The site has duplicate pick stores from previous overlays. R16/QF/SF render paths may read old values from secondary stores and draw stale highlights or cards.

## Rule
Game 1 pick state has one canonical authority. Compatibility stores may exist, but they must not independently authorize rendering.

## Acceptance
- Empty Game 1 state leaves only R32 pick actions live.
- R16/QF/SF menus are blocked until feeder picks exist.
- Stored downstream picks are ignored or cleared when feeders are missing.
- Menu preselect/highlight cannot come from stale downstream storage.
- Clear picks clears canonical state and compatibility mirrors.
