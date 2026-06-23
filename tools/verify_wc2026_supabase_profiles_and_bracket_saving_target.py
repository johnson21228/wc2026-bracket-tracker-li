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

    sql = read("source/sql/wc2026_supabase_profiles_and_bracket_saving_target.sql")
    doc = read("docs/backend/wc2026_supabase_profiles_and_bracket_saving_target.md")
    makefile = read("Makefile")

    require("create table if not exists public.profiles" in sql, "SQL target must define public.profiles.", errors)
    require("display_name text not null" in sql, "profiles must include display_name.", errors)
    require("references auth.users(id)" in sql, "profiles/user_brackets must reference auth.users(id).", errors)
    require("create table if not exists public.user_brackets" in sql, "SQL target must define public.user_brackets.", errors)
    require("bracket_json jsonb not null" in sql, "user_brackets must store canonical BracketDocument JSON.", errors)
    require("bracket_json ? 'picksBySlot'" in sql, "SQL target must preserve picksBySlot shape validation.", errors)
    require("bracket_json ->> 'tournamentId' = tournament_id" in sql, "SQL target must require bracket_json.tournamentId to match row tournament_id.", errors)
    require("bracket_json ->> 'gameId' = game_id" in sql, "SQL target must require bracket_json.gameId to match row game_id.", errors)
    require("unique (user_id, tournament_id, game_id)" in sql, "user_brackets must be one row per user/tournament/game.", errors)
    require("alter table public.profiles enable row level security" in sql, "profiles must enable RLS.", errors)
    require("alter table public.user_brackets enable row level security" in sql, "user_brackets must enable RLS.", errors)
    require("(select auth.uid()) = id" in sql, "profile write policies must be owner-only.", errors)
    require("(select auth.uid()) = user_id" in sql, "bracket write/read policies must be owner-only.", errors)
    require("visibility = 'public'" in sql and "status in ('submitted', 'locked')" in sql, "shared read policy must be gated by visibility/status.", errors)
    require("to anon, authenticated" in sql, "public/shared read targets should be explicit.", errors)

    forbidden = [
        "email text",
        "auth.email",
        "handle_new_user",
        "create trigger on auth.users",
        "picks_json",
    ]
    for token in forbidden:
        require(token.lower() not in sql.lower(), f"SQL target must not include forbidden token yet: {token}", errors)

    require("It does not store auth email." in doc, "Doc must state profiles do not store auth email.", errors)
    require("Profile creation is intentionally client-driven" in doc, "Doc must explain no auth.users trigger yet.", errors)
    require(
        "python3 tools/verify_wc2026_supabase_profiles_and_bracket_saving_target.py" in makefile,
        "Makefile verify must run the SQL target verifier.",
        errors,
    )

    if errors:
        print("Supabase profiles/bracket saving SQL target verification failed: " + "; ".join(errors))
        return 1

    print("OK: Supabase profiles + bracket saving SQL target is captured with owner-write RLS and unchanged picksBySlot contract.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
