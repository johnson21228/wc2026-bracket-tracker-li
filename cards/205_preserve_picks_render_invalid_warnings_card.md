# Card 205: Preserve Picks and Render Invalid Warnings

## Intent
Separate user pick intent from current model validity.

## Change
A pick can remain stored and visible even when current standings or feeder paths make it invalid. Invalid picks render with a thin red outline and red `!` marker.

## Runtime
- Model computes `pickValidity` per slot.
- View renders invalid pick warning state.
- CSS provides the red outline and warning badge.
- Auto-clear is no longer the default validity response.

## Acceptance
- User picks are not silently erased by standings or feeder changes.
- Invalid picks are conspicuous but non-destructive.
- Verification is wired into `make verify`.
