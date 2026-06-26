# Card 1019: Hydrate only Supabase Admin R32 into player picks

## Intent

Restore player-site R16++ preselection by materializing Supabase Admin_/official R32 occupants into player picks while copying no Admin later-round official truth.

Copy ONLY R32 from Supabase Admin_/official.

## Changes

- Add a model hydration path that strips stale player/local R32 values and then copies ONLY R32 from Supabase Admin_/official.
- Render normal player slots from the hydrated player picks map.
- Keep Admin editor display routed to official truth.
- Preserve normal player R16++ ownership.
- Tighten R32 hydration so static JSON is not a player copy source.

## Verification

```bash
python3 tools/verify_wc2026_hydrate_only_supabase_admin_r32_into_player_picks.py
make verify
```
