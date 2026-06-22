<!-- WC2026_SINGLE_GEOMETRY_TRUTH_START -->
## Final Four Geometry Direction

The existing single tall `FINAL_FOUR` center card is legacy/current geometry behavior, not permanent geometry truth.

Future Final Four center geometry should be modeled from the source-truth geometry as explicit center-stack cells:

- upper semifinal-winner cell
- shorter final-winner / champion cell
- lower semifinal-winner cell
- third-place winner cell when required by the bracket model

These cells must originate in the source-truth SVG/source geometry and then appear in the generated/runtime JSON manifest projection.

Do not patch only the JSON manifest for this change unless the LI explicitly marks that patch as temporary and requires follow-up regeneration from the SVG/source geometry.
<!-- WC2026_SINGLE_GEOMETRY_TRUTH_END -->
