# Card 183: Define group standings panel LI

## Purpose

Define the Living Infrastructure rule for a group standings panel that can support Round of 32 pick context, current group evidence, match results, and optional highlight links without damaging the clean MVC single-site runtime.

## Boundary

This card defines LI only. It does not implement the panel UI, fetch live standings, scrape ESPN, or change pick behavior.

## Intent

The site should be able to show a group standings panel that explains the current group context behind a pick menu.

The panel should help a user answer questions such as:

- Which team is currently first in Group A?
- Which team is currently runner-up in Group C?
- Which team is currently third in a group?
- What matches have been played in this group?
- What were the scores?
- Is there a highlight link for the match?

## Required LI rule

Add `li/world_cup/group_standings_panel_rule.md`.

## Acceptance criteria

- The LI defines the group standings panel as part of the one site, not a second site.
- The LI states that current standings/matches are stored as site data, not scraped by the browser at runtime.
- The LI defines a data-updated-by-WB workflow: CB updates may refresh standings, scores, match status, and highlight links as games are played.
- The LI preserves clean MVC responsibility:
  - Model owns standings/match/highlight data and derived ranking.
  - View renders the panel.
  - Controller opens/closes the panel and routes user actions.
- The LI states that R32 pick menu titles can link to or invoke the group standings panel.
- The LI distinguishes group winner, runner-up, and third-place source context.
- The LI states that third-place R32 slots must display constrained group-source context such as `3RD A/E/H/I/J`, not third-place rank positions 1–8.

## Non-goals

- No automatic scraping in the browser.
- No second site or test page.
- No change to the active pick cascade model.
- No YouTube search automation in the site runtime.
