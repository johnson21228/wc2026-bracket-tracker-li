#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

checks = {
    "site/js/app.js": [
        "createSupabaseIdentitySurface",
        "createPlayerStandingsSurface",
        "setupCurrentPlayerScore",
        "standingsStore.listPlayerStandings()",
        "currentPlayer?.score ?? 0",
    ],
    "site/css/app.css": [
        "CB 1026 hard override: identity child stays inside right-pinned card",
        "--player-standings-width: 64px",
        "[Pool readable pill] gap [Join/Profile circle] 16px browser right edge",
        "[data-supabase-identity-surface] .identity-compact-card",
        "right: calc(env(safe-area-inset-right, 0px) + var(--player-control-right)) !important",
        "body [data-supabase-identity-surface] .identity-compact-card .identity-status-button",
        "position: static !important",
        "inset: auto !important",
        ".player-standings-control",
        "+ var(--player-identity-size)",
        "+ var(--player-control-gap)",
        ".player-standings-control .standings-icon-button",
        "border-radius: 999px !important",
        "font-size: 17px !important",
        "content: none !important",
        ".current-player-score",
        "--wc-top-score-width: 88px",
        "font-variant-numeric: tabular-nums",
    ],
    "site/js/standings/PlayerStandingsSurface.js": [
        "button.textContent = \"Pool\"",
        "data-player-standings-control",
        "data-player-standings-open",
    ],
    "site/js/identity/SupabaseIdentitySurface.js": [
        "forceCircularIdentityButton",
        "aria-label\", \"Join Bracketeering",
        "aria-label\", \"Profile",
    ],
}

errors = []
for rel, tokens in checks.items():
    p = ROOT / rel
    if not p.exists():
        errors.append(f"{rel} missing")
        continue
    text = p.read_text()
    for token in tokens:
        if token not in text:
            errors.append(f"{rel} missing token: {token}")

app = (ROOT / "site/js/app.js").read_text()
for token in [
    "installR16AnchoredTopControls",
    "installR16AnchoredIdentityStandingsControls",
    "installTopRightPlayerControls",
]:
    if token in app:
        errors.append(f"site/js/app.js still wires experimental mover: {token}")

if errors:
    print("CSS-owned top-right player controls verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: Join/Profile child is static inside the right-pinned card; Pool is pinned to its left.")
