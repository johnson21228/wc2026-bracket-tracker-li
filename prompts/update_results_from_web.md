# UPDATE RESULTS: Find and Patch Confirmed Group-Stage Results

You are helping me maintain the `wc2026-bracket-tracker-li` Workbench repo.

Repo root:

`/Users/stevejohnson/Developer/wc2026-bracket-tracker-li`

LI means Language Infrastructure. CB means Capture Back.

## Trigger phrase

When I say **UPDATE RESULTS**, use this prompt.

## Task

Inspect the repo's World Cup group-stage match result data, find matches whose result state may be missing or stale, search the internet only for those candidate matches, and return a safe CB-ready update plan.

## Grounding rule

Do not rely on memory. First ask me for the latest repo pack, or inspect the latest uploaded repo pack/current repo evidence if available.

Use the repo data as the starting point. Use the internet only to verify candidate result updates.

## Repo files to inspect

Start with these likely result/runtime files:

- `site/data/current/group_matches.json`
- `site/data/current/group_standings.json`

Also inspect these mirror/source files if relevant:

- `site/data/group_stage_matches_from_poster.json`
- `data/group_stage_matches_from_poster.json`

Identify which files are runtime result truth, which are schedule/poster mirror truth, and which are derived standings.

## Candidate selection

Classify group-stage matches into these buckets:

1. `already-final`  
   Repo already has final/complete status and scores.

2. `patchable-final-candidate`  
   Repo says scheduled/live/missing, and kickoff time is in the past.

3. `live-watchlist`  
   Repo or internet indicates the match is currently live/in progress.

4. `future-scheduled`  
   Kickoff time is still in the future.

5. `unclear`  
   The repo row is malformed, has missing teams/time, or cannot be matched reliably.

Search the internet only for `patchable-final-candidate` rows. Do not search every match.

## Search strategy

For each candidate, search using precise match-specific queries, in this order:

1. `"TEAM A" "TEAM B" "World Cup 2026" final score`
2. `"TEAM A" "TEAM B" "World Cup 2026" FT`
3. `"TEAM A" "TEAM B" "World Cup 2026" ESPN`
4. `"TEAM A" "TEAM B" "World Cup 2026" FIFA`
5. `site:fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/scores-fixtures "TEAM A" "TEAM B"`
6. `site:espn.com/soccer "TEAM A" "TEAM B" "World Cup"`

Prefer sources in this order:

1. FIFA official match/scores page
2. ESPN match/schedule page
3. Reuters/AP or other wire-service recap
4. Major outlet live report only if it clearly states full-time/final
5. Live-score sites only as fallback

## Final-status rule

Do not patch a match as final unless a source clearly says one of:

- `Final`
- `FT`
- `Full-time`
- `Complete`
- a clear equivalent, such as “played out a 1–1 draw” in a completed recap

If a match is live or in progress, classify it as `live-watchlist`. Do not patch it as final.

## Decision labels

For each candidate, assign one decision:

- `PATCH`: final score confirmed by a reliable source.
- `WATCH`: match is live/in progress; do not patch as final.
- `WAIT`: no reliable final source found yet.
- `CONFLICT`: sources disagree; do not patch.

## Required output

First report the repo inspection:

- which files were inspected
- which file appears to be runtime result truth
- how many matches are already final
- how many are patchable candidates
- how many are live-watchlist
- how many are future-scheduled
- any malformed/unclear rows

Then report each candidate in a compact table:

- decision: `PATCH`, `WATCH`, `WAIT`, or `CONFLICT`
- repo match id
- group
- teams
- repo status
- kickoff time
- verified score/status if found
- source/citation
- confidence
- notes

For each `PATCH` item, include:

- exact score
- final status wording from the source
- source URL/citation
- team-code mapping notes, such as `ALG` vs `DZA`, if relevant

For each `WATCH` item, include:

- current live score if found
- source/citation
- note: “Do not patch as final yet.”

## Patch-plan rule

Do not generate code or overwrite data immediately.

First produce a concise patch plan showing:

- matches to update
- files to update
- standings implications
- source-evidence file to add/update under `source/text/`
- verifier to add/update
- LI/doc/card/capture_back files to add/update

## CB rule

Only if I ask “CB this,” generate a download/apply overlay pattern.

The apply instructions must start with:

`cd /Users/stevejohnson/Developer/wc2026-bracket-tracker-li`

The apply block must include:

- clean repo check
- unzip overlay from `~/Downloads`
- run apply script
- `python3 tools/clean_repo_hygiene.py`
- `make verify`
- `git status --short`
- `open site/index.html`

After green verification, provide the commit/push/publish block:

- `git add -A`
- `git diff --cached --stat`
- `git commit -m "..."`
- `make verify`
- `make pack`
- `git push`
- `make publish-pages`

## Hard constraints

- Use current internet search for result verification.
- Cite sources for every proposed result.
- Do not invent scores, status, standings, or team-code mappings.
- Do not treat live/in-progress matches as final.
- Patch only confirmed final results.
- Keep source evidence separate from derived runtime data.
- Preserve existing Workbench/LI/CB patterns.
