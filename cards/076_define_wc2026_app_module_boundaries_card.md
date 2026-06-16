# Card 076 — Define WC2026 App Module Boundaries

## Intent

Create a durable LI boundary map for the WC2026 static website app so tournament data, qualification rules, game rules, scoring, geometry, UI rendering, and persistence stop collapsing into one page script.

## Why now

The app has at least two games:

- Game 1: predict/fill the Round of 32 qualification field from the 48-team group stage.
- Game 2: pick the knockout bracket from a fixed Round-of-32 seed.

The repo already has many focused LI rules, but the next architectural layer should define module responsibilities before more UI behavior is added.

## Scope

Add:

- `li/world_cup/app_module_boundaries_rule.md`
- `docs/architecture/wc2026_app_module_boundaries.md`
- `prompts/define_wc2026_app_modules.md`
- `capture_back/CAPTURE_BACK_WC2026_APP_MODULE_BOUNDARIES.md`

Future follow-up cards should extract code gradually and update verification.

## Acceptance

- Module boundaries are explicit.
- Game 1 and Game 2 remain separate.
- Tournament truth remains separate from player picks.
- Qualification rules remain separate from board geometry.
- UI rendering is not allowed to become hidden rule authority.
