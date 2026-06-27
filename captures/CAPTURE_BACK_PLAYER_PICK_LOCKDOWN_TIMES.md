# Capture Back: Player Pick Lockdown Times

## Outcome

Player pick lockdown now means one global finality rule:

After `LockDownTime2`, no player-owned pick can be changed, cleared, or replaced.

## Preserved behavior

- Locked picks remain visible.
- Rendering does not change merely because a pick is locked.
- Player-owned pick writes are blocked after the global lock.
- Admin/site-owned official truth remains outside player-pick lockdown.

## Removed behavior

The previous first-lock gate has been removed.

The previous match-specific / R32 slot-specific lock path is no longer part of the model, runtime, or LI.


## Manual LockDown property

`LockDown` is a top-level site property.

When `LockDown` is `true`, all player-owned picks are frozen immediately and cannot be changed, cleared, or replaced.

When `LockDown` is `false`, the timed `LockDownTime2` rule controls the global player-pick freeze.
