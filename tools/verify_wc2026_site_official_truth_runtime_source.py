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

model = read("site/js/mvc/model.js")
standings = read("site/js/standings/SupabasePlayerStandingsStore.js")
user_model = read("site/js/model/UserBracketModel.js")
makefile = read("Makefile")

required_model = [
    'officialTruth: "data/current/official_truth.json"',
    "readJson(DATA_URLS.officialTruth)",
    "function normalizeSiteOfficialTruthDocument(payload = {})",
    'officialR32AuthoritySource: "site/data/current/official_truth.json"',
    'officialResultsTruthSource: "site/data/current/official_truth.json"',
    'source: "site-owned-official-truth"',
    'authority: "site-owned-official-truth"',
    '[WC2026 OfficialResults] loaded site-owned official truth picks',
]

for token in required_model:
    if token not in model:
        errors.append(f"model missing site official truth runtime token: {token}")

for forbidden in [
    "const loadOfficialR32BracketAuthority =",
    "await loadOfficialR32BracketAuthority.call",
    "missing-admin-official-row",
    "Supabase-connected admin editor remains open to create it",
]:
    if forbidden in model:
        errors.append(f"model still contains obsolete Supabase Admin official load path: {forbidden}")

required_standings = [
    'const SITE_OFFICIAL_TRUTH_URL = "data/current/official_truth.json"',
    'const SITE_OFFICIAL_TRUTH_SOURCE = "site/data/current/official_truth.json"',
    "async function loadSiteOfficialTruth()",
    "const officialTruth = await loadSiteOfficialTruth();",
    '.eq("bracket_kind", "player")',
    "function scoreAgainstOfficialTruth",
]

for token in required_standings:
    if token not in standings:
        errors.append(f"standings store missing site official truth token: {token}")

for forbidden in [
    "ADMIN_OFFICIAL_USER_ID",
    "ADMIN_OFFICIAL_TRUTH_SOURCE",
    "function isAdminOfficialTruthRow",
    "function normalizeAdminOfficialTruth",
    '.in("bracket_kind", ["player", "official"])',
    "scoreAgainstAdminOfficialTruth",
]:
    if forbidden in standings:
        errors.append(f"standings store still contains obsolete Admin official row path: {forbidden}")

required_user_model = [
    'officialR32?.source === "site-owned-official-truth"',
    'return source === "site/data/current/official_truth.json" || source === "Supabase:Admin_/official";',
    'source: "site-owned-official-truth"',
    'authority: "site-owned-official-truth"',
]

for token in required_user_model:
    if token not in user_model:
        errors.append(f"UserBracketModel missing site official truth hydration token: {token}")

if "python3 tools/verify_wc2026_site_official_truth_runtime_source.py" not in makefile:
    errors.append("Makefile verify must include site official truth runtime source verifier")

if errors:
    print("WC2026 site official truth runtime source verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: runtime loads official truth from site JSON while player picks remain Supabase-backed.")
