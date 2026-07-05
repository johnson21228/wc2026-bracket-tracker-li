#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors = []
model = Path("site/js/mvc/model.js").read_text()

def read(rel):
    path = ROOT / rel
    if not path.exists():
        errors.append(f"missing file: {rel}")
        return ""
    return path.read_text(encoding="utf-8")

standings = read("site/js/standings/SupabasePlayerStandingsStore.js")
site_rule = read("li/world_cup/site_owned_official_truth_rule.md")
editable_rule = read("li/world_cup/editable_site_official_truth_json_rule.md")
runtime_verifier = read("tools/verify_wc2026_site_official_truth_runtime_source.py")

required = [
    'const SITE_OFFICIAL_TRUTH_URL = "data/current/official_truth.json"',
    'const SITE_OFFICIAL_TRUTH_SOURCE = "site/data/current/official_truth.json"',
    "async function loadSiteOfficialTruth()",
    "const officialTruth = await loadSiteOfficialTruth();",
    '.eq("bracket_kind", "player")',
    "function scoreAgainstOfficialTruth",
    "score: score.score",
    "maxPossible: score.maxPossible",
]

for token in required:
    if token not in standings:
        errors.append(f"standings store missing site-owned official truth token: {token}")

for forbidden in [
    "ADMIN_OFFICIAL_USER_ID",
    "ADMIN_OFFICIAL_TRUTH_SOURCE",
    "function isAdminOfficialTruthRow",
    "function normalizeAdminOfficialTruth",
    '.in("bracket_kind", ["player", "official"])',
    "scoreAgainstAdminOfficialTruth",
]:
    if forbidden in standings:
        errors.append(f"standings store still requires obsolete Supabase Admin_/official truth: {forbidden}")

for token in [
    "Player standings are not stored as standings",
    "Supabase must not be the source of official R32 occupants or official tournament results",
]:
    if token not in site_rule:
        errors.append(f"site-owned official truth rule missing token: {token}")

for token in [
    "site/data/current/official_truth.json",
    "same effective payload contract previously supplied by the Supabase `Admin_/official` official row",
    "Player standings are computed, not stored",
]:
    if token not in editable_rule:
        errors.append(f"editable official truth rule missing token: {token}")

if "runtime loads official truth from site JSON while player picks remain Supabase-backed" not in runtime_verifier:
    errors.append("runtime verifier must protect site JSON official truth with Supabase-backed player picks")


for token in [
    "const officialKnockoutResult = officialKnockoutResultsByWinnerSlotId.get(normalizedSlotId) || null;",
    "if (officialKnockoutResult?.winnerTeamId) {",
    "return officialTeam(slotId) || persistedPlayerTeam(slotId);",
]:
    if token not in model:
        errors.append(f"site/js/mvc/model.js missing official result slot precedence token: {token}")

if errors:
    print("Site-owned official results truth verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: site-owned official truth is the source for standings, scoring comparison, and R32/results truth.")
