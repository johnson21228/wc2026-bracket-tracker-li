# Capture Back — WC2026 App Module Boundaries

## Captured decision

The WC2026 Bracket Tracker should be treated as a modular static app, not as a single HTML experiment.

The main modules are:

1. Source Evidence
2. Tournament Data
3. Qualification Rules
4. Game 1 R32 Qualifier Prediction
5. Game 2 Knockout Bracket Prediction
6. Scoring
7. Board Geometry
8. UI Surface
9. Persistence / Export
10. Verification

## Key boundary

Tournament truth, player picks, scoring, and UI rendering must remain separate.

Game 1 can provide comparison/tiebreaker metadata to Game 2, but Game 1 picks must not mutate the fixed Game 2 R32 seed.

## Current-state note

The current site still embeds substantial Game 1 data/runtime behavior directly in `site/game1/index.html`. This is accepted as transitional. Future work should extract shared facts and rules into `site/data/` JSON and `site/assets/js/` modules.
