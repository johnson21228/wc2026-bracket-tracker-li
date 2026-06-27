# Single Game Admin_/official Runtime

This cleanup reconciles stale two-game presentation code with the current Bracketeering model.

- One persisted game id: `game1`.
- Legacy `game-2` means only “show the bracket board”.
- Admin_/official owns R32 occupants in a public locked/submitted Supabase row.
- Players cannot edit R32 occupants.
- Player picks use the existing dependency-map winner path after R32 is hydrated.
- Missing official R32 authority fails closed for players.
- Missing official R32 authority does not blank the signed-in admin editor; the connected admin can create the row.

## Superseded by site-owned official truth

This document is superseded by `li/world_cup/site_owned_official_truth_rule.md`.

Current authority:

- Official R32 occupants are site-owned truth under `site/data/current/`.
- Official results are site-owned truth under `site/data/current/`.
- Supabase stores player identity/profile and player bracket picks only.
- Player standings are computed, not stored.
- The Supabase `Admin_/official` official bracket row is no longer an official truth source.

This file remains as historical context only and must not be used as current runtime authority.

