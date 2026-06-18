# Pick conflicts warn, not block

User picks are durable user intent. The picker must not reject a known team in a known source-scoped slot merely because the current bracket state says the pick conflicts with another pick or with current standings.

## Rule

A slot menu remains source-scoped:

- A group-winner slot shows teams from its source group.
- A group-runner-up slot shows teams from its source group.
- A third-place candidate slot shows teams from its candidate source groups.
- Knockout slots show their feeder-path teams.

Within that source scope, conflicts are rendered, not blocked.

## Hard boundaries

The runtime may still reject:

- an unknown slot id;
- an unknown team id;
- a team outside the slot source scope;
- malformed import data.

## Soft conflicts

The runtime must preserve the pick and render a warning for:

- duplicate Round-of-32 use of the same team;
- a team currently ranked differently than the slot expects;
- a pick that became stale after standings or upstream picks changed.

The visible warning is the invalid-pick rendering contract: a thin red outline around the pick cell and a red `!` marker. The reason should be available through the existing pick validity reason path.
