# Pick Validity Rendering Rule

A user pick is durable user intent. Current standings and slot rules judge whether that intent is valid, but they must not silently erase it.

The picker may allow a broad set of user choices for a slot. After a choice is made, the model must evaluate the pick against the slot's current rule and return a pick-validity state for rendering.

Invalid picks remain visible in the bracket. They are rendered as the same compact picked-cell identity plus:

- a thin red outline around the pick cell
- a red `!` marker inside the picked cell
- an accessible/title reason explaining why the pick is invalid when available

The invalid marker is non-destructive. It does not replace the flag or the three-letter code, and it does not clear the user's pick.

Auto-clearing invalid picks is not the default behavior. Clearing or repairing an invalid pick is an explicit user action.

## Validity states

The runtime may use these states:

- `valid` — the selected team currently satisfies the slot rule.
- `invalid` — the selected team is known not to satisfy the slot rule.
- `unknown` — the current model cannot fully judge validity yet.
- `empty` — no team is selected.

Only `invalid` receives the red warning treatment.

## First-pass slot checks

For Round-of-32 group-winner and group-runner-up slots, current standings rank is enough to identify a known invalid pick:

- group-winner slots expect current rank 1 from that group
- group-runner-up slots expect current rank 2 from that group

Third-place allocation may remain provisional until the official source group is resolved. The UI may preserve third-place picks without red invalid treatment unless the current model can prove the pick does not satisfy the source rule.
