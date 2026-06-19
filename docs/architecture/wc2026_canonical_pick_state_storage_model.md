# WC2026 Canonical Pick State Storage Model

## Purpose

Define the durable user bracket document that local storage, export/import, and future server storage can all share.

## User storage unit

A user has one pick-state document per game:

```text
user + game1 -> one bracket document
user + game2 -> one bracket document
```

## Pick counts

Game 1 expected total: 64 picks.

```text
32 R32 entrants
16 R32 winners
8 R16 winners
4 QF winners
2 SF winners / finalists
1 champion
1 third-place winner
```

Game 2 expected total: 32 picks.

```text
16 R32 winners
8 R16 winners
4 QF winners
2 SF winners / finalists
1 champion
1 third-place winner
```

## Canonical JSON shape

```json
{
  "schemaVersion": 1,
  "gameId": "game1",
  "status": "draft",
  "expectedPickCount": 64,
  "picksBySlot": {
    "L-R32-01": {
      "slotId": "L-R32-01",
      "teamId": "MEX",
      "label": "Mexico"
    },
    "CHAMPION": {
      "slotId": "CHAMPION",
      "teamId": "MEX",
      "label": "Mexico"
    },
    "THIRD-PLACE-WINNER": {
      "slotId": "THIRD-PLACE-WINNER",
      "teamId": "FRA",
      "label": "France"
    }
  },
  "updatedAt": "2026-06-19T12:00:00Z"
}
```

Slot IDs are logical identifiers owned by the repo. A later implementation should generate or validate against a manifest rather than hardcoding every slot in the backend.

## Status values

- `draft`: editable
- `submitted`: user-submitted and not editable by normal client flow
- `locked`: locked by contest timing or admin policy

## Final Four behavior

The UI can manage finalists, champion, and third-place winner through one Final Four menu. The storage model records the result:

- two semifinal winner/finalist slots
- champion slot
- third-place winner slot

The third-place winner must be selected from the losers of the two semifinal matches.

## Local first

The current local storage system should be routed through this shape before adding a remote backend. That makes server storage a transport change, not a game-state rewrite.
