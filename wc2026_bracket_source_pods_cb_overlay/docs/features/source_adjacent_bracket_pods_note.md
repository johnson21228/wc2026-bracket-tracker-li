# Source-Adjacent Bracket Pods Note

The current bracket is trying to align rounds with global spacing.

A better layout is to group each source pair and result into a pod.

## Example

```text
R32 Match 1 ┐
            ├ R16 result
R32 Match 2 ┘
```

This places the result directly beside the games that feed it.

## Why this is better

- less fragile than spacer values
- easier to understand visually
- easier to screenshot and recover
- easier to tune with CSS
- closer to the actual tournament tree

## Implementation direction

Replace the current column/spacer layout with nested source pods.

Start with R32 → R16 pods.

Then compose:

```text
two R16 pods → QF pod
two QF pods → SF pod
SF left/right → Final
```
