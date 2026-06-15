WB_SESSION:
Create WC2026 Bracket Tracker Workbench From Template — Initial Capture Back

Repo intent:
- Create a new Workbench repo for a World Cup 2026 bracket pool tracker.
- The repo can be built from any II reasoner.
- The user will build it from this chatbot.
- The static HTML is the user-facing surface.
- The Workbench is the durable source of truth.

Initial source data:
- The first source artifact is the uploaded match schedule poster image.
- The poster image is preserved under `source/images/`.
- Poster-derived structured data is preserved under `data/`.
- Poster-derived data is marked pending official verification.

Product direction:
- Start as a single downloadable static HTML file.
- Allow local browser use.
- Later allow GitHub Pages hosting by copying current release to `index.html`.
- Later may evolve to a lightweight server if direct user submissions are needed.

Tournament data:
- Store teams, groups, group-stage matches, standings, official Round of 32, and official knockout results.
- The WB can ultimately hold all data.
- Use Capture Back after results are entered.

Two-game model:
- Game 1: players pick the 32 teams that advance from the 48-team group stage.
- Game 2: after the official Round of 32 is known, players fill out the full knockout bracket through champion.
- Game 1 and Game 2 have separate picks, scoring rules, scores, and lock timing.

Storage model:
- `data/teams.json`
- `data/groups.json`
- `data/group_stage_matches.json`
- `data/group_standings.json`
- `data/official_round_of_32.json`
- `data/official_knockout_results.json`
- `data/game_1_round_of_32_picks.json`
- `data/game_1_scoring_rules.json`
- `data/game_1_scores.json`
- `data/game_2_bracket_picks.json`
- `data/game_2_scoring_rules.json`
- `data/game_2_scores.json`

LI installed:
- `li/world_cup/source_authority_rule.md`
- `li/world_cup/source_ingestion_rule.md`
- `li/world_cup/data_storage_rule.md`
- `li/world_cup/two_game_pool_model_rule.md`
- `li/world_cup/player_scoring_rule.md`
- `li/world_cup/static_html_release_rule.md`
- `li/world_cup/update_capture_rule.md`

Cards installed:
- Card 000: capture poster source
- Card 001: create initial static HTML tracker
- Card 002: add Game 1 Round-of-32 pick UI
- Card 003: add Game 2 knockout bracket pick UI
- Card 004: update results and Capture Back

Known uncertainty:
- Poster-derived source data must be verified against official FIFA sources.
- Existing poster extraction noted one apparent ambiguity around a match/team grouping that needs official verification.
- Final scoring rules are proposed, not locked.

Next:
- Create repo from WB template.
- Apply this overlay.
- Run verify.
- Commit initial repo.
- Continue with Card 002: Game 1 Round-of-32 pick UI.
