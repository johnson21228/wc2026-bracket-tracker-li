# Admin official full bracket editor mode rule

`Admin_/official` may edit every official bracket truth slot.

Normal players may not edit R32. Normal players may edit only their own R16++ player picks.

`Admin_/official` edits must save to the Supabase `Admin_/official` official bracket document.
Normal player edits must save only to the normal player's bracket document.

Player-visible R32 always mirrors `Admin_/official` R32 truth. localStorage/static JSON must not masquerade as public official truth.

## Superseded by site-owned official truth

This document is superseded by `li/world_cup/site_owned_official_truth_rule.md`.

Current authority:

- Official R32 occupants are site-owned truth under `site/data/current/`.
- Official results are site-owned truth under `site/data/current/`.
- Supabase stores player identity/profile and player bracket picks only.
- Player standings are computed, not stored.
- The Supabase `Admin_/official` official bracket row is no longer an official truth source.

This file remains as historical context only and must not be used as current runtime authority.

