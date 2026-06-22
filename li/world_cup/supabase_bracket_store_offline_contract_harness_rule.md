# SupabaseBracketStore offline contract harness rule

The Supabase bracket store may be tested offline before remote mode is activated.

## Rule

A harness may exercise the inactive `SupabaseBracketStore` against a fake in-memory Supabase client.

This validates adapter contract shape without dashboard/network coupling.

## Required boundary

The harness must not:

- call the real Supabase network
- apply SQL
- activate remote mode
- import the store from public runtime
- import the remote activation guard from public runtime
- move View or Controller behavior into Supabase
- imply a merge to `main`

## Active runtime invariant

Public runtime remains local/browser-store active.

Only a later explicit CB may wire signed-in remote mode.
