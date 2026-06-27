# Audit: Supabase Admin Official Truth Conflicts

Generated: 2026-06-27T04:35:27Z

## New authority

Official R32 occupants and official results are site-owned truth under site/data/current/.

Player standings are computed, not stored.

Supabase stores player identity/profile and player bracket picks only.

## Terms searched

- Admin_/official
- Admin_ physical
- Supabase:Admin_/official
- bracket_kind.*official
- officialTruth
- official R32 hydration
- Supabase Admin

## Conflicting references

li/world_cup/single_game_admin_official_runtime_rule.md:1:# Single Game Admin_/official Runtime Rule
li/world_cup/single_game_admin_official_runtime_rule.md:7:Admin_/official owns Round-of-32 occupants. Player-owned picks begin with winners after the official R32 field is supplied. Players may render R32 occupants but may not author them.
li/world_cup/single_game_admin_official_runtime_rule.md:9:Supabase is required for connected play. The site may not silently fall back to disconnected authority. If the public locked/submitted Admin_/official row is missing, normal players fail closed. A signed-in Admin_/official editor may still render the bracket board while connected so the missing official row can be created.
li/world_cup/official_truth_bracket_as_hidden_player_rule.md:5:- `bracket_kind = official`
li/world_cup/official_truth_bracket_as_hidden_player_rule.md:13:1. `bracket_kind = official` must not appear in the Players panel.
li/world_cup/bracket_lifecycle_state_rule.md:19:- Supabase Admin_/official R32 occupant truth mirrored into player BracketDocuments with `playerAuthored: false`
li/world_cup/bracket_lifecycle_state_rule.md:22:Loading Admin_/official R32 truth must not overwrite player-owned R16++ picks and must not copy Admin_/official later-round truth into player documents.
li/world_cup/bracket_lifecycle_state_rule.md:32:- Admin R32 setup phase: R32 slots use group/slot eligibility choices only in Admin_/official editor mode.
li/world_cup/app_module_boundaries_rule.md:77:### 4. Admin_/official Module — Round-of-32 Occupant Authority
li/world_cup/app_module_boundaries_rule.md:83:- let Admin_/official assign official team occupants to Game 1 R32 slots
li/world_cup/app_module_boundaries_rule.md:84:- persist those occupants in the Supabase Admin_/official official bracket document
li/world_cup/app_module_boundaries_rule.md:85:- expose ONLY Supabase Admin_/official R32 entrants for player BracketDocument hydration
li/world_cup/app_module_boundaries_rule.md:86:- preserve partial Admin_/official truth without filling missing R32 slots from static JSON, localStorage, or stale player documents
li/world_cup/app_module_boundaries_rule.md:90:- copy Admin_/official R16, QF, SF, Final, Champion, or third-place truth into normal player documents
li/world_cup/app_module_boundaries_rule.md:100:- hydrate ONLY R32 entrant slots from Supabase Admin_/official into player BracketDocuments for rendering, scoring, and R16++ preselection compatibility
li/world_cup/app_module_boundaries_rule.md:101:- mark hydrated R32 entries with Admin_/official source/authority metadata and `playerAuthored: false`
li/world_cup/app_module_boundaries_rule.md:109:- copy Admin_/official later-round truth into player documents
li/world_cup/player_standings_max_possible_reachability_rule.md:7:A player pick counts toward `Max Possible` only if that pick could still become `Admin_/official` truth.
li/world_cup/player_standings_max_possible_reachability_rule.md:15:- If the player has a pick but prior resolved `Admin_/official` truth has already eliminated that team from reaching that slot, the slot contributes 0 to Max Possible.
li/world_cup/player_standings_max_possible_reachability_rule.md:21:- If the player's pick matches `Admin_/official`, the slot contributes its weight to both `Score` and `Max Possible`.
li/world_cup/player_standings_max_possible_reachability_rule.md:22:- If the player's pick does not match `Admin_/official`, the slot contributes 0 to both `Score` and `Max Possible`.
li/world_cup/player_standings_max_possible_reachability_rule.md:26:A team is no longer reachable for a future slot when a required earlier slot in that team's bracket path has been resolved by `Admin_/official` to a different team.
li/world_cup/player_standings_max_possible_reachability_rule.md:30:If a player picked Brazil to win R16, R8, R4, R2, and Champion, but `Admin_/official` resolves Brazil as losing in R16, then Brazil's later R8/R4/R2/Champion picks no longer count toward Max Possible.
li/world_cup/player_standings_max_possible_reachability_rule.md:34:`Admin_/official` is the only source of elimination and scoring truth.
li/world_cup/hydrate_only_supabase_admin_r32_into_player_picks_rule.md:1:# Hydrate only Supabase Admin R32 into player picks rule
li/world_cup/hydrate_only_supabase_admin_r32_into_player_picks_rule.md:3:Copy ONLY R32 entrant slots from Supabase Admin_/official into player BracketDocument picks.
li/world_cup/hydrate_only_supabase_admin_r32_into_player_picks_rule.md:5:Player-visible R32 may be stored in player `picksBySlot` for rendering, scoring, and R16++ preselection compatibility, but it is not player-authored. Hydrated R32 records must carry Admin_/official source/authority metadata and `playerAuthored: false`.
li/world_cup/hydrate_only_supabase_admin_r32_into_player_picks_rule.md:7:Do not copy Admin_/official R16, QF, SF, Final, Champion, or third-place picks into player documents. Player R16++ picks remain player-owned.
li/world_cup/hydrate_only_supabase_admin_r32_into_player_picks_rule.md:9:Do not copy R32 from localStorage, static JSON, bundled data, or stale player documents. If Supabase Admin R32 is missing, keep player R32 unset/fail-closed.
li/world_cup/knockout_only_game_model.md:7:`Admin_/official` owns the R32 field. The R32 field means the team occupants assigned to the official Round-of-32 match slots.
li/world_cup/knockout_only_game_model.md:9:Non-admin players may render R32 occupants from `Admin_/official`, but non-admin players cannot author R32 occupants. A player bracket must not treat group winners, group runners-up, third-place qualifiers, or R32 team occupants as player-authored picks.
li/world_cup/knockout_only_game_model.md:20:This CB is LI-only and does not change runtime behavior. Future runtime CBs should implement official R32 hydration first. Future UI CBs should then remove or rename Game 1/Game 2 and group-prediction language so the product copy matches this knockout-only model.
li/world_cup/player_standings_scoring_rule.md:3:Player Standings must compute each player's earned points and maximum possible points from the player's submitted/live bracket picks compared against `Admin_/official` result truth.
li/world_cup/player_standings_scoring_rule.md:29:A player's earned points are the sum of weighted player picks that match resolved `Admin_/official` result truth.
li/world_cup/player_standings_scoring_rule.md:34:2. `Admin_/official` has resolved truth for that slot.
li/world_cup/player_standings_scoring_rule.md:52:`Admin_/official` is the only source of scoring truth.
li/world_cup/player_standings_scoring_rule.md:54:Normal player picks never define official results. Normal player picks are compared against `Admin_/official` truth.
li/world_cup/r32_pick_card_rendering_rule.md:46:For Game 1, the R32 card represents the Admin_/official hydrated occupant for that slot. In normal player mode it is not a player-authored qualifier prediction. A player BracketDocument may carry the R32 occupant for rendering/preselection compatibility only when that record was copied from Supabase Admin_/official and marked `playerAuthored: false`.
li/world_cup/official_r32_hydration_rule.md:1:# Official R32 Hydration Rule
li/world_cup/official_r32_hydration_rule.md:4:`Admin_/official` owns the R32 field. Non-admin players cannot author R32 occupants.
li/world_cup/official_r32_hydration_rule.md:6:Non-admin player brackets may render R32 occupants, but those occupants are official input copied from `Admin_/official`, not player-owned picks.
li/world_cup/official_r32_hydration_rule.md:9:Hydration must copy `Admin_/official` R32 occupants into non-admin player BracketDocuments at creation, load, import, and save boundaries.
li/world_cup/official_r32_hydration_rule.md:14:BracketDocument remains the persistence container. The official R32 occupants may be present inside each non-admin BracketDocument after hydration, but their authority remains `Admin_/official`.
li/world_cup/admin_r32_hydration_compatibility_model_rule.md:1:# Admin R32 hydration compatibility model rule
li/world_cup/admin_r32_hydration_compatibility_model_rule.md:3:Current Bracketeering is knockout-only. Admin_/official owns R32 occupant truth. Normal players do not assign, project, or predict R32 occupants.
li/world_cup/admin_r32_hydration_compatibility_model_rule.md:5:Player BracketDocuments may contain R32 entrant records only as Supabase Admin_/official hydrated mirror entries. Those records exist for rendering, scoring, standings, and R16++ preselection compatibility, not player authorship.
li/world_cup/admin_r32_hydration_compatibility_model_rule.md:7:Hydrated R32 records must be copied ONLY from the Supabase Admin_/official official bracket document. They must carry Admin_/official source/authority metadata and `playerAuthored: false`.
li/world_cup/admin_r32_hydration_compatibility_model_rule.md:9:Admin_/official R16, QF, SF, Final, Champion, and third-place truth must never be copied into normal player BracketDocuments. Normal players own R32 match-winner and later-round picks. Existing player R16++ picks must survive R32 hydration.
li/world_cup/admin_official_full_bracket_editor_mode_rule.md:3:`Admin_/official` may edit every official bracket truth slot.
li/world_cup/admin_official_full_bracket_editor_mode_rule.md:7:`Admin_/official` edits must save to the Supabase `Admin_/official` official bracket document.
li/world_cup/admin_official_full_bracket_editor_mode_rule.md:10:Player-visible R32 always mirrors `Admin_/official` R32 truth. localStorage/static JSON must not masquerade as public official truth.
li/world_cup/admin_official_r32_editor_mode_rule.md:3:Only Admin_/official may edit R32 occupant slots.
li/world_cup/admin_official_r32_editor_mode_rule.md:4:All players mirror Admin_/official R32 occupant truth.
li/world_cup/admin_official_r32_editor_mode_rule.md:6:Admin_/official authors R32 through an explicit editor mode. Non-admin player boards must not receive R32 authoring choices and must continue to hydrate R32 from the Supabase `Admin_/official` official bracket document.
li/world_cup/official_r32_as_player_feeder_teams_rule.md:19:Now, Admin_/official authors R32 occupants. Normal players must see those R32 occupants as read-only official truth, and the existing bracket feeder system must treat those official occupants as the selected teams for R32.
li/world_cup/official_r32_as_player_feeder_teams_rule.md:32:- new R32 selected-team source: Admin_/official truth
li/world_cup/official_r32_as_player_feeder_teams_rule.md:36:- every R32 display slot resolves its selected team from Admin_/official truth;
li/world_cup/official_r32_as_player_feeder_teams_rule.md:39:- when an R16 feeder slot is R32, that feeder’s selected team comes from Admin_/official truth;
li/world_cup/official_r32_as_player_feeder_teams_rule.md:48:2. Admin_/official owns R32 occupants.
docs/features/admin_r32_hydration_compatibility_model.md:1:# Admin R32 hydration compatibility model
docs/features/admin_r32_hydration_compatibility_model.md:5:Admin_/official owns the R32 occupant field. Normal players do not author R32 occupants, but their BracketDocuments may store R32 entries copied from Supabase Admin_/official so existing rendering, standings, scoring, and R16++ preselection paths continue to work.
docs/features/admin_r32_hydration_compatibility_model.md:10:- Copy ONLY from Supabase Admin_/official.
docs/features/admin_r32_hydration_compatibility_model.md:11:- Mark copied R32 entries with Admin_/official source/authority metadata and `playerAuthored: false`.
docs/features/admin_r32_hydration_compatibility_model.md:12:- Do not copy Admin_/official R16, QF, SF, Final, Champion, or third-place truth into player documents.
docs/features/force_player_r32_matches_admin_official.md:1:# Force player R32 display to match Admin_/official
docs/features/force_player_r32_matches_admin_official.md:5:`playerVisibleR32 = Admin_/official R32 truth`.
docs/features/force_player_r32_matches_admin_official.md:7:R32 picks/occupants are not player picks. R32 occupants are not player-authored picks. They are owned by `Admin_/official` in Supabase. Player BracketDocuments may store hydrated R32 mirror records for rendering, scoring, and R16++ preselection compatibility, but those records must be copied only from Supabase Admin_/official and marked `playerAuthored: false`.
docs/features/force_player_r32_matches_admin_official.md:13:- read the Supabase `Admin_/official` official bracket document on app startup
docs/features/force_player_r32_matches_admin_official.md:16:- copy ONLY Supabase Admin_/official R32 entrants into player `picksBySlot` as mirror records
docs/features/force_player_r32_matches_admin_official.md:20:- fail closed when `Admin_/official` is missing or unreadable
docs/features/force_player_r32_matches_admin_official.md:22:Partial Admin truth is valid. If `Admin_/official` has one R32 occupant, the player board shows exactly one R32 occupant and leaves the rest unset. Static JSON and localStorage must not complete the field in public runtime.
docs/features/force_player_r32_matches_admin_official.md:28:- Admin_/official R32 truth
docs/features/force_player_r32_matches_admin_official.md:43:The main board model hydrates ONLY Supabase Admin_/official R32 entrants into player `picksBySlot`. Rendering and R16++ preselection can then use the existing player-document path, while normal player R32 `setPick` calls remain rejected and stale local/static R32 values remain invalid copy sources.
docs/features/player_standings_max_possible_reachability.md:5:An unresolved Admin slot does not automatically count as possible. The player's pick for that slot must still be reachable under already-resolved `Admin_/official` truth.
docs/features/player_standings_max_possible_reachability.md:12:2. `Admin_/official` has not resolved that slot yet, and
docs/features/game1_tap_chooser_playfield_note.md:5:The HTML/CSS adds transparent hit-test areas over each R32 cell. Under the current model, normal players do not choose R32 occupants; Admin_/official editor mode may use those slot rules to author official R32 truth.
docs/features/game1_data_driven_slot_menu.md:39:Maps a tapped R32 slot to its eligible teams only for Admin_/official R32 editing. Normal players do not store player-authored R32 occupant picks.
docs/features/official_r32_as_player_feeder_teams.md:19:Now, Admin_/official authors R32 occupants. Normal players must see those R32 occupants as read-only official truth, and the existing bracket feeder system must treat those official occupants as the selected teams for R32.
docs/features/official_r32_as_player_feeder_teams.md:32:- new R32 selected-team source: Admin_/official truth
docs/features/official_r32_as_player_feeder_teams.md:36:- every R32 display slot resolves its selected team from Admin_/official truth;
docs/features/official_r32_as_player_feeder_teams.md:39:- when an R16 feeder slot is R32, that feeder’s selected team comes from Admin_/official truth;
docs/features/official_r32_as_player_feeder_teams.md:48:2. Admin_/official owns R32 occupants.
docs/features/player_standings_scoring.md:3:Player Standings computes earned points and maximum possible points by comparing player picks against `Admin_/official` result truth.
docs/features/player_standings_scoring.md:17:Earned points are awarded only for resolved official slots where the player's canonical team ID matches the `Admin_/official` canonical team ID.
docs/features/admin_official_full_bracket_editor_mode.md:5:Allow the `Admin_/official` identity to edit all official bracket truth slots, not just R32, while preserving normal player ownership rules.
docs/features/admin_official_full_bracket_editor_mode.md:9:`Admin_/official` owns official bracket truth.
docs/features/admin_official_full_bracket_editor_mode.md:11:Player-visible R32 always mirrors `Admin_/official`.
docs/features/admin_official_full_bracket_editor_mode.md:15:- If active identity is `Admin_/official`, every bracket slot is editable.
docs/features/admin_official_full_bracket_editor_mode.md:16:- `Admin_/official` edits save to the Supabase `Admin_/official` bracket document.
docs/features/admin_official_full_bracket_editor_mode.md:17:- If active identity is not `Admin_/official`, R32 remains read-only.
docs/features/admin_official_full_bracket_editor_mode.md:18:- If active identity is not `Admin_/official`, R16++ remains normal player-editable picks.
docs/features/admin_official_full_bracket_editor_mode.md:20:- `Admin_/official` editing must not write into a normal player bracket.
docs/features/admin_official_full_bracket_editor_mode.md:21:- Normal player editing must not write into the `Admin_/official` bracket.
docs/features/admin_official_full_bracket_editor_mode.md:29:- Normal player mode keeps R32 as a read-only projection from `Admin_/official` and writes later picks only to the player document.
docs/features/admin_official_full_bracket_editor_mode.md:30:- R32 mirror behavior remains exact and partial: if `Admin_/official` has one R32 value, players see exactly one.
docs/features/admin_official_full_bracket_editor_mode.md:34:- `Admin_/official` can edit R32, R16, QF, SF, Final, and Champion slots.
docs/features/admin_official_full_bracket_editor_mode.md:35:- `Admin_/official` edits save to the `Admin_/official` Supabase bracket document.
docs/features/admin_official_full_bracket_editor_mode.md:38:- A normal player sees `Admin_/official` R32 values after hydration.
docs/features/admin_official_full_bracket_editor_mode.md:39:- If `Admin_/official` changes an R32 value, player display changes to match.
docs/features/admin_official_full_bracket_editor_mode.md:40:- `Admin_/official` later-round truth remains separate from normal player picks.
docs/features/admin_official_r32_editor_mode.md:5:Only Admin_/official may edit R32 occupant slots.
docs/features/admin_official_r32_editor_mode.md:6:All players mirror Admin_/official R32 occupant truth.
docs/features/admin_official_r32_editor_mode.md:10:R32 occupant slots are official truth fields, not normal player picks. The public player board continues to hydrate R32 from the Supabase `Admin_/official` bracket document and refuses normal player R32 authoring.
docs/features/admin_official_r32_editor_mode.md:12:A separate explicit Admin_/official editor mode may reopen R32 slot menus for the official row only:
docs/features/admin_official_r32_editor_mode.md:14:- `?adminOfficialR32Editor=1` enables Admin_/official R32 editor mode.
docs/features/admin_official_r32_editor_mode.md:16:- R32 edits are written to the Supabase `Admin_/official` row with `bracket_kind = official`.
docs/features/admin_official_r32_editor_mode.md:17:- The saved records are R32 entrant records with `source = Admin_/official` and `authority = Admin_/official`.
docs/features/admin_official_r32_editor_mode.md:19:- Normal players continue to see exactly the Admin_/official R32 truth, including partial truth.
docs/features/admin_official_r32_editor_mode.md:30:Admin_/official authors R32.
docs/features/official_truth_bracket_as_hidden_player.md:5:- `bracket_kind = official`
docs/features/official_truth_bracket_as_hidden_player.md:13:1. `bracket_kind = official` must not appear in the Players panel.
docs/features/unified_game1_game2_bracket_lifecycle.md:3:This document is a historical lifecycle note. It is superseded by the current knockout-only Admin_/official R32 authority model, but remains useful for geometry/lifecycle context.
docs/features/unified_game1_game2_bracket_lifecycle.md:10:### Phase 1 — Admin_/official Round of 32 occupant setup
docs/features/unified_game1_game2_bracket_lifecycle.md:11:Admin_/official assigns official R32 occupants. Normal players do not assign, project, or predict R32 occupants.
docs/features/unified_game1_game2_bracket_lifecycle.md:14:When both teams for a bracket match are known from hydrated Supabase Admin_/official R32 entrants or upstream player-owned winners, the app may allow the player to pick a winner for that match.
docs/features/unified_game1_game2_bracket_lifecycle.md:17:When Admin_/official has entered official R32 occupants, player BracketDocuments may store those R32 entries as hydrated mirror records for rendering and R16++ preselection. These entries are copied only from Supabase Admin_/official and are not scored as player-authored predictions.
docs/features/unified_game1_game2_bracket_lifecycle.md:20:The Supabase Admin_/official Round of 32 is the canonical starting truth for knockout play. Static JSON, localStorage, and stale player documents must not supply public R32 truth.
docs/features/unified_game1_game2_bracket_lifecycle.md:31:- Admin_/official R32 slot occupant
docs/features/unified_game1_game2_bracket_lifecycle.md:35:- Admin_/official later-round official truth, which must not be copied into player documents
docs/features/single_game_admin_official_runtime.md:1:# Single Game Admin_/official Runtime
docs/features/single_game_admin_official_runtime.md:7:- Admin_/official owns R32 occupants in a public locked/submitted Supabase row.
docs/features/game1_r32_pick_controller.md:5:Legacy note: this controller described the old player-authored R32 projection model. Current Bracketeering rules supersede that behavior: Admin_/official owns R32 occupant truth, and normal players do not project or assign R32 occupants.
docs/features/game1_r32_pick_controller.md:27:- legacy local persistence; current public R32 occupant truth must come only from Supabase Admin_/official
docs/features/hydrate_only_supabase_admin_r32_into_player_picks.md:1:# Hydrate only Supabase Admin R32 into player picks
docs/features/hydrate_only_supabase_admin_r32_into_player_picks.md:5:Restore player-site R16++ preselection by materializing Supabase Admin_/official R32 occupants into each player BracketDocument, while copying no Admin later-round truth.
docs/features/hydrate_only_supabase_admin_r32_into_player_picks.md:9:Copy ONLY R32 entrant slots from Supabase Admin_/official into player picks.
docs/features/hydrate_only_supabase_admin_r32_into_player_picks.md:11:Do not copy Admin_/official R16, QF, SF, Final, Champion, or third-place truth into a player bracket. Player R16++ picks remain player-owned and must survive hydration.
docs/features/hydrate_only_supabase_admin_r32_into_player_picks.md:15:The only valid copy source is Supabase Admin_/official. R32 must not be copied from localStorage, static JSON, bundled data, or stale player documents.
docs/features/hydrate_only_supabase_admin_r32_into_player_picks.md:17:If Supabase Admin R32 is missing or unreadable, player R32 remains unset/fail-closed and R16++ preselection remains unavailable.
docs/features/hydrate_only_supabase_admin_r32_into_player_picks.md:24:2. Load the Supabase Admin_/official official bracket document.
docs/features/hydrate_only_supabase_admin_r32_into_player_picks.md:25:3. Copy only Admin R32 entrant slots into the player picks map.
docs/features/hydrate_only_supabase_admin_r32_into_player_picks.md:26:4. Mark copied R32 entries with `source: "Admin_/official"`, `authority: "Admin_/official"`, `playerAuthored: false`, and `hydratedFrom: "Supabase:Admin_/official"`.
docs/features/game1_r16_winner_picks.md:23:- Admin_/official hydrated R32 slot occupant
docs/features/official_r32_hydration.md:1:# Official R32 Hydration
docs/features/official_r32_hydration.md:6:`Admin_/official` owns the R32 field. Non-admin players cannot author R32 occupants. Non-admin player brackets may render those R32 occupants so every player starts from the same official field.
docs/features/official_r32_hydration.md:14:Hydration must copy `Admin_/official` R32 occupants into non-admin player BracketDocuments at creation, load, import, and save boundaries.
docs/features/official_r32_hydration.md:32:Runtime hydration treats `Admin_/official` as the R32 authority. Non-admin BracketDocuments may carry hydrated R32 entrant records with `source: "Admin_/official"`, `authority: "Admin_/official"`, and `playerAuthored: false`, but player action cannot author those entrant records.
docs/features/official_r32_hydration.md:38:## Supabase Admin_/official source
docs/features/official_r32_hydration.md:39:Production official R32 hydration now reads the Supabase `Admin_/official` bracket row as the primary authority. The explicit runtime authority path is `SupabaseBracketStore.loadOfficialR32BracketAuthority`, which loads `user_id = "Admin_/official"`, `tournament_id = "wc2026"`, and `game_id = "game1"` from the existing row-per-user-per-game `user_brackets` table.
docs/features/official_r32_hydration.md:43:Hydrated non-admin R32 entrant records must retain `source: "Admin_/official"`, `authority: "Admin_/official"`, `playerAuthored: false`, and `hydratedFrom: "Supabase:Admin_/official"` when Supabase authority is available. Player actions still cannot author R32 entrants, and existing player-owned knockout winner picks are preserved.
docs/features/admin_official_results_truth.md:1:# Admin_/official results truth
docs/features/admin_official_results_truth.md:3:WC2026 Bracketeering uses `Admin_/official` as the source of official tournament truth.
docs/features/admin_official_results_truth.md:8:R32 entrants = Admin_/official entrant truth
docs/features/admin_official_results_truth.md:9:Official results/winners = Admin_/official result truth
docs/features/admin_official_results_truth.md:11:Scoring = player predictions compared against Admin_/official truth
docs/features/admin_official_results_truth.md:14:The `Admin_/official` row may be partial while the tournament is being set up or results are being entered. Partial truth is still authoritative. Empty official winner slots do not score yet; they are not filled from player picks or static fallback data.
docs/features/admin_official_results_truth.md:26:Static fallback data is only a local/dev missing-admin-source fallback. It must not override an existing `Admin_/official` source, including a partial source.
cards/292_player_standings_scoring_rule_card.md:19:- Earned points compare player picks against `Admin_/official` truth.
cards/1018_admin_official_full_bracket_editor_mode_card.md:5:Allow the `Admin_/official` identity to edit all official bracket truth slots while preserving player ownership rules.
cards/1018_admin_official_full_bracket_editor_mode_card.md:16:`Admin_/official` owns official bracket truth.
cards/1018_admin_official_full_bracket_editor_mode_card.md:18:Player-visible R32 always mirrors `Admin_/official`.
cards/1020_admin_r32_hydration_compatibility_model_card.md:1:# Card 1020: Admin R32 hydration compatibility model
cards/1020_admin_r32_hydration_compatibility_model_card.md:9:Admin_/official owns R32 occupant truth. Player BracketDocuments may store R32 entries only as Supabase Admin_/official hydrated mirror entries with `playerAuthored: false`. Normal players own R32 match-winner and later picks.
cards/116_add_bracket_lifecycle_state_card.md:21:- Admin_/official R32 occupant truth mirrored into player BracketDocuments with `playerAuthored: false`
cards/1017_admin_official_r32_editor_mode_card.md:5:Allow the Admin_/official bracket identity to author and edit R32 occupant truth while keeping all non-admin player brackets read-only for R32.
cards/1017_admin_official_r32_editor_mode_card.md:9:Only Admin_/official may edit R32 occupant slots.
cards/1017_admin_official_r32_editor_mode_card.md:10:All players mirror Admin_/official R32 occupant truth.
cards/1017_admin_official_r32_editor_mode_card.md:15:- Reopen R32 choices only in Admin_/official editor mode.
cards/1017_admin_official_r32_editor_mode_card.md:16:- Save Admin_/official R32 edits to the Supabase official bracket row.
cards/1017_admin_official_r32_editor_mode_card.md:22:`tools/verify_wc2026_admin_official_r32_editor_mode.py` proves that Admin_/official can edit R32 truth while normal players cannot.
cards/287_official_r32_as_player_feeder_teams_card.md:19:Now, Admin_/official authors R32 occupants. Normal players must see those R32 occupants as read-only official truth, and the existing bracket feeder system must treat those official occupants as the selected teams for R32.
cards/287_official_r32_as_player_feeder_teams_card.md:32:- new R32 selected-team source: Admin_/official truth
cards/287_official_r32_as_player_feeder_teams_card.md:36:- every R32 display slot resolves its selected team from Admin_/official truth;
cards/287_official_r32_as_player_feeder_teams_card.md:39:- when an R16 feeder slot is R32, that feeder’s selected team comes from Admin_/official truth;
cards/287_official_r32_as_player_feeder_teams_card.md:48:2. Admin_/official owns R32 occupants.
cards/288_single_game_admin_official_runtime_card.md:1:# Card 288: Single Game Admin_/official Runtime
cards/288_single_game_admin_official_runtime_card.md:12:- Admin_/official missing-row create mode
cards/288_single_game_admin_official_runtime_card.md:17:`make verify` includes the single-game Admin_/official runtime verifier.
cards/1013_supabase_admin_official_r32_source_card.md:1:# Card 1013 — Supabase Admin_/official R32 Source
cards/1013_supabase_admin_official_r32_source_card.md:4:Make the Supabase `Admin_/official` bracket row the production authority for official R32 hydration.
cards/1013_supabase_admin_official_r32_source_card.md:8:- It loads the row-per-user-per-game `user_brackets` row for `user_id = "Admin_/official"`, `tournament_id = "wc2026"`, and `game_id = "game1"`.
cards/1013_supabase_admin_official_r32_source_card.md:9:- `BracketRepository.loadOfficialR32Source` tries Supabase Admin_/official first.
cards/1013_supabase_admin_official_r32_source_card.md:15:- `source: "Admin_/official"`
cards/1013_supabase_admin_official_r32_source_card.md:16:- `authority: "Admin_/official"`
cards/1013_supabase_admin_official_r32_source_card.md:18:- `hydratedFrom: "Supabase:Admin_/official"` when Supabase authority is available
cards/286_official_truth_bracket_as_hidden_player_card.md:5:- `bracket_kind = official`
cards/286_official_truth_bracket_as_hidden_player_card.md:13:1. `bracket_kind = official` must not appear in the Players panel.
cards/1016_force_player_r32_matches_admin_official_card.md:1:# Card 1016 — Force player R32 display to match Admin_/official
cards/1016_force_player_r32_matches_admin_official_card.md:7:`playerVisibleR32 = Admin_/official R32 truth`.
cards/1016_force_player_r32_matches_admin_official_card.md:11:- R32 picks/occupants are not player picks. They are Admin_/official-owned truth.
cards/1016_force_player_r32_matches_admin_official_card.md:13:- R32 display slots project from Supabase `Admin_/official` only.
cards/1016_force_player_r32_matches_admin_official_card.md:19:- A partial Admin_/official R32 truth document renders exactly partial.
cards/1016_force_player_r32_matches_admin_official_card.md:21:- LocalStorage cannot override Admin_/official R32 truth.
cards/1016_force_player_r32_matches_admin_official_card.md:22:- Static JSON cannot complete public R32 when Admin_/official is required.
cards/295_player_standings_max_possible_reachability_card.md:11:- Prior resolved Admin_/official results can eliminate later player picks from Max Possible.
cards/295_player_standings_max_possible_reachability_card.md:12:- Score remains based only on resolved Admin_/official matches.
cards/1011_official_r32_hydration_rule_card.md:1:# Card 1011: Official R32 Hydration Rule
cards/1011_official_r32_hydration_rule_card.md:4:Define the official R32 hydration LI for the simplified knockout-only Bracketeering game before runtime implementation.
cards/1011_official_r32_hydration_rule_card.md:16:- `Admin_/official` owns the R32 field.
cards/1012_official_r32_hydration_runtime_card.md:1:# Card 1012: Official R32 Hydration Runtime Boundary
cards/1012_official_r32_hydration_runtime_card.md:4:Implement the LI-defined runtime/model boundary for official R32 hydration without UI copy cleanup.
cards/1012_official_r32_hydration_runtime_card.md:17:- Admin_/official is the authority for R32 occupants.
cards/1014_admin_official_results_truth_card.md:1:# Card 1014: Admin_/official results truth
cards/1014_admin_official_results_truth_card.md:5:Make `Admin_/official` the official result-truth source used by standings, scoring comparison, and read-only player board comparison.
cards/1014_admin_official_results_truth_card.md:9:- `Admin_/official` owns official R32 entrants and official result winners.
cards/1014_admin_official_results_truth_card.md:19:- It separates the `Admin_/official` row from player rows.
cards/1014_admin_official_results_truth_card.md:21:- Read-only board viewer rows carry `officialTruthPicksBySlot` and `officialResultsTruthSource` for comparison display.
cards/1019_hydrate_only_supabase_admin_r32_into_player_picks_card.md:1:# Card 1019: Hydrate only Supabase Admin R32 into player picks
cards/1019_hydrate_only_supabase_admin_r32_into_player_picks_card.md:5:Restore player-site R16++ preselection by materializing Supabase Admin_/official R32 occupants into player picks while copying no Admin later-round official truth.
cards/1019_hydrate_only_supabase_admin_r32_into_player_picks_card.md:7:Copy ONLY R32 from Supabase Admin_/official.
cards/1019_hydrate_only_supabase_admin_r32_into_player_picks_card.md:11:- Add a model hydration path that strips stale player/local R32 values and then copies ONLY R32 from Supabase Admin_/official.
captures/CAPTURE_BACK_OFFICIAL_R32_HYDRATION_RUNTIME.md:1:# Capture Back: Official R32 Hydration Runtime Boundary
captures/CAPTURE_BACK_OFFICIAL_R32_HYDRATION_RUNTIME.md:4:Implemented the runtime/model boundary for official R32 hydration.
captures/CAPTURE_BACK_OFFICIAL_R32_HYDRATION_RUNTIME.md:10:- `Admin_/official` is the authority for R32 occupants.
captures/CAPTURE_BACK_OFFICIAL_R32_AS_PLAYER_FEEDER_TEAMS.md:19:Now, Admin_/official authors R32 occupants. Normal players must see those R32 occupants as read-only official truth, and the existing bracket feeder system must treat those official occupants as the selected teams for R32.
captures/CAPTURE_BACK_OFFICIAL_R32_AS_PLAYER_FEEDER_TEAMS.md:32:- new R32 selected-team source: Admin_/official truth
captures/CAPTURE_BACK_OFFICIAL_R32_AS_PLAYER_FEEDER_TEAMS.md:36:- every R32 display slot resolves its selected team from Admin_/official truth;
captures/CAPTURE_BACK_OFFICIAL_R32_AS_PLAYER_FEEDER_TEAMS.md:39:- when an R16 feeder slot is R32, that feeder’s selected team comes from Admin_/official truth;
captures/CAPTURE_BACK_OFFICIAL_R32_AS_PLAYER_FEEDER_TEAMS.md:48:2. Admin_/official owns R32 occupants.
captures/CAPTURE_BACK_OFFICIAL_TRUTH_BRACKET_AS_HIDDEN_PLAYER.md:5:- `bracket_kind = official`
captures/CAPTURE_BACK_OFFICIAL_TRUTH_BRACKET_AS_HIDDEN_PLAYER.md:13:1. `bracket_kind = official` must not appear in the Players panel.
captures/CAPTURE_BACK_HYDRATE_ONLY_SUPABASE_ADMIN_R32_INTO_PLAYER_PICKS.md:1:# Capture Back: Hydrate only Supabase Admin R32 into player picks
captures/CAPTURE_BACK_HYDRATE_ONLY_SUPABASE_ADMIN_R32_INTO_PLAYER_PICKS.md:9:Copy ONLY R32 entrant slots from Supabase Admin_/official into each player BracketDocument. Do not copy any Admin_/official later-round official truth.
captures/CAPTURE_BACK_HYDRATE_ONLY_SUPABASE_ADMIN_R32_INTO_PLAYER_PICKS.md:13:- Supabase Admin_/official remains the only R32 authority.
captures/CAPTURE_BACK_HYDRATE_ONLY_SUPABASE_ADMIN_R32_INTO_PLAYER_PICKS.md:18:- Missing Supabase Admin R32 fails closed, leaving R32 unset and R16++ preselection unavailable.
captures/CAPTURE_BACK_HYDRATE_ONLY_SUPABASE_ADMIN_R32_INTO_PLAYER_PICKS.md:24:- Copy ONLY R32 from Supabase Admin_/official.
captures/CAPTURE_BACK_HYDRATE_ONLY_SUPABASE_ADMIN_R32_INTO_PLAYER_PICKS.md:28:- Stale player/local R32 is overwritten by Supabase Admin R32.
captures/CAPTURE_BACK_HYDRATE_ONLY_SUPABASE_ADMIN_R32_INTO_PLAYER_PICKS.md:29:- Missing Supabase Admin R32 remains unset/fail-closed.
captures/CAPTURE_BACK_ADMIN_OFFICIAL_FULL_BRACKET_EDITOR_MODE.md:5:Added Admin official full bracket editor mode so the `Admin_/official` identity can edit all official bracket truth slots, not just R32.
captures/CAPTURE_BACK_ADMIN_OFFICIAL_FULL_BRACKET_EDITOR_MODE.md:9:- `Admin_/official` owns official bracket truth.
captures/CAPTURE_BACK_ADMIN_OFFICIAL_FULL_BRACKET_EDITOR_MODE.md:11:- Player-visible R32 always mirrors `Admin_/official`.
captures/CAPTURE_BACK_ADMIN_OFFICIAL_FULL_BRACKET_EDITOR_MODE.md:20:Admin_/official editor selection -> officialPicks -> Supabase Admin_/official bracket document
captures/CAPTURE_BACK_ADMIN_OFFICIAL_FULL_BRACKET_EDITOR_MODE.md:32:playerVisibleR32 = Admin_/official R32 truth
captures/CAPTURE_BACK_ADMIN_OFFICIAL_R32_EDITOR_MODE.md:5:Only Admin_/official may edit R32 occupant slots.
captures/CAPTURE_BACK_ADMIN_OFFICIAL_R32_EDITOR_MODE.md:6:All players mirror Admin_/official R32 occupant truth.
captures/CAPTURE_BACK_ADMIN_OFFICIAL_R32_EDITOR_MODE.md:8:This capture adds an explicit Admin_/official R32 editor mode. The normal public/player runtime remains read-only for R32 and continues to force player-visible R32 from Supabase `Admin_/official`.
captures/CAPTURE_BACK_ADMIN_OFFICIAL_R32_EDITOR_MODE.md:12:- Normal player mode: R32 is read-only and mirrors Admin_/official.
captures/CAPTURE_BACK_ADMIN_OFFICIAL_R32_EDITOR_MODE.md:13:- Admin_/official editor mode: R32 slots become editable and save back to the Supabase `Admin_/official` official bracket document.
captures/CAPTURE_BACK_ADMIN_OFFICIAL_RESULTS_TRUTH.md:1:# Capture Back: Admin_/official results truth
captures/CAPTURE_BACK_ADMIN_OFFICIAL_RESULTS_TRUTH.md:5:`Admin_/official` is the source of official results truth for WC2026 Bracketeering.
captures/CAPTURE_BACK_ADMIN_OFFICIAL_RESULTS_TRUTH.md:9:- R32 entrants are official `Admin_/official` entrant truth.
captures/CAPTURE_BACK_ADMIN_OFFICIAL_RESULTS_TRUTH.md:10:- Official results and resolved winners are `Admin_/official` result truth.
captures/CAPTURE_BACK_ADMIN_OFFICIAL_RESULTS_TRUTH.md:12:- Scoring compares player predictions against `Admin_/official` truth.
captures/CAPTURE_BACK_ADMIN_OFFICIAL_RESULTS_TRUTH.md:16:The Supabase standings store reads both player rows and the `Admin_/official` official row from `user_brackets`. The official row is normalized as an Admin truth document and is not rendered as a player standings participant. Player rows are scored against the official truth picks by slot.
captures/CAPTURE_BACK_ADMIN_OFFICIAL_RESULTS_TRUTH.md:18:Partial official truth is allowed during setup/testing. Missing official winner slots simply do not score yet. The static JSON fallback remains a local/dev fallback only when an admin source is unavailable; it must not override an existing `Admin_/official` row.
captures/CAPTURE_BACK_PLAYER_STANDINGS_SCORING_RULE.md:26:Earned points come only from player picks that match resolved `Admin_/official` truth.
captures/CAPTURE_BACK_SINGLE_GAME_ADMIN_OFFICIAL_RUNTIME.md:1:# Capture Back: Single Game Admin_/official Runtime
captures/CAPTURE_BACK_SINGLE_GAME_ADMIN_OFFICIAL_RUNTIME.md:13:- Require Admin_/official Supabase R32 authority for player rendering.
captures/CAPTURE_BACK_OFFICIAL_R32_HYDRATION_RULE.md:1:# Capture Back: Official R32 Hydration Rule
captures/CAPTURE_BACK_OFFICIAL_R32_HYDRATION_RULE.md:4:Defined the official R32 hydration LI for the simplified knockout-only Bracketeering game model.
captures/CAPTURE_BACK_OFFICIAL_R32_HYDRATION_RULE.md:9:- `Admin_/official` owns the R32 field.
captures/CAPTURE_BACK_PLAYER_STANDINGS_MAX_POSSIBLE_REACHABILITY.md:9:A player earns Score points when their pick matches `Admin_/official` truth.
captures/CAPTURE_BACK_ADMIN_R32_HYDRATION_COMPATIBILITY_MODEL.md:1:# Capture Back: Admin R32 hydration compatibility model
captures/CAPTURE_BACK_ADMIN_R32_HYDRATION_COMPATIBILITY_MODEL.md:7:- Admin_/official owns R32 occupant truth.
captures/CAPTURE_BACK_ADMIN_R32_HYDRATION_COMPATIBILITY_MODEL.md:9:- Player BracketDocuments may store R32 entries only as Supabase Admin_/official hydrated mirror entries.
captures/CAPTURE_BACK_ADMIN_R32_HYDRATION_COMPATIBILITY_MODEL.md:11:- Admin_/official later-round truth must not be copied into player documents.
captures/CAPTURE_BACK_FORCE_PLAYER_R32_MATCHES_ADMIN_OFFICIAL.md:1:# Capture Back: force player R32 display to match Admin_/official
captures/CAPTURE_BACK_FORCE_PLAYER_R32_MATCHES_ADMIN_OFFICIAL.md:5:Make the public player site always display R32 occupant slots from the Supabase `Admin_/official` official bracket document.
captures/CAPTURE_BACK_FORCE_PLAYER_R32_MATCHES_ADMIN_OFFICIAL.md:9:`playerVisibleR32 = Admin_/official R32 truth`.
captures/CAPTURE_BACK_FORCE_PLAYER_R32_MATCHES_ADMIN_OFFICIAL.md:16:- Made R32 display slots resolve through Admin_/official truth instead of player/local picks.
captures/CAPTURE_BACK_FORCE_PLAYER_R32_MATCHES_ADMIN_OFFICIAL.md:20:- Added fail-closed Admin_/official R32 documents for missing/unreadable official truth.
captures/CAPTURE_BACK_FORCE_PLAYER_R32_MATCHES_ADMIN_OFFICIAL.md:27:- the main player board uses Supabase Admin_/official as the official R32 source
captures/CAPTURE_BACK_FORCE_PLAYER_R32_MATCHES_ADMIN_OFFICIAL.md:28:- R32 display is projected from Admin_/official
captures/CAPTURE_BACK_FORCE_PLAYER_R32_MATCHES_ADMIN_OFFICIAL.md:36:If `Admin_/official` has only Germany in R32, the player site must show exactly Germany in that official R32 slot and no additional fake R32 occupants.
captures/CAPTURE_BACK_SUPABASE_ADMIN_OFFICIAL_R32_SOURCE.md:1:# Capture Back — Supabase Admin_/official R32 Source
captures/CAPTURE_BACK_SUPABASE_ADMIN_OFFICIAL_R32_SOURCE.md:4:Official R32 hydration is now sourced from the Supabase `Admin_/official` bracket row as the primary production authority.
captures/CAPTURE_BACK_SUPABASE_ADMIN_OFFICIAL_R32_SOURCE.md:8:- Added `BracketRepository.loadOfficialR32Source`, which tries Supabase Admin_/official first and only then falls back to static JSON.
captures/CAPTURE_BACK_SUPABASE_ADMIN_OFFICIAL_R32_SOURCE.md:9:- Tagged Supabase-derived hydration as `Supabase:Admin_/official`.
captures/CAPTURE_BACK_SUPABASE_ADMIN_OFFICIAL_R32_SOURCE.md:23:The verifier fails if production hydration only reads static `site/data/official_round_of_32.json`. It passes only when the Supabase `Admin_/official` load path is present and BracketRepository prefers it before static fallback.
tools/verify_wc2026_group_stage_r16_interaction_gate.py:11:print("OK: legacy group stage R16 interaction gate verifier superseded by one-game Admin_/official runtime rule.")
tools/verify_wc2026_game2_resolved_r32_field.py:11:print("OK: legacy game2 resolved R32 field verifier superseded by one-game Admin_/official runtime rule.")
tools/verify_wc2026_single_game_admin_official_runtime.py:12:# - Admin_ Supabase row may act as Admin_/official R32 authority during reset/migration.
tools/verify_wc2026_single_game_admin_official_runtime.py:20:    errors.append("Admin_ Supabase user id must be explicit for Admin_/official migration authority.")
tools/verify_wc2026_single_game_admin_official_runtime.py:22:if "loaded Admin_ player row as Admin_/official R32 authority" not in store:
tools/verify_wc2026_single_game_admin_official_runtime.py:23:    errors.append("Admin_ player row must be accepted as Admin_/official R32 authority during reset/migration.")
tools/verify_wc2026_single_game_admin_official_runtime.py:42:    print("WC2026 single-game Admin_/official runtime verification failed:")
tools/verify_wc2026_single_game_admin_official_runtime.py:47:print("OK: WC2026 single-game Admin_/official runtime uses game1, Admin_ migration authority, strict canonical team IDs, and joined Supabase-only play.")
tools/verify_wc2026_official_truth_bracket_hidden_player.py:11:require('.eq("bracket_kind", "official")' in store, "official loader must query official row")
tools/verify_wc2026_official_truth_bracket_hidden_player.py:15:require('R32 occupants are supplied by Admin_/official' in model, "model must reject player R32 edits")
tools/verify_wc2026_official_truth_bracket_hidden_player.py:16:require('Round of 32 occupants are set by Admin_/official' in controller, "controller must explain read-only R32")
tools/verify_wc2026_game1_game2_state_separation_no_r16_preselect_highlight.py:11:print("OK: legacy game1 game2 state separation verifier superseded by one-game Admin_/official runtime rule.")
tools/verify_wc2026_admin_official_full_bracket_editor_mode.py:21:# - Admin_ physical Supabase row is accepted as Admin_/official authority
tools/verify_wc2026_admin_official_full_bracket_editor_mode.py:23:# - Runtime projects Admin_ as semantic Admin_/official.
tools/verify_wc2026_admin_official_full_bracket_editor_mode.py:24:# - Admin_/official editor mode may author R32 occupants.
tools/verify_wc2026_admin_official_full_bracket_editor_mode.py:28:# - Do not require a separate physical "Admin_/official" user_id row.
tools/verify_wc2026_admin_official_full_bracket_editor_mode.py:35:require(".eq(\"user_id\", ADMIN_OFFICIAL_SUPABASE_USER_ID)" in store, "store must load Admin_ physical row as authority")
tools/verify_wc2026_admin_official_full_bracket_editor_mode.py:36:require("loaded Admin_ player row as Admin_/official R32 authority" in store, "store must recognize Admin_ row as Admin_/official authority")
tools/verify_wc2026_admin_official_full_bracket_editor_mode.py:37:require("userId: ADMIN_OFFICIAL_USER_ID" in store, "store must project Admin_ physical row as semantic Admin_/official")
tools/verify_wc2026_admin_official_full_bracket_editor_mode.py:39:require(".eq(\"user_id\", ADMIN_OFFICIAL_USER_ID)" not in store, "store must not query fake semantic Admin_/official user id")
tools/verify_wc2026_admin_official_full_bracket_editor_mode.py:41:require("adminOfficialEditor" in app, "app must wire Admin_/official editor flag")
tools/verify_wc2026_admin_official_full_bracket_editor_mode.py:42:require("adminOfficialEditorFromUrl" in model, "model must derive Admin_/official editor flag from URL/app")
tools/verify_wc2026_admin_official_full_bracket_editor_mode.py:43:require("adminOfficialEditorActive" in model, "model must expose Admin_/official editor active state")
tools/verify_wc2026_admin_official_full_bracket_editor_mode.py:44:require("adminOfficialR32EditorActive" in model, "model must expose Admin_/official R32 editor active state")
tools/verify_wc2026_admin_official_full_bracket_editor_mode.py:47:require("officialTeam(slotId)" in model, "selectedTeam must consult Admin_/official authority")
tools/verify_wc2026_admin_official_full_bracket_editor_mode.py:54:require("Round of 32 occupants are set by Admin_/official" in controller, "normal players must be blocked from R32 authoring")
tools/verify_wc2026_admin_official_full_bracket_editor_mode.py:55:require("if (adminOfficialEditorActive()) return \"\";" in controller, "Admin_/official editor must not be blocked from R32 authoring")
tools/verify_wc2026_admin_official_full_bracket_editor_mode.py:57:require("saveOfficialR32BracketAuthority" in store, "store must keep Admin_/official save boundary")
tools/verify_wc2026_admin_official_full_bracket_editor_mode.py:60:require(".update(rowPayload)" in store, "Admin_/official save must update the existing physical Admin_ row when present")
tools/verify_wc2026_admin_official_full_bracket_editor_mode.py:61:require(".insert(rowPayload)" in store, "Admin_/official save may insert only the physical Admin_ row when missing")
tools/verify_wc2026_admin_official_full_bracket_editor_mode.py:62:require('bracket_kind: "player"' in store, "Admin_/official durable save must keep the physical row bracket_kind as player")
tools/verify_wc2026_admin_official_full_bracket_editor_mode.py:63:require('bracket_kind: "official"' not in store, "Admin_/official durable save must not write a physical official row")
tools/verify_wc2026_admin_official_full_bracket_editor_mode.py:64:require('bracketKind: "official"' in store, "projected Admin_/official document must retain semantic official bracket kind")
tools/verify_wc2026_admin_official_full_bracket_editor_mode.py:65:require('persistedBracketKind: "player"' in store, "projected Admin_/official document must remember physical player row kind")
tools/verify_wc2026_admin_official_full_bracket_editor_mode.py:68:    print("WC2026 Admin_/official full bracket editor mode verification failed:")
tools/verify_wc2026_admin_official_full_bracket_editor_mode.py:73:print("OK: Admin_/official full editor verifier aligned with single-game Admin_ authority, semantic projection, player R32 lockout, and canonical team IDs.")
tools/verify_wc2026_lifecycle_stage_presentation_only_picks.py:11:print("OK: legacy lifecycle stage presentation only picks verifier superseded by one-game Admin_/official runtime rule.")
tools/verify_wc2026_admin_official_results_truth.py:2:"""Verify Admin_/official is the result-truth source for standings/scoring/viewer."""
tools/verify_wc2026_admin_official_results_truth.py:29:require('const ADMIN_OFFICIAL_USER_ID = "Admin_/official"' in store, "standings store must name Admin_/official")
tools/verify_wc2026_admin_official_results_truth.py:30:require('const ADMIN_OFFICIAL_TRUTH_SOURCE = "Supabase:Admin_/official"' in store, "standings store must name Supabase Admin truth source")
tools/verify_wc2026_admin_official_results_truth.py:31:require('function isAdminOfficialTruthRow' in store, "standings store must identify the official truth row")
tools/verify_wc2026_admin_official_results_truth.py:32:require('function normalizeAdminOfficialTruth' in store, "standings store must normalize official truth separately")
tools/verify_wc2026_admin_official_results_truth.py:33:require('.in("bracket_kind", ["player", "official"])' in store, "standings query must read player and official rows")
tools/verify_wc2026_admin_official_results_truth.py:34:require('const officialTruth = normalizeAdminOfficialTruth(allRows.find(isAdminOfficialTruthRow) || null)' in store, "standings store must separate official truth before player normalization")
tools/verify_wc2026_admin_official_results_truth.py:35:require('const bracketRows = allRows.filter((row) => !isAdminOfficialTruthRow(row))' in store, "official row must be excluded from player standings rows")
tools/verify_wc2026_admin_official_results_truth.py:36:require('scoreAgainstAdminOfficialTruth' in store, "standings store must score against Admin official truth")
tools/verify_wc2026_admin_official_results_truth.py:38:require('officialTruthPicksBySlot' in store and 'officialResultsTruthSource' in store, "player rows must carry official truth comparison metadata")
tools/verify_wc2026_admin_official_results_truth.py:43:for forbidden in ['officialTruth = bracketRows', 'officialTruth = playerRows', 'normalizeBracketRow(row, profileByUserId)' ]:
tools/verify_wc2026_admin_official_results_truth.py:46:require('officialTruthPicksBySlot' in surface, "read-only board viewer must receive official truth picks separately")
tools/verify_wc2026_admin_official_results_truth.py:53:require('officialResultsTruthSource: "Supabase:Admin_/official"' in model, "runtime model must tag Admin official result truth source")
tools/verify_wc2026_admin_official_results_truth.py:59:require('officialResultsTruthSource: "Supabase:Admin_/official"' in repo, "repository official source must carry result truth metadata")
tools/verify_wc2026_admin_official_results_truth.py:63:    require('Admin_/official' in rel_text, f"{label} must document Admin official source")
tools/verify_wc2026_admin_official_results_truth.py:70:    raise SystemExit("Admin_/official results truth verification failed: " + "; ".join(errors))
tools/verify_wc2026_admin_official_results_truth.py:72:print("OK: Admin_/official is the source of results truth for standings, scoring comparison, and read-only viewer context.")
tools/verify_wc2026_player_standings_weighted_reachability_runtime.py:17:    "function scoringSlotIds(playerPicksBySlot, officialTruthPicksBySlot)",
tools/verify_wc2026_player_standings_weighted_reachability_runtime.py:18:    "function canTeamStillReachSlot(teamId, slotId, officialTruthPicksBySlot",
tools/verify_wc2026_player_standings_weighted_reachability_runtime.py:26:    "canTeamStillReachSlot(playerTeamId, slotId, officialTruthPicksBySlot)",
tools/verify_wc2026_official_r32_hydration_li.py:2:"""Verify official R32 hydration LI is captured without runtime changes."""
tools/verify_wc2026_official_r32_hydration_li.py:10:        "`Admin_/official` owns the R32 field",
tools/verify_wc2026_official_r32_hydration_li.py:17:        "`Admin_/official` owns the R32 field",
tools/verify_wc2026_official_r32_hydration_li.py:19:        "Hydration must copy `Admin_/official` R32 occupants into non-admin player BracketDocuments at creation, load, import, and save boundaries",
tools/verify_wc2026_official_r32_hydration_li.py:27:        "`Admin_/official` owns the R32 field",
tools/verify_wc2026_official_r32_hydration_li.py:30:        "Hydration must copy `Admin_/official` R32 occupants into non-admin player BracketDocuments at creation, load, import, and save boundaries",
tools/verify_wc2026_official_r32_hydration_li.py:37:        "Admin_/official` owns the R32 field",
tools/verify_wc2026_official_r32_hydration_li.py:47:        "Admin_/official` owns the R32 field",
tools/verify_wc2026_official_r32_hydration_li.py:73:    missing.append("Makefile verify target does not include official R32 hydration LI verifier")
tools/verify_wc2026_official_r32_hydration_li.py:90:    print("WC2026 official R32 hydration LI verification failed:")
tools/verify_wc2026_official_r32_hydration_li.py:95:print("OK: WC2026 official R32 hydration LI defines knockout-only R32 authority, hydration boundaries, persistence, scoring, and LI-only scope.")
tools/verify_wc2026_admin_official_r32_editor_mode.py:22:# - Runtime projects Admin_ as semantic Admin_/official.
tools/verify_wc2026_admin_official_r32_editor_mode.py:25:# - Saves must use physical signed-in Supabase user identity, not fake Admin_/official user_id.
tools/verify_wc2026_admin_official_r32_editor_mode.py:28:require("adminOfficialEditor" in app, "app must pass Admin_/official editor flag")
tools/verify_wc2026_admin_official_r32_editor_mode.py:29:require("adminOfficialEditorFromUrl" in model, "model must derive Admin_/official editor mode from URL/app flag")
tools/verify_wc2026_admin_official_r32_editor_mode.py:30:require("adminOfficialEditorActive" in model, "model must expose Admin_/official editor active state")
tools/verify_wc2026_admin_official_r32_editor_mode.py:31:require("adminOfficialR32EditorActive" in model, "model must expose Admin_/official R32 editor active state")
tools/verify_wc2026_admin_official_r32_editor_mode.py:34:require("Round of 32 occupants are set by Admin_/official" in controller, "normal players must be blocked from authoring R32")
tools/verify_wc2026_admin_official_r32_editor_mode.py:39:require("loaded Admin_ player row as Admin_/official R32 authority" in store, "store must recognize Admin_ row as Admin_/official authority")
tools/verify_wc2026_admin_official_r32_editor_mode.py:40:require("userId: ADMIN_OFFICIAL_USER_ID" in store, "store must project Admin_ row as semantic Admin_/official document")
tools/verify_wc2026_admin_official_r32_editor_mode.py:42:require(".eq(\"user_id\", ADMIN_OFFICIAL_USER_ID)" not in store, "store must not query fake semantic Admin_/official user id")
tools/verify_wc2026_admin_official_r32_editor_mode.py:44:require("saveOfficialR32BracketAuthority" in store, "store must keep Admin_/official save boundary")
tools/verify_wc2026_admin_official_r32_editor_mode.py:45:require('bracket_kind: "player"' in store, "Admin_/official R32 save must persist through the physical Admin_ player row")
tools/verify_wc2026_admin_official_r32_editor_mode.py:46:require('bracket_kind: "official"' not in store, "Admin_/official R32 save must not write a physical official row")
tools/verify_wc2026_admin_official_r32_editor_mode.py:48:require("bracket_kind: \"official\"" in store or "bracketKind: \"official\"" in store, "projected/saved Admin document must keep official semantic bracket kind")
tools/verify_wc2026_admin_official_r32_editor_mode.py:54:    print("WC2026 Admin_/official R32 editor mode verification failed:")
tools/verify_wc2026_admin_official_r32_editor_mode.py:59:print("OK: Admin_/official R32 editor uses Admin_ physical authority, semantic Admin_/official projection, canonical team IDs, and player R32 lockout.")
tools/verify_wc2026_admin_r32_hydration_compatibility_model_li.py:2:"""Verify LI/docs align with Admin R32 hydration compatibility model."""
tools/verify_wc2026_admin_r32_hydration_compatibility_model_li.py:16:require("verify_wc2026_admin_r32_hydration_compatibility_model_li.py" in makefile, "Makefile must run the Admin R32 compatibility LI verifier.")
tools/verify_wc2026_admin_r32_hydration_compatibility_model_li.py:20:    "Admin_/official owns R32 occupant truth",
tools/verify_wc2026_admin_r32_hydration_compatibility_model_li.py:21:    "Player BracketDocuments may contain R32 entrant records only as Supabase Admin_/official hydrated mirror entries",
tools/verify_wc2026_admin_r32_hydration_compatibility_model_li.py:23:    "copied ONLY from the Supabase Admin_/official official bracket document",
tools/verify_wc2026_admin_r32_hydration_compatibility_model_li.py:33:require("let Admin_/official assign official team occupants" in app_modules, "App module boundaries must name Admin_/official as R32 occupant author.")
tools/verify_wc2026_admin_r32_hydration_compatibility_model_li.py:34:require("hydrate ONLY R32 entrant slots from Supabase Admin_/official" in app_modules, "App module boundaries must preserve hydration compatibility rule.")
tools/verify_wc2026_admin_r32_hydration_compatibility_model_li.py:38:require("Admin_/official hydrated occupant" in r32_rendering, "R32 rendering rule must describe Admin_/official hydrated occupants.")
tools/verify_wc2026_admin_r32_hydration_compatibility_model_li.py:42:require("superseded by the current knockout-only Admin_/official R32 authority model" in unified, "Unified lifecycle note must be explicitly superseded by current Admin R32 authority model.")
tools/verify_wc2026_admin_r32_hydration_compatibility_model_li.py:44:require("Admin_/official R32 slot occupant" in unified, "Unified lifecycle note must name Admin R32 occupant truth.")
tools/verify_wc2026_admin_r32_hydration_compatibility_model_li.py:48:require("Legacy note" in controller and "Admin_/official owns R32 occupant truth" in controller, "R32 pick controller doc must be marked legacy/superseded.")
tools/verify_wc2026_admin_r32_hydration_compatibility_model_li.py:52:require("copy ONLY Supabase Admin_/official R32 entrants into player `picksBySlot`" in force_doc, "Force-player-R32 doc must describe player picksBySlot materialization.")
tools/verify_wc2026_admin_r32_hydration_compatibility_model_li.py:57:require("Supabase Admin_/official R32 occupant truth mirrored into player BracketDocuments" in lifecycle, "Lifecycle rule must describe mirrored Admin R32 evidence.")
tools/verify_wc2026_admin_r32_hydration_compatibility_model_li.py:61:require("Admin_/official R32 occupant truth mirrored into player BracketDocuments" in card116, "Lifecycle card must describe mirrored Admin R32 truth.")
tools/verify_wc2026_admin_r32_hydration_compatibility_model_li.py:70:    require("Admin_/official" in text, f"{rel} must name Admin_/official.")
tools/verify_wc2026_admin_r32_hydration_compatibility_model_li.py:75:require("Copy ONLY R32 entrant slots from Supabase Admin_/official" in hydrate_rule, "Hydration rule must keep only-R32 Supabase Admin copy boundary.")
tools/verify_wc2026_admin_r32_hydration_compatibility_model_li.py:76:require("Do not copy Admin_/official R16, QF, SF, Final, Champion, or third-place picks" in hydrate_rule, "Hydration rule must block Admin later-round copy.")
tools/verify_wc2026_admin_r32_hydration_compatibility_model_li.py:79:    print("WC2026 Admin R32 hydration compatibility LI verification failed:")
tools/verify_wc2026_admin_r32_hydration_compatibility_model_li.py:84:print("OK: LI/docs align with Admin R32 hydration compatibility model and no longer describe normal-player R32 occupant authoring as current behavior.")
tools/verify_wc2026_active_game_pick_gating.py:11:print("OK: legacy active game pick gating verifier superseded by one-game Admin_/official runtime rule.")
tools/verify_wc2026_supabase_admin_official_r32_source.py:15:# Current one-game Admin_/official authority model:
tools/verify_wc2026_supabase_admin_official_r32_source.py:17:# - Admin_ Supabase user row is accepted as Admin_/official R32 authority during migration/reset.
tools/verify_wc2026_supabase_admin_official_r32_source.py:18:# - Runtime projects Admin_ persisted row as Admin_/official.
tools/verify_wc2026_supabase_admin_official_r32_source.py:29:require("loaded Admin_ player row as Admin_/official R32 authority" in store, "loader must log Admin_ row as Admin_/official authority")
tools/verify_wc2026_supabase_admin_official_r32_source.py:34:require("no Admin_/official R32 source row found" in store, "loader must fail closed when no Admin_ source row exists")
tools/verify_wc2026_supabase_admin_official_r32_source.py:36:require('userId: ADMIN_OFFICIAL_USER_ID' in store, "loader must project Admin_ row as Admin_/official document")
tools/verify_wc2026_supabase_admin_official_r32_source.py:38:require('authority: "Admin_/official"' in store, "loader must mark projected source as Admin_/official authority")
tools/verify_wc2026_supabase_admin_official_r32_source.py:51:require('.eq("user_id", ADMIN_OFFICIAL_USER_ID)' not in store, "must not query fake Admin_/official user_id")
tools/verify_wc2026_supabase_admin_official_r32_source.py:54:    print("WC2026 Supabase Admin_/official R32 source verification failed:")
tools/verify_wc2026_supabase_admin_official_r32_source.py:59:print("OK: one-game Supabase Admin_/official R32 source uses Admin_ migration authority, strict canonical team IDs, and joined Supabase-only play.")
tools/verify_wc2026_force_player_r32_matches_admin_official.py:18:# - R32 occupants are Admin_/official authority, not player-owned picks.
tools/verify_wc2026_force_player_r32_matches_admin_official.py:19:# - Admin_ Supabase row may be projected as Admin_/official during reset/migration.
tools/verify_wc2026_force_player_r32_matches_admin_official.py:25:require("loaded Admin_ player row as Admin_/official R32 authority" in store, "store must load Admin_ row as Admin_/official authority")
tools/verify_wc2026_force_player_r32_matches_admin_official.py:26:require("userId: ADMIN_OFFICIAL_USER_ID" in store, "store must project Admin_ row as semantic Admin_/official")
tools/verify_wc2026_force_player_r32_matches_admin_official.py:32:require("officialTeam(slotId)" in model, "R32 rendering must consult Admin_/official authority")
tools/verify_wc2026_force_player_r32_matches_admin_official.py:36:require("Round of 32 occupants are set by Admin_/official" in controller, "players must be blocked from authoring R32 occupants")
tools/verify_wc2026_force_player_r32_matches_admin_official.py:45:print("OK: R32 occupants render from Admin_/official authority; players cannot author R32 and must pick later winners.")
tools/verify_wc2026_game2_fifa_final_r32_source_with_game1_fallback.py:11:print("OK: legacy game2 FIFA final R32 source verifier superseded by one-game Admin_/official runtime rule.")
tools/verify_wc2026_active_game_pick_rules_pipeline.py:11:print("OK: legacy active game pick rules pipeline verifier superseded by one-game Admin_/official runtime rule.")
tools/verify_wc2026_hydrate_only_supabase_admin_r32_into_player_picks.py:21:# - R32 occupants are Admin_/official authority.
tools/verify_wc2026_hydrate_only_supabase_admin_r32_into_player_picks.py:22:# - Admin_ physical Supabase row may be projected as semantic Admin_/official.
tools/verify_wc2026_hydrate_only_supabase_admin_r32_into_player_picks.py:32:require(".eq(\"user_id\", ADMIN_OFFICIAL_SUPABASE_USER_ID)" in store, "store must load Admin_ physical row")
tools/verify_wc2026_hydrate_only_supabase_admin_r32_into_player_picks.py:33:require("loaded Admin_ player row as Admin_/official R32 authority" in store, "store must project Admin_ row as Admin_/official authority")
tools/verify_wc2026_hydrate_only_supabase_admin_r32_into_player_picks.py:34:require("userId: ADMIN_OFFICIAL_USER_ID" in store, "store must expose semantic Admin_/official document")
tools/verify_wc2026_hydrate_only_supabase_admin_r32_into_player_picks.py:36:require(".eq(\"user_id\", ADMIN_OFFICIAL_USER_ID)" not in store, "store must not query fake semantic Admin_/official user id")
tools/verify_wc2026_hydrate_only_supabase_admin_r32_into_player_picks.py:39:require("officialTeam(slotId)" in model, "selectedTeam must consult Admin_/official authority")
tools/verify_wc2026_hydrate_only_supabase_admin_r32_into_player_picks.py:44:require("failClosedAdminOfficialR32TruthDocument" in model, "model must fail closed when Admin_/official R32 truth is missing")
tools/verify_wc2026_hydrate_only_supabase_admin_r32_into_player_picks.py:47:require("Round of 32 occupants are set by Admin_/official" in controller, "normal players must be blocked from R32 authoring")
tools/verify_wc2026_hydrate_only_supabase_admin_r32_into_player_picks.py:48:require("if (adminOfficialEditorActive()) return \"\";" in controller, "Admin_/official editor must be allowed to author R32")
tools/verify_wc2026_hydrate_only_supabase_admin_r32_into_player_picks.py:55:    print("WC2026 Supabase-only Admin R32 hydration verification failed:")
tools/verify_wc2026_hydrate_only_supabase_admin_r32_into_player_picks.py:60:print("OK: Supabase Admin R32 hydration verifier aligned with Admin_/official authority, player R32 lockout, and canonical team IDs.")
tools/verify_wc2026_official_r32_hydration_runtime.py:2:"""Verify official R32 hydration runtime/model boundary."""
tools/verify_wc2026_official_r32_hydration_runtime.py:13:        "source: \"Admin_/official\"",
tools/verify_wc2026_official_r32_hydration_runtime.py:14:        "authority: \"Admin_/official\"",
tools/verify_wc2026_official_r32_hydration_runtime.py:42:        "Admin_/official is the authority for R32 occupants",
tools/verify_wc2026_official_r32_hydration_runtime.py:68:    errors.append("Makefile verify target does not include official R32 hydration runtime verifier")
tools/verify_wc2026_official_r32_hydration_runtime.py:86:  userId: "Admin_/official",
tools/verify_wc2026_official_r32_hydration_runtime.py:88:  officialR32AuthoritySource: "Supabase:Admin_/official",
tools/verify_wc2026_official_r32_hydration_runtime.py:100:if (bracket.picksBySlot["L-R32-01"].source !== "Admin_/official") throw new Error("hydrated R32 source is not official");
tools/verify_wc2026_official_r32_hydration_runtime.py:139:    print("WC2026 official R32 hydration runtime verification failed:")
tools/verify_wc2026_official_r32_hydration_runtime.py:144:print("OK: WC2026 official R32 hydration runtime keeps R32 occupants official, preserves player knockout winner picks, and wires creation/load/import/save boundaries without UI cleanup.")
tools/verify_wc2026_group_stage_hides_later_round_pick_fills.py:11:print("OK: legacy group stage hides later round pick fills verifier superseded by one-game Admin_/official runtime rule.")
tools/verify_wc2026_official_r32_as_player_feeder_teams.py:20:    "new R32 selected-team source: Admin_/official truth",
tools/verify_wc2026_official_r32_as_player_feeder_teams.py:21:    "every R32 display slot resolves its selected team from Admin_/official truth",
tools/verify_wc2026_official_r32_as_player_feeder_teams.py:59:        "controller.js must preserve Admin_/official editor detection.",
tools/verify_wc2026_game2_r32_readonly_rendering.py:11:print("OK: legacy game2 R32 readonly rendering verifier superseded by one-game Admin_/official runtime rule.")
tools/verify_wc2026_player_standings_scoring_rule.py:29:    "Admin_/official",
tools/verify_wc2026_player_standings_scoring_rule.py:49:print("OK: Player Standings scoring rule defines earned points, max possible points, round weights, and Admin_/official truth.")
tools/verify_wc2026_player_standings_max_possible_reachability_rule.py:21:    "could still become `Admin_/official` truth",
tools/verify_wc2026_player_standings_max_possible_reachability_rule.py:24:    "prior resolved `Admin_/official` truth",
tools/verify_wc2026_player_standings_max_possible_reachability_rule.py:27:    "`Admin_/official` is the only source of elimination and scoring truth",
site/js/mvc/controller.js:51:      return "Round of 32 occupants are set by Admin_/official. Pick winners in the next round.";
site/js/mvc/view.js:548:  function officialTruthLabel(team) {
site/js/mvc/view.js:626:          if (slot.officialPickComparison?.state === "incorrect" && slot.officialTruthTeam) {
site/js/mvc/view.js:629:            correct.textContent = `Correct: ${officialTruthLabel(slot.officialTruthTeam)}`;
site/js/mvc/view.js:685:        if (slot.officialTruthTeam) {
site/js/mvc/view.js:686:          button.title = `Official result: ${fullTeamLabel(slot.officialTruthTeam)}`;
site/js/mvc/model.js:234:    userId: "Admin_/official",
site/js/mvc/model.js:237:    officialR32AuthoritySource: "Supabase:Admin_/official",
site/js/mvc/model.js:238:    officialResultsTruthSource: "Supabase:Admin_/official",
site/js/mvc/model.js:239:    source: "Supabase:Admin_/official",
site/js/mvc/model.js:240:    authority: "Admin_/official",
site/js/mvc/model.js:374:          userId: "Admin_/official",
site/js/mvc/model.js:376:          officialR32AuthoritySource: "Supabase:Admin_/official",
site/js/mvc/model.js:377:          officialResultsTruthSource: "Supabase:Admin_/official",
site/js/mvc/model.js:378:          source: "Supabase:Admin_/official",
site/js/mvc/model.js:379:          authority: "Admin_/official",
site/js/mvc/model.js:382:      officialPicks = clearUnknownTeamPicks(legacyPicksFromRemoteBracketDocument(officialBracketDocument), "Admin_/official bracket");
site/js/mvc/model.js:383:      console.info("[WC2026 OfficialResults] loaded Supabase Admin_/official truth bracket picks", {
site/js/mvc/model.js:384:        source: officialBracketDocument?.officialR32AuthoritySource || "Supabase:Admin_/official",
site/js/mvc/model.js:385:        userId: officialBracketDocument?.userId || "Admin_/official",
site/js/mvc/model.js:389:      console.error("[WC2026 OfficialR32] Admin_/official R32 truth unavailable; failing closed", error);
site/js/mvc/model.js:396:        console.warn("[WC2026 OfficialR32] Admin_/official R32 truth missing; Supabase-connected admin editor remains open to create it.");
site/js/mvc/model.js:398:          userId: "Admin_/official",
site/js/mvc/model.js:401:          officialR32AuthoritySource: "Supabase:Admin_/official",
site/js/mvc/model.js:402:          officialResultsTruthSource: "Supabase:Admin_/official",
site/js/mvc/model.js:403:          source: "Supabase:Admin_/official",
site/js/mvc/model.js:404:          authority: "Admin_/official",
site/js/mvc/model.js:410:        console.error("[WC2026 OfficialR32] Admin_/official R32 truth missing; failing closed");
site/js/mvc/model.js:478:      source: "Admin_/official R32 authority",
site/js/mvc/model.js:628:      source: "Admin_/official",
site/js/mvc/model.js:629:      authority: "Admin_/official",
site/js/mvc/model.js:631:      hydratedFrom: "Supabase:Admin_/official",
site/js/mvc/model.js:643:      source: "Admin_/official",
site/js/mvc/model.js:644:      authority: "Admin_/official",
site/js/mvc/model.js:646:      officialTruth: true,
site/js/mvc/model.js:647:      hydratedFrom: "Supabase:Admin_/official",
site/js/mvc/model.js:662:      userId: "Admin_/official",
site/js/mvc/model.js:679:      officialR32AuthoritySource: "Supabase:Admin_/official",
site/js/mvc/model.js:680:      officialResultsTruthSource: "Supabase:Admin_/official",
site/js/mvc/model.js:681:      source: "Supabase:Admin_/official",
site/js/mvc/model.js:682:      authority: "Admin_/official",
site/js/mvc/model.js:690:  function persistAdminOfficialTruth(reason = "admin-official-full-bracket-edit") {
site/js/mvc/model.js:700:        console.info("[WC2026 AdminOfficialFullBracketEditor] saved Admin_/official full bracket truth", {
site/js/mvc/model.js:701:          userId: "Admin_/official",
site/js/mvc/model.js:707:        console.error("[WC2026 AdminOfficialFullBracketEditor] Admin_/official full bracket save failed", error);
site/js/mvc/model.js:713:      persistAdminOfficialTruth(reason);
site/js/mvc/model.js:725:        console.info("[WC2026 AdminOfficialR32Editor] saved Admin_/official R32 truth", {
site/js/mvc/model.js:726:          userId: "Admin_/official",
site/js/mvc/model.js:732:        console.error("[WC2026 AdminOfficialR32Editor] Admin_/official R32 save failed", error);
site/js/mvc/model.js:845:    // Normal players never get R32 choices; player-visible R32 mirrors Admin_/official only.
site/js/mvc/model.js:846:    // In Admin_/official editor mode, R32 choices reopen so the official truth document can be authored.
site/js/mvc/model.js:988:      persistAdminOfficialTruth("set-admin-official-bracket-truth-pick");
site/js/mvc/model.js:994:        adminOfficialTruthEdited: true,
site/js/mvc/model.js:999:        return { ok: false, reason: "R32 occupants are supplied by Admin_/official and cannot be edited by players.", cleared: [] };
site/js/mvc/model.js:1021:      persistAdminOfficialTruth("clear-admin-official-bracket-truth");
site/js/mvc/model.js:1022:      return { ok: true, cleared: allPickSlots().map((slot) => slot.slotId), adminOfficialTruthEdited: true };
site/js/mvc/model.js:1285:      officialTruthTeam: officialTeam(slotId),
site/js/mvc/model.js:1341:        officialTruthTeam: officialTeam(slot.slotId),
site/js/standings/PlayerStandingsSurface.js:68:  const officialTruthPicksBySlot = row?.officialTruthPicksBySlot && typeof row.officialTruthPicksBySlot === "object" && !Array.isArray(row.officialTruthPicksBySlot)
site/js/standings/PlayerStandingsSurface.js:69:    ? row.officialTruthPicksBySlot
site/js/standings/PlayerStandingsSurface.js:82:    officialTruthPicksBySlot,
site/js/standings/PlayerStandingsSurface.js:306:function boardViewerOfficialTruthLabel(team) {
site/js/standings/PlayerStandingsSurface.js:413:  const officialTruthPicksBySlot = row?.officialTruthPicksBySlot || {};
site/js/standings/PlayerStandingsSurface.js:414:  const officialTruthSource = row?.officialResultsTruthSource || "";
site/js/standings/PlayerStandingsSurface.js:420:    const officialTeam = normalizeBoardViewerTeam(pickTeamIdFromRecord(officialTruthPicksBySlot[slot.slotId]), teamById);
site/js/standings/PlayerStandingsSurface.js:427:    const officialLabel = boardViewerOfficialTruthLabel(officialTeam);
site/js/standings/PlayerStandingsSurface.js:432:    const ariaOfficial = officialTeam ? ` Official result from ${officialTruthSource || "Admin_/official"}: ${officialLabel}.` : "";
site/js/standings/SupabasePlayerStandingsStore.js:5:const ADMIN_OFFICIAL_USER_ID = "Admin_/official";
site/js/standings/SupabasePlayerStandingsStore.js:6:const ADMIN_OFFICIAL_TRUTH_SOURCE = "Supabase:Admin_/official";
site/js/standings/SupabasePlayerStandingsStore.js:94:function scoringSlotIds(playerPicksBySlot, officialTruthPicksBySlot) {
site/js/standings/SupabasePlayerStandingsStore.js:97:    ...Object.keys(officialTruthPicksBySlot || {}),
site/js/standings/SupabasePlayerStandingsStore.js:101:function canTeamStillReachSlot(teamId, slotId, officialTruthPicksBySlot, visiting = new Set()) {
site/js/standings/SupabasePlayerStandingsStore.js:108:  const officialTeamId = pickTeamIdFromRecord(officialTruthPicksBySlot?.[currentSlotId]);
site/js/standings/SupabasePlayerStandingsStore.js:118:    canTeamStillReachSlot(candidateTeamId, feederSlotId, officialTruthPicksBySlot, nextVisiting)
site/js/standings/SupabasePlayerStandingsStore.js:122:function scoreAgainstAdminOfficialTruth(playerPicksBySlot, officialTruthPicksBySlot) {
site/js/standings/SupabasePlayerStandingsStore.js:127:  for (const slotId of scoringSlotIds(playerPicksBySlot, officialTruthPicksBySlot)) {
site/js/standings/SupabasePlayerStandingsStore.js:128:    const officialRecord = officialTruthPicksBySlot?.[slotId];
site/js/standings/SupabasePlayerStandingsStore.js:146:    if (canTeamStillReachSlot(playerTeamId, slotId, officialTruthPicksBySlot)) {
site/js/standings/SupabasePlayerStandingsStore.js:161:function isAdminOfficialTruthRow(row) {
site/js/standings/SupabasePlayerStandingsStore.js:164:    || row?.bracket_kind === "official"
site/js/standings/SupabasePlayerStandingsStore.js:169:function normalizeAdminOfficialTruth(row) {
site/js/standings/SupabasePlayerStandingsStore.js:178:    partialOfficialTruthAllowed: true,
site/js/standings/SupabasePlayerStandingsStore.js:182:function normalizeBracketRow(row, profileByUserId, officialTruth = null) {
site/js/standings/SupabasePlayerStandingsStore.js:190:  const officialTruthPicksBySlot = officialTruth?.picksBySlot || {};
site/js/standings/SupabasePlayerStandingsStore.js:191:  const score = scoreAgainstAdminOfficialTruth(picksBySlot, officialTruthPicksBySlot);
site/js/standings/SupabasePlayerStandingsStore.js:204:    officialTruthPicksBySlot,
site/js/standings/SupabasePlayerStandingsStore.js:205:    officialResultsTruthSource: officialTruth?.officialResultsTruthSource || "",
site/js/standings/SupabasePlayerStandingsStore.js:206:    officialResultsTruthUserId: officialTruth?.userId || "",
site/js/standings/SupabasePlayerStandingsStore.js:255:      .in("bracket_kind", ["player", "official"])
site/js/standings/SupabasePlayerStandingsStore.js:261:    const officialTruth = normalizeAdminOfficialTruth(allRows.find(isAdminOfficialTruthRow) || null);
site/js/standings/SupabasePlayerStandingsStore.js:262:    const bracketRows = allRows.filter((row) => !isAdminOfficialTruthRow(row));
site/js/standings/SupabasePlayerStandingsStore.js:271:    return bracketRows.map((row) => normalizeBracketRow(row, profileByUserId, officialTruth));
site/js/model/UserBracketModel.js:55:  if (officialR32?.source === "Supabase:Admin_/official") return "Supabase:Admin_/official";
site/js/model/UserBracketModel.js:56:  if (officialR32?.userId === "Admin_/official" && officialR32?.bracketKind === "official") return "Supabase:Admin_/official";
site/js/model/UserBracketModel.js:71:      source: "Admin_/official",
site/js/model/UserBracketModel.js:104:    source: "Admin_/official",
site/js/model/UserBracketModel.js:105:    authority: "Admin_/official",
site/js/model/UserBracketModel.js:107:    hydratedFrom: occupant.hydratedFrom || "Supabase:Admin_/official",
site/js/model/UserBracketModel.js:117:    source: "Admin_/official",
site/js/model/UserBracketModel.js:118:    authority: "Admin_/official",
site/js/model/UserBracketModel.js:128:  return source === "Supabase:Admin_/official";
site/js/model/UserBracketModel.js:148:      source: "Admin_/official",
site/js/model/UserBracketModel.js:260:    if (incomingRecord?.source === "Admin_/official" || incomingRecord?.authority === "Admin_/official") {
site/js/model/UserBracketModel.js:261:      slotRecord.source = "Admin_/official";
site/js/model/UserBracketModel.js:262:      slotRecord.authority = "Admin_/official";
site/js/model/UserBracketModel.js:264:      slotRecord.hydratedFrom = incomingRecord?.hydratedFrom || "Supabase:Admin_/official";
site/js/model/UserBracketModel.js:313:        source: "Admin_/official",
site/js/model/UserBracketModel.js:329:    officialEdit ? "Admin_/official" : (normalizedPick.kind === "unpicked" ? "empty" : "user")
site/js/model/UserBracketModel.js:332:    record.authority = "Admin_/official";
site/js/model/UserBracketModel.js:334:    record.officialTruth = true;
site/js/model/UserBracketModel.js:335:    record.hydratedFrom = "Supabase:Admin_/official";
site/js/services/SupabaseBracketStore.js:14:const ADMIN_OFFICIAL_USER_ID = "Admin_/official";
site/js/services/SupabaseBracketStore.js:16:const ADMIN_OFFICIAL_AUTHORITY_SOURCE = "Supabase:Admin_/official";
site/js/services/SupabaseBracketStore.js:216:        || bracket.authority === "Admin_/official"
site/js/services/SupabaseBracketStore.js:233:        authority: "Admin_/official",
site/js/services/SupabaseBracketStore.js:245:      .eq("bracket_kind", "official")
site/js/services/SupabaseBracketStore.js:279:      console.info("[WC2026 OfficialR32] loaded Admin_ player row as Admin_/official R32 authority", {
site/js/services/SupabaseBracketStore.js:290:    console.warn("[WC2026 OfficialR32] no Admin_/official R32 source row found", {
site/js/services/SupabaseBracketStore.js:312:      throw new Error("SupabaseBracketStore can only save Admin_/official authority as the physical Admin_ Supabase user.");
site/js/services/SupabaseBracketStore.js:315:    assertPlainObject(bracket, "SupabaseBracketStore requires an Admin_/official BracketDocument object.");
site/js/services/SupabaseBracketStore.js:316:    assertPlainObject(bracket.picksBySlot, "SupabaseBracketStore requires Admin_/official picksBySlot.");
site/js/services/SupabaseBracketStore.js:364:      authority: "Admin_/official",
site/js/services/SupabaseBracketStore.js:369:        throw new Error(`SupabaseBracketStore refused to save incomplete Admin_/official BracketDocument; missing ${key}.`);
site/js/services/SupabaseBracketStore.js:409:      authority: "Admin_/official",
site/js/services/SupabaseBracketStore.js:455:          bracket_kind: canonicalBracketDocument.bracketKind === "official" ? "official" : "player",
site/js/services/BracketRepository.js:19:    userId: "Admin_/official",
site/js/services/BracketRepository.js:22:    officialR32AuthoritySource: "Supabase:Admin_/official",
site/js/services/BracketRepository.js:23:    officialResultsTruthSource: "Supabase:Admin_/official",
site/js/services/BracketRepository.js:24:    source: "Supabase:Admin_/official",
site/js/services/BracketRepository.js:25:    authority: "Admin_/official",
site/js/services/BracketRepository.js:38:    authority: "Admin_/official",
site/js/services/BracketRepository.js:90:        // Admin_/official is authoritative when the row exists, even while partial.
site/js/services/BracketRepository.js:95:            userId: "Admin_/official",
site/js/services/BracketRepository.js:97:            officialR32AuthoritySource: "Supabase:Admin_/official",
site/js/services/BracketRepository.js:98:            officialResultsTruthSource: "Supabase:Admin_/official",
site/js/services/BracketRepository.js:99:            source: "Supabase:Admin_/official",
site/js/services/BracketRepository.js:100:            authority: "Admin_/official",
site/js/services/BracketRepository.js:104:        console.error("[WC2026 Official R32] Supabase Admin_/official bracket unavailable; failing closed", error);
site/js/services/BracketRepository.js:108:      console.error("[WC2026 Official R32] Supabase Admin_/official bracket missing; failing closed");
