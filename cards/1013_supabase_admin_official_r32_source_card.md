# Card 1013 — Supabase Admin_/official R32 Source

## Intent
Make the Supabase `Admin_/official` bracket row the production authority for official R32 hydration.

## Runtime boundary
- `SupabaseBracketStore.loadOfficialR32BracketAuthority` is the explicit production authority path.
- It loads the row-per-user-per-game `user_brackets` row for `user_id = "Admin_/official"`, `tournament_id = "wc2026"`, and `game_id = "game1"`.
- `BracketRepository.loadOfficialR32Source` tries Supabase Admin_/official first.
- Static `official_round_of_32.json` is retained only as `StaticJsonFallback:official_round_of_32` for local/dev/no-remote conditions.

## Hydration contract
Hydrated player bracket R32 entrants retain official authority metadata:

- `source: "Admin_/official"`
- `authority: "Admin_/official"`
- `playerAuthored: false`
- `hydratedFrom: "Supabase:Admin_/official"` when Supabase authority is available

## Preservation
- BracketDocument remains the persistence container.
- Supabase remains one row per user per game.
- Local anonymous play remains valid through static fallback.
- Existing player knockout winner picks remain player-owned and are preserved.
- Player action cannot author or overwrite R32 entrant records.

## Non-goals
No player-facing copy cleanup. No Game 1/Game 2 copy cleanup. No schema replacement.

## Superseded by site-owned official truth

This document is superseded by `li/world_cup/site_owned_official_truth_rule.md`.

Current authority:

- Official R32 occupants are site-owned truth under `site/data/current/`.
- Official results are site-owned truth under `site/data/current/`.
- Supabase stores player identity/profile and player bracket picks only.
- Player standings are computed, not stored.
- The Supabase `Admin_/official` official bracket row is no longer an official truth source.

This file remains as historical context only and must not be used as current runtime authority.

