from pathlib import Path

js = Path('site/js/standings/PlayerStandingsSurface.js').read_text()
css = Path('site/css/app.css').read_text()
data = Path('site/data/current/PlayerSuppliedLinks.json').read_text()
makefile = Path('Makefile').read_text()

required_js = [
    'PLAYER_SUPPLIED_LINKS_URL = "data/current/PlayerSuppliedLinks.json"',
    'data-player-supplied-links-open',
    'data-player-supplied-links-panel',
    'normalizePlayerSuppliedLinks',
    '.sort((a, b) => (b.sortTime - a.sortTime)',
    'target="_blank"',
    'rel="noopener noreferrer"',
]
missing = [snippet for snippet in required_js if snippet not in js]
if missing:
    raise SystemExit('Player supplied links runtime missing: ' + ', '.join(missing))

required_css = [
    '.player-supplied-links-button',
    '.player-supplied-links-panel',
    'text-overflow: ellipsis',
    'white-space: nowrap',
]
missing = [snippet for snippet in required_css if snippet not in css]
if missing:
    raise SystemExit('Player supplied links CSS missing: ' + ', '.join(missing))

if 'PlayerSuppliedLinks' not in data:
    raise SystemExit('PlayerSuppliedLinks data source missing expected key')

if 'Send Steve any links you think the group might appreciate as they follow the World Cup.' not in js:
    raise SystemExit('Player supplied links intro copy missing')

if 'https://www.bbc.com/sport/football/articles/c4gy9yd8lgwo' not in data:
    raise SystemExit('First player supplied BBC link missing')

if 'tools/verify_wc2026_player_supplied_links_panel.py' not in makefile:
    raise SystemExit('Player supplied links verifier is not wired into make verify')

print('OK: Pool panel includes a player-supplied links button, date-sorted data loading, truncated titles, and new-tab links.')
