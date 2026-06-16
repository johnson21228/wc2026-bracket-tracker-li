# Apply Overlay Terminal Workflow

Use this shape when applying a Capture Back overlay to the WC2026 Bracket Tracker Workbench.

```bash
cd /Users/stevejohnson/Developer/wc2026-bracket-tracker-li

unzip -o ~/Downloads/<overlay>.zip -d .
python3 <overlay_dir>/<apply_script>.py

make verify
make pack

git status --short

open site/index.html
open site/game1/index.html
open site/game2/index.html
```

The app `open` commands are required review evidence for any overlay that changes site runtime, game data, game assets, game behavior, or shared board geometry.

For LI-only overlays, open the changed LI/docs files and include app opens when the LI affects future Game 1 or Game 2 behavior.
