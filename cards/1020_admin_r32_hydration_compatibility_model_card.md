# Card 1020: Admin R32 hydration compatibility model

## Intent

Align LI and feature docs with the current knockout-only game model.

## Rule

Admin_/official owns R32 occupant truth. Player BracketDocuments may store R32 entries only as Supabase Admin_/official hydrated mirror entries with `playerAuthored: false`. Normal players own R32 match-winner and later picks.

## Verification

Run:

```bash
python3 tools/verify_wc2026_admin_r32_hydration_compatibility_model_li.py
```

## Superseded by site-owned official truth

This document is superseded by `li/world_cup/site_owned_official_truth_rule.md`.

Current authority:

- Official R32 occupants are site-owned truth under `site/data/current/`.
- Official results are site-owned truth under `site/data/current/`.
- Supabase stores player identity/profile and player bracket picks only.
- Player standings are computed, not stored.
- The Supabase `Admin_/official` official bracket row is no longer an official truth source.

This file remains as historical context only and must not be used as current runtime authority.

