#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def read(path):
    return (ROOT / path).read_text()

def require(condition, message, errors):
    if not condition:
        errors.append(message)

def main():
    errors = []

    rule = read("li/world_cup/supabase_remote_bracket_store_contract_rule.md")
    doc = read("docs/architecture/bracketeering_supabase_remote_bracket_store_contract.md")
    capture = read("captures/CAPTURE_BACK_SUPABASE_REMOTE_BRACKET_STORE_CONTRACT_BEFORE_IMPLEMENTATION.md")
    card = read("cards/269_supabase_remote_bracket_store_contract_before_implementation_card.md")
    makefile = read("Makefile")

    combined = "\n".join([rule, doc, capture, card])

    required_phrases = [
        "does not implement `SupabaseBracketStore`",
        "does not apply Supabase SQL",
        "does not change public Supabase dashboard state",
        "does not change runtime site behavior",
        "The site owns View and Controller behavior",
        "Supabase/Postgres provides durable Model persistence only",
        "store/repository/session seam",
        "`loadUserBracket(userId)`",
        "`saveUserBracket(bracketDocument)`",
        "Only the active store is authoritative",
        "Local mode and remote mode are separate storage modes",
        "There is no automatic merge, migration, or reconciliation",
        "one `user_brackets` row per player/game",
        "full canonical `BracketDocument` stored in `picks_json`",
        "Do not model one row per pick",
        "`phaseLocks.r32LockedAt`",
        "R32 picks cannot be changed by the player",
        "client-side model/session write path",
        "Supabase/Postgres persistence policy or mutation guard",
        "UI-only hiding is not sufficient",
        "Remote save/load failures must not silently corrupt local state",
        "A failed remote save must not be treated as a successful contest save",
        "Local browser mode must continue to work without Supabase",
        "View and Controller code must not call Supabase directly",
        "bracket persistence must remain behind the bracket store seam",
        "direct Supabase calls from board View code",
        "direct Supabase calls from pick Controller code",
    ]

    for phrase in required_phrases:
        require(phrase in combined, f"remote bracket store contract missing phrase: {phrase}", errors)

    require(
        "python3 tools/verify_wc2026_supabase_remote_bracket_store_contract.py" in makefile,
        "new Supabase remote bracket store contract verifier must be included in make verify",
        errors,
    )

    require(
        (ROOT / "site/js/services/ActiveBracketSession.js").exists(),
        "ActiveBracketSession seam must exist before remote store implementation",
        errors,
    )
    require(
        (ROOT / "site/js/services/BracketRepository.js").exists(),
        "BracketRepository seam must exist before remote store implementation",
        errors,
    )
    require(
        (ROOT / "source/sql/wc2026_supabase_shared_pick_schema_draft.sql").exists(),
        "canonical Supabase schema draft should remain available but not applied by this verifier",
        errors,
    )
    # SupabaseBracketStore.js may now exist after the inactive-seam implementation CB.
    # This contract verifier remains responsible for the architecture boundary; the inactive-seam verifier proves runtime activation has not happened accidentally.
    if (ROOT / "site/js/services/SupabaseBracketStore.js").exists():
        store_text = read("site/js/services/SupabaseBracketStore.js")
        require(
            "class SupabaseBracketStore" in store_text and "loadUserBracket(userId)" in store_text and "saveUserBracket(bracketDocument)" in store_text,
            "SupabaseBracketStore.js may exist only if it implements the expected remote store contract",
            errors,
        )

    controller_paths = [
        ROOT / "site/js/controllers/Game1R32PickController.js",
        ROOT / "site/js/mvc/view.js",
        ROOT / "site/js/board/BoardShell.js",
        ROOT / "site/js/board/R32PickMenuLayer.js",
    ]
    forbidden_runtime_tokens = [
        "createClient(",
        "supabase.from(",
        ".from(\"user_brackets\")",
        ".from('user_brackets')",
    ]

    for path in controller_paths:
        text = path.read_text()
        for token in forbidden_runtime_tokens:
            require(
                token not in text,
                f"View/Controller runtime file must not call Supabase directly: {path.relative_to(ROOT)} contains {token}",
                errors,
            )

    if errors:
        print("WC2026 Supabase remote bracket store contract verification failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("OK: WC2026 Supabase remote bracket store contract is defined before implementation and keeps persistence behind the active store seam.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
