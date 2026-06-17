# Card 173 — Bracket repository API boundary

## Intent

Add a repository/API boundary so the site can use static JSON plus localStorage now and a REST/SQLite backend later without changing the UI model.

## Architecture

```text
Site UI
  ↓
BracketRepository
  ↓
Model source + bracket store
  ├── StaticJsonModelSource + LocalStorageBracketStore
  └── RestBracketApiAdapter + server/SQLite later
```

## Acceptance

- `BracketRepository` exposes one UI-facing boundary for teams, users, slots, FIFA mapping, and user brackets.
- `StaticJsonModelSource` loads committed JSON model data from `site/data/model`.
- `RestBracketApiAdapter` exists as a future REST-backed boundary.
- The current static site can keep using JSON/localStorage.
- The model remains unchanged when storage moves to REST/SQLite.
- `make verify` and `make pack` pass.
