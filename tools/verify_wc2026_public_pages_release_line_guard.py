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

    rule = read("li/repo/public_pages_release_line_guard_rule.md")
    doc = read("docs/dev/public_pages_release_line_guard.md")
    card = read("cards/268_public_pages_release_line_guard_for_supabase_prep_card.md")
    capture = read("captures/CAPTURE_BACK_PUBLIC_PAGES_RELEASE_LINE_GUARD_FOR_SUPABASE_PREP.md")
    makefile = read("Makefile")

    combined = "\n".join([rule, doc, card, capture])

    required_phrases = [
        "`main` is the public Pages release line",
        "feature branches until intentionally approved",
        "integration/prep lane, not a public release lane",
        "must not accidentally publish unfinished Supabase/Auth/storage behavior",
        "`python3 tools/clean_repo_hygiene.py` passes",
        "`make verify` passes",
        "`make pack` passes",
        "Browser smoke test passes",
        "Local/browser play still works without Supabase",
        "Identity surface remains intentionally configured",
        "Supabase SQL/dashboard state is intentionally ready",
        "public Pages publish risk is explicitly accepted",
        "`tools/force_pages_publish.py`",
        "must not be used from Supabase prep branches unless",
        "browser-safe Supabase publishable key is not a release signal",
        "Supabase SQL must not be applied merely because a Pages prep branch exists",
        "Supabase dashboard changes are separate explicit actions",
        "does not change runtime site behavior",
        "does not implement `SupabaseBracketStore`",
        "does not apply Supabase SQL",
        "does not merge to `main`",
    ]

    for phrase in required_phrases:
        require(phrase in combined, f"release-line guard missing phrase: {phrase}", errors)

    require(
        "python3 tools/verify_wc2026_fail_closed_pages_publish.py" in makefile,
        "existing fail-closed Pages publish verifier must remain in make verify",
        errors,
    )
    require(
        "python3 tools/verify_wc2026_public_pages_release_line_guard.py" in makefile,
        "new public Pages release-line guard verifier must be included in make verify",
        errors,
    )

    runtime_files = [
        "site/index.html",
        "site/js/app.js",
        "site/js/services/SupabaseAuthService.js",
        "site/js/services/BracketRepository.js",
        "site/js/services/ActiveBracketSession.js",
        "site/js/model/UserBracketModel.js",
        "site/js/mvc/model.js",
        "site/js/controllers/Game1R32PickController.js",
    ]

    # This verifier intentionally does not require runtime content changes.
    for path in runtime_files:
        require((ROOT / path).exists(), f"expected runtime file missing while checking guard: {path}", errors)

    if errors:
        print("WC2026 public Pages release-line guard verification failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("OK: WC2026 public Pages release-line guard protects main while Supabase prep remains on feature branches.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
