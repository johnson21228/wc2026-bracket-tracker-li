# Capture Back: Single Rules Display

## Intent

Replace the selector-driven Game 1 / Game 2 Rules modal with one player-facing Rules display for Bracketeering Pub-Hub.

## Product direction

Bracketeering Pub-Hub should explain itself as one continuous two-game World Cup pool:

- Game 1 predicts the Round of 32 field before the final group-stage matches.
- Game 2 carries the Pub-Hub forward into the knockout bracket once FIFA finalizes the Round of 32.
- The live product should transition seamlessly from Game 1 into Game 2 as official results resolve the bracket field.

## Development-state explanation

The Dev Game View selector remains visible while the site is under development. It is explained as a development preview tool. Current viewers are encouraged to play Game 1 and try the simulated Game 2 view before the site becomes live for real pool play.

## Player-facing rule

The Rules panel should not switch based on the Dev Game View selector. It should show one coherent rules explanation.

## Verification

`tools/verify_wc2026_banner_rules_panel_ui.py` now verifies the single Rules display and rejects the old selector-driven rules sections.

## Group Stage Finale lock language

Game 1 lock timing should be described player-facing as the start of the **Group Stage Finale**.

Canonical spelling: `Finale`.

The rule copy should still define the exact lock condition: all Game 1 picks must be submitted before kickoff of the earliest third-round group-stage match.

