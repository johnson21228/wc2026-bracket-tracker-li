#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def read(rel):
    path = ROOT / rel
    if not path.exists():
        raise AssertionError(f"Missing required file: {rel}")
    return path.read_text(encoding="utf-8", errors="ignore")

def require(condition, message, errors):
    if not condition:
        errors.append(message)

def main():
    errors = []

    standings_store = read("site/js/standings/SupabasePlayerStandingsStore.js")
    supabase_store = read("site/js/services/SupabaseBracketStore.js")
    model = read("site/js/mvc/model.js")
    view = read("site/js/mvc/view.js")
    css = read("site/css/app.css")
    app = read("site/js/app.js")
    makefile = read("Makefile")

    docs = "\n".join(read(rel) for rel in [
        "cards/286_official_truth_bracket_as_hidden_player_card.md",
        "docs/features/official_truth_bracket_as_hidden_player.md",
        "captures/CAPTURE_BACK_OFFICIAL_TRUTH_BRACKET_AS_HIDDEN_PLAYER.md",
        "li/world_cup/official_truth_bracket_as_hidden_player_rule.md",
    ])

    require('.eq("bracket_kind", "player")' in standings_store, "Standings store must read only player brackets.", errors)
    require("bracket_kind" in standings_store, "Standings store must select bracket_kind.", errors)
    require("loadOfficialBracket" in supabase_store, "Supabase bracket store must expose official bracket loader.", errors)
    require('.eq("bracket_kind", "official")' in supabase_store, "Official loader must query bracket_kind official.", errors)
    require("bracket_kind:" in supabase_store, "Supabase saves must preserve bracket_kind.", errors)
    require("officialPicks" in model and "officialPickComparisonForSlot" in model, "Model must compute official truth comparisons.", errors)
    require("editingOfficialResults" in model and "bracketKind" in model, "Model summary must expose official editing state.", errors)
    require("data-official-results-banner" in view and "Editing Official Results" in view, "View must render official editing banner.", errors)
    require("has-official-correct-pick" in view and "has-official-incorrect-pick" in view, "View must render official correct/incorrect hooks.", errors)
    require("picked-cell-official-truth" in view, "View must render official truth beside incorrect user pick.", errors)
    require("officialBracketStore" in app or "officialBracketStore" in model, "App/model must expose official bracket store seam.", errors)
    require(".official-results-banner" in css, "CSS must style official editing banner.", errors)
    require(".has-official-correct-pick" in css and ".has-official-incorrect-pick" in css, "CSS must style official comparison states.", errors)

    for token in [
        "bracket_kind = official",
        "bracket_kind = player",
        "Editing Official Results",
        "compared against user picks only where official picks exist",
    ]:
        require(token in docs, f"Docs/capture/card/rule missing protected token: {token}", errors)

    if "python3 tools/verify_wc2026_official_truth_bracket_hidden_player.py" not in makefile:
        errors.append("Makefile verify must run official truth hidden player verifier.")

    if errors:
        print("Official truth hidden player verification failed: " + "; ".join(errors))
        return 1

    print("OK: Official truth bracket is hidden from player standings, loaded separately, and rendered as comparison truth.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
