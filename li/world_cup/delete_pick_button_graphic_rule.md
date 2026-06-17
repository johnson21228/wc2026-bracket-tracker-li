# Delete Pick Button Graphic Rule

The World Cup bracket pick menu must not expose prototype wording such as "UnPick" to reviewers. Removal affordances should be displayed as a delete graphic while preserving the underlying pick-removal behavior.

Invariant:

- Presentation may change from "UnPick" to a delete graphic.
- Pick deletion semantics must not change.
- The control must remain accessible with a clear delete label.
- Dynamic menu rendering must be normalized after insertion.
