# Completed Match Highlight Links

The group panel can make a completed match row/card clickable only when `site/data/current/match_highlights.json` contains a verified URL for that match ID.

This data file is checked-in model evidence. The browser runtime must not search, scrape, or infer highlight URLs.

## Verification rule

A link is stored only when external metadata identifies the relevant teams and FIFA World Cup 2026 context, while `site/data/current/group_matches.json` supplies the final-score evidence for the local model.

Stored highlight entries include:

- provider
- title
- url
- verifiedAt
- matchEvidence
- verificationNote

Completed matches without a verified URL must render as static evidence. Scheduled matches must not become highlight actions unless a valid URL is explicitly present in the local highlight model.

## Current update

This update fills links for the completed group-stage matches in the current snapshot, including the explicit missing example: United States 4-1 Paraguay.
