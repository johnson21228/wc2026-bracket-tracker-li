# SupabaseBracketStore offline contract harness

`SupabaseBracketStore` now has an offline contract harness.

The harness is a development/test artifact only.

## File

`tools/run_wc2026_supabase_bracket_store_offline_contract_harness.js`

## What it proves

The harness proves that the inactive Supabase store adapter can:

- load a player/game bracket row
- save a player/game bracket row
- use `user_brackets`
- preserve `picks_json`
- preserve canonical `BracketDocument` shape
- preserve `picksBySlot`
- use owner/game upsert semantics

## What it does not do

The harness does not activate remote mode.

The harness does not call the real Supabase network.

The harness does not apply SQL.

The harness does not change dashboard state.

The harness does not merge to `main`.

The harness does not move View/Controller behavior into Supabase.

Local browser storage remains the active public path.
