# Source-Adjacent Bracket Pod Layout Rule

## Purpose

The bracket should place later-round results directly adjacent to the source games that feed them.

Spacer-based global column layouts are fragile and can make R16/QF/SF slots feel visually disconnected.

## Preferred model

Use bracket pods.

A pod groups source games and the result slot they feed.

Example:

```text
R32 Match 1 ┐
            ├─ R16 slot
R32 Match 2 ┘
```

For the opposite side:

```text
R16 slot ─┤
          ├ R32 Match 1
          └ R32 Match 2
```

## Recursive model

The same idea applies recursively:

```text
R32 pod + R32 pod → QF slot
QF pod  + QF pod  → SF slot
SF left + SF right → Final
```

## CSS guidance

Prefer nested CSS grid or flex containers over arbitrary spacer math.

Acceptable structures:

- local two-column grids for R32 → R16 pods
- nested pod containers for R16 → QF
- mirrored left/right pod layouts
- connectors drawn inside pods

## Data model requirement

Each pod should know:

- source matches
- result slot
- side
- round
- label
- tooltip

## Screenshot rule

A screenshot should make it visually obvious which source matches feed which result slot.

The goal is not just visual beauty; the bracket should be recoverable as data from the visible layout.
