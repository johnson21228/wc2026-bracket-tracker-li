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

- `docs/backend/wc2026_supabase_shared_pick_sql_target.md` — canonical Supabase profiles/user_brackets shared-pick SQL target before dashboard execution.
- `source/sql/wc2026_supabase_shared_pick_schema_draft.sql` — draft schema SQL for profiles and user_brackets.
- `source/sql/wc2026_supabase_shared_pick_rls_draft.sql` — draft RLS SQL for owner-only writes and owner-or-shared reads.

- `captures/CAPTURE_BACK_EMPTY_PICK_STATE_STORAGE_MODEL.md` — Capture Back for complete empty pick-state storage refinement.

- `tools/verify_wc2026_empty_pick_state_storage_li.py` — Verifies the empty pick-state storage LI refinement.

- `prompts/implement_card_212_empty_pick_state_storage.md` — Next implementation prompt for Card 212.

## Capture Back governance

- Current Capture Back reports live in `captures/`.
- Legacy/historical Capture Back material may remain in `capture_back/`.
- New CB overlays should write report markdown to `captures/CAPTURE_BACK_*.md` and print the written path during apply.
- Governance rule: `li/repo/capture_back_governance_rule.md`.
- Current governance report: `captures/CAPTURE_BACK_CB_GOVERNANCE.md`.

## Raw Pick ID Truth Model

- Capture Back: `captures/CAPTURE_BACK_PICK_ID_TRUTH_MODEL.md`
- LI rule: `li/world_cup/raw_pick_id_truth_rule.md`
- Architecture: `docs/architecture/wc2026_raw_pick_id_truth_model.md`
- Card: `cards/221_define_raw_pick_id_truth_model_card.md`
- Prompt: `prompts/implement_raw_pick_id_truth_model.md`
- Verifier: `tools/verify_wc2026_raw_pick_id_truth_model.py`

Invariant: `pickId is truth; visual slot is projection; UI geometry may change; pickId must not change.`

## Bracketeering Model Persistence Contract

- `cards/222_confirm_bracketeering_model_persistence_contract_card.md` — confirms the saved bracket model seam before Supabase SQL is applied.
- `docs/architecture/bracketeering_model_persistence_contract.md` — durable model contract for Pages runtime state to Supabase/Postgres persistence.
- `li/world_cup/bracketeering_model_persistence_contract_rule.md` — requires owner-write/shared-read persistence design and keeps Supabase behind BracketStore.
- `captures/CAPTURE_BACK_BRACKETEERING_MODEL_PERSISTENCE_CONTRACT.md` — Capture Back record for the model persistence contract.
- `tools/verify_wc2026_bracketeering_model_persistence_contract.py` — verifier for this capture.

## Pages-Owned Board Zoom-Out Scale

- `captures/CAPTURE_BACK_PAGES_OWNED_BOARD_ZOOM_OUT_SCALE.md` — Capture Back for the reversible board zoom-out scope.
- `cards/223_add_pages_owned_board_zoom_out_scale_card.md` — Next implementation card for Pages-owned zoom-out scale.
- `docs/features/pages_owned_board_zoom_out_scale.md` — Explains native coordinate preservation and render-scale conversion.
- `li/world_cup/pages_owned_board_zoom_out_scale_rule.md` — LI rule keeping zoom in the Pages View/Controller layer.
- `prompts/implement_pages_owned_board_zoom_out_scale.md` — Implementation prompt for the future zoom-out patch.
- `tools/verify_wc2026_pages_owned_board_zoom_out_scale.py` — Verifies the zoom-out LI capture is installed.

Invariant: all board actors speak native gameboard coordinates; only the Pages View shell converts native coordinates to rendered screen coordinates.

- `li/world_cup/active_bracket_store_boundary_rule.md` — keeps local and future Supabase bracket stores separate while sharing BracketDocument/R32 lock rules.

- `li/repo/public_pages_release_line_guard_rule.md` — protects `main` as the public Pages-safe line while Supabase prep stays on feature branches.

- `li/world_cup/supabase_remote_bracket_store_contract_rule.md` — defines the future Supabase bracket store contract before implementation while preserving the active store seam.

- `li/world_cup/supabase_bracket_store_inactive_seam_rule.md` — allows `SupabaseBracketStore` to exist behind the inactive remote seam while local browser mode remains active.

- `li/world_cup/remote_store_activation_guard_rule.md` — defines a fail-closed future switch point for remote bracket persistence without enabling remote mode.

- `li/world_cup/supabase_bracket_store_offline_contract_harness_rule.md` — verifies the inactive Supabase bracket store adapter against a fake offline client without activating remote mode.

- `li/world_cup/supabase_sql_dashboard_apply_checklist_rule.md` — requires checklist and evidence capture before any Supabase dashboard SQL application, without activating remote mode.
- `li/world_cup/guarded_supabase_remote_smoke_path_rule.md` — keeps Supabase remote smoke testing explicit, terminal-only, and outside public runtime activation.
- `li/world_cup/supabase_sign_in_identity_only_smoke_path_rule.md` — enables optional Supabase sign-in as an identity-only smoke path while bracket persistence remains local.

- `li/world_cup/supabase_roomy_identity_panel_rule.md` — keeps Supabase sign-in in a roomy identity panel while preserving local bracket persistence.
