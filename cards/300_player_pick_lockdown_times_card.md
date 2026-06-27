# Card 300: Player Pick Lockdown Times

## Intent

Keep a single global player-pick lockdown rule.

## Rule

After `LockDownTime2`, no player-owned pick can be changed, cleared, or replaced.

## Runtime requirements

- `LockDownTime2` is loaded from `site/data/current/site_properties.json`.
- The lock applies globally to player-owned picks.
- Locked picks remain visible.
- Lockdown is enforced at write boundaries.
- Late UI interactions are blocked.
- Late model/controller writes are rejected.

## Removed

The previous first-lock gate is removed.

No match-specific, R32-slot-specific, or feeder-team lockdown behavior remains.


## Manual LockDown property

`LockDown` is a top-level site property.

When `LockDown` is `true`, all player-owned picks are frozen immediately and cannot be changed, cleared, or replaced.

When `LockDown` is `false`, the timed `LockDownTime2` rule controls the global player-pick freeze.
