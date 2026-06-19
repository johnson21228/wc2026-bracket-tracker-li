# Canonical Pick State Storage Model Rule

User bracket storage must be represented as one canonical pick-state document per user per game.

## Game states

Each authenticated user has at most one active bracket document for each game:

- `game1`: full group-stage prediction bracket
- `game2`: knockout prediction bracket after the actual Round of 32 field is known

## Expected pick counts

The model must account for champion and third-place picks.

- Game 1 expected pick count: 64
- Game 2 expected pick count: 32

Game 1 contains:

- 32 Round-of-32 entrant picks
- 16 Round-of-32 winner picks
- 8 Round-of-16 winner picks
- 4 quarterfinal winner picks
- 2 semifinal winner/finalist picks
- 1 final winner/champion pick
- 1 third-place winner pick

Game 2 contains:

- 16 Round-of-32 winner picks
- 8 Round-of-16 winner picks
- 4 quarterfinal winner picks
- 2 semifinal winner/finalist picks
- 1 final winner/champion pick
- 1 third-place winner pick

## Canonical document shape

The stable storage unit is a JSON document with this conceptual shape:

```json
{
  "schemaVersion": 1,
  "gameId": "game1",
  "status": "draft",
  "expectedPickCount": 64,
  "picksBySlot": {
    "SLOT-ID": {
      "slotId": "SLOT-ID",
      "teamId": "MEX",
      "label": "Mexico"
    }
  }
}
```

The exact slot IDs are repo-owned and must come from a canonical slot manifest or model authority, not from backend table assumptions.

## Storage implementations

Local and remote stores must use the same canonical document shape:

- `LocalStorageBracketStore` is the first implementation.
- `RemoteBracketStore` is a later implementation.
- Export/import should be able to round-trip through the same shape.

## UI ownership

The UI may use a single Final Four menu to choose finalists, champion, and third-place winner. The server does not need to understand the menu. The saved document records the resulting slots.

## Validation ownership

The model layer validates:

- expected slot completeness
- champion is drawn from final participants
- third-place winner is drawn from semifinal losers
- downstream picks are invalidated or warned when upstream picks change
