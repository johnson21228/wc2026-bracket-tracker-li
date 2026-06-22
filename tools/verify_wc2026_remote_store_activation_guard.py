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

    guard_path = ROOT / "site/js/services/RemoteStoreActivationGuard.js"
    require(guard_path.exists(), "RemoteStoreActivationGuard.js must exist", errors)
    guard = read("site/js/services/RemoteStoreActivationGuard.js") if guard_path.exists() else ""

    for token in [
        "REMOTE_STORE_DISABLED_REASON",
        "DEFAULT_REMOTE_STORE_ACTIVATION",
        "remoteStoreEnabled: false",
        "function createRemoteStoreActivationGuard",
        "DEFAULT_REMOTE_STORE_ACTIVATION_GUARD",
        "assertRemoteStoreEnabled()",
        "throw new Error(activation.reason)",
        "createRemoteStoreActivationGuard",
    ]:
        require(token in guard, f"RemoteStoreActivationGuard missing token: {token}", errors)

    for token in [
        "SupabaseBracketStore",
        "createSupabaseBracketStore",
        "createClient",
        ".from(",
        ".upsert(",
        "picks_json",
        "user_brackets",
    ]:
        require(token not in guard, f"RemoteStoreActivationGuard must not activate persistence token: {token}", errors)

    runtime_paths = [
        "site/js/app.js",
        "site/js/services/BracketRepository.js",
        "site/js/mvc/view.js",
        "site/js/mvc/controller.js",
        "site/js/controllers/Game1R32PickController.js",
    ]
    for rel in runtime_paths:
        text = read(rel)
        require("RemoteStoreActivationGuard" not in text, f"{rel} must not import the remote store guard yet", errors)
        require("SupabaseBracketStore" not in text, f"{rel} must not activate SupabaseBracketStore yet", errors)

    repo_text = read("site/js/services/BracketRepository.js")
    require("new LocalStorageBracketStore()" in repo_text, "BracketRepository must still default to LocalStorageBracketStore", errors)

    combined_docs = "\n".join([
        read("li/world_cup/remote_store_activation_guard_rule.md"),
        read("docs/architecture/bracketeering_remote_store_activation_guard.md"),
        read("captures/CAPTURE_BACK_REMOTE_STORE_ACTIVATION_GUARD_WITHOUT_ENABLING_REMOTE_MODE.md"),
        read("cards/271_add_remote_store_activation_guard_without_enabling_remote_mode_card.md"),
    ])

    for phrase in [
        "remoteStoreEnabled: false",
        "does not enable remote mode",
        "public runtime remains local/browser-store active",
        "View and Controller do not call Supabase",
        "no SQL is applied",
        "no merge to main",
    ]:
        require(phrase in combined_docs, f"remote store activation guard docs missing phrase: {phrase}", errors)

    makefile = read("Makefile")
    require(
        "python3 tools/verify_wc2026_remote_store_activation_guard.py" in makefile,
        "remote store activation guard verifier must be included in make verify",
        errors,
    )

    if errors:
        print("WC2026 remote store activation guard verification failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("OK: WC2026 remote store activation guard is fail-closed and remote mode remains inactive.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
