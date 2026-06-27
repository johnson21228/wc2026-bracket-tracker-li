# Card 1017: Admin official R32 editor mode

## Goal

Allow the Admin_/official bracket identity to author and edit R32 occupant truth while keeping all non-admin player brackets read-only for R32.

## Invariant

Only Admin_/official may edit R32 occupant slots.
All players mirror Admin_/official R32 occupant truth.

## Implementation

- Add explicit `adminOfficialR32Editor` runtime mode.
- Reopen R32 choices only in Admin_/official editor mode.
- Save Admin_/official R32 edits to the Supabase official bracket row.
- Preserve normal player R32 read-only mirror behavior.
- Preserve R16++ player-owned picks.

## Verification

`tools/verify_wc2026_admin_official_r32_editor_mode.py` proves that Admin_/official can edit R32 truth while normal players cannot.

## Superseded by site-owned official truth

This document is superseded by `li/world_cup/site_owned_official_truth_rule.md`.

Current authority:

- Official R32 occupants are site-owned truth under `site/data/current/`.
- Official results are site-owned truth under `site/data/current/`.
- Supabase stores player identity/profile and player bracket picks only.
- Player standings are computed, not stored.
- The Supabase `Admin_/official` official bracket row is no longer an official truth source.

This file remains as historical context only and must not be used as current runtime authority.

