#!/usr/bin/env python3
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
def fail(msg): print(msg,file=sys.stderr); sys.exit(1)
def read(path):
    p=ROOT/path
    if not p.exists(): fail(f"Missing required file: {path}")
    return p.read_text(encoding='utf-8')
html=read('site/game1/index.html')
for marker in ['src="../assets/playfield/uniform_pick_card_gameboard.svg"','data-board-source="site/assets/playfield/uniform_pick_card_gameboard.svg"','data-board-visual-authority="uniform-svg-gameboard"','data-board-layer-role="transparent-svg-linework"','uniform_pick_card_gameboard_manifest.js','validateUniformSvgGameboardManifestForGame1','uniform-svg-r32-manifest']:
    if marker not in html: fail(f"Game 1 missing uniform SVG board marker: {marker}")
for layer in ['class="pickLayer" id="pickLayer"','class="hitLayer" id="hitLayer"','game1_pub_options_background.jpeg']:
    if layer not in html: fail(f"Game 1 lost expected layer marker: {layer}")
game2_path=ROOT/'site/game2/index.html'
if game2_path.exists():
    game2=game2_path.read_text(encoding='utf-8')
    if 'src="../assets/playfield/uniform_pick_card_gameboard.svg"' in game2 or 'uniform_pick_card_gameboard_manifest.js' in game2:
        fail('Game 2 must not switch/load the uniform SVG board in this Game 1-only CB')
print('WC2026 Game 1 uniform SVG board layer checks passed.')
