# R32 Pick Card Tooltip Rule

A filled R32 pick card may expose extended team, slot, and rule properties through a tooltip or details popover.

## Boundary

The card remains compact and team-first. Extended data belongs in tooltip/detail surfaces, not in the always-visible card.

## Extended properties

The tooltip/details surface may show:

- selected team name
- team flag
- FIFA/team code
- team group
- R32 slot id
- visible slot rule
- long qualification route
- eligible group source
- game surface
- pick status
- edit/change affordance

## Interaction

Hover, keyboard focus, or long press may reveal explanatory details. Tap/click may open the same slot chooser or a details popover.

For Game 1, the tooltip should help the user answer:

1. Who did I pick?
2. Why is this team valid for this slot?

## Accessibility

Tooltip content must also be represented in accessible labels or title text so keyboard and assistive-technology users can inspect pick context.
