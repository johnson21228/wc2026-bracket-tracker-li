#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def read(path):
    return (ROOT / path).read_text(encoding="utf-8", errors="ignore")

def require(condition, message, errors):
    if not condition:
        errors.append(message)

def main():
    errors = []

    required = [
        "site/js/model/UserBracketModel.js",
        "site/js/services/BracketRepository.js",
        "site/js/services/LocalStorageBracketStore.js",
        "site/js/services/ActiveBracketSession.js",
    ]
    for rel in required:
        require((ROOT / rel).exists(), f"missing required file: {rel}", errors)

    model_text = read("site/js/model/UserBracketModel.js")
    repo_text = read("site/js/services/BracketRepository.js")
    active_session_text = read("site/js/services/ActiveBracketSession.js")

    require("normalizeBracketDocument" in model_text, "canonical BracketDocument normalizer must exist", errors)
    require("picksBySlot" in model_text, "BracketDocument must preserve picksBySlot", errors)
    require("phaseLocks" in model_text, "BracketDocument must preserve phaseLocks", errors)
    require("r32LockedAt" in model_text, "BracketDocument must preserve phaseLocks.r32LockedAt", errors)

    require("BracketRepository" in repo_text, "BracketRepository seam must exist", errors)
    require("LocalStorageBracketStore" in repo_text, "BracketRepository must keep local store available", errors)
    require("new LocalStorageBracketStore()" in repo_text, "BracketRepository must still default to LocalStorageBracketStore", errors)
    require("saveUserBracket" in repo_text, "BracketRepository must expose saveUserBracket seam", errors)
    require("loadUserBracket" in repo_text, "BracketRepository must expose loadUserBracket seam", errors)
    require("this.bracketStore.saveUserBracket(bracket)" in repo_text, "BracketRepository must route saves through bracketStore save seam", errors)

    require("ActiveBracketSession" in active_session_text, "ActiveBracketSession must exist", errors)
    require("saveUserBracket" in active_session_text, "ActiveBracketSession must route saves through the active store seam", errors)

    inactive_store_path = ROOT / "site/js/services/SupabaseBracketStore.js"
    if inactive_store_path.exists():
        inactive_store_text = read("site/js/services/SupabaseBracketStore.js")
        require(
            "class SupabaseBracketStore" in inactive_store_text
            and "loadUserBracket(userId)" in inactive_store_text
            and "saveUserBracket(bracketDocument)" in inactive_store_text,
            "Inactive SupabaseBracketStore may exist only if it implements the bracket store seam.",
            errors,
        )

    # SupabaseBracketStore.js is now the one allowed persistence adapter file.
    # All other site runtime files must not activate direct Supabase/Postgres bracket persistence.
    forbidden_tokens = [
        ".from(\"user_brackets\")",
        ".from('user_brackets')",
        ".from(`user_brackets`)",
        "picks_json",
        ".upsert(",
        ".insert(",
    ]

    for path in (ROOT / "site/js").rglob("*.js"):
        if path.name == "SupabaseBracketStore.js":
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for token in forbidden_tokens:
            require(
                token not in text,
                f"site/js runtime must not activate Supabase/Postgres bracket persistence outside SupabaseBracketStore: {path.relative_to(ROOT)} contains {token}",
                errors,
            )

    runtime_activation_paths = [
        "site/js/app.js",
        "site/js/services/BracketRepository.js",
        "site/js/mvc/view.js",
        "site/js/mvc/controller.js",
        "site/js/controllers/Game1R32PickController.js",
    ]
    for rel in runtime_activation_paths:
        text = read(rel)
        require(
            "SupabaseBracketStore" not in text,
            f"{rel} must not activate SupabaseBracketStore yet",
            errors,
        )

    if errors:
        for error in errors:
            print(error)
        raise SystemExit(1)

    print("OK: WC2026 BracketDocument save seam is in place before active Supabase persistence; inactive SupabaseBracketStore is isolated.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
