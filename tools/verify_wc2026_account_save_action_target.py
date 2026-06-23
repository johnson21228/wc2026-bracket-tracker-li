#!/usr/bin/env python3
from pathlib import Path


def require(condition, message, errors):
    if not condition:
        errors.append(message)


def main():
    errors = []

    source = Path("site/js/identity/AccountSaveActionSurface.js").read_text()
    makefile = Path("Makefile").read_text()

    require("AUTOSAVE_DELAY_MS" in source,
            "Joined live picks must use debounced autosave.", errors)
    require("wc2026:picks-changed" in source,
            "Joined live picks must listen for pick changes.", errors)
    require("saveUserBracket" in source,
            "Joined live picks must save through BracketStore seam.", errors)
    require("loadUserBracket" in source,
            "Joined live picks must detect existing saved picks.", errors)

    require("You already have picks saved. Use saved picks or keep this board?" in source,
            "Existing joined picks conflict must be handled once.", errors)
    require("Use saved picks" in source and "Keep this board" in source,
            "Conflict UI must offer saved picks vs current board.", errors)

    require("Saving…" in source,
            "Autosave may show active saving state.", errors)
    require("Could not save — retrying" in source,
            "Autosave failure must remain visible and retry-oriented.", errors)
    require("Picks saved" not in source,
            "Successful autosave must be quiet; do not persistently show Picks saved.", errors)

    for forbidden in [
        "Save Picks",
        "Load Saved",
        "Storage mode",
        "Remote store",
        "Manual save",
    ]:
        require(forbidden not in source,
                f"Joined live-picks UI must not expose manual persistence copy: {forbidden}", errors)

    require("python3 tools/verify_wc2026_account_save_action_target.py" in makefile,
            "Makefile verify must include account save action verifier.", errors)

    if errors:
        print("Join-first live autosave verification failed: " + "; ".join(errors))
        return 1

    print("OK: joined player persistence uses quiet-success live autosave with visible saving/error states and no Save/Load commands.")


if __name__ == "__main__":
    raise SystemExit(main())
