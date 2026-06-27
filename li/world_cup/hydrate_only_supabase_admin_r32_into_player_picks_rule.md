# Hydrate only Supabase Admin R32 into player picks rule

Copy ONLY R32 entrant slots from Supabase Admin_/official into player BracketDocument picks.

Player-visible R32 may be stored in player `picksBySlot` for rendering, scoring, and R16++ preselection compatibility, but it is not player-authored. Hydrated R32 records must carry Admin_/official source/authority metadata and `playerAuthored: false`.

Do not copy Admin_/official R16, QF, SF, Final, Champion, or third-place picks into player documents. Player R16++ picks remain player-owned.

Do not copy R32 from localStorage, static JSON, bundled data, or stale player documents. If Supabase Admin R32 is missing, keep player R32 unset/fail-closed.

## Superseded by site-owned official truth

This document is superseded by `li/world_cup/site_owned_official_truth_rule.md`.

Current authority:

- Official R32 occupants are site-owned truth under `site/data/current/`.
- Official results are site-owned truth under `site/data/current/`.
- Supabase stores player identity/profile and player bracket picks only.
- Player standings are computed, not stored.
- The Supabase `Admin_/official` official bracket row is no longer an official truth source.

This file remains as historical context only and must not be used as current runtime authority.

