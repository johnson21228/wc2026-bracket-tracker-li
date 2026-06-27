# CAPTURE BACK: Knockout Pub Background Image Prompt

Captured a reusable site prompt for updating `site/assets/board/knockout_pub_background.jpeg` from current knockout schedule and official R32 truth.

The prompt asks the next LLM session to use the existing runtime image as the base/reference image, preserve the pub/gameboard style, and regenerate a readable calendar-style background.

Required visual behavior:

- Each day section shows the date at the top.
- Each match gets one row.
- Known rows show `Flag vs Flag`.
- Unknown or uncertain rows show `TBD`.
- Flags should be as tall as possible while fitting cleanly inside the row.

Data authority remains JSON:

- `site/data/current/knockout_matches.json` owns schedule and bracket edges.
- `site/data/current/official_truth.json` owns known R32 occupants.
- The generated image is projection only.
