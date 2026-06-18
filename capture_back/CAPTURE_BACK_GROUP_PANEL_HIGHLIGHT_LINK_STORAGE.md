# Capture Back: Group Panel Highlight Link Storage

## Captured decision

Completed matches in the group panel may become clickable highlight actions, but only when a verified highlight URL exists in local checked-in model data.

## Runtime boundary

The site runtime reads `site/data/current/match_highlights.json`. It does not fetch, parse, or scrape ESPN, YouTube, or FIFA pages at runtime.

## User-provided seed

The user provided this highlight link for Argentina 3-0 Algeria:

```text
https://youtu.be/JH_WRKTCPK4
```

The overlay stores it against match `66457018`.

## Rendering behavior

- Completed match + verified URL: external link opens in a new browser tab/window.
- Completed match without URL: static result evidence.
- Future match: kickoff time / Time TBD.

## Verification

The verifier checks the local highlight file shape, the seeded user URL, and the external-link runtime terms in the group panel view.
