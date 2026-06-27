# Admin official full bracket editor mode

## Goal

Allow the `Admin_/official` identity to edit all official bracket truth slots, not just R32, while preserving normal player ownership rules.

## Invariant

`Admin_/official` owns official bracket truth.
Normal players own only their player bracket picks after R32.
Player-visible R32 always mirrors `Admin_/official`.

## Rules

- If active identity is `Admin_/official`, every bracket slot is editable.
- `Admin_/official` edits save to the Supabase `Admin_/official` bracket document.
- If active identity is not `Admin_/official`, R32 remains read-only.
- If active identity is not `Admin_/official`, R16++ remains normal player-editable picks.
- Normal player edits save only to that player bracket document.
- `Admin_/official` editing must not write into a normal player bracket.
- Normal player editing must not write into the `Admin_/official` bracket.
- Do not use localStorage/static JSON as public official truth.

## Runtime behavior

The same board surface is allowed to show different edit authority based on active identity:

- Admin official full bracket editor mode writes selected slot values into `officialPicks` and persists a canonical official BracketDocument.
- Normal player mode keeps R32 as a read-only projection from `Admin_/official` and writes later picks only to the player document.
- R32 mirror behavior remains exact and partial: if `Admin_/official` has one R32 value, players see exactly one.

## Verification

- `Admin_/official` can edit R32, R16, QF, SF, Final, and Champion slots.
- `Admin_/official` edits save to the `Admin_/official` Supabase bracket document.
- A normal player cannot edit R32.
- A normal player can still edit R16++ player picks.
- A normal player sees `Admin_/official` R32 values after hydration.
- If `Admin_/official` changes an R32 value, player display changes to match.
- `Admin_/official` later-round truth remains separate from normal player picks.

## Superseded by site-owned official truth

This document is superseded by `li/world_cup/site_owned_official_truth_rule.md`.

Current authority:

- Official R32 occupants are site-owned truth under `site/data/current/`.
- Official results are site-owned truth under `site/data/current/`.
- Supabase stores player identity/profile and player bracket picks only.
- Player standings are computed, not stored.
- The Supabase `Admin_/official` official bracket row is no longer an official truth source.

This file remains as historical context only and must not be used as current runtime authority.

