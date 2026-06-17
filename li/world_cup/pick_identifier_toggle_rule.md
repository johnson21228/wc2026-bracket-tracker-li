# Pick identifier toggle rule

The pick identifier layer must be developer-toggleable.

Requirements:

- The board plane owns `data-show-pick-identifiers`.
- DeveloperFrame exposes a `Show pick identifiers` control.
- The control must not mutate player pick state.
- Copyable developer properties should include `showPickIdentifiers`.
