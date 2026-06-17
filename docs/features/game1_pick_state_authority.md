# Game 1 Pick State Authority

The current Game 1 implementation accumulated several localStorage keys and window mirrors while R32, R16, QF/SF, menu selection, Pages review acceptance, and stored-pick rendering were added in separate overlays.

This caused stale downstream picks to survive in secondary stores. A renderer could find an old R16 pick and draw a card or highlight even after the user believed the bracket was cleared.

The best-practice fix is to consolidate authority:

1. Treat `wc2026.game1.bracketPicks` as canonical browser-side state.
2. Treat all other stores as mirrors only.
3. Make downstream picks renderable only when feeder picks exist.
4. Disable prototype memory such as short-term R16 holds.
5. Clear all stores on Clear picks, then render from canonical empty state.

The important bug pattern is a renderer like this:

```js
const pick = storedPickForSlot(rule.slotId);
if (!pick) return;
renderOneR16Pick(rule, pick);
```

That is insufficient. The renderer must ask whether the stored pick is currently valid:

```js
const pick = storedPickForSlot(rule.slotId);
if (!storedKnockoutPickIsRenderable(rule, pick)) return;
renderOneR16Pick(rule, pick);
```
