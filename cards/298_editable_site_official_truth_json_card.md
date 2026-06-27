# Card 298: Editable Site Official Truth JSON

## Intent

Capture the data workflow for site-owned official truth.

## Decision

Use `site/data/current/official_truth.json` as the editable, versioned source of official R32 occupants and official knockout results.

The JSON preserves the same effective `picksBySlot` contract previously supplied by the Supabase Admin_/official row.

## Acceptance

- Official truth lives in site data.
- The data file can be partial.
- R32 occupants are read from site data.
- R16/R8/R4/R2/Champion result truth is read from site data.
- Supabase stores player picks only.
- Standings are computed, not stored.
- Runtime migration changes official truth source, not the scoring contract.
