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

    auth = read("site/js/services/SupabaseAuthService.js")
    identity = read("site/js/identity/SupabaseIdentitySurface.js")

    require("email: user.email ||" in auth, "Auth summary must expose private email for account display.", errors)
    require('if (state.status === "signed-in") return "Signed in";' in identity, "Compact signed-in button must stay concise.", errors)
    require("private account identity, not your public player name" in identity, "Identity UI must distinguish private email from public player name.", errors)
    require("Public player name" in identity, "Identity UI must expose public player name surface.", errors)
    require("Supabase-backed profile" in identity, "Identity UI must describe the Supabase-backed profile boundary.", errors)
    require("Bracket saving:" in identity and "not enabled yet" in identity, "Identity UI must still say bracket saving is not enabled.", errors)

    forbidden_identity_tokens = [
        'from("user_brackets")',
        "SupabaseBracketStore",
        "bracket_json",
        "picks_json",
    ]
    for token in forbidden_identity_tokens:
        require(token not in identity, f"Identity UI must not enable bracket persistence yet: {token}", errors)

    if errors:
        print("Signed-in identity UI polish verification failed: " + "; ".join(errors))
        return 1

    print("OK: signed-in identity UI keeps private email separate from public player name while bracket persistence remains disabled.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
