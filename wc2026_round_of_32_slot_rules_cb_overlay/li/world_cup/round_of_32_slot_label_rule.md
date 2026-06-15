# Round-of-32 Slot Label Rule

## Purpose

Round-of-32 bracket slots should not be treated as empty generic placeholders.

Before the teams are officially known, each slot should preserve the qualification meaning of that slot.

Examples:

```text
Winner Group A
Runner-up Group B
Best third-place team from Group C/D/E/F
```

## Principle

Separate:

```text
slot meaning
```

from:

```text
team assigned to slot
```

The slot meaning can exist before the team is known.

The team assignment should only be resolved after official group-stage results and advancement rules determine the team.

## Slot object

Each Round-of-32 slot should support:

```json
{
  "slotId": "R32-M1-A",
  "matchId": "R32-M1",
  "side": "A",
  "label": "Winner Group A",
  "qualificationRule": "group_winner",
  "sourceGroup": "A",
  "thirdPlacePool": [],
  "team": null,
  "status": "pending",
  "source": "official_bracket_rule",
  "notes": ""
}
```

## Status values

Use:

```text
pending
resolved
manual_override
needs_verification
```

## HTML behavior

Before resolution, the bracket should display the slot label.

After resolution, the bracket should display both:

```text
team name
slot label
```

Example:

```text
🇲🇽 Mexico
Winner Group A
```

## Capture Back requirement

Adding, changing, or resolving bracket slot labels requires Capture Back.

The capture should record:

- slot id
- previous label
- new label
- source
- team resolution, if any
- uncertainty, if any
