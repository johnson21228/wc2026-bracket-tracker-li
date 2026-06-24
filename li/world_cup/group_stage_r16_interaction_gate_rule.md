# LI Rule: Group Stage R16+ Interaction Gate

Group Stage R16+ suppression is both visual and interactive.

If the lifecycle presentation state is Group Stage, any non-R32 pick slot must be frame-only and must not be exposed as a pick-menu target.

Required behavior:
- no R16+ pickable cursor during Group Stage
- no R16+ pick menu during Group Stage
- controller backstop blocks R16+ slot menu invocation during Group Stage
- R32 interaction is unchanged
- Knockout Stage restores R16+ interaction
- model/persistence data remains untouched
