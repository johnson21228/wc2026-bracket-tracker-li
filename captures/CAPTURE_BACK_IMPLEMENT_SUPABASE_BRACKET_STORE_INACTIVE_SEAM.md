# Capture Back: Implement SupabaseBracketStore behind inactive remote store seam

This capture adds the future remote persistence store module without activating it in public runtime.

Implemented:

- `site/js/services/SupabaseBracketStore.js`
- `SupabaseBracketStore.loadUserBracket(userId)`
- `SupabaseBracketStore.saveUserBracket(bracketDocument)`
- `createSupabaseBracketStore(options)`
- full canonical `BracketDocument` persistence to `public.user_brackets.picks_json`
- one row per signed-in user/game through `user_id,game_id`
- explicit remote save/load errors
- optional canonical model context for `normalizeBracketDocument`

Still intentionally not done:

- no public runtime switch to remote mode
- no `BracketRepository` default remote store wiring
- no View or Controller Supabase calls
- no Supabase SQL applied
- no Supabase dashboard state changed
- no merge to `main`

Local browser mode remains the active public path.
