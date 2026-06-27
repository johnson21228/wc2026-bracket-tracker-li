# Admin R32 hydration compatibility model

This feature note aligns the LI with the current knockout-only game model.

Admin_/official owns the R32 occupant field. Normal players do not author R32 occupants, but their BracketDocuments may store R32 entries copied from Supabase Admin_/official so existing rendering, standings, scoring, and R16++ preselection paths continue to work.

The copy rule is narrow:

- Copy ONLY R32 entrant slots.
- Copy ONLY from Supabase Admin_/official.
- Mark copied R32 entries with Admin_/official source/authority metadata and `playerAuthored: false`.
- Do not copy Admin_/official R16, QF, SF, Final, Champion, or third-place truth into player documents.
- Preserve existing player R16++ picks.

This supersedes older language that described player-authored R32 occupant prediction.

## Superseded by site-owned official truth

This document is superseded by `li/world_cup/site_owned_official_truth_rule.md`.

Current authority:

- Official R32 occupants are site-owned truth under `site/data/current/`.
- Official results are site-owned truth under `site/data/current/`.
- Supabase stores player identity/profile and player bracket picks only.
- Player standings are computed, not stored.
- The Supabase `Admin_/official` official bracket row is no longer an official truth source.

This file remains as historical context only and must not be used as current runtime authority.

