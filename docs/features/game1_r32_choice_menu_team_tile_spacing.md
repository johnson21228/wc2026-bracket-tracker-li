# Game 1 R32 Choice Menu Team Tile Spacing

## Problem

The choice menu still displayed joined labels such as `GermanyGER · Group E` after several spacing repairs.

Inspection showed the live renderer is not the `.choiceText` path. It is this `.teamTile` path:

```html
<span class="teamMeta">
  <span class="teamName">Germany</span>
  <span class="teamDetail">GER · Group E</span>
</span>
```

The old `.teamMeta` rule only set `min-width: 0`, so the two inline spans rendered adjacent.

## Repair

Make `.teamMeta` an inline flex layout and give it an explicit gap. Also give `.teamDetail` a margin-left fallback so spacing survives if flex is later overridden.

## Player-facing requirement

The country name and metadata must read as separate regions:

```text
Germany  GER · Group E
Curacao  CUW · Group E
Ivory Coast  CIV · Group E
```
