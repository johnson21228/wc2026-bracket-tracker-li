# From Bar Photo To World Cup Game

This Workbench began with a photo of a World Cup match schedule poster seen in a bar.

That matters because it demonstrates the Workbench product pattern:

```text
real-world source artifact
↓
captured evidence
↓
structured data
↓
current solution
↓
continued evolution
```

The initial source artifact is:

```text
source/images/match_schedule_group_stage_poster_michelob_ultra.jpeg
```

From that image, the Workbench derived:

```text
source/text/poster_transcription.md
data/group_stage_matches_from_poster.json
data/groups_from_poster.json
```

The first current solution is a static HTML bracket tracker.

The next current solution is a Game 1 pool where players pick the 32 teams that advance from the 48-team group stage.

Later, after the official Round of 32 is known, the solution evolves into a full knockout bracket pool.

## Product lesson

The Workbench did not begin by designing a complete software system.

It began by capturing the work.

The solution emerged from the captured source, LI, and Capture Back history.
