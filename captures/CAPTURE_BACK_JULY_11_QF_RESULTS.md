# Capture Back: July 11 quarterfinal results

## Intent

Record the final two World Cup quarterfinal results in append-only
Bracketeering truth and resolve the right-side semifinal.

## Official results

- Norway 1–2 England after extra time.
- England advances from `R-QF-01` / `R-QF-02` into `R-SF-01`.
- Argentina 3–1 Switzerland after extra time.
- Argentina advances from `R-QF-03` / `R-QF-04` into `R-SF-02`.
- The right-side semifinal resolves as England vs Argentina.

## Match identity

- Norway vs England: FIFA match `53452529`.
- Argentina vs Switzerland: FIFA match `53452531`.

## Files changed

- `site/data/official_knockout_results.json`
- `tools/verify_wc2026_official_knockout_results_append_only.py`
- `captures/CAPTURE_BACK_JULY_11_QF_RESULTS.md`

## Guardrails

- Preserve every existing knockout-result row.
- Upsert only `qf-nor-eng-2026-07-11` and
  `qf-arg-sui-2026-07-11`.
- Keep `site/data/current/official_truth.json` R32-only.
- Do not add highlight URLs in this slice.
