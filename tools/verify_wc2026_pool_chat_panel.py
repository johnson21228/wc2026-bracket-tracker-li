#!/usr/bin/env python3
from pathlib import Path

root = Path(__file__).resolve().parents[1]
js = (root / "site/js/standings/PlayerStandingsSurface.js").read_text(encoding="utf-8")
css = (root / "site/css/app.css").read_text(encoding="utf-8")
makefile = (root / "Makefile").read_text(encoding="utf-8")

start_marker = "panel.innerHTML = `"
end_marker = '<section id="player-supplied-links-panel"'

if start_marker not in js:
    raise SystemExit("Could not find Pool panel render markup start")
if end_marker not in js:
    raise SystemExit("Could not find Player Links panel marker")

rendered_header = js.split(start_marker, 1)[1].split(end_marker, 1)[0]

required_js = [
    'Pool Chat hidden until broadcast, storage, and visibility rules are explicitly governed.',
    'data-player-supplied-links-open aria-expanded="false" aria-controls="player-supplied-links-panel"',
]

for marker in required_js:
    if marker not in js:
        raise SystemExit(f"Missing Pool panel chat hiding marker: {marker}")

for forbidden in [
    'class="pool-chat-button"',
    'data-pool-chat-open',
    '<section id="pool-chat-panel"',
    'data-pool-chat-panel hidden',
    'data-pool-chat-form',
    'data-pool-chat-input maxlength="280"',
    '<h3>Pool Chat</h3>',
    'Open Pool Chat',
]:
    if forbidden in rendered_header:
        raise SystemExit(f"Pool Chat UI marker must not render: {forbidden}")

for forbidden in [
    '.pool-chat-button',
    '.pool-chat-panel',
    '.pool-chat-status',
    '.pool-chat-messages',
    '.pool-chat-form',
]:
    if forbidden in css:
        raise SystemExit(f"Pool Chat CSS marker must not remain: {forbidden}")

if 'python3 tools/verify_wc2026_pool_chat_panel.py' not in makefile:
    raise SystemExit("Makefile verify target must include Pool Chat hiding verifier")

print("OK: Pool panel hides Pool Chat UI while preserving governed Pool links and standings.")
