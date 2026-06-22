# Supabase SQL dashboard apply checklist rule

Supabase SQL dashboard application must be checklist- and evidence-driven.

## Rule

Before SQL is applied in Supabase, the repo must contain a checklist that names:

- schema SQL source
- RLS SQL source
- canonical SQL target
- required evidence after apply
- runtime non-activation invariants

## Boundary

Adding this checklist does not apply SQL.
Adding this checklist does not activate remote mode.
Adding this checklist does not change Supabase dashboard state.
Adding this checklist does not merge or publish public Pages.

## Runtime invariant

Until a later explicit CB activates remote mode:

- public runtime remains local/browser-store active
- BracketRepository defaults to LocalStorageBracketStore
- RemoteStoreActivationGuard remains fail-closed
- View and Controller do not call Supabase
