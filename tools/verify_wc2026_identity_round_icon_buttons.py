#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def read(path):
    return (ROOT / path).read_text()

def require(path, token):
    text = read(path)
    if token not in text:
        raise SystemExit(f"Missing token in {path}: {token}")

identity = read("site/js/identity/SupabaseIdentitySurface.js")
app_css = read("site/css/app.css")

for token in [
    "function identityIconSvg(kind)",
    'person-add',
    'person-check',
    'identity-icon-svg',
    'aria-label="Join Bracketeering"',
    'title="Join Bracketeering"',
    'aria-label="Profile"',
    'title="Profile"',
]:
    if token not in identity:
        raise SystemExit(f"Identity surface missing token: {token}")

for forbidden in [
    ">Join</button>",
    ">Profile</button>",
]:
    if forbidden in identity:
        raise SystemExit(f"Identity text button remains: {forbidden}")

for token in [
    ".identity-icon-button",
    "border-radius: 50% !important",
    "width: 44px",
    "height: 44px",
    "width: 44px !important",
    "height: 44px !important",
    "min-width: 44px !important",
    "max-width: 44px !important",
    "min-height: 44px !important",
    "max-height: 44px !important",
    "aspect-ratio: 1 / 1",
    "border-radius: 50% !important",
    "padding: 0 !important",
    "display: inline-grid !important",
    "flex: 0 0 44px",
    ".identity-icon-svg",
    "stroke-linecap: round",
]:
    if token not in app_css:
        raise SystemExit(f"Identity icon CSS missing token: {token}")

require("Makefile", "python3 tools/verify_wc2026_identity_round_icon_buttons.py")

print("OK: identity Join/Profile controls use round SVG icon buttons with tooltips.")
