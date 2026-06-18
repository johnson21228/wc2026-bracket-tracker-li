# Card 198 — Capture knockout schedule model and pub image authority

## Intent

Capture all knockout matches needed by the site and make the knockout pub background asset usable without preserving the incorrect `24 TEAMS` label.

## Changes

- Add `site/data/current/knockout_matches.json` for Matches 73–104.
- Add source evidence under `source/text/`.
- Add corrected source image under `source/images/`.
- Add runtime image projection under `site/assets/board/`.
- Add LI and docs defining model authority versus generated-image decoration.
- Add verifier for model completeness, image dimensions, and runtime references.

## Acceptance

- `make verify` passes.
- Knockout model has 32 matches and no `TBD` kickoff values.
- Match 103 is present.
- Match 85 carries the source-disagreement note.
- Runtime background points at the corrected knockout pub background.
