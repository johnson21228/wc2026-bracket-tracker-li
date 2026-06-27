#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors = []

def read(rel):
    path = ROOT / rel
    if not path.exists():
        errors.append(f"missing file: {rel}")
        return ""
    return path.read_text(encoding="utf-8")

user_model = read("site/js/model/UserBracketModel.js")
mvc_model = read("site/js/mvc/model.js")
truth_json = read("site/data/current/official_truth.json")
runtime_verifier = read("tools/verify_wc2026_site_official_truth_runtime_source.py")

required = [
    'source: "site-owned-official-truth"',
    'authority: "site-owned-official-truth"',
    'hydratedFrom: occupant.hydratedFrom || "site/data/current/official_truth.json"',
    'source === "site/data/current/official_truth.json"',
]

for token in required:
    if token not in user_model:
        errors.append(f"UserBracketModel missing site-owned R32 hydration token: {token}")

for token in [
    'officialTruth: "data/current/official_truth.json"',
    "normalizeSiteOfficialTruthDocument",
    'officialR32AuthoritySource: "site/data/current/official_truth.json"',
]:
    if token not in mvc_model:
        errors.append(f"mvc model missing site-owned official truth token: {token}")

if '"picksBySlot"' not in truth_json:
    errors.append("official_truth.json must expose picksBySlot for R32 hydration")

if "runtime loads official truth from site JSON while player picks remain Supabase-backed" not in runtime_verifier:
    errors.append("site official truth runtime verifier must protect replacement source")

for forbidden in [
    'source: "Admin_/official"',
    'authority: "Admin_/official"',
    'hydratedFrom: "Supabase:Admin_/official"',
]:
    if forbidden in user_model:
        errors.append(f"UserBracketModel still contains obsolete Admin hydration token: {forbidden}")

if errors:
    print("WC2026 site-owned official R32 hydration runtime verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: official R32 hydration runtime uses site-owned official truth JSON and preserves player-owned later picks.")
