# Card 228: Add BracketDocument save seam before Supabase

## Intent

Teach the Pages runtime to save the canonical `BracketDocument` through the repository/store boundary before Supabase is connected.

## Required sequence

1. Site code learns to save the canonical `BracketDocument`.
2. Anonymous play continues through `LocalStorageBracketStore`.
3. Later signed-in play routes the same document save through `SupabaseBracketStore` into `user_brackets.picks_json`.

## Invariants

- Same `BracketDocument`. Different store.
- Pages owns View, Controller, runtime model, board rendering, and pick behavior.
- Supabase/Postgres owns durable persistence only.
- UI/controller code must not call Supabase directly.
- This card must not add Supabase client code, Supabase Auth UI, SQL execution, or RLS policies.

## Implementation notes

- `BracketRepository.saveUserBracket` remains the persistence boundary.
- `LocalStorageBracketStore.saveUserBracket` remains the current concrete persistence target.
- `Game1R32PickController` mirrors R32 projection pick changes into the canonical user bracket and saves it through `BracketRepository`.
- Legacy R32 projection localStorage is preserved during this transition so existing rendering/event behavior is not broken.

## Acceptance

- Pick mutation updates the canonical `BracketDocument`.
- Pick mutation requests save through `BracketRepository`.
- LocalStorage stores canonical `BracketDocument` fields.
- Reload/load can restore the canonical `BracketDocument`.
- No direct Supabase calls are introduced.
- `make verify` passes.
- `make pack` completes.
