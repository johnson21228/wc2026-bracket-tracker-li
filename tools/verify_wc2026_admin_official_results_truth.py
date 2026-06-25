#!/usr/bin/env python3
"""Verify Admin_/official is the result-truth source for standings/scoring/viewer."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors = []

def require(condition, message):
    if not condition:
        errors.append(message)

def read(rel):
    path = ROOT / rel
    if not path.exists():
        errors.append(f"missing file: {rel}")
        return ""
    return path.read_text(encoding="utf-8")

store = read("site/js/standings/SupabasePlayerStandingsStore.js")
surface = read("site/js/standings/PlayerStandingsSurface.js")
model = read("site/js/mvc/model.js")
repo = read("site/js/services/BracketRepository.js")
css = read("site/css/app.css")
card = read("cards/1014_admin_official_results_truth_card.md")
capture = read("captures/CAPTURE_BACK_ADMIN_OFFICIAL_RESULTS_TRUTH.md")
doc = read("docs/features/admin_official_results_truth.md")
makefile = read("Makefile")

require('const ADMIN_OFFICIAL_USER_ID = "Admin_/official"' in store, "standings store must name Admin_/official")
require('const ADMIN_OFFICIAL_TRUTH_SOURCE = "Supabase:Admin_/official"' in store, "standings store must name Supabase Admin truth source")
require('function isAdminOfficialTruthRow' in store, "standings store must identify the official truth row")
require('function normalizeAdminOfficialTruth' in store, "standings store must normalize official truth separately")
require('.in("bracket_kind", ["player", "official"])' in store, "standings query must read player and official rows")
require('const officialTruth = normalizeAdminOfficialTruth(allRows.find(isAdminOfficialTruthRow) || null)' in store, "standings store must separate official truth before player normalization")
require('const bracketRows = allRows.filter((row) => !isAdminOfficialTruthRow(row))' in store, "official row must be excluded from player standings rows")
require('scoreAgainstAdminOfficialTruth' in store, "standings store must score against Admin official truth")
require('isR32EntrantRecord' in store and 'if (isR32EntrantRecord(slotId, officialRecord)) continue' in store, "scoring must skip official R32 entrants and score result winners")
require('officialTruthPicksBySlot' in store and 'officialResultsTruthSource' in store, "player rows must carry official truth comparison metadata")
require('groupPoints: 0' in store, "group-stage player scoring must remain zero/no group-stage picks")

for forbidden in ['officialTruth = bracketRows', 'officialTruth = playerRows', 'normalizeBracketRow(row, profileByUserId)' ]:
    require(forbidden not in store, f"store must not derive official truth from player rows: {forbidden}")

require('officialTruthPicksBySlot' in surface, "read-only board viewer must receive official truth picks separately")
require('officialResultsTruthSource' in surface, "read-only board viewer must keep official truth source metadata")
require('data-official-result-state' in surface, "read-only board viewer must expose official comparison state")
require('Official result from' in surface, "read-only board viewer must label official comparison source")
require('player-board-viewer-official-truth' in surface, "read-only board viewer must render official truth feedback")
require('has-official-correct-pick' in css and 'has-official-incorrect-pick' in css, "CSS must style official comparison states")

require('officialResultsTruthSource: "Supabase:Admin_/official"' in model, "runtime model must tag Admin official result truth source")
require('officialResultsTruthPickCount' in model, "runtime model summary must expose official result truth pick count")
require('officialPicks = legacyPicksFromRemoteBracketDocument(officialBracketDocument)' in model, "runtime model must load result truth from Admin official bracket document")
require('officialPickComparisonForSlot' in model and 'officialTeam(slotId)' in model, "runtime model must compare player picks to official truth")

require('if (officialBracket)' in repo, "repository must treat partial Admin official source as authoritative")
require('officialResultsTruthSource: "Supabase:Admin_/official"' in repo, "repository official source must carry result truth metadata")
require('return staticOfficialR32Fallback(modelBundle)' in repo, "static fallback must remain only after Admin official source is unavailable/missing")

for rel_text, label in [(card, "card"), (capture, "capture"), (doc, "doc")]:
    require('Admin_/official' in rel_text, f"{label} must document Admin official source")
    require('Partial official truth' in rel_text or 'partial official truth' in rel_text or 'Partial truth' in rel_text, f"{label} must document partial official truth")
    require('player' in rel_text.lower(), f"{label} must distinguish player picks from official truth")

require('python3 tools/verify_wc2026_admin_official_results_truth.py' in makefile, "Makefile verify must include admin official results truth verifier")

if errors:
    raise SystemExit("Admin_/official results truth verification failed: " + "; ".join(errors))

print("OK: Admin_/official is the source of results truth for standings, scoring comparison, and read-only viewer context.")
