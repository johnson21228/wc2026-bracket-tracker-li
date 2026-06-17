# Card 149 — Replace UnPick Word With Delete Graphic

## Intent
The pick menu should not use the awkward prototype word "UnPick". Pick-removal affordances should render as a compact delete graphic so the menu language matches the polished bracket board interaction.

## Rule
- Detect existing pick-removal controls that use `UnPick`, `Unpick`, or equivalent prototype labels.
- Preserve their existing behavior and event handlers.
- Replace only the visible presentation with a compact trash/delete graphic.
- Provide accessible labeling with `aria-label="Delete pick"` and `title="Delete pick"`.
- Continue to work for dynamically rendered menu content.

## Verification
Run:

```bash
python3 tools/verify_wc2026_delete_pick_button_graphic_patch.py
python3 tools/verify_wc2026_bracket_tracker.py
make verify
```
