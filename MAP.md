# MAP

## Purpose

This repo maintains a World Cup 2026 bracket pool tracker as a modular web app backed by Workbench data and LI.

## Key folders

```text
li/world_cup/      governance rules
source/            source artifacts and source notes
data/              canonical data storage
cards/             work cards
prompts/           reusable prompts for any II reasoner
releases/          immutable release/review snapshots
tools/             optional validation/build helpers
```

## Current source artifacts

- `source/images/match_schedule_group_stage_poster_michelob_ultra.jpeg`
- `source/text/poster_transcription.md`
- `data/group_stage_matches_from_poster.json`
- `data/groups_from_poster.json`

## Two games

Game 1:
Players pick the 32 teams that will advance from the 48-team group stage.

Game 2:
After the official Round of 32 is known, players fill the full knockout bracket through champion.
- `site/game2/index.html` — Game 2 foundation board surface: same pub back layer and transparent geometry board layer as Game 1; picking rules intentionally deferred.


## Modular MVC/TDD Source Boundary

- `li/world_cup/modular_mvc_tdd_source_rule.md` — current architectural rule: modular source, MVC boundaries, and TDD for behavior.
- `li/world_cup/static_html_release_rule.md` — rewritten as static-hostable deployment/review posture, not a page-concentrated source goal.
- `docs/architecture/wc2026_modular_mvc_tdd_source_boundary.md` — architecture note for extracting rules/state/views out of HTML entry points.
- `cards/151_remove_static_single_file_architecture_goal_card.md` — governed card for removing the page-concentrated architecture goal.
- `capture_back/CAPTURE_BACK_REMOVE_STATIC_SINGLE_FILE_ARCHITECTURE_GOAL.md` — Capture Back record for the correction.

## Game 2 Official Seed + Game 1 Tiebreaker Rule

- `li/world_cup/game2_official_seed_and_game1_tiebreaker_rule.md` — durable LI rule for fixed Game 2 Round-of-32 seed authority and Game 1 comparison/tiebreaker metadata.
- `docs/rules/game2_official_seed_and_game1_tiebreaker.md` — product-facing explanation of the two-game boundary.
- `cards/048_capture_game2_official_seed_tiebreaker_rule_card.md` — implementation card for the rule capture.
- `capture_back/CAPTURE_BACK_GAME2_OFFICIAL_SEED_TIEBREAKER_RULE.md` — Capture Back record of the decision.

## Game 1 Pick State Model-First Capture

- `li/world_cup/game1_pick_state_model_first_rule.md` — requires Game 1 pick behavior to be repaired through a canonical model before UI/render changes.
- `docs/features/game1_pick_state_model_first.md` — explains the model-first insight behind the pick-state authority cleanup.
- `cards/153_capture_game1_pick_state_model_first_insight_card.md` — captures the Workbench card for this insight.
- `tools/verify_wc2026_game1_pick_state_model_first_li.py` — verifies the model-first LI capture is installed.
- `cards/154_implement_game1_canonical_pick_state_model_card.md` — implementation card for the canonical JavaScript Game 1 pick-state model.
- `cards/156_normalize_canonical_rendered_knockout_visual_state_card.md` — normalizes canonical rendered R16/QF/SF card visual state.
- `docs/features/game1_canonical_render_visual_uniformity.md` — explains that all rendered knockout cards come from canonical state and share one visual treatment.
- `li/world_cup/game1_canonical_render_visual_uniformity_rule.md` — requires canonical rendered knockout picks to use consistent visual treatment.

## Public Multi-User Play LI

- `li/world_cup/public_multi_user_play_rule.md` — invite-ready public play rule.
- `li/world_cup/canonical_pick_state_storage_model_rule.md` — Game 1/Game 2 canonical user pick-state storage model.
- `li/world_cup/site_running_public_play_invariant_rule.md` — keep-site-running invariant for backend migration.
- `docs/architecture/wc2026_public_multi_user_play_architecture.md` — static site + local/remote storage architecture.
- `docs/backend/wc2026_inexpensive_backend_options.md` — inexpensive backend options and Supabase posture.

