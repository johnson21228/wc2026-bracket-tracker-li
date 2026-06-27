# Card 1021: Knockout Pub Background Image Prompt

## Intent
Add a reusable prompt for regenerating the knockout pub background image from current site truth.

## Rule
The prompt must use `site/assets/board/knockout_pub_background.jpeg` as the base/reference image and runtime target. It must inspect current schedule and official R32 truth before producing a new image.

## Acceptance
- `prompts/update_knockout_pub_background_image.md` exists.
- The prompt references `site/assets/board/knockout_pub_background.jpeg` as the base image.
- The prompt uses `site/data/current/knockout_matches.json` as schedule authority.
- The prompt uses `site/data/current/official_truth.json` as known R32 team truth.
- The prompt requires date headers and one row per match.
- Known rows render as `Flag vs Flag`; unresolved rows render as `TBD`.
- Flag sizing guidance is captured.
- Verification is wired into `make verify`.
