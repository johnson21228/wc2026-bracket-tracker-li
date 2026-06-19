# Card 213: Define Remote Bracket Store Contract

## Intent

Define the remote storage API boundary before connecting a backend.

## Scope

The contract should cover:

- `getCurrentUser()`
- `loadGameState(gameId)`
- `saveGameState(gameId, pickState)`
- `submitGameState(gameId)`
- `signIn()`
- `signOut()`

## Acceptance

- Remote storage is defined as a sibling implementation to local storage.
- No backend SDK or key is required by this card.
- The current site remains local-only and running.

## Shared-read constraint

The contract should not assume remote rows are private forever. Card 215 allows owner reads plus shared reads when `visibility`, `submitted_at`, or `locked_at` allows it. Card 216 may defer shared-pick UI, but the API boundary should leave room for a later `loadSharedGameStates(gameId)` or equivalent query without changing the storage schema.
