#!/usr/bin/env python3
from pathlib import Path

js = Path("site/js/standings/PlayerStandingsSurface.js").read_text(encoding="utf-8")
css = Path("site/css/app.css").read_text(encoding="utf-8")
makefile = Path("Makefile").read_text(encoding="utf-8")

for forbidden in [
    'data-pool-chat-open',
    'data-pool-chat-panel',
    'data-pool-chat-form',
    'id="pool-chat-panel"',
    'class="pool-chat-button"',
    '<h3>Pool Chat</h3>',
]:
    if forbidden in js:
        raise SystemExit(f"Pool Chat UI must stay hidden; found rendered marker: {forbidden}")

for required in [
    'data-player-supplied-links-open',
    'data-player-supplied-links-panel',
    'data-player-standings-close',
    'player-standings-title',
    'Pool Standings',
    'World Cup Links',
]:
    if required not in js:
        raise SystemExit(f"Pool panel lost required non-chat UI marker: {required}")

# CSS/runtime support may remain while the feature is hidden, but it must not be rendered.
for allowed_runtime_marker in [
    'POOL_CHAT_CHANNEL_NAME',
    'POOL_CHAT_BROADCAST_EVENT',
]:
    if allowed_runtime_marker not in js:
        raise SystemExit(f"Expected dormant Pool Chat runtime marker to remain for reversible hiding: {allowed_runtime_marker}")

if "verify_wc2026_pool_chat_panel.py" not in makefile:
    raise SystemExit("Makefile verify target must include Pool Chat hidden verifier")

surface = Path(
    "site/js/standings/PlayerStandingsSurface.js"
).read_text(encoding="utf-8")

if "setPoolChatPanelOpen(false)" in surface:
    raise SystemExit(
        "Pool close path must not call removed Pool Chat UI functions."
    )

close_panel_markers = [
    "function closePanel()",
    "setPlayerSuppliedLinksPanelOpen(false);",
    "panel.hidden = true;",
]
missing_close_markers = [
    marker for marker in close_panel_markers if marker not in surface
]
if missing_close_markers:
    raise SystemExit(
        "Pool close path must close links and hide the Pool panel; "
        f"missing: {missing_close_markers}"
    )

print("OK: Pool panel hides Pool Chat UI and its close path no longer calls removed chat functions.")
