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

    service = read("site/js/services/SupabaseAuthService.js")
    surface = read("site/js/identity/SupabaseIdentitySurface.js")
    makefile = read("Makefile")

    combined_site_js = "\n".join(
        p.read_text(encoding="utf-8", errors="ignore")
        for p in (ROOT / "site/js").rglob("*.js")
    )

    require("email: user.email ||" in service, "Auth user summary should expose private account email to the identity UI.", errors)
    require('if (state.status === "signed-in") return "Signed in";' in surface, "Signed-in compact button should stay concise.", errors)
    require("This email is used for login. It is not your public player name." in surface, "Signed-in panel message should distinguish email from public player name.", errors)
    require("private account identity, not your public player name" in surface, "Signed-in details should label email as private account identity.", errors)
    require("Your public player name will be added later through a Supabase-backed profile." in surface, "Signed-in UI should point to later Supabase-backed profile work.", errors)
    require("Bracket saving:</strong> not enabled yet" in surface, "Signed-in UI should clearly state bracket saving is not enabled yet.", errors)
    require("identity-panel-signed-in-details" in surface, "Signed-in panel should render explicit account details.", errors)

    forbidden_tokens = [
        ".from(\"profiles\")",
        ".from('profiles')",
        ".from(`profiles`)",
        ".from(\"user_brackets\")",
        ".from('user_brackets')",
        ".from(`user_brackets`)",
        "SupabaseProfileStore",
        "SupabaseBracketStore",
        "ProfileStore",
        ".upsert(",
        ".insert(",
        "picks_json",
    ]
    for token in forbidden_tokens:
        require(
            token.lower() not in combined_site_js.lower(),
            f"Signed-in identity polish must not introduce profile/bracket Supabase persistence yet: found {token}",
            errors,
        )

    require(
        "python3 tools/verify_wc2026_signed_in_identity_ui_polish.py" in makefile,
        "Makefile verify should run signed-in identity UI polish verifier.",
        errors,
    )

    if errors:
        print("Signed-in identity UI polish verification failed: " + "; ".join(errors))
        return 1

    print("OK: signed-in identity UI polish clarifies private email, future player name, and local-only bracket persistence without changing bracket storage.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
