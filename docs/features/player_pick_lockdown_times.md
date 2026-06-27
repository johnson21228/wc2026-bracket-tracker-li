# Player Pick Lockdown Times

Bracketeering has one active player-pick lockdown concept:

After `LockDownTime2`, player picks are final.

## Behavior

When `LockDownTime2` is reached:

- all player-owned picks are frozen;
- existing picks remain visible;
- the board should not visually change just because picks are locked;
- players cannot change, clear, or replace picks;
- UI attempts are blocked;
- model/controller write attempts are rejected.

This applies to player-owned picks only. Admin/site-owned official truth remains separate.

## Removed behavior

The previous first-lock gate has been removed.

There is no match-specific lock, no slot-specific R32 lock, and no feeder-team based lockdown behavior.


## Manual LockDown property

`LockDown` is a top-level site property.

When `LockDown` is `true`, all player-owned picks are frozen immediately and cannot be changed, cleared, or replaced.

When `LockDown` is `false`, the timed `LockDownTime2` rule controls the global player-pick freeze.
