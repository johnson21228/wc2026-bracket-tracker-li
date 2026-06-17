# Game 1 Canonical Render Visual Uniformity

## Summary

After the Game 1 canonical pick-state model was introduced, rendering should be understood as a projection of canonical truth.

If a knockout pick renders, it renders because the canonical model says it is valid.

That means rendered R16/QF/SF picks should not carry visual differences from older storage paths, stored bridges, or finality/adornment passes.

## Rule

All rendered knockout cards share one baseline visual treatment.

The UI may use hover/focus affordances, but it must not persistently mark a rendered canonical pick with a heavier white outline, glow, or shadow merely because of:

- old storage source
- stored bridge class
- R32 fit metadata
- finality metadata
- downstream repair pass

## Correct Mental Model

```text
Canonical model = whether the pick exists and is valid.
Renderer = displays the canonical pick.
CSS = one consistent visual language for every valid rendered knockout pick.
```

## Visual State Boundary

Persistent state should be semantic, not decorative.

A card may carry data attributes needed by later logic, but those attributes must not make one valid rendered R16/QF/SF pick look more selected than another.

Heavy outline belongs only to interaction states:

- `:hover`
- `:focus-visible`
