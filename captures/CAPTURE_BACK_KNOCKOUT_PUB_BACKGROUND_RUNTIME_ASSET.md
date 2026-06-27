# Capture Back — Knockout Pub Background Runtime Asset

## What changed

The latest generated knockout pub calendar image is promoted as the runtime knockout background asset:

- `site/assets/board/knockout_pub_background.jpeg`

The generation manifest is retained at:

- `source/text/knockout_pub_background_generated_manifest.json`

The reusable prompt is refined so the next `UPDATE KNOCKOUT PUB BACKGROUND IMAGE` run starts from the latest accepted runtime image and performs an incremental refresh.

## Why

The background is a pub-photo-inspired calendar asset. Future updates should not redesign the calendar. They should preserve the accepted image and replace only unresolved `TBD` rows when authoritative site data has new teams.

## Guardrails

- JSON data remains authority.
- The JPEG is only a visual projection.
- Do not invent teams.
- Do not change gameplay logic.
- Do not add row frames or footer/provenance text.
- Keep `TBD` and `vs` small/subtle.
- Keep upper-left bulb/neon lighting dimmed.

## Verification

- `python3 tools/verify_wc2026_knockout_pub_background_runtime_asset.py`
- `make verify`
