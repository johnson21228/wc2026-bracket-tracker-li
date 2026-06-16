# Capture Back — Player Pick Storage Model

This CB captures the next storage boundary for WC2026 Bracket Tracker.

## Decision

User picks must be stored in a model that can later support real players, submissions, locks, scoring, and Game 2 tiebreaker rendering.

## Rule

- Browser `localStorage` is local draft state.
- Durable player pick records are separate JSON objects with player identity, game identity, status, timestamps, and picks.
- Official/fixed data remains separate from user picks.
- Game 1 picks can be imported into Game 2 only as comparison metadata.
- Correct Game 1 Round-of-32 slot/team matches can become a visible Game 2 tiebreaker.

## Files

- `li/world_cup/player_pick_storage_model_rule.md`
- `docs/data/player_pick_storage_model.md`
- `data/schema/player_pick_record_schema.json`
- `cards/051_capture_player_pick_storage_model_card.md`
