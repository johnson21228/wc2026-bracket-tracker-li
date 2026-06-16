# Game 1 Board Layers Milestone

Game 1 is now governed as a layered board surface rather than a single static image.

## Layer Order

1. Pub image background.
2. Transparent bracket geometry overlay.
3. Visible DOM slot buttons.
4. Modal chooser.

## Invariants

- The transparent PNG is not responsible for clicks.
- Hit targets must remain DOM elements above all decorative layers.
- Decorative layers must use `pointer-events: none`.
- Slot buttons must use `pointer-events: auto`.
- The chooser must filter teams according to the clicked slot rule.

## Debug Checks

In the browser console:

```js
document.querySelectorAll('.hotspot').length
```

Expected:

```text
32
```

In terminal:

```bash
grep -n "const STORAGE_KEY" site/game1/index.html
grep -n "r32_bracket_geometry_overlay" site/game1/index.html
grep -n "hitLayer" site/game1/index.html
grep -n "eligibleTeamsForSlot" site/game1/index.html
```

Expected: exactly one `const STORAGE_KEY`, plus the geometry, hit layer, and chooser filter tokens.
