# Capture Back — User bracket storage model

## Decision

Create the storage model before choosing permanent storage.

## Current storage path

Use browser `localStorage` for the clean static site.

## Future storage path

SQLite can be used later behind a server/API adapter. The browser should not write a shared SQLite database directly.

## Invariants

- Team IDs are uppercase three-letter codes.
- Pick values are either `{ "kind": "unpicked" }` or `{ "kind": "team", "teamId": "USA" }`.
- Every user bracket stores every site pick ID.
- Missing pick keys are invalid.
- FIFA bracket order is a mapping layer.
