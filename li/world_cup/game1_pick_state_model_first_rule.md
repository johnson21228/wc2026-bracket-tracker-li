# Game 1 Pick State Model-First Rule

## Rule

Game 1 bracket work must define and use a canonical pick-state model before changing UI, rendering, menu behavior, highlights, or persistence mirrors.

The UI is not the authority.

Rendering is not the authority.

LocalStorage mirrors are not the authority.

The canonical model is the authority.

## Required Architecture

Game 1 pick state should be represented by one canonical model:

```text
WC2026_GAME1_PICK_STATE
```

The model owns:

- loading canonical state
- saving canonical state
- clearing canonical state
- reading a pick by slot id
- writing a pick by slot id
- clearing a pick by slot id
- finding source/feeder slots
- deciding whether a pick is valid
- deciding whether a slot is pickable
- producing renderable picks

## Required API Shape

The model should expose functions equivalent to:

```js
window.WC2026_GAME1_PICK_STATE = {
  load(),
  save(nextState),
  clear(),
  getPick(slotId),
  setPick(slotId, team, rule),
  clearPick(slotId),
  getSourceSlotIds(slotId),
  isPickValid(slotId),
  isSlotPickable(slotId),
  getRenderablePicks()
};
```

## Required Data Shape

Each pick must contain enough information to validate itself against the current bracket state:

```json
{
  "round": "R16",
  "slotId": "L-R16-01",
  "teamId": "USA",
  "abbr": "USA",
  "name": "United States",
  "flagEmoji": "🇺🇸",
  "sourceSlotIds": ["L-R32-01", "L-R32-02"]
}
```

Required fields:

- `slotId`
- `round`
- team identity: `teamId`, `abbr`, `name`, `flagEmoji`
- `sourceSlotIds` for downstream picks

## Validity Rule

R32 picks are valid if they contain a team.

Downstream picks are valid only if all feeder picks still exist and are valid.

- R16 requires both source R32 picks.
- QF requires both source R16 picks.
- SF requires both source QF picks.
- Final / Champion requires feeder picks.

Do not ask only:

```text
Is there a stored R16 pick?
```

Ask:

```text
Is there a stored R16 pick and are its source slots currently valid?
```

## UI Rule

No UI layer may decide pick validity.

No render layer may render a downstream pick directly from localStorage.

No menu layer may decide current-pick highlighting directly from stale storage.

All pickability, current-pick, highlight, and renderability decisions must go through the canonical Game 1 pick-state model.

## Repair Order

When changing Game 1 pick behavior, use this order:

1. Define or update the canonical state model.
2. Define or update validity rules.
3. Route writes through the model.
4. Route rendering through the model.
5. Route menu pickability/highlighting through the model.
6. Retire or mirror legacy stores only after the model is authoritative.

Do not add another late DOM scrub, render wrapper, or highlight patch as a substitute for canonical model repair.
