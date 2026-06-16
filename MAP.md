# MAP

## Purpose

This repo maintains a World Cup 2026 bracket pool tracker as a static HTML app backed by Workbench data.

## Key folders

```text
li/world_cup/      governance rules
source/            source artifacts and source notes
data/              canonical data storage
cards/             work cards
prompts/           reusable prompts for any II reasoner
releases/          immutable HTML releases
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

## Game 2 Official Seed + Game 1 Tiebreaker Rule

- `li/world_cup/game2_official_seed_and_game1_tiebreaker_rule.md` — durable LI rule for fixed Game 2 Round-of-32 seed authority and Game 1 comparison/tiebreaker metadata.
- `docs/rules/game2_official_seed_and_game1_tiebreaker.md` — product-facing explanation of the two-game boundary.
- `cards/048_capture_game2_official_seed_tiebreaker_rule_card.md` — implementation card for the rule capture.
- `capture_back/CAPTURE_BACK_GAME2_OFFICIAL_SEED_TIEBREAKER_RULE.md` — Capture Back record of the decision.

