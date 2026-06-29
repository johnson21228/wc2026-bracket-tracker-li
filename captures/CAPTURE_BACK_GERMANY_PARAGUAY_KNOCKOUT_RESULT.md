# Capture Back: Germany-Paraguay Knockout Result

Germany-Paraguay is recorded as an append-only knockout result.

## Result

Germany 1–1 Paraguay after extra time.

Paraguay advances 4–3 on penalties.

## Runtime effect

- `winnerTeamId`: `PAR`
- `siteWinnerSlotId`: `L-R16-01`
- `siteSlotPair`: `L-R32-01`, `L-R32-02`

## Guardrails

- Result is stored in `site/data/official_knockout_results.json`.
- `site/data/current/official_truth.json` remains R32 seed-only.
- Existing protected results remain present:
  - CAN/RSA
  - BRA/JPN
  - GER/PAR
