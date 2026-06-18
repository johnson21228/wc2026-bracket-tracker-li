# Current Group Order Rendering

The group UI should feel like a live tournament surface, not a static draw poster. Once standings data exists, any team list inside a group should follow the current standings order.

This keeps the group rail, group panels, and pick-menu group choices aligned with the player's real question: who currently sits first, second, third, and fourth in the group?

The model now owns a single ordering helper. It uses `site/data/current/group_standings.json` first and falls back to checked-in group membership order only when standings are missing or incomplete.

For Group A after the Czechia/South Africa draw, the expected order is:

```text
MEX, KOR, CZE, RSA
```

The runtime still consumes checked-in local data only. It does not scrape ESPN, FIFA, or any external site in the browser.
