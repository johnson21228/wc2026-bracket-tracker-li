# Player Pick Lockdown Times Rule

Player pick lockdown is a global player-pick finality rule.

After `LockDownTime2`, no player-owned pick may be changed, cleared, or replaced.

## Current rule

- `LockDownTime2` is the only active player-pick lockdown time.
- `LockDownTime2` applies to all player-owned picks.
- Locked picks remain visible exactly as they were before lockdown.
- Lockdown is not a rendering change.
- Lockdown is enforced at player-pick write boundaries.
- Late browser interactions should be blocked before they reach pick editors.
- Late model/controller writes must be rejected.
- Site-owned official truth remains outside player-pick lockdown.

## Removed rule

The previous first-lock gate has been removed.

The code and LI should not describe any match-specific, R32-only, slot-specific, or feeder-team lockdown behavior.


## Manual LockDown property

`LockDown` is a top-level site property.

When `LockDown` is `true`, all player-owned picks are frozen immediately and cannot be changed, cleared, or replaced.

When `LockDown` is `false`, the timed `LockDownTime2` rule controls the global player-pick freeze.
