# Bracketeering Canonical BracketDocument Runtime

## Runtime first, Supabase second

The Pages site must use the durable Bracketeering game document locally before Supabase/Postgres is introduced.

```text
Runtime model first. Supabase persistence second.
```

Supabase will later persist the document in `public.user_brackets.picks_json`; Supabase does not define bracket geometry, pick menus, advancement rules, or View/Controller behavior.

## Canonical document

A runtime bracket is a complete `BracketDocument`:

```json
{
  "schemaVersion": 1,
  "gameId": "game1",
  "status": "draft",
  "expectedPickCount": 64,
  "createdAt": null,
  "updatedAt": null,
  "picksBySlot": {
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

During the transition, a compatibility `picks` map may exist for older render code. The durable authority is `picksBySlot`.

## Pick counts

Game 1 expected total: 64 picks.

Game 2 expected total: 32 picks.

Both counts include a first-class third-place winner slot.

## Identity boundary

Account identity belongs outside the durable document whenever possible:

- Supabase row owns `user_id`, `game_id`, `visibility`, `submitted_at`, and `locked_at`.
- `picks_json` owns the portable `BracketDocument`.

Anonymous localStorage and signed-in Supabase play therefore use the same document shape.
