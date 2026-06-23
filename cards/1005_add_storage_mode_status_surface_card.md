# Card 1005 — Add storage mode status surface

## Intent

Players need a visible truth surface that says where their picks are being saved before remote persistence becomes a normal product feature.

## Scope

Add a small browser-chrome storage mode indicator in the upper-right account chrome, to the left of the login/status button:

- `Playing locally` for normal public gameplay.
- `Playing locally` for signed-in users on the normal URL.
- `Playing locally` when dev remote mode is requested but no signed-in session exists.
- `Remote save test mode` only when the hidden dev Supabase bracket store is active.

## Non-goals

- Do not enable remote save by default.
- Do not add opt-in remote save UI yet.
- Do not migrate local picks to Supabase.
- Do not dual-write local and remote saves.
- Do not move Supabase persistence into View or Controller code.

## Verification

`tools/verify_wc2026_storage_mode_status_surface.py`
