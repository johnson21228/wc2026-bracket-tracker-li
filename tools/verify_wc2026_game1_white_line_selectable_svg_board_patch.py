#!/usr/bin/env python3
from pathlib import Path
import json, re, sys
import xml.etree.ElementTree as ET
ROOT=Path.cwd()
SVG=ROOT/'site/assets/playfield/uniform_pick_card_gameboard.svg'
MANIFEST=ROOT/'site/data/geometry/uniform_pick_card_gameboard_manifest.json'
HTML=ROOT/'site/game1/index.html'
GAME2=ROOT/'site/game2/index.html'
required=[
 'li/world_cup/game1_white_line_selectable_svg_board_rule.md',
 'docs/geometry/game1_white_line_selectable_svg_board.md',
 'cards/098_game1_white_line_selectable_svg_board_card.md',
 'prompts/tune_game1_white_line_selectable_svg_board.md',
 'capture_back/CAPTURE_BACK_GAME1_WHITE_LINE_SELECTABLE_SVG_BOARD.md',
 'tools/generate_uniform_pick_card_gameboard.py',
 'site/assets/playfield/uniform_pick_card_gameboard.svg',
 'site/assets/playfield/uniform_pick_card_gameboard.png',
 'site/data/geometry/uniform_pick_card_gameboard_manifest.json',
]
missing=[p for p in required if not (ROOT/p).exists()]
if missing: raise SystemExit('Missing expected files: '+', '.join(missing))
svg_text=SVG.read_text(encoding='utf-8')
if 'proof v2c' in svg_text or '<title>' in svg_text:
    raise SystemExit('SVG still contains proof/title presentation text')
if re.search(r'<rect[^>]+width="1536"[^>]+height="1024"', svg_text):
    raise SystemExit('SVG appears to contain an opaque/full-board background rectangle')
if 'data-presentation-style="white-line-selectable-r32"' not in svg_text:
    raise SystemExit('SVG missing white-line selectable presentation marker')
root=ET.parse(SVG).getroot()
rects=[e for e in root.iter() if e.tag.endswith('rect')]
paths=[e for e in root.iter() if e.tag.endswith('path')]
if len(rects)!=61: raise SystemExit(f'Expected 61 slot rects; found {len(rects)}')
if not paths: raise SystemExit('Expected connector paths')
if any((p.attrib.get('stroke') or '').lower() not in {'#ffffff','#fff','white'} for p in paths):
    raise SystemExit('All connector paths must use white stroke for middle-layer board presentation')
r32=[r for r in rects if r.attrib.get('data-round')=='R32']
if len(r32)!=32: raise SystemExit(f'Expected 32 R32 selectable rects; found {len(r32)}')
for r in r32:
    cls=r.attrib.get('class','')
    if 'slot-r32-selectable' not in cls: raise SystemExit('R32 rect missing slot-r32-selectable class')
    if float(r.attrib.get('fill-opacity','0')) < 0.18: raise SystemExit('R32 selectable fill opacity too low')
    if (r.attrib.get('stroke') or '').lower() not in {'#ffffff','#fff','white'}: raise SystemExit('R32 selectable target stroke is not white')
manifest=json.loads(MANIFEST.read_text(encoding='utf-8'))
if manifest.get('presentationStyle')!='white_line_selectable_r32': raise SystemExit('Manifest missing white_line_selectable_r32 style')
slots=manifest.get('slots',[])
if len(slots)!=61: raise SystemExit(f'Manifest expected 61 slots; found {len(slots)}')
if sum(1 for s in slots if s.get('round')=='R32' and s.get('game1SelectableTarget'))!=32:
    raise SystemExit('Manifest must mark all 32 R32 slots as Game 1 selectable targets')
html=HTML.read_text(encoding='utf-8')
if 'uniform_pick_card_gameboard.svg' not in html: raise SystemExit('Game 1 does not reference uniform SVG board')
if 'uniform-svg-r32-manifest' not in html: raise SystemExit('Game 1 does not appear to use manifest-driven R32 placement')
if GAME2.exists() and 'uniform_pick_card_gameboard.svg' in GAME2.read_text(encoding='utf-8'):
    raise SystemExit('Game 2 should not be migrated by this CB')
print('WC2026 Game 1 white-line selectable SVG board checks passed.')
