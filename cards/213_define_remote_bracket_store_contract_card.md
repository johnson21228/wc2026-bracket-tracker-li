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
