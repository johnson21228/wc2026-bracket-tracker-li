# Card 227 — Normalize runtime to full canonical BracketDocument before Supabase persistence

## Intent

Update the Bracketeering Pages runtime data model before Supabase is applied.

The invariant is:

```text
Runtime model first. Supabase persistence second.
```

## Context

Bracketeering is preparing to use Supabase/Postgres as durable Model persistence, but Supabase must persist the same canonical game document that the Pages runtime already uses.

GitHub Pages owns:

- View behavior;
- Controller behavior;
- runtime game model;
- board rendering;
- pick behavior;
- anonymous localStorage play.

Supabase/Postgres owns durable persistence only.

## Required model

The runtime must use a canonical `BracketDocument` shape before Supabase integration:

```json
{
  "schemaVersion": 1,
  "gameId": "game1",
  "status": "draft",
  "expectedPickCount": 64,
  "updatedAt": "...",
  "picksBySlot": {
    "L-R32-01": {
      "slotId": "L-R32-01",
      "kind": "entrant",
      "round": "R32_ENTRANT",
      "pick": null,
      "source": "empty"
    },
    "CHAMPION": {
      "slotId": "CHAMPION",
      "kind": "winner",
      "round": "CHAMPION",
      "pick": null,
      "source": "empty"
    },
    "THIRD-PLACE-WINNER": {
      "slotId": "THIRD-PLACE-WINNER",
      "kind": "winner",
      "round": "THIRD_PLACE",
      "pick": null,
      "source": "empty"
    }
  }
}
```

## Game counts

Game 1 supports 64 stored picks:

- 32 R32 entrant picks;
- 16 R32 winner picks;
- 8 R16 winner picks;
- 4 QF winner picks;
- 2 SF winner picks;
- 1 champion / final winner pick;
- 1 third-place winner pick.

Game 2 supports 32 stored winner picks when R32 entrants are fixed/given:

- 16 R32 winner picks;
- 8 R16 winner picks;
- 4 QF winner picks;
- 2 SF winner picks;
- 1 champion / final winner pick;
- 1 third-place winner pick.

## Implementation notes

- Add canonical pick-slot metadata to the runtime slot model.
- Preserve existing board geometry slots for rendering.
- Add first-class canonical slots for `CHAMPION` and `THIRD-PLACE-WINNER`.
- Normalize old `{ picks: { ... } }` bracket shapes into `picksBySlot`.
- Keep a temporary compatibility `picks` map for existing render code while the canonical document becomes the storage authority.
- Update localStorage so saved user brackets are canonical `BracketDocument` records.
- Do not add Supabase client code in this card.
- Do not apply Supabase SQL in this card.

## Acceptance

- Pages still owns View, Controller, and runtime model.
- Supabase remains durable persistence only.
- Runtime uses canonical `BracketDocument` before Supabase integration.
- `LocalStorageBracketStore` saves canonical `BracketDocument` records.
- Existing older localStorage shape is migrated or safely tolerated.
- Game 1 runtime model supports 64 total picks.
- Game 2 runtime model supports 32 winner picks when R32 entrants are fixed/given.
- `CHAMPION` is a first-class slot.
- `THIRD-PLACE-WINNER` is a first-class slot.
- Export/storage language includes third-place winner.
- Board pick/delete/render/reload behavior still works.
- Supabase SQL docs describe the same `BracketDocument` shape the runtime uses.
- No Supabase client code is added.
- No Supabase dashboard SQL is applied.
- `make verify` passes.
- `make pack` completes.
