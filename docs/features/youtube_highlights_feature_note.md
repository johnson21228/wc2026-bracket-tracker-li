# YouTube Highlights Feature Note

## Feature

Each match card in the static HTML site may include a YouTube highlight area.

Before the match:

```text
Highlights: not available yet
```

After the match:

```text
Highlights: Watch on YouTube
```

or an embedded video player.

## Why this fits the Workbench

The feature makes the public site more useful while preserving the Workbench separation between:

- official tournament truth
- user-facing enrichment
- player scoring
- static HTML release state

## Data posture

Highlights should be stored as optional match metadata.

They should not be used to calculate standings or scores.

## Suggested UI

Each match card can include:

```text
Mexico vs South Africa
Score: —
Highlights: Add YouTube link
```

After a link is added:

```text
Mexico vs South Africa
Score: 2–1
Highlights: Official FIFA highlights
[embedded YouTube video]
```

## Later evolution

The static HTML can support manual entry first.

A later server-backed version could allow an admin to paste highlight URLs directly into a protected admin UI.
