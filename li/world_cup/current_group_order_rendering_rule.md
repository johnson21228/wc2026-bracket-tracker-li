# Current Group Order Rendering Rule

Group-scoped team displays must use current standings order whenever current standings are available.

The source group/draw membership order remains model evidence, but it is not the preferred display order after standings exist. A group panel, group rail team grid, pick-menu group section, or future group card must present teams in the order supplied by `site/data/current/group_standings.json` when that group has standings entries.

If a standings entry cannot be resolved to a local team record, or if standings are unavailable for a group, the runtime may fall back to the checked-in group membership order from the group/team model. The fallback must be stable and deterministic.

The View should not invent a standings order. The Model owns group team ordering and provides already-ordered group collections to renderers.

## Acceptance

- Group panel rows render in standings entry order.
- R32 pick-menu group sections use current group order when standings exist.
- The group rail flag grid uses current group order when standings exist.
- Original draw order is only a fallback when standings are unavailable or incomplete.
- Group A after the current Czechia/South Africa result renders as `MEX, KOR, CZE, RSA`.
