# Capture Back — Group-stage match times

This CB fills the full group-stage match-time model from published schedule evidence.

It separates group-stage match timing from knockout timing:

- Group-stage times live in group-stage schedule data.
- Knockout times live in `knockout_matches.json`.
- UI fallbacks may still exist for genuinely unknown values, but scheduled group matches should not display `Time TBD`.
