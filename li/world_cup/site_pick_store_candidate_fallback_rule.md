# Site Pick Store Candidate Fallback Rule

The unified site bracket pick store must not make existing bracket picks invisible.

For candidate resolution, a knockout slot reads from its upstream source slot IDs. Each source slot may be resolved through:

- unified bracket pick store
- current runtime pick state
- legacy localStorage buckets
- known manifest aliases

The store is preferred, but legacy and alias fallbacks are required during migration.
