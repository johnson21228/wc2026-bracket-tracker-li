# Card 1022 — Use Generated Knockout Pub Background as Runtime Asset

## Intent

Promote the latest generated knockout pub calendar image into the site runtime asset path and preserve a prompt that can generate the next incremental update.

## Runtime target

- `site/assets/board/knockout_pub_background.jpeg`

## Prompt target

- `prompts/update_knockout_pub_background_image.md`

## Acceptance

- The site continues to use `site/assets/board/knockout_pub_background.jpeg` for the knockout-board background.
- The generated image is present at that path.
- The generated manifest is present at `source/text/knockout_pub_background_generated_manifest.json`.
- The update prompt says future runs use the latest accepted runtime image as base.
- The update prompt says newly known teams replace only resolved `TBD` rows.
- The update prompt preserves no row frames, tiny/subtle `TBD`, tiny/subtle centerline `vs`, dimmed upper-left lighting, and no footer/caption text.
- Verification remains local and does not alter gameplay logic.

## Verification

- `python3 tools/verify_wc2026_knockout_pub_background_runtime_asset.py`
- `python3 tools/verify_wc2026_knockout_pub_background_image_prompt.py`
- `make verify`
