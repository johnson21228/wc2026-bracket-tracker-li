# Group Standings Panel Rule

## Rule

The World Cup bracket tracker may include a group standings panel that projects the current group context behind a bracket pick.

The panel is part of the single site runtime. It must not create a second site, a parallel page architecture, or a separate app.

## User-facing purpose

The panel should let a user inspect the evidence behind group-derived picks:

- current group table
- group rank position: winner, runner-up, third place, fourth place
- all group matches for that group
- match status: scheduled, live, final, postponed, or unknown
- kickoff time when known
- score when known
- optional highlight link when known

## Data authority

Current standings and match information must be represented as site data, not as direct browser scraping.

Recommended data files:

```text
site/data/current/group_standings.json
site/data/current/group_matches.json
site/data/current/match_highlights.json
```

A Workbench CB update may refresh these files as games are played. The update may use public sources such as ESPN standings/schedules, official FIFA sources, or manually verified highlight links, but the site runtime should consume the normalized checked-in data.

The site must be able to run from its own stored data after a CB update. It must not depend on the user browser successfully scraping ESPN, YouTube, or another third-party site at runtime.

## MVC responsibility

The clean MVC single-site boundary applies:

- Model loads group standings, group matches, and highlight-link data.
- Model derives group ranking and exposes winner, runner-up, third-place, and eliminated status.
- Model exposes group context for any group-derived R32 pick menu.
- View renders the standings panel, match list, scores, statuses, kickoff times, and highlight links.
- Controller opens and closes the panel and routes actions from pick menu context.
- Controller must not hardcode group ranking, scores, or highlight URLs.

## Pick menu relationship

A group-derived pick menu should be able to project or invoke the group standings panel for its source context.

Examples:

- `1A` menu title: `Group A winner`
- `2C` menu title: `Group C runner-up`
- `3RD A/E/H/I/J` menu title before allocation is resolved: `Third-place team from Group A/E/H/I/J`
- resolved third-place source title: `Group H third-place`

The panel should help explain those titles by showing the relevant group table and matches.

## Third-place source rule

Round of 32 third-place slots are FIFA-constrained group-source slots, not third-place rank positions 1 through 8.

The UI must not describe a bracket slot as “third-place position 1,” “third-place position 2,” etc. when it means the FIFA source label. A slot labeled like `3RD A/E/H/I/J` means the assigned third-place team must come from one of those groups, according to the qualified third-place group combination and FIFA bracket allocation.

Before the source is resolved, the UI should show the constrained source set. After it is resolved, the UI should show the assigned group source.

## Highlight-link rule

Highlight links are optional per match.

If a highlight link exists, the panel may show it as a user-facing link. If no highlight link is known, the panel should show no link or an explicit neutral state such as `Highlights not added yet`.

The runtime must not invent a highlight URL.

## Update workflow

As games are played, a CB update may:

- update match status and score
- update group standings
- update derived group rank
- add or correct highlight links
- preserve source notes when helpful

Every data update should remain normalized enough for the Model to consume without scraping.
