# Round-of-32 Drop Only Rule

## Purpose

Drag/drop placement should be limited to Round-of-32 slots.

Later-round slots should not accept arbitrary team drops.

## Principle

Round-of-32 slots are the entry points into the knockout bracket.

Later rounds should be populated by:

- player winner selections
- official results
- derived advancement
- bracket scoring logic

not by dragging teams directly into later-round slots.

## UI rule

Only slots whose ids begin with `R32-` should be drop targets.

Examples of valid drop slots:

```text
R32-L-M1A
R32-L-M1B
R32-R-M8A
R32-R-M8B
```

Examples of non-drop slots:

```text
R16-L-S1
QF-L-S1
SF-R-S2
FINAL-A
CHAMPION
```

## Later-round interaction

Later-round slots may still be clickable/selectable later, but they should represent a pick from the valid upstream winners.

A later implementation may allow:

```text
click winner in R32 → advances to R16
click winner in R16 → advances to QF
```

But that is different from arbitrary drag/drop.

## Data rule

Exported state should distinguish:

```text
seeded R32 teams
```

from:

```text
derived or selected winners
```

Do not store later-round arbitrary drops as if they were valid bracket picks.
