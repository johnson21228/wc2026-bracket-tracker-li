# Unified Game 1 to Game 2 Bracket Lifecycle

This document is a historical lifecycle note. It is superseded by the current knockout-only Admin_/official R32 authority model, but remains useful for geometry/lifecycle context.

## Core idea
Game 1 can grow from a Round of 32 prediction game into the long-lived bracket workspace. Game 2 does not necessarily need to be a separate visual board. It may become a later phase of the same bracket board.

## Lifecycle

### Phase 1 — Admin_/official Round of 32 occupant setup
Admin_/official assigns official R32 occupants. Normal players do not assign, project, or predict R32 occupants.

### Phase 2 — Conditional knockout picking
When both teams for a bracket match are known from hydrated Supabase Admin_/official R32 entrants or upstream player-owned winners, the app may allow the player to pick a winner for that match.

### Phase 3 — FIFA official Round of 32 announcement
When Admin_/official has entered official R32 occupants, player BracketDocuments may store those R32 entries as hydrated mirror records for rendering and R16++ preselection. These entries are copied only from Supabase Admin_/official and are not scored as player-authored predictions.

### Phase 4 — Official truth replaces or overlays prediction truth
The Supabase Admin_/official Round of 32 is the canonical starting truth for knockout play. Static JSON, localStorage, and stale player documents must not supply public R32 truth.

### Phase 5 — Knockout bracket continuation
The same manifest-driven bracket board continues servicing winner picks, advancement, and scoring. This is the Game 2 behavior, but it may be a board state rather than a separate visual implementation.

## Product value
A unified lifecycle reduces duplicate geometry and lets the player remain in one board surface from prediction through officialization and knockout play.

## Data distinction
The implementation should keep these concepts separate:

- Admin_/official R32 slot occupant
- player BracketDocument R32 mirror entry with `playerAuthored: false`
- player-owned R32 match-winner pick
- player-owned later-round knockout pick
- Admin_/official later-round official truth, which must not be copied into player documents
- pick viability status
- Game 1 scoring evidence
- Game 2 scoring evidence

## Geometry implication
The uniform SVG gameboard and manifest should remain the shared geometry authority. Any Game 1/Game 2 lifecycle state should map to manifest-defined slots rather than maintaining independent bracket geometry.

## Implementation posture
This is a reference design note only. It should inform future CBs before Game 2 migration proceeds too far as a separate surface.
