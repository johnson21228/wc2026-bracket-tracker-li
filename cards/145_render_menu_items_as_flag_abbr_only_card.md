# Card 145 — Render Choice Menu Items as Flag + Three-Letter Code Only

## Intent
Choice menu rows should visually match the compact R32 item language: flag plus three-letter team code only.

## Rule
Menus may retain semantic data attributes and click behavior, but their visible content should be reduced to:

- flag
- FIFA-style three-letter abbreviation

Do not show full country names in menu rows.

## Acceptance
- Choice menu opens normally.
- Each team option displays compact flag + code.
- Existing pick selection behavior is preserved.
- Board-attached menu behavior is preserved.
- Long menu internal scrolling is preserved.
