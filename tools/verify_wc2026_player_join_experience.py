#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "site/js/services/SupabaseAuthService.js",
    "site/js/identity/SupabaseIdentitySurface.js",
    "captures/CAPTURE_BACK_PLAYER_JOIN_EXPERIENCE.md",
    "docs/features/player_join_experience.md",
    "li/world_cup/player_join_experience_rule.md",
]

REQUIRED_TOKENS = [
    'Play locally on this browser',
    'Email me a sign-in link',
    'Continue with Google',
    'redirectTo = `${window.location.origin}${window.location.pathname}`',
    'provider: "google"',
    'signInWithOAuth',
    'signInWithGoogle',
    "Continue with Google",
    "Email me a sign-in link",
    "Play locally on this browser",
    "Picks will be saved",
    "Loaded your bracket",
    "GitHub Pages owns View and Controller behavior",
    "Supabase Auth proves identity",
    "Supabase/Postgres provides durable Model persistence later",
    "The game board should not contain Google-specific pick logic",
]

FORBIDDEN_PLAYER_PANEL_TERMS = [
    "RLS",
    "JWT",
    "auth metadata",
]


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


def main():
    errors = []

    for rel in REQUIRED_FILES:
        if not (ROOT / rel).exists():
            errors.append(f"missing {rel}")

    if errors:
        print("Player join experience verification failed: " + "; ".join(errors))
        return 1

    combined = "\n".join(read(rel) for rel in REQUIRED_FILES)

    for token in REQUIRED_TOKENS:
        if token not in combined:
            errors.append(f"missing required token: {token}")

    rule_text = read("li/world_cup/player_join_experience_rule.md")
    for token in FORBIDDEN_PLAYER_PANEL_TERMS:
        if token not in rule_text:
            errors.append(f"rule must explicitly forbid player-facing term: {token}")

    pick_controller_candidates = list((ROOT / "site").glob("**/*pick*controller*.js"))
    pick_controller_candidates += list((ROOT / "site").glob("**/*Pick*Controller*.js"))

    for path in pick_controller_candidates:
        text = path.read_text(encoding="utf-8")
        if "provider: \"google\"" in text or "provider: 'google'" in text:
            errors.append(f"Google provider logic leaked into pick controller: {path.relative_to(ROOT)}")
        if "signInWithOAuth" in text:
            errors.append(f"OAuth sign-in leaked into pick controller: {path.relative_to(ROOT)}")

    if errors:
        print("Player join experience verification failed: " + "; ".join(errors))
        return 1

    print("OK: Bracketeering player join experience captures Google preferred path, email fallback, local play, and auth/pick boundary.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
