# WC2026 Player Pick Storage Model

This document defines the storage model needed before introducing user picks, multiplayer records, scoring, and Game 2 tiebreaker display.

## Goals

- Preserve current local browser play.
- Make future player picks portable across users/devices.
- Support Game 1 and Game 2 as separate games.
- Allow Game 1 picks to become Game 2 comparison metadata and tiebreaker evidence.
- Keep official FIFA/live data separate from user picks.

## Primary objects

### Player

```json
{
  "playerId": "player_001",
  "displayName": "Steve",
  "createdAt": "2026-06-15T00:00:00Z"
}
```

### Game 1 draft state

Browser-local and editable:

```json
{
  "schemaVersion": "wc2026.pickDraft.v1",
  "gameId": "game1-r32-qualifier-picks",
  "playerId": "local-player",
  "status": "draft",
  "updatedAt": "2026-06-15T00:00:00Z",
  "picks": {
    "1A": { "teamAbbr": "MEX", "teamName": "Mexico", "flag": "🇲🇽", "group": "A" },
    "2A": { "teamAbbr": "KOR", "teamName": "South Korea", "flag": "🇰🇷", "group": "A" }
  }
}
```

### Game 1 submitted pick record

Durable record for scoring and comparison:

```json
{
  "schemaVersion": "wc2026.playerPickRecord.v1",
  "recordId": "pickrec_game1_player_001_20260615",
  "gameId": "game1-r32-qualifier-picks",
  "playerId": "player_001",
  "displayName": "Steve",
  "status": "submitted",
  "submittedAt": "2026-06-15T00:00:00Z",
  "lockedAt": null,
  "picks": {
    "1A": { "teamAbbr": "MEX", "teamName": "Mexico", "flag": "🇲🇽", "group": "A" }
  }
}
```

### Official Round-of-32 seed

Authoritative Game 2 bracket truth once known:

```json
{
  "schemaVersion": "wc2026.officialR32Seed.v1",
  "source": "official-or-demo",
  "updatedAt": "2026-06-15T00:00:00Z",
  "slots": {
    "1A": { "teamAbbr": "MEX", "teamName": "Mexico", "flag": "🇲🇽", "group": "A" }
  }
}
```

### Game 2 draft/submitted bracket picks

```json
{
  "schemaVersion": "wc2026.playerPickRecord.v1",
  "recordId": "pickrec_game2_player_001_20260615",
  "gameId": "game2-knockout-bracket-picks",
  "playerId": "player_001",
  "displayName": "Steve",
  "status": "draft",
  "seedSource": "official-or-demo",
  "r32SeedId": "official-r32-2026-v1",
  "updatedAt": "2026-06-15T00:00:00Z",
  "picks": {
    "r16_m01": { "teamAbbr": "MEX", "teamName": "Mexico", "from": ["1A", "2B"] }
  }
}
```

## Game 2 tiebreaker comparison

Game 2 may load a Game 1 submitted pick record as comparison metadata:

```json
{
  "schemaVersion": "wc2026.game1TiebreakerComparison.v1",
  "playerId": "player_001",
  "game1RecordId": "pickrec_game1_player_001_20260615",
  "officialR32SeedId": "official-r32-2026-v1",
  "correctSlotCount": 21,
  "totalSlots": 32,
  "slotResults": {
    "1A": { "game1TeamAbbr": "MEX", "officialTeamAbbr": "MEX", "correct": true },
    "2A": { "game1TeamAbbr": "KOR", "officialTeamAbbr": "CZE", "correct": false }
  }
}
```

## LocalStorage keys

Recommended keys while the site is static/local:

```text
wc2026.player.local.v1
wc2026.game1.draft.v1
wc2026.game1.submitted.v1
wc2026.game2.draft.v1
wc2026.game2.submitted.v1
wc2026.game2.tiebreakerComparison.v1
```

Later, these same JSON objects can be moved to a backend database without changing the game rules.
