WB_SESSION:
Card 000 Capture Back — Initial Group-Stage Schedule From Poster

Card:
- `cards/000_capture_initial_group_stage_schedule_from_poster_card.md`

Intent:
- Preserve the original photo of the World Cup match schedule poster as the first source artifact.
- Preserve the story that this Workbench-backed game began from a real-world image seen in a bar.
- Use the poster-derived source data as starter data for the WC2026 Bracket Tracker.
- Mark poster-derived data as preliminary until official sources verify it.

Source artifact:
- `source/images/match_schedule_group_stage_poster_michelob_ultra.jpeg`

Derived artifacts:
- `source/text/poster_transcription.md`
- `data/group_stage_matches_from_poster.json`
- `data/groups_from_poster.json`

Product story captured:
```text
Photo in a bar
↓
Workbench source artifact
↓
structured schedule data
↓
static HTML bracket game
↓
Game 1 Round-of-32 pick pool
↓
Game 2 knockout bracket pool
↓
scored, updateable World Cup site
```

LI meaning:
- The Workbench can begin with imperfect real-world source material.
- The source artifact is preserved.
- The data derived from it is explicit and reviewable.
- Later official sources can correct it without erasing the origin story.
- The current solution evolves from the captured source and living intent.

Acceptance:
- Original poster image exists in `source/images/`.
- Poster transcription exists in `source/text/`.
- Poster-derived JSON exists in `data/`.
- The data authority is marked poster-derived / pending official verification.
- The project story is captured in `docs/story/from_bar_photo_to_world_cup_game.md`.

Known uncertainty:
- Poster-derived data must still be verified against official FIFA schedule data.
- Any conflict must be captured as a correction, not silently overwritten.

Next:
- Move to Card 002: Add Game 1 Round-of-32 Pick UI.
