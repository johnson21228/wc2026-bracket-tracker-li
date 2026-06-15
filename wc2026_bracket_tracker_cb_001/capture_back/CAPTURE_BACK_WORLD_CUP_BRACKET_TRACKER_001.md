WB_SESSION:
World Cup Bracket Tracker Capture Back 001

Changed:
- Captured the project as a Workbench-backed static HTML / future GitHub Pages tracker.
- Preserved the uploaded Michelob Ultra / FIFA World Cup 26 group-stage poster image as source evidence.
- Preserved the poster-derived input artifact zip containing extracted match data, groups, transcription, manifest, and Card 000.
- Captured the LI starter zip for the World Cup Bracket Tracker Workbench.
- Added a two-game pool model:
  - Game 1: players pick the 32 teams that advance from the 48-team group stage.
  - Game 2: after the official Round of 32 is known, players fill the full knockout bracket through champion.
- Added storage rules separating tournament truth, official results, player picks, scoring rules, scores, and HTML releases.
- Added starter JSON storage files for both games.

Source Evidence:
- source/images/match_schedule_group_stage_poster_michelob_ultra.jpeg
- source/artifacts/wc2026_schedule_poster_input_artifact.zip
- data/group_stage_matches_from_poster.json
- data/groups_from_poster.json
- capture_back/poster_transcription.md
- capture_back/poster_input_manifest.json

User Decisions Captured:
- The first backing data should come from the uploaded poster image.
- The Workbench needs storage for groups, bracket, player picks, and scoring rules.
- The Round of 32 field will be provided later.
- There are two games:
  1. Round-of-32 qualifier prediction game.
  2. Full 32-team knockout bracket prediction game.
- Game 2 should store picks from Round of 32 through the final.
- The static HTML can later be served by GitHub Pages or a server.

Data Model Captured:
- data/teams.json
- data/groups.json
- data/group_stage_matches.json
- data/group_standings.json
- data/official_round_of_32.json
- data/official_knockout_results.json
- data/game_1_round_of_32_picks.json
- data/game_1_scoring_rules.json
- data/game_1_scores.json
- data/game_2_bracket_picks.json
- data/game_2_scoring_rules.json
- data/game_2_scores.json

LI Added:
- li/world_cup/two_game_pool_model_rule.md
- li/world_cup/data_storage_rule.md

Cards Added:
- cards/005_capture_two_game_pool_data_model_card.md

Known Uncertainty:
- The poster-derived data is not official authority yet.
- The extracted poster artifact includes a noted ambiguity around a poster entry that appears to show HAI vs AUT in Group J, which conflicts with Haiti's apparent Group C placement. This needs official verification.
- Final scoring rules are proposed, not locked.

Next:
- Apply this Capture Back bundle into the World Cup Bracket Tracker LI repo.
- Verify official team/group/schedule data against FIFA.
- Add Game 1 UI for selecting 32 advancing teams.
- Add player roster and bracket lock policy.
- Later, add official Round of 32 bracket and Game 2 full bracket intake.
