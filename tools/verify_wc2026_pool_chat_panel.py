#!/usr/bin/env python3
from pathlib import Path

root = Path(__file__).resolve().parents[1]
js = (root / "site/js/standings/PlayerStandingsSurface.js").read_text()
css = (root / "site/css/app.css").read_text()
makefile = (root / "Makefile").read_text()

required_js = [
    'data-pool-chat-open aria-expanded="false" aria-controls="pool-chat-panel"',
    'data-player-supplied-links-open aria-expanded="false" aria-controls="player-supplied-links-panel"',
    'data-pool-chat-form',
    'window.sessionStorage?.setItem(POOL_CHAT_SESSION_STORAGE_KEY',
    'import { getSharedSupabaseClient } from "../services/SupabaseClient.js";',
    'const POOL_CHAT_CHANNEL_NAME = "pool-chat:bracketeering-pub";',
    'const POOL_CHAT_BROADCAST_EVENT = "pool-chat-message";',
    'supabase.channel(POOL_CHAT_CHANNEL_NAME',
    'poolChatChannel.on("broadcast", { event: POOL_CHAT_BROADCAST_EVENT }',
    'await channel.send({',
    'type: "broadcast"',
    'Messages are broadcast only and are not saved as chat history.',
]

for marker in required_js:
    if marker not in js:
        raise SystemExit(f"Missing Pool Chat runtime marker: {marker}")

if js.index('data-pool-chat-open') > js.index('data-player-supplied-links-open'):
    raise SystemExit("Pool Chat button must remain before Player Links in the Pool header")

for forbidden in [
    'pool_chat_messages',
    '.from("pool_chat_messages")',
    ".from('pool_chat_messages')",
    '.insert({ body',
    '.insert([{ body',
]:
    if forbidden in js:
        raise SystemExit(f"Pool Chat must not persist chat messages through Supabase tables: {forbidden}")

required_css = [
    '.pool-chat-button',
    '.pool-chat-panel',
    '.pool-chat-status',
    '.pool-chat-messages',
    '.pool-chat-form',
]

for marker in required_css:
    if marker not in css:
        raise SystemExit(f"Missing Pool Chat CSS marker: {marker}")

if 'python3 tools/verify_wc2026_pool_chat_panel.py' not in makefile:
    raise SystemExit("Makefile verify target must include Pool Chat verifier")

print("OK: Pool panel includes ephemeral live broadcast chat before Player Links without storing chat messages in Supabase.")
