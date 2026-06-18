# WC2026 REST API storage boundary

The site is being factored to support two storage modes with the same model.

## Static mode

```text
Browser
  → static JSON files
  → localStorage user bracket records
```

## Shared mode

```text
Browser
  → REST API
  → server
  → SQLite
```

## Future REST endpoints

```text
GET  /api/teams
GET  /api/bracket-slots
GET  /api/fifa-r32-slot-map
GET  /api/users
GET  /api/users/:userId/bracket

PUT  /api/users/:userId/bracket
POST /api/users
```

The UI should not need to change when the storage adapter changes.
