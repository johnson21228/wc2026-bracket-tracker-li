# YouTube Highlight Enrichment Rule

## Purpose

The World Cup Bracket Tracker may include a YouTube highlight link for each match.

Highlights are optional enrichment for the public-facing site. They are not the authoritative source of match results unless explicitly marked as a manual source.

## Principle

A match result and a match highlight are different data.

- Match result: governed by official source authority.
- Match highlight: optional media enrichment.
- Player scoring: must be based on official or accepted result data, not highlight availability.

## Preferred highlight sources

Preferred order:

1. official FIFA highlight video
2. official broadcaster highlight video
3. official federation/team highlight video
4. reputable sports channel highlight video
5. manual user-provided YouTube link, marked as manual

## Required highlight fields

Each match may include:

```json
{
  "highlight": {
    "youtubeUrl": "",
    "youtubeId": "",
    "title": "",
    "source": "official|broadcaster|team|reputable_media|manual",
    "addedAt": null,
    "verifiedAt": null,
    "notes": ""
  }
}
```

## Static HTML behavior

The site should show a placeholder when no highlight is available.

When a YouTube link exists, the site may show:

- a link to the video
- an embedded player
- a thumbnail preview
- a title and source note

## Capture Back requirement

Adding, changing, or removing a highlight link requires Capture Back.

The capture note should include:

- match id
- teams
- YouTube URL
- source type
- whether it was verified
- release version affected
