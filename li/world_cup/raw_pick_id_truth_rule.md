# Raw Pick ID Truth Rule

Raw pick storage must be keyed by durable semantic pick IDs, not by visual board geometry.

## Rule

The raw pick data record is the storage truth. It must contain user/account identity, game identity, status metadata, and a picks object keyed by stable `pickId` values.

```text
pickId is truth.
visual slot is projection.
UI geometry may change.
pickId must not change.
```

## Required separation

- `bracket_slots.json` is a projection/UI geometry authority.
- `sitePickId` values are visual board projection identifiers.
- Raw pick IDs are stable semantic identifiers that survive UI layout changes.
- LocalStorage and future RemoteBracketStore must persist raw pick-state records keyed by `pickId`.
- Projection code may map `pickId -> sitePickId`, but storage must not depend on `boundsPx`, layout coordinates, or board-only display IDs.

## Canonical raw record shape

```json
{
  "schemaVersion": 1,
  "userId": "local-user",
  "tournamentId": "wc2026",
  "gameId": "game1",
  "status": "draft",
  "picks": {
    "game1.r32.slot01": null,
    "game1.final.champion": null,
    "game1.thirdPlace.winner": null
  }
}
```

## Game counts

- Game 1 must initialize 64 stable raw pick IDs.
- Game 2 must initialize 32 stable raw pick IDs.
- Empty picks must be explicit null/unpicked values for every required pick ID.

## Projection constraint

Any visual or runtime projection map must reference existing raw pick IDs. A projection slot may change; a raw pick ID must remain stable.
