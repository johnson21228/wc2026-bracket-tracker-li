# Game 1 Pick State Model-First Insight

## Insight

The bracket bugs are not primarily visual bugs. They are state-authority bugs.

The current page has multiple stores and multiple render wrappers. This lets old R16/QF/SF data survive in one path and get rendered by another path.

The fix is to build the data model first, then make UI/rendering obey the model.

## Problem Pattern

The dangerous pattern is:

```js
const pick = storedPickForSlot(rule.slotId);
if (!pick) return;
renderOneR16Pick(rule, pick);
```

This renders a downstream pick just because it exists in storage.

That is not enough.

A downstream pick must be valid against its feeder picks.

## Correct Pattern

```js
const pick = model.getPick(slotId);
if (!model.isPickValid(slotId)) return;
renderPick(slotId, pick);
```

## Correct Build Order

1. Canonical model
2. Validity rules
3. Writes
4. Rendering
5. Menus/highlights
6. Legacy mirror retirement

## Why This Matters

If the UI is allowed to decide state, the page can display stale picks.

If rendering reads directly from legacy stores, Clear picks can appear to fail.

If menu highlighting reads from stale downstream state, a slot can look preselected even when the bracket should be empty.

The model must answer these questions:

- What picks exist?
- Which picks are valid?
- Which slots are pickable?
- Which picks are renderable?
- Which menu item, if any, is current?

The UI should only display those answers.
