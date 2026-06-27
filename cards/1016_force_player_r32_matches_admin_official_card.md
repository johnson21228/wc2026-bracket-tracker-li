# Card 1016 — Force player R32 display to match Admin_/official

## Intent

Lock the anti-slop LI invariant for public play:

`playerVisibleR32 = Admin_/official R32 truth`.

## Scope

- R32 picks/occupants are not player picks. They are Admin_/official-owned truth.
- Player/local/static R32 values are never trusted in public runtime.
- R32 display slots project from Supabase `Admin_/official` only.
- Missing/unreadable Admin truth fails closed.
- Player-owned picks remain later-round/winner-pick state only.

## Acceptance

- A partial Admin_/official R32 truth document renders exactly partial.
- Stale player R32 values are ignored/overwritten.
- LocalStorage cannot override Admin_/official R32 truth.
- Static JSON cannot complete public R32 when Admin_/official is required.
- R32 `setPick` from a player is rejected.

## Verifier

`python3 tools/verify_wc2026_force_player_r32_matches_admin_official.py`

## Superseded by site-owned official truth

This document is superseded by `li/world_cup/site_owned_official_truth_rule.md`.

Current authority:

- Official R32 occupants are site-owned truth under `site/data/current/`.
- Official results are site-owned truth under `site/data/current/`.
- Supabase stores player identity/profile and player bracket picks only.
- Player standings are computed, not stored.
- The Supabase `Admin_/official` official bracket row is no longer an official truth source.

This file remains as historical context only and must not be used as current runtime authority.

