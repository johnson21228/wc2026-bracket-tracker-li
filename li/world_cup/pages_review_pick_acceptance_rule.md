# Pages Review Pick Acceptance Rule

A public review URL is not valid unless picks can be accepted, rendered, and preserved by the browser.

For review builds:

- a selection gesture must write to the canonical bracket pick store;
- legacy pick stores may be mirrored for compatibility;
- render must be invoked after storage mutation;
- finality validation must not block the act of making a pick;
- invalid or non-final picks may be visually adorned after they are accepted.
