# Player Pick Lockdown Times

The runtime reads lockdown properties from site/data/current/site_properties.json.

Required properties:

- LockDownTimeZone: America/New_York
- LockDownTime1: 2026-06-28T15:00:00-04:00
- LockDownTime2: 2026-06-29T13:00:00-04:00

LockDownTime1 is slot-scoped to the Canada vs South Africa Round of 32 pick.

LockDownTime2 is bracket-scoped and freezes all remaining player-owned picks.

Locked picks remain visible. Locked pick interactions are blocked by site/js/services/PickLockdownPolicy.js.
