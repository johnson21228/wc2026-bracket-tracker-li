#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def read(path):
    return (ROOT / path).read_text()

def require(path, token):
    text = read(path)
    if token not in text:
        raise SystemExit(f"Banner lifecycle Stage selector UI verification failed:\n- missing {token!r} in {path}")

def forbid_segment(path, start_token, end_token, forbidden_tokens):
    text = read(path)
    if start_token not in text:
        raise SystemExit(
            f"Banner lifecycle Stage selector UI verification failed:\n"
            f"- missing segment start {start_token!r} in {path}"
        )
    start = text.index(start_token)
    end = text.index(end_token, start) if end_token in text[start:] else len(text)
    segment = text[start:end]
    errors = [
        token for token in forbidden_tokens
        if token in segment
    ]
    if errors:
        raise SystemExit(
            "Banner lifecycle Stage selector UI verification failed:\n"
            + "\n".join(
                f"- active Game selector must remain presentation-only; found {token!r}"
                for token in errors
            )
        )

index = read("site/index.html")
require("site/index.html", 'data-dev-game-selector')
require("site/index.html", 'data-dev-game-selector-option')
require("site/index.html", 'value="game-1" checked')
require("site/index.html", 'value="game-2"')
require("site/index.html", 'Dev game view')
require("site/index.html", '>Group Stage<')
require("site/index.html", '>Knockout Stage<')

app = read("site/js/app.js")
require("site/js/app.js", "setupInfoPanel(root);")
require("site/js/app.js", "setupActiveGameBackground(root);")
require("site/js/app.js", "ACTIVE_GAME_BACKGROUND_IMAGES")
require("site/js/app.js", '"game-1": "assets/board/pub_background_game1.jpeg"')
require("site/js/app.js", '"game-2": "assets/board/knockout_pub_background.jpeg"')

# The selector may now drive presentation-only runtime:
# rules panel text and board background image. It must not drive gameplay.
forbid_segment(
    "site/js/app.js",
    "function setupActiveGameBackground",
    "async function main()",
    [
        "createBracketModel",
        "createBracketController",
        "localStorage",
        "Supabase",
        "score",
        "route",
        "fetch(",
        "official_round_of_32",
        "official_knockout_results",
    ],
)

print(
    "OK: WC2026 banner Stage selector UI defaults to Group Stage and only drives presentation-only rules/background state."
)
