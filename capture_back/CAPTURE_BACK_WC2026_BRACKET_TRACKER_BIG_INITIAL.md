WB_SESSION:
WC2026 Bracket Tracker — Big Initial Capture Back

Purpose:
- Consolidate all current Workbench decisions, source artifacts, LI additions, starter data, feature ideas, and repo-creation overlays into one initial Capture Back bundle.
- This bundle is intended to initialize or continue the `wc2026-bracket-tracker-li` repo from the WB template.

Core product understanding:
- The Workbench does not merely generate artifacts.
- The Workbench presents the current best solution against living intent.
- Continuity keeps the solution up to date against LI-stated goals.
- The public solution may be a static HTML site, GitHub Pages site, or later hosted app.
- The Workbench preserves the source data, LI, decisions, player picks, scoring, releases, and update history needed to continue evolving the solution.

Proof case:
- A photo of a World Cup schedule poster becomes source evidence.
- The source evidence becomes structured schedule and group data.
- The structured data backs a static HTML bracket tracker.
- The tracker evolves into Game 1: Round-of-32 qualifier picks.
- After the official Round of 32 is known, it evolves into Game 2: full knockout bracket picks.
- Results and scoring updates are entered over time.
- Each meaningful update is Capture Backed and can produce a new static HTML release.

User decisions captured:
- The first data source should be the uploaded poster image.
- The WB can ultimately hold all tournament and game data.
- Use Capture Back after results are entered.
- The static HTML file is the user-facing surface and can be downloaded/opened locally.
- The same site can later be served by GitHub Pages.
- The repo should be buildable/maintainable from any II reasoner.
- The user will build it from this chatbot.
- There are two games:
  1. Game 1: players pick the 32 teams that advance from the 48-team group stage.
  2. Game 2: after official Round of 32 is known, players fill the full 32-team knockout bracket through champion.
- Store player picks for Game 1 and Game 2 separately.
- Store scoring rules separately for each game.
- Add optional YouTube highlights for each match as enrichment, separate from official results and scoring.

Source evidence included:
- `source/images/match_schedule_group_stage_poster_michelob_ultra.jpeg`
- `source/artifacts/wc2026_schedule_poster_input_artifact.zip`
- `source/artifacts/wc2026_bracket_tracker_initial_repo_cb_overlay.zip` or uploaded equivalent
- `source/artifacts/wc2026_bracket_tracker_cb_001.zip`
- `source/artifacts/wc2026_current_solution_li_overlay.zip`
- `source/artifacts/wc2026_youtube_highlights_cb_overlay.zip`
- `source/artifacts/workbench-li-template.pack(47).zip` if present
- `releases/world_cup_bracket_tracker_v001.html` if present

Data model captured:
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
- `data/group_stage_matches_from_poster.json`
- `data/groups_from_poster.json`
- `data/schema/match_highlight_schema.json`

LI captured:
- source authority
- source ingestion
- data storage
- two-game pool model
- player scoring
- static HTML release
- update capture
- current solution against living intent
- YouTube highlight enrichment

Current solution framing:
- The current solution is not only the software artifact.
- The current solution is the user-facing artifact plus the LI state that explains and governs it.
- For the public user, this may appear as a simple bracket site.
- For the Workbench, it is a living solution state that can keep updating as results and needs change.

YouTube highlights feature:
- Each match may hold optional YouTube highlight metadata.
- Preferred sources: official FIFA, broadcaster, team/federation, reputable media, manual.
- Highlights are enrichment only.
- Highlights do not determine official results or scores unless explicitly marked manual.
- Adding/changing/removing highlights requires Capture Back.

Result update loop:
Enter results
↓
Update WB data
↓
Update standings/advancement
↓
Update Game 1 or Game 2 scores
↓
Regenerate static HTML
↓
Capture Back
↓
Release/pass around next HTML

Known uncertainties:
- Poster-derived data is preliminary and must be verified against official sources.
- Prior extraction noted a possible ambiguity around one poster match/team grouping; official source verification is required.
- Final scoring rules are proposed, not locked.
- Game 2 cannot be opened until the official Round of 32 field and slots are known.
- Hosting path is optional: local HTML first, GitHub Pages next, server later if direct submissions are needed.

Next recommended work:
1. Create `wc2026-bracket-tracker-li` from the WB template.
2. Apply this Big Initial Capture Back bundle or the included initial repo overlay.
3. Run verification.
4. Commit the initial repo.
5. Implement Game 1 Round-of-32 pick UI.
6. Add player roster and lock policy.
7. Later verify poster data against official FIFA schedule.
8. Later add YouTube highlight fields to match cards.
