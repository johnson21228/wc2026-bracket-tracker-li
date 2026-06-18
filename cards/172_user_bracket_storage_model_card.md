# Card 172 — User bracket storage model

## Intent

Define a storage-ready WC2026 data model for multiple users filling out bracket picks.

## Model

- Team records use uppercase three-letter codes as canonical IDs.
- User records identify people filling out brackets.
- Bracket slot records define every durable site pick identifier.
- User bracket records store every pick by site pick identifier.
- Unpicked is explicit and valid: `{ "kind": "unpicked" }`.
- FIFA R32 bracket order is represented by a mapping layer, not by changing storage keys.

## Storage decision

The static site starts with a browser `localStorage` adapter. SQLite is reserved for the later server/API storage adapter when the game needs real shared persistence.

## Acceptance

- `site/data/model/teams.json` exists.
- `site/data/model/users.json` exists.
- `site/data/model/bracket_slots.json` exists.
- `site/data/model/fifa_r32_slot_map.json` exists.
- `site/data/model/user_brackets_seed.json` exists.
- JS model modules exist for Team, PickValue, UserBracket, and storage adapter boundary.
- `make verify` and `make pack` pass.
