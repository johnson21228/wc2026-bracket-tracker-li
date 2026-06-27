# Admin_/official results truth

WC2026 Bracketeering uses `Admin_/official` as the source of official tournament truth.

## Model

```text
R32 entrants = Admin_/official entrant truth
Official results/winners = Admin_/official result truth
Player brackets = player predictions only
Scoring = player predictions compared against Admin_/official truth
```

The `Admin_/official` row may be partial while the tournament is being set up or results are being entered. Partial truth is still authoritative. Empty official winner slots do not score yet; they are not filled from player picks or static fallback data.

## Standings

The standings store reads the official row separately from player rows. The official row is filtered out of player rankings and used only as comparison truth. Player scores are computed by comparing player pick slots to non-R32 official truth slots.

## Read-only player board viewer

The viewer renders player picks as read-only and receives official truth separately for comparison. It does not treat a player bracket as official truth.

## Static fallback boundary

Static fallback data is only a local/dev missing-admin-source fallback. It must not override an existing `Admin_/official` source, including a partial source.

## Superseded by site-owned official truth

This document is superseded by `li/world_cup/site_owned_official_truth_rule.md`.

Current authority:

- Official R32 occupants are site-owned truth under `site/data/current/`.
- Official results are site-owned truth under `site/data/current/`.
- Supabase stores player identity/profile and player bracket picks only.
- Player standings are computed, not stored.
- The Supabase `Admin_/official` official bracket row is no longer an official truth source.

This file remains as historical context only and must not be used as current runtime authority.

