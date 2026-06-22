# Capture Back: SupabaseBracketStore offline contract harness

Adds an offline contract harness for `SupabaseBracketStore`.

The harness runs against a fake in-memory Supabase client.

It verifies:

- load uses the `user_brackets` table
- save uses `upsert`
- save stores `picks_json`
- save preserves canonical `BracketDocument` shape
- load returns the saved `BracketDocument`
- factory construction remains available
- missing user id is rejected

It intentionally does not:

- use the real Supabase dashboard
- use the real Supabase client over the network
- apply SQL
- activate remote mode
- import the store from public runtime
- merge anything to `main`

The public runtime remains local/browser-store active.
