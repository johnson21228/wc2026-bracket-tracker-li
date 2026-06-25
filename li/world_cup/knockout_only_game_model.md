# Knockout-Only Game Model

## Rule
Bracketeering is now a knockout-only game. The player-owned game begins only after FIFA determines the official Round of 32 field.

## R32 ownership
`Admin_/official` owns the R32 field. The R32 field means the team occupants assigned to the official Round-of-32 match slots.

Non-admin players may render R32 occupants from `Admin_/official`, but non-admin players cannot author R32 occupants. A player bracket must not treat group winners, group runners-up, third-place qualifiers, or R32 team occupants as player-authored picks.

## Player-owned picks
Player-owned picks begin with R32 match winners. Those winner choices populate the player's R16 picks and continue through later knockout rounds.

Player-owned knockout picks include only winner choices and later-round advancement choices that belong to the player. They do not include choosing which teams occupy the R32 field.

## Old model superseded
The old group-stage prediction model is no longer player-owned game behavior. Group-stage prediction language may remain only as archived/history context until future UI CBs remove or rename Game 1/Game 2 and group-prediction language.

## Runtime boundary
This CB is LI-only and does not change runtime behavior. Future runtime CBs should implement official R32 hydration first. Future UI CBs should then remove or rename Game 1/Game 2 and group-prediction language so the product copy matches this knockout-only model.
