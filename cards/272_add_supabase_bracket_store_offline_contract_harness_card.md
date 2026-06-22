# Card 272 — Add SupabaseBracketStore offline contract harness

Add an offline contract harness for the inactive Supabase bracket store.

## Acceptance

- `tools/run_wc2026_supabase_bracket_store_offline_contract_harness.js` exists.
- The harness uses a fake in-memory Supabase client.
- The harness exercises `loadUserBracket`.
- The harness exercises `saveUserBracket`.
- The harness verifies `user_brackets`.
- The harness verifies `picks_json`.
- The harness verifies upsert behavior.
- The harness verifies `createSupabaseBracketStore`.
- The harness does not use the real Supabase network/client.
- The harness does not activate remote mode.
- Public runtime still does not import `SupabaseBracketStore`.
- Public runtime still does not import the remote activation guard.
