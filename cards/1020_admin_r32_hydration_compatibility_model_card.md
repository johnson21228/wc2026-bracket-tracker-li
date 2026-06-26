# Card 1020: Admin R32 hydration compatibility model

## Intent

Align LI and feature docs with the current knockout-only game model.

## Rule

Admin_/official owns R32 occupant truth. Player BracketDocuments may store R32 entries only as Supabase Admin_/official hydrated mirror entries with `playerAuthored: false`. Normal players own R32 match-winner and later picks.

## Verification

Run:

```bash
python3 tools/verify_wc2026_admin_r32_hydration_compatibility_model_li.py
```
