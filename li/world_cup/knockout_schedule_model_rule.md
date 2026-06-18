# Knockout Schedule Model Rule

The Workbench must model the full FIFA World Cup 2026 knockout stage as structured data, not as unreadable text embedded inside generated pub art.

Required model truth:

- 32 knockout teams qualify from the group stage.
- 32 knockout matches are modeled: Match 73 through Match 104.
- The model includes Round of 32, Round of 16, quarter-finals, semi-finals, third-place match, and final.
- No kickoff field may remain `TBD` unless current sources truly have not published it.
- Match edges such as `W73`, `L101`, and third-place candidate sets are preserved as bracket references.
- FIFA is preferred for bracket allocation and venue authority.
- Published broadcaster schedules may provide kickoff-time evidence when FIFA pages are not automation-readable.

Image rule:

- `source/images/wc2026_knockout_pub_calendar_background.jpeg` is the Workbench truth asset.
- `site/assets/board/knockout_pub_background.jpeg` is the runtime projection.
- The left chalkboard must say `32 TEAMS`, not `24 TEAMS`.
- Fine schedule text inside the generated image is decorative only. The JSON model is the data authority.
