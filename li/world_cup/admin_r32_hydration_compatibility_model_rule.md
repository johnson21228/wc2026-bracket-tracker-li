# Admin R32 hydration compatibility model rule

Current Bracketeering is knockout-only. Admin_/official owns R32 occupant truth. Normal players do not assign, project, or predict R32 occupants.

Player BracketDocuments may contain R32 entrant records only as Supabase Admin_/official hydrated mirror entries. Those records exist for rendering, scoring, standings, and R16++ preselection compatibility, not player authorship.

Hydrated R32 records must be copied ONLY from the Supabase Admin_/official official bracket document. They must carry Admin_/official source/authority metadata and `playerAuthored: false`.

Admin_/official R16, QF, SF, Final, Champion, and third-place truth must never be copied into normal player BracketDocuments. Normal players own R32 match-winner and later-round picks. Existing player R16++ picks must survive R32 hydration.

## Superseded by site-owned official truth

This document is superseded by `li/world_cup/site_owned_official_truth_rule.md`.

Current authority:

- Official R32 occupants are site-owned truth under `site/data/current/`.
- Official results are site-owned truth under `site/data/current/`.
- Supabase stores player identity/profile and player bracket picks only.
- Player standings are computed, not stored.
- The Supabase `Admin_/official` official bracket row is no longer an official truth source.

This file remains as historical context only and must not be used as current runtime authority.

