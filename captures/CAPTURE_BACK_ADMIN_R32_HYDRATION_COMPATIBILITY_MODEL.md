# Capture Back: Admin R32 hydration compatibility model

Updated stale LI/docs that still described player-authored R32 occupant prediction.

Current rule:

- Admin_/official owns R32 occupant truth.
- Normal players own R32 match-winner and later picks.
- Player BracketDocuments may store R32 entries only as Supabase Admin_/official hydrated mirror entries.
- Hydrated R32 entries must be `playerAuthored: false`.
- Admin_/official later-round truth must not be copied into player documents.

Verifier:

`tools/verify_wc2026_admin_r32_hydration_compatibility_model_li.py` checks that stale player-authored R32 occupant language is removed or explicitly superseded and that the compatibility model is documented.
