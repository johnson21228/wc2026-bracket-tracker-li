# Game 1 Pick State Authority Rule

## Status
Active.

## Intent
Game 1 must have one authority for bracket pick state. R32 picks are the root inputs. R16, QF, SF, Final, and Champion picks are downstream decisions that are valid only while their feeder picks still exist.

## Canonical authority
`wc2026.game1.bracketPicks` is the canonical browser-side Game 1 pick record until a server-backed store replaces it.

Legacy stores may exist only as compatibility mirrors:

- `wc2026.game1.r32.picks`
- `wc2026.game1.r16.winnerPicks`
- `wc2026.game1.qfSf.winnerPicks`
- `wc2026.game1.knockoutPicks`
- `picks`
- `r16Picks`
- `advancementPicks`
- `window.game1KnockoutPicks`

These mirrors must never act as independent render authority.

## Required invariant
A downstream stored pick is renderable only if every feeder slot currently has a valid pick.

- R16 picks require both feeder R32 picks.
- QF picks require both feeder R16 picks.
- SF picks require both feeder QF picks.
- Later picks require their immediate feeders.

If a downstream stored pick exists but its feeders are missing, the downstream pick is stale. It must be ignored for rendering and may be cleared from all stores.

## Empty bracket invariant
When Game 1 has no R32 picks:

- R32 assignment slots remain live.
- R16/QF/SF/Final/Champion slots do not open choice menus.
- R16/QF/SF/Final/Champion stored pick cards, highlights, checkmarks, and current-choice adornments must not render.
- No short-term, hardcoded, or prototype hold may create a downstream pick.

## Menu invariant
Menu rows must not use stale stored downstream picks to preselect, highlight, outline, or check a candidate. If a menu displays current-choice state, that state must come from the canonical authority and must pass the feeder-validity rule.

## Clear picks invariant
Clear picks must reset the canonical authority and all compatibility mirrors. After Clear picks and refresh, the site must render an empty Game 1 state with only R32 pick actions live.

## Prohibited pattern
Do not add late DOM scrubbers or render wrappers as the primary solution. The primary fix must happen at the state read/render boundary: stale downstream picks must not be returned as renderable picks.

## Preferred implementation shape
Use one helper at the read boundary:

```js
function wc2026StoredKnockoutPickIsRenderable(rule, pick) {
  if (!pick) return false;
  const sourceIds = wc2026SourceIdsForRule(rule, pick);
  if (sourceIds.length < 2) return false;
  return sourceIds.every(wc2026SourcePickExists);
}
```

Renderers must check this before drawing stored R16/QF/SF/Final/Champion picks.
