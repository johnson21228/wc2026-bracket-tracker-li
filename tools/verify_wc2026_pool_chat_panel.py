from pathlib import Path

js = Path("site/js/standings/PlayerStandingsSurface.js").read_text()
css = Path("site/css/app.css").read_text()
makefile = Path("Makefile").read_text()

required_js = [
    'data-pool-chat-open',
    'data-pool-chat-panel',
    'POOL_CHAT_SESSION_STORAGE_KEY = "wc2026.poolChat.sessionMessages.v1"',
    'window.sessionStorage?.setItem(POOL_CHAT_SESSION_STORAGE_KEY',
    'setPoolChatPanelOpen',
    'addPoolChatMessage',
    'Session-only chat for signed-in pool members',
]
missing_js = [token for token in required_js if token not in js]
if missing_js:
    raise SystemExit('Pool chat runtime missing: ' + ', '.join(missing_js))

required_css = [
    '.pool-chat-button',
    '.pool-chat-panel',
    '.pool-chat-messages',
    '.pool-chat-message',
    '.pool-chat-form',
]
missing_css = [token for token in required_css if token not in css]
if missing_css:
    raise SystemExit('Pool chat CSS missing: ' + ', '.join(missing_css))

if js.index('data-pool-chat-open') > js.index('data-player-supplied-links-open'):
    raise SystemExit('Pool chat button should appear before the player links button')

if 'tools/verify_wc2026_pool_chat_panel.py' not in makefile:
    raise SystemExit('Pool chat verifier is not wired into make verify')

print('OK: Pool panel includes a session-only chat sub-panel before Player Links.')
