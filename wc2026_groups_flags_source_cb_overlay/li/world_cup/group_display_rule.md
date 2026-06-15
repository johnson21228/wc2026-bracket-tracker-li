# Group Display Rule

## Purpose

The site should include a visible Groups section.

The Groups section should show all 12 groups, A through L, with:

- group letter
- flag
- team name
- optional abbreviation
- canonical team name
- friendly display name, if different

## Source posture

Group display data may be seeded from images, but must remain marked as pending official verification until checked against official sources.

## Canonical vs display names

Some images use common or alternate names.

The Workbench should preserve both when useful:

```json
{
  "name": "Côte d’Ivoire",
  "displayNameFromImage": "Ivory Coast",
  "abbr": "CIV"
}
```

## Static HTML requirement

The site should include:

```text
Groups
  Group A
  Group B
  ...
  Group L
```

Each group should be visible enough to support:

- user review
- screenshots
- Game 1 pick selection
- later group standings
- source verification

## Game 1 relevance

The Game 1 picker should allow users to select teams from group cards.

The group display should make it obvious which four teams belong to each group.
