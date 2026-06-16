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
 'li/world_cup/game1_material_svg_board_colors_rule.md',
 'docs/geometry/game1_material_svg_board_colors.md',
 'cards/098_game1_material_svg_board_colors_card.md',
 'prompts/tune_game1_material_svg_board_colors.md',
 'capture_back/CAPTURE_BACK_GAME1_MATERIAL_SVG_BOARD_COLORS.md',
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
if 'data-presentation-style="material-brown-selectable-r32"' not in svg_text:
    raise SystemExit('SVG missing material-brown selectable presentation marker')
root=ET.parse(SVG).getroot()
rects=[e for e in root.iter() if e.tag.endswith('rect')]
paths=[e for e in root.iter() if e.tag.endswith('path')]
if len(rects)!=61: raise SystemExit(f'Expected 61 slot rects; found {len(rects)}')
if not paths: raise SystemExit('Expected connector paths')
for p in paths:
    stroke=(p.attrib.get('stroke') or '').lower()
    if stroke != '#542c23': raise SystemExit(f'Connector path must use #542C23 stroke, found {stroke}')
    if p.attrib.get('fill')!='none': raise SystemExit('Connector paths must remain fill="none"')
r32=[r for r in rects if r.attrib.get('data-round')=='R32']
if len(r32)!=32: raise SystemExit(f'Expected 32 R32 selectable rects; found {len(r32)}')
for r in rects:
    stroke=(r.attrib.get('stroke') or '').lower()
    fill=(r.attrib.get('fill') or '').lower()
    if stroke != '#542c23': raise SystemExit(f'Slot outline must use #542C23 stroke, found {stroke}')
    if fill != '#816a51': raise SystemExit(f'Slot fill must use #816A51, found {fill}')
for r in r32:
    cls=r.attrib.get('class','')
    if 'slot-r32-selectable' not in cls: raise SystemExit('R32 rect missing slot-r32-selectable class')
    if float(r.attrib.get('fill-opacity','0')) < 0.45: raise SystemExit('R32 selectable fill opacity too low for material target affordance')
manifest=json.loads(MANIFEST.read_text(encoding='utf-8'))
if manifest.get('presentationStyle')!='material_brown_selectable_r32': raise SystemExit('Manifest missing material_brown_selectable_r32 style')
policy=manifest.get('presentationPolicy',{})
if (policy.get('connectorStroke') or '').lower()!='#542c23': raise SystemExit('Manifest connectorStroke must be #542C23')
if (policy.get('r32SelectableFill') or '').lower()!='#816a51': raise SystemExit('Manifest r32SelectableFill must be #816A51')
slots=manifest.get('slots',[])
if len(slots)!=61: raise SystemExit(f'Manifest expected 61 slots; found {len(slots)}')
if sum(1 for s in slots if s.get('round')=='R32' and s.get('game1SelectableTarget'))!=32:
    raise SystemExit('Manifest must mark all 32 R32 slots as Game 1 selectable targets')
html=HTML.read_text(encoding='utf-8')
for marker in ['uniform_pick_card_gameboard.svg','uniform-svg-r32-manifest','material-brown-selectable-r32','applyUniformSvgR32ManifestGeometryToGame1SlotRules','class="pickLayer" id="pickLayer"','class="hitLayer" id="hitLayer"','game1_pub_options_background.jpeg']:
    if marker not in html: raise SystemExit(f'Game 1 missing material SVG board marker: {marker}')
if GAME2.exists() and ('uniform_pick_card_gameboard.svg' in GAME2.read_text(encoding='utf-8') or 'uniform_pick_card_gameboard_manifest.js' in GAME2.read_text(encoding='utf-8')):
    raise SystemExit('Game 2 should not be migrated by this CB')
print('WC2026 Game 1 material SVG board color checks passed.')
