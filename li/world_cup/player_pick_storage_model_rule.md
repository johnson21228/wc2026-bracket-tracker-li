# Player Pick Storage Model Rule

The WC2026 bracket tracker must separate local draft state from durable submitted player picks.

## Storage layers

1. Browser draft state
   - Lives in `localStorage`.
   - Supports in-progress play, resets, edits, and local testing.
   - Is not authoritative for scoring or multiplayer comparison.

2. Durable player pick record
   - Represents a user's submitted picks for a named game.
   - Must include player identity, game identity, storage schema version, pick set, timestamps, and lock/submission status.
   - Is the future source for multiplayer display, scoring, leaderboards, and Game 2 tiebreaker comparison.

3. Official result / seed data
   - Represents FIFA/live truth.
   - Must not be mutated by user picks.
   - Game 2 bracket truth must come from official/fixed Round-of-32 seed data, while Game 1 picks may be imported only as comparison metadata.

## Game 1

Game 1 stores Round-of-32 qualification-slot predictions keyed by official slot label, such as `1A`, `2F`, or `3 A/B/C/D/F`.

A submitted Game 1 pick record can later be compared against official Round-of-32 seed data. Correct slot/team matches may be rendered in Game 2 and used as a tiebreaker.

## Game 2

Game 2 stores knockout winner picks keyed by bracket node ID. Game 2 seed truth is fixed from demo, Game 1 test import, or official Round-of-32 seed data. Once official data exists, Game 1 picks must not mutate the Game 2 bracket structure.

## Invalidation

Game 2 downstream picks must be cleared when an upstream winner pick changes or is cleared. Durable submitted records should preserve the submitted state; local draft state may be edited before lock/submission.
