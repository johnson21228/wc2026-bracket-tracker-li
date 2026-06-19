# WC2026 Canonical Pick-State Storage Model

## Goal

Define the storage model that lets the current local-only Bracketeering Pub site evolve into an invite-ready public-play site with signed-in user storage.

The storage model is intentionally simple: one canonical pick-state JSON document per user per game.

## Two stored game states

Each user has two possible pick-state documents:

| Game | Meaning | Expected slots |
| --- | --- | ---: |
| `game1` | Full group-stage prediction bracket | 64 |
| `game2` | Knockout-round prediction bracket | 32 |

## Pick counts

### Game 1

Game 1 starts before the Round of 32 field is known from the user's prediction. It stores:

- 32 Round-of-32 entrant picks;
- 16 Round-of-32 match winners;
- 8 Round-of-16 match winners;
- 4 quarterfinal match winners;
- 2 semifinal winners/finalists;
- 1 final winner/champion;
- 1 third-place winner.

Total: 64 stored pick slots.

### Game 2

Game 2 starts when the actual Round of 32 field is known. It stores:

- 16 Round-of-32 match winners;
- 8 Round-of-16 match winners;
- 4 quarterfinal match winners;
- 2 semifinal winners/finalists;
- 1 final winner/champion;
- 1 third-place winner.

Total: 32 stored pick slots.

## Empty-document invariant

A new pick state is not sparse.

The app must create a complete empty bracket document first:

- `game1` always has 64 slot records;
- `game2` always has 32 slot records;
- every required slot is present from initialization;
- an unpicked slot has `pick: null` and `source: "empty"`;
- a missing required slot is an error.

This is the key bridge to server-backed play. The server should never need to infer which slots exist.

## Canonical document shape

```json
{
  "schemaVersion": 1,
  "gameId": "game1",
  "status": "draft",
  "expectedPickCount": 64,
  "createdAt": "2026-06-19T00:00:00Z",
  "updatedAt": "2026-06-19T00:00:00Z",
  "picksBySlot": {
    "L-R32-01": {
      "slotId": "L-R32-01",
      "round": "R32_ENTRANT",
      "pick": null,
      "source": "empty"
    },
    "L-R16-01": {
      "slotId": "L-R16-01",
      "round": "R32_WINNER",
      "pick": null,
      "source": "empty"
    },
    "FINAL-LEFT": {
      "slotId": "FINAL-LEFT",
      "round": "SF_WINNER",
      "pick": null,
      "source": "empty"
    },
    "CHAMPION": {
      "slotId": "CHAMPION",
      "round": "CHAMPION",
      "pick": null,
      "source": "empty"
    },
    "THIRD-PLACE-WINNER": {
      "slotId": "THIRD-PLACE-WINNER",
      "round": "THIRD_PLACE",
      "pick": null,
      "source": "empty"
    }
  }
}
```

The exact slot IDs should come from the repo's game board and slot manifests. The backend should store the document; it should not define bracket geometry.

## Draft, submitted, locked

- `draft`: empty required slots are allowed.
- `submitted`: every required slot must have a non-empty pick.
- `locked`: submitted state is preserved against later editing.

## Third-place pick

The third-place winner is an explicit stored pick. The UI may manage it from the same Final Four menu as champion/finalist selection, but storage must store the resulting third-place winner in its own required slot.

The third-place candidate set is derived from the semifinal losers. That derivation is UI/model logic; the stored result is the selected third-place winner.

## Local first, remote later

The current implementation should use this document shape with local storage before any remote backend is added.

```text
UI picks
  ↓
Canonical complete pick-state document
  ↓
BracketRepository
  ↓
LocalStorageBracketStore now
  ↓
RemoteBracketStore later
```

This keeps the site running while preparing the exact document that Supabase/Postgres can later store.

## Canonical public play pick counts

Game 1 expected total: 64 picks
Game 2 expected total: 32 picks

Game 1 initializes all 64 required pick slots as empty.
Game 2 initializes all 32 required pick slots as empty.

