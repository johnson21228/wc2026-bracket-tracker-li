# Unified Game 1 to Game 2 Bracket Lifecycle

This document captures a possible product direction for the WC2026 bracket tracker.

## Core idea
Game 1 can grow from a Round of 32 prediction game into the long-lived bracket workspace. Game 2 does not necessarily need to be a separate visual board. It may become a later phase of the same bracket board.

## Lifecycle

### Phase 1 — Pre-official Round of 32 prediction
Players assign predicted qualifiers to Round of 32 slots. This is the original Game 1 behavior.

### Phase 2 — Conditional knockout picking
When both teams for a bracket match are known in the player prediction layer, the app may allow the player to pick a winner for that match. These picks are still provisional if the underlying teams are not yet official.

### Phase 3 — FIFA official Round of 32 announcement
When FIFA announces the official Round of 32, Game 1 can be scored. The app should preserve each player's original predicted R32 slot choices as evidence and compare them to official FIFA truth.

### Phase 4 — Official truth replaces or overlays prediction truth
The official Round of 32 becomes the canonical starting truth for knockout play. The UI can still show the player's original prediction layer, including missed, matched, and still-relevant picks.

### Phase 5 — Knockout bracket continuation
The same manifest-driven bracket board continues servicing winner picks, advancement, and scoring. This is the Game 2 behavior, but it may be a board state rather than a separate visual implementation.

## Product value
A unified lifecycle reduces duplicate geometry and lets the player remain in one board surface from prediction through officialization and knockout play.

## Data distinction
The implementation should keep these concepts separate:

- player predicted R32 slot occupant
- official FIFA R32 slot occupant
- provisional knockout pick
- official-truth knockout pick
- pick viability status
- Game 1 scoring evidence
- Game 2 scoring evidence

## Geometry implication
The uniform SVG gameboard and manifest should remain the shared geometry authority. Any Game 1/Game 2 lifecycle state should map to manifest-defined slots rather than maintaining independent bracket geometry.

## Implementation posture
This is a reference design note only. It should inform future CBs before Game 2 migration proceeds too far as a separate surface.
