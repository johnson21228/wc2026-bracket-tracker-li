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

    site_js_files = sorted((ROOT / "site/js").rglob("*.js"))
    combined_site_js = "\n".join(
        p.read_text(encoding="utf-8", errors="ignore")
        for p in site_js_files
    )

    bracket_repo_path = ROOT / "site/js/services/BracketRepository.js"
    local_store_path = ROOT / "site/js/services/LocalStorageBracketStore.js"

    require(bracket_repo_path.exists(), "BracketRepository seam file must remain present.", errors)
    require(local_store_path.exists(), "LocalStorageBracketStore must remain present before remote bracket persistence.", errors)

    if bracket_repo_path.exists():
        bracket_repo = bracket_repo_path.read_text(encoding="utf-8", errors="ignore")
        require(
            "create" in bracket_repo.lower() or "repository" in bracket_repo.lower() or "save" in bracket_repo.lower(),
            "BracketRepository should remain an active save/repository seam.",
            errors,
        )

    if local_store_path.exists():
        local_store = local_store_path.read_text(encoding="utf-8", errors="ignore")
        require(
            "localStorage" in local_store or "localstorage" in local_store.lower(),
            "LocalStorageBracketStore should remain the active local bracket persistence path.",
            errors,
        )

    # Public profile persistence is allowed after Supabase profile SQL application.
    profile_store_path = ROOT / "site/js/services/SupabaseProfileStore.js"
    if profile_store_path.exists():
        profile_store = profile_store_path.read_text(encoding="utf-8", errors="ignore")
        require('.from("profiles")' in profile_store, "SupabaseProfileStore should own public profile persistence.", errors)
        require(".upsert(" in profile_store, "SupabaseProfileStore should upsert public player names.", errors)
        require("display_name" in profile_store, "SupabaseProfileStore should persist display_name.", errors)

    # Remote bracket persistence is still intentionally blocked until SupabaseBracketStore.
    forbidden_bracket_tokens = [
        '.from("user_brackets")',
        ".from('user_brackets')",
        ".from(`user_brackets`)",
        "SupabaseBracketStore",
        "bracket_json",
        "picks_json",
    ]
    for token in forbidden_bracket_tokens:
        require(
            token.lower() not in combined_site_js.lower(),
            f"site/js must not introduce remote bracket persistence before SupabaseBracketStore: found {token}",
            errors,
        )

    if errors:
        print("BracketDocument save seam before Supabase verification failed: " + "; ".join(errors))
        return 1

    print("OK: bracket save seam remains local-only while SupabaseProfileStore may persist public player names.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
