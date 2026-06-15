# Game 1 Hit Testing Repair Rule

The canonical playable page is:

```text
game1_playfield.html
```

Release files under `releases/` are snapshots. They are not the page the user should normally open while iterating.

Hit testing must satisfy:

```text
board image pointer-events: none
hotspots z-index above board image
modal z-index above hotspots
32 R32 hotspots active
```

The page should visibly report the hotspot count so failures are obvious.
