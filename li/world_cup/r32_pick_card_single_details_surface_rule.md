# R32 Pick Card Single Details Surface Rule

A filled Round of 32 pick card must expose at most one visible details surface at a time.

## Rule

The visible card is the compact identity surface. It shows the selected team flag and selected team name.

The details surface is the explanatory surface. It may show team code, group, slot, qualification route, eligible source, and edit action.

The UI must not show both a native browser title tooltip and a custom tooltip for the same card. Native `title` attributes are not allowed on filled pick cards when a custom details surface exists.

## Fit requirement

The team name must fit the pick card when reasonably possible. The renderer may widen the card within the pixel-native board plane and may reduce the team-name font size to avoid truncation.

Truncation is allowed only as a fallback for unusually long team names after the card width and font-size fit strategy has been applied.

## Interaction

Hover and keyboard focus may show the details surface. Tap/click may reopen the chooser for the associated slot. The details surface must not block the card's primary interaction.
