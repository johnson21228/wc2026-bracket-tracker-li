# Data Storage Rule

## Purpose

This rule defines the core files that back the static HTML and later hosted site.

## Source-derived tournament data

```text
data/teams.json
data/groups.json
data/group_stage_matches.json
data/group_standings.json
```

The initial version may be derived from the uploaded poster image, but official sources should later verify or correct it.

## Official knockout data

```text
data/official_round_of_32.json
data/official_knockout_results.json
```

The official Round of 32 is unknown during initial setup and must be added later.

## Game 1 data

```text
data/game_1_round_of_32_picks.json
data/game_1_scoring_rules.json
data/game_1_scores.json
```

Game 1 asks players to pick the 32 teams that will advance from the 48-team group stage.

## Game 2 data

```text
data/game_2_bracket_picks.json
data/game_2_scoring_rules.json
data/game_2_scores.json
```

Game 2 asks players to complete the full knockout bracket after the official Round of 32 is known.

## HTML state

The HTML release may embed a copy of these data objects, but the Workbench data files are the canonical project source.
