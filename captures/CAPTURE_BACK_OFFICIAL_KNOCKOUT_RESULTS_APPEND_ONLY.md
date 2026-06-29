# Capture Back: Official knockout results append-only rule

## Intent

Official knockout results are historical truth. Adding a new result must never erase or rewrite prior result rows.

## Protected invariant

`site/data/official_knockout_results.json` is append/upsert-by-`resultId`.

When adding a result:

- Load the existing JSON.
- Preserve every existing `matches[]` row.
- Replace only the row with the same `resultId`, if it already exists.
- Append the new row if it does not exist.
- Never rebuild `matches[]` from only the latest result.

## Protected existing result

Canada’s Round of 32 result must remain present:

- `resultId`: `r32-rsa-can-2026-06-28`
- South Africa 0, Canada 1
- winner: Canada
- winner slot: `L-R16-03`

## Current added result

Brazil’s Round of 32 result is added without deleting Canada:

- `resultId`: `r32-bra-jpn-2026-06-29`
- Brazil 2, Japan 1
- winner: Brazil
- winner slot: `R-R16-01`
