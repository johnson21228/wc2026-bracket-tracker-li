# Capture Back: Safe Group Result for Czechia South Africa

## Change
Patched the confirmed Czechia 1-1 South Africa final result.

## Safety boundary
Only confirmed finals are patched. Switzerland vs Bosnia and Herzegovina was treated as WATCH and left unmodified because it was live/in-progress at decision time.

## Verification
Added `tools/verify_wc2026_safe_group_result_cze_rsa.py` and wired it into `make verify`.
