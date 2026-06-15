# Public Team Identifier Display Rule

## Purpose

The public bracket should emphasize flags and team names, not internal identifiers.

## Rule

Hide small metadata identifiers in the public UI by default, such as:

```text
MEX - GA
BRA - GC
team abbreviation + group
```

## Data preservation

Do not remove identifiers from the data model.

The site should still preserve:

- team abbreviation
- group
- canonical name
- source identifiers
- exported JSON state

## Builder controls

A later builder/debug view may show identifiers again for Steve.

The public player-facing view should keep them hidden unless explicitly requested.
