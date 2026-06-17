# Game 1 Canonical Render Visual Uniformity Rule

## Rule

All rendered Game 1 knockout picks must be read from canonical pick state and rendered with one normal visual treatment.

Once a pick is rendered by canonical state, its appearance must not depend on legacy storage source, stored bridge path, finality marker, or stale adornment class.

## Required Boundary

The canonical model answers:

- does the pick exist?
- is the pick valid?
- is the pick renderable?

The visual layer answers only:

- how does a normal valid pick look?
- how does an actively hovered/focused pick look?

## Prohibited Persistent Visual Signals

Normal rendered R16/QF/SF cards must not persistently show:

- heavy white outline
- heavy white border
- stored-state glow
- finality glow
- special drop shadow that makes one valid pick appear more selected than another

## Allowed Visual Signals

Heavy outline is allowed only during active interaction:

- hover
- focus-visible

## Implementation Requirement

Normalize the following rendered knockout card selectors to one baseline treatment:

- `.r16PickCard`
- `.advancePickCard`
- `.storedKnockoutPickCard`
- `[data-r32-slot-fit="true"]`
- `[data-choice-can-remain-final]`
- `.finalEligiblePick`

The normalization must preserve Card 154 and Card 155 invariants:

- `WC2026_GAME1_PICK_STATE` remains the canonical state source.
- stored knockout rendering continues to read through canonical state.
