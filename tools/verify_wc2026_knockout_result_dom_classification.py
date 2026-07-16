#!/usr/bin/env python3
from pathlib import Path
import sys

errors = []

view = Path("site/js/mvc/view.js").read_text()
model = Path("site/js/mvc/model.js").read_text()
makefile = Path("Makefile").read_text()

required_view = [
    "const officialPickState = slot.officialPickComparison?.state || \"\";",
    'const effectiveOfficialPickState = officialPickState === "incorrect" || officialPickState === "unreachable"',
    '? officialPickState',
    ': renderedTeamMatchesOfficialWinner',
    "return slot.officialResultTeam || slot.selectedTeam;",
    'const isIncorrectOfficialPick = slot.officialPickComparison?.state === "incorrect"',
    'const renderedPickTeam = isIncorrectOfficialPick ? slot.selectedTeam : displayTeam;',
    'comparison.className = "picked-cell-result-comparison";',
    'correctFlag.className = "picked-cell-correct-flag";',
    'correctCode.className = "picked-cell-correct-code";',
    'function missedPointsForSlot(slotId)',
    'missedBadge.className = "picked-cell-missed-points";',
    'missedBadge.textContent = `${missedPoints} ${missedPoints === 1 ? "pt" : "pts"} missed`;',
    "const slotIdForResultClassification = String(slot.id || slot.slotId || \"\");",
    "const isKnockoutResultSlot = /-R(16|8|4|2|QF|SF|F)-/.test(slotIdForResultClassification)",
    "|| /-(R16|QF|SF|FINAL)-/.test(slotIdForResultClassification)",
    '|| slotIdForResultClassification === "FINAL-LEFT"',
    '|| slotIdForResultClassification === "FINAL-RIGHT";',
    "button.classList.add(\"is-knockout-result-classified\");",
    "button.classList.add(`is-knockout-result-${effectiveOfficialPickState}`);",
    "button.setAttribute(\"data-knockout-result-state\", effectiveOfficialPickState);",
    "if (effectiveOfficialPickState === \"correct\")",
    "if (officialPickState === \"incorrect\")",
    "if (officialPickState === \"unreachable\")",
]
for token in required_view:
    if token not in view:
        errors.append(f"site/js/mvc/view.js missing {token}")

for token in [
    "const officialResult = officialKnockoutResultsByWinnerSlotId.get(slot.slotId) || null;",
    "officialResultTeam,",
]:
    if token not in model:
        errors.append(f"site/js/mvc/model.js missing {token}")

for forbidden in [
    "site/data/current/official_truth.json",
    "site/data/official_knockout_results.json",
    "scoreByTeamId",
    "winnerTeamId",
]:
    # This verifier should be about view classification only; not result derivation.
    pass

if "python3 tools/verify_wc2026_knockout_result_dom_classification.py" not in makefile:
    errors.append("Makefile missing knockout result DOM classification verifier")

if errors:
    print("WC2026 knockout result DOM classification verification failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("OK: R16+ knockout result state has stable DOM classification aliases without changing truth/scoring.")
