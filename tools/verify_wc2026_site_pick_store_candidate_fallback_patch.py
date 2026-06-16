from pathlib import Path

html = Path("site/game1/index.html").read_text(encoding="utf-8")
required = [
    "WC2026_SITE_PICK_STORE_CANDIDATE_FALLBACK_START",
    "api.migrateLegacy()",
    "wc2026R32AliasIdsForCanonicalSlot",
    "R32-${side}-M${matchNo}${half}",
    "wc2026PickForAnySlotAlias",
    "wc2026CandidateForSourceSlot",
    "wc2026.game1.r32.picks",
]
missing = [item for item in required if item not in html]
if missing:
    raise SystemExit("Missing site pick store candidate fallback markers: " + ", ".join(missing))
print("Site pick store candidate fallback verification passed.")
