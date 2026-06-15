# Data Storage Rule

## Tournament truth

```text
data/teams.json
data/groups.json
data/group_stage_matches.json
data/group_standings.json
data/official_round_of_32.json
data/official_knockout_results.json
```

## Game 1

Round-of-32 Qualifier Pick Game:

```text
data/game_1_round_of_32_picks.json
data/game_1_scoring_rules.json
data/game_1_scores.json
```

## Game 2

Full Knockout Bracket Pick Game:

```text
data/game_2_bracket_picks.json
data/game_2_scoring_rules.json
data/game_2_scores.json
```

## Release state

Static HTML releases may embed the same state, but the Workbench data files are canonical.

## Separation rule

Do not mix tournament truth, player predictions, scoring rules, and calculated scores into one undocumented blob.
