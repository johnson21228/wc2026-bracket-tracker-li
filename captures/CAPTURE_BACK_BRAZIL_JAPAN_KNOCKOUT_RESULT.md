# Capture Back: Brazil 2–1 Japan knockout result

## Intent

Record Brazil 2–1 Japan as official knockout result truth for Bracketeering.

## Site truth

- R32 site pair: `R-R32-01` Brazil vs `R-R32-02` Japan.
- Official result: Brazil 2, Japan 1.
- Official winner: Brazil.
- Brazil advances into `R-R16-01`.

## Related migration

Canada’s earlier South Africa 0–1 Canada knockout winner is also migrated out of `site/data/current/official_truth.json` and into `site/data/official_knockout_results.json`.

## Runtime boundary

`site/data/current/official_truth.json` remains the R32 seed only.

`site/data/official_knockout_results.json` stores official knockout result rows. Runtime and standings derive later-round official truth from those result rows so `L-R16-03` resolves to Canada and `R-R16-01` resolves to Brazil without polluting the R32 seed file.
