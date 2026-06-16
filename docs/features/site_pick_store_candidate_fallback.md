# Site Pick Store Candidate Fallback

The site bracket pick store is the preferred location for every Game 1 bracket pick, but it must remain compatible with existing R32 picks.

R16 menu choices are source candidates. They should be read from the upstream R32 cells, not from the target R16 cell.

Resolution order:

1. unified site pick store
2. current runtime R32 `picks`
3. legacy `wc2026.game1.r32.picks`
4. manifest aliases such as `R32-L-M1A`

This preserves the rule: the bracket cell is the storage key, while candidate resolution still follows upstream slot relationships.
