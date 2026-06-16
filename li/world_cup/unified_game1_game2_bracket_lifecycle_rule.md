# LI Rule — Unified Game 1 to Game 2 Bracket Lifecycle

Game 1 and Game 2 may be implemented as phases of one long-lived manifest-driven bracket board.

## Rule
The app may treat Game 1 as the pre-official Round of 32 prediction phase and Game 2 as the official-truth knockout continuation phase of the same bracket surface.

## Required distinction
The implementation must preserve the distinction between:

- predicted Round of 32 slot occupants
- official FIFA Round of 32 slot occupants
- provisional knockout picks made from predicted matchups
- knockout picks governed by official FIFA truth
- Game 1 scoring evidence
- Game 2 scoring evidence

## Officialization behavior
When FIFA announces the official Round of 32:

1. Game 1 prediction evidence must remain visible or recoverable.
2. Official FIFA Round of 32 truth must become the canonical starting truth for knockout advancement.
3. Existing player picks may be marked matched, missed, invalidated, provisional, or still viable.
4. The board may continue into knockout-pick play without abandoning the original prediction surface.

## Geometry authority
The uniform SVG gameboard manifest should remain the shared geometry authority. Game 1 and Game 2 lifecycle states must not create independent bracket slot geometry when a manifest slot already exists.

## Non-goal
This rule does not require immediate runtime changes. It preserves a product architecture option for future CB work.
