# Card 190: Add Group Panel Highlight Link Storage

## Intent

Capture the local highlight-link storage contract for completed group matches and keep external highlight navigation inside the group panel evidence surface.

## Scope

- Store verified highlight URLs in `site/data/current/match_highlights.json`.
- Seed the user-provided Argentina 3-0 Algeria YouTube highlight link.
- Seed a small set of verified FIFA YouTube highlight links where the match title/result clearly match local completed-match evidence.
- Preserve empty/absent highlights for completed matches without verified URLs.
- Keep runtime ESPN-free.
- Use normal external-link behavior: `target="_blank"` and `rel="noopener noreferrer"`.

## Out of scope

- Third-place slot semantics.
- Scraping ESPN or YouTube at runtime.
- Inventing links for completed matches that do not have a verified highlight URL.
