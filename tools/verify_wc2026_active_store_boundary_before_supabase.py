#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def require(condition, message, errors):
    if not condition:
        errors.append(message)

def read(path):
    return (ROOT / path).read_text()

def main():
    errors = []
    user_model = read("site/js/model/UserBracketModel.js")
    session = read("site/js/services/ActiveBracketSession.js")
    repo = read("site/js/services/BracketRepository.js")
    mvc_model = read("site/js/mvc/model.js")
    r32_controller = read("site/js/controllers/Game1R32PickController.js")
    docs = "\n".join([
        read("li/world_cup/active_bracket_store_boundary_rule.md"),
        read("docs/architecture/bracketeering_active_store_boundary.md"),
        read("docs/backend/wc2026_supabase_shared_pick_sql_target.md"),
    ])

    for token in ["phaseLocks", "r32LockedAt", "canEditBracketSlot", "canMutateBracketPick", "R32 picks are locked"]:
        require(token in user_model, f"UserBracketModel missing {token}", errors)

    for token in ["ACTIVE_BRACKET_MODES", 'LOCAL: "local"', 'REMOTE: "remote"', "ActiveBracketSession", "createLocalActiveBracketSession", "createRemoteActiveBracketSessionPlaceholder"]:
        require(token in session, f"ActiveBracketSession missing {token}", errors)

    require("createLocalActiveBracketSession" in repo and "activeSession" in repo, "BracketRepository must route through an active local session seam", errors)
    require("SupabaseBracketStore" not in session, "This CB must not implement SupabaseBracketStore in the active session file", errors)
    require("SupabaseBracketStore" not in repo, "This CB must not route repository to SupabaseBracketStore", errors)

    for token in ["activeBracketDocument", "setR32LockedAtForTesting", "canEditSlotInActiveBracket", "activeBracketSlotBlockedReason"]:
        require(token in mvc_model, f"MVC model missing active write-path guard token {token}", errors)

    require("canEditBracketSlot" in r32_controller and "Round of 32 picks are locked and cannot be changed" in r32_controller, "R32 projection controller must use the shared R32 lock guard", errors)

    for token in [
        "Only the active store is authoritative",
        "do not need to match, merge, migrate, reconcile",
        "one `user_brackets` row per player/game",
        "full document in `picks_json`",
        "does not apply Supabase SQL",
        "does not implement `SupabaseBracketStore`",
    ]:
        require(token in docs, f"docs missing storage boundary token: {token}", errors)

    if errors:
        print("WC2026 active store boundary before Supabase verification failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("OK: WC2026 active store boundary keeps local and future Supabase modes separate and blocks post-lock R32 mutation through the active write path.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
