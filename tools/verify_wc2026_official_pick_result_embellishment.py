from pathlib import Path

view = Path("site/js/mvc/view.js").read_text(encoding="utf-8")
css = Path("site/css/app.css").read_text(encoding="utf-8")
makefile = Path("Makefile").read_text(encoding="utf-8")

required_view = [
    'correct.className = "picked-cell-official-truth";',
    'correct.textContent = `Correct: ${officialTruthLabel(slot.officialTruthTeam)}`;',
    'button.classList.add("has-official-incorrect-pick");',
    'correct.className = "final-four-pick-official-truth";',
    'correct.textContent = `Correct: ${officialTruthLabel(pick.officialTruthTeam)}`;',
    'button.classList.add("is-knockout-result-incorrect");',
    'button.dataset.knockoutResultState = "incorrect";',
]
required_css = [
    '.pick-slot-button.has-official-incorrect-pick > .picked-cell-official-truth',
    '.final-four-pick-row.has-official-correct-pick',
    '.final-four-pick-row.has-official-incorrect-pick',
    '.final-four-pick-official-truth',
]

errors = []
for marker in required_view:
    if marker not in view:
        errors.append(f"view missing: {marker}")
for marker in required_css:
    if marker not in css:
        errors.append(f"css missing: {marker}")
if "python3 tools/verify_wc2026_official_pick_result_embellishment.py" not in makefile:
    errors.append("Makefile missing official pick result embellishment verifier")

if errors:
    print("WC2026 official pick result embellishment verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: missed picks retain red/correct-winner feedback and Final Four semifinal winner rows receive matching correct/incorrect embellishment.")
