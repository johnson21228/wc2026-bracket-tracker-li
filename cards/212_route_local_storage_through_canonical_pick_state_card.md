# Card 212: Route Local Storage Through Canonical Pick State

## Purpose

Make the current local/static site use the same canonical pick-state document that future signed-in remote storage will save.

This is the first implementation step toward public multi-user play.

## Scope

Implement the storage foundation only:

- no login;
- no Supabase;
- no remote backend;
- no submit/lock behavior;
- no leaderboard.

The site must keep running as a local-only bracket game.

## Required behavior

The app must initialize complete empty pick-state documents:

- `game1`: 64 explicit required slots, all initialized empty;
- `game2`: 32 explicit required slots, all initialized empty.

Unpicked slots must be represented as explicit empty values. Missing required slots are errors.

## Canonical functions

The implementation should provide a model/service boundary equivalent to:

```text
createEmptyPickState(gameId)
loadGameState(gameId)
saveGameState(gameId, pickState)
updatePick(gameId, slotId, pick)
validateDraftPickState(gameId, pickState)
validateCompletePickState(gameId, pickState)
```

Draft validation requires all required slots to exist. Complete validation requires every required slot to have a pick.

## Storage adapter

Local storage is the first storage adapter:

```text
BracketRepository
  -> LocalStorageBracketStore
```

The repository API should be compatible with a later `RemoteBracketStore`.

## Expected implementation files

Likely files:

```text
site/js/model/PickStateMap.js
site/js/services/BracketRepository.js
site/js/services/LocalStorageBracketStore.js
tools/verify_wc2026_local_storage_uses_canonical_pick_state.py
```

The exact file names may change if the existing MVC structure already has preferred locations.

## Migration behavior

Existing local pick data must not be discarded. The implementation should either:

- hydrate old local picks into the new complete pick-state document; or
- preserve legacy reads while writing the new canonical state.

The site-running invariant wins: existing local play must remain usable.

## Acceptance criteria

- The current static site still opens and plays locally.
- `game1` initializes to 64 explicit pick slots.
- `game2` initializes to 32 explicit pick slots.
- Empty picks are explicit, not missing.
- Champion is an explicit required slot.
- Third-place winner is an explicit required slot.
- Local storage persists the canonical document or can losslessly derive it.
- Export/import can be derived from the canonical document.
- `make verify` passes.
- `make pack` passes.

## Out of scope

- User accounts.
- Supabase project creation.
- Remote database writes.
- Submit/lock.
- Leaderboard/scoring.
