#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def require(condition, message, errors):
    if not condition:
        errors.append(message)


def main():
    errors = []
    index = (ROOT / "site/index.html").read_text()
    css = (ROOT / "site/css/app.css").read_text()
    makefile = (ROOT / "Makefile").read_text()

    # Existing runtime hooks and accessible labels must remain intact.
    for token in [
        'data-board-zoom-in aria-label="Zoom in"',
        'data-board-zoom-out aria-label="Zoom out"',
        'data-info-panel-open data-rules-panel-open aria-haspopup="dialog" aria-controls="info-panel" aria-label="Get info"',
    ]:
        require(token in index, f"missing runtime/accessibility token: {token}", errors)

    # The player-facing glyphs are now decorative icon spans rather than text nodes.
    for token in [
        'class="map-control-svg" viewBox="0 0 44 44"',
        'class="map-control-svg" viewBox="0 0 44 44"',
        'class="map-control-svg map-control-info-svg" viewBox="0 0 44 44"',
    ]:
        require(token in index, f"missing map inline SVG glyph: {token}", errors)

    forbidden_markup = [
        'aria-label="Zoom in">+</button>',
        'aria-label="Zoom out">−</button>',
        'aria-label="Get info">i</button>',
    ]
    for token in forbidden_markup:
        require(token not in index, f"font text glyph still used in button markup: {token}", errors)

    # CSS owns centering and geometry.
    for token in [
        'display: inline-grid;',
        'place-items: center;',
        '.map-icon-glyph {',
        '.map-icon-glyph::before,',
        '.map-icon-glyph::after {',
        '.map-icon-glyph-plus::before,',
        '.map-icon-glyph-minus::before {',
        '.map-icon-glyph-plus::after {',
        '.map-icon-glyph-minus::after {',
        'display: none;',
        '.map-icon-glyph-info::before {',
        '.map-icon-glyph-info::after {',
        'border-radius: 999px;',
    ]:
        require(token in css, f"missing CSS icon geometry token: {token}", errors)

    forbidden_css = [
        '.map-icon-button[data-rules-panel-open]',
        'font-family: Georgia, "Times New Roman", serif;',
        'font-style: italic;',
        'font: 800 24px/1 ui-sans-serif',
    ]
    for token in forbidden_css:
        require(token not in css, f"font-dependent icon styling still present: {token}", errors)

    for path in [
        ROOT / 'captures/CAPTURE_BACK_MAP_CONTROL_ICON_CENTERING.md',
        ROOT / 'cards/288_map_control_icon_centering_card.md',
        ROOT / 'li/world_cup/map_control_icon_centering_rule.md',
    ]:
        require(path.exists(), f"missing capture/card/rule artifact: {path.relative_to(ROOT)}", errors)

    require('python3 tools/verify_wc2026_map_control_icon_centering.py' in makefile,
            'Makefile does not run map-control icon-centering verifier', errors)

    if errors:
        print('Card 288 verification failed: ' + '; '.join(errors))
        return 1

    print('OK: WC2026 map controls use centered geometric icon glyphs instead of font text glyphs.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
