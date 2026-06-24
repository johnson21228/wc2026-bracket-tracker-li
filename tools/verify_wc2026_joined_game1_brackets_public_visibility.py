#!/usr/bin/env python3
from pathlib import Path

errors = []

def require(condition, message):
    if not condition:
        errors.append(message)

store = Path("site/js/services/SupabaseBracketStore.js").read_text()
sql = Path("source/sql/wc2026_supabase_profiles_and_bracket_saving_target.sql").read_text()

require(
    'visibility: normalizeVisibility(gameId === "game1" ? "public" : bracket.visibility)' in store,
    "SupabaseBracketStore must force joined Game 1 remote bracket visibility to public.",
)

require(
    "visibility: canonicalBracketDocument.visibility" in store,
    "Supabase table visibility column must be written from the canonical BracketDocument.",
)

require(
    "bracket_json: canonicalBracketDocument" in store,
    "Supabase bracket_json must store the same canonical public visibility document.",
)

require(
    "for update" in sql and "auth.uid" in sql and "user_id" in sql,
    "SQL target must preserve owner-write policy.",
)

makefile = Path("Makefile").read_text()
require(
    "tools/verify_wc2026_joined_game1_brackets_public_visibility.py" in makefile,
    "Makefile must run joined Game 1 public visibility verifier.",
)

if errors:
    raise SystemExit("Joined Game 1 public visibility verification failed: " + "; ".join(errors))

print("OK: joined Game 1 bracket rows are public for shared standings while owner-write remains protected.")
