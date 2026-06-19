# Canonical Pick-State Storage Model Rule

## Rule

Workbench must treat a user's Bracketeering Pub bracket state as a complete canonical pick-state document, not as an ad hoc sparse set of browser-local picks.

Each user has two game pick states:

- `game1`: full group-stage prediction bracket, with 64 explicit pick slots.
- `game2`: knockout prediction bracket, with 32 explicit pick slots.

The canonical document must be created as a complete empty pick-state shell before the user makes picks.

## Required empty initialization

A new bracket state must initialize every required slot explicitly:

- `game1`: 32 Round-of-32 entrant slots, 16 Round-of-32 winners, 8 Round-of-16 winners, 4 quarterfinal winners, 2 semifinal winners/finalists, 1 champion, and 1 third-place winner.
- `game2`: 16 Round-of-32 winners, 8 Round-of-16 winners, 4 quarterfinal winners, 2 semifinal winners/finalists, 1 champion, and 1 third-place winner.

All initialized slots must be empty until the user makes a pick. A missing required slot is a model error. An empty required slot is a valid draft value.

## Canonical shape

The storage shape should support this semantic form:

```json
{
  "schemaVersion": 1,
  "gameId": "game1",
  "status": "draft",
  "expectedPickCount": 64,
  "picksBySlot": {
    "L-R32-01": {
      "slotId": "L-R32-01",
      "round": "R32_ENTRANT",
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

The exact slot IDs are repo-owned and must be derived from the bracket slot manifest/model, not invented in the backend.

## Draft vs submitted

Draft state may contain empty picks. Submitted/locked state must not contain empty required picks.

## Storage adapter invariant

Local storage and future remote storage must use the same canonical document. The difference between local-only mode and signed-in mode is the storage adapter, not the bracket state shape.

## Site-running invariant

Any implementation of this rule must preserve the current local/static site as playable. Backend work must not be required for the anonymous local bracket workflow to run.

## Public play storage adapter requirements

Game 1 expected pick count: 64
Game 2 expected pick count: 32

The canonical pick state must explicitly account for semifinal losers so the third-place winner can be selected from the two semifinal losers.

LocalStorageBracketStore is the first storage adapter and must keep the static/local site running.

RemoteBracketStore is the future signed-in storage adapter and must use the same canonical pick-state document shape.

