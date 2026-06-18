# Picked Bracket Cell Identity Rendering Rule

A picked bracket cell is a compact identity token, not an explanatory menu item.

When a team has been picked into a bracket slot, the visible cell must render only:

- the team flag visual
- the canonical three-letter display code

The picked cell must not visibly render the full team name, group/place prose, source labels, or slot explanation text.

The flag visual is the dominant visual identifier. It should scale to the available cell height and use as much vertical space as the cell shape allows while preserving recognizability.

The current runtime may use emoji flags as the flag visual. Emoji flags are scaled with font size because they are text glyphs. This rule must also allow later image/SVG flag assets without changing the picked-cell semantic contract.

The three-letter code must come from the selected team model. The renderer must not invent country-code normalizations locally.

Menus, group panels, tooltips, aria labels, and detail surfaces may still show full team names and explanatory source context.
