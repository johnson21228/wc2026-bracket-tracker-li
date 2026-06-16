#!/usr/bin/env python3
from pathlib import Path
import re

html = Path('site/index.html')
if not html.exists():
    raise SystemExit('Missing site/index.html')
text = html.read_text(encoding='utf-8')
start = '// WC2026_PAGES_REVIEW_PICK_ACCEPTANCE_START'
end = '// WC2026_PAGES_REVIEW_PICK_ACCEPTANCE_END'
assert start in text, 'missing start marker'
assert end in text, 'missing end marker'
start_i = text.index(start)
end_i = text.index(end, start_i) + len(end)
prev_script = text.rfind('<script', 0, start_i)
prev_script_close = text.rfind('</script>', 0, start_i)
next_script_close = text.find('</script>', end_i)
assert prev_script > prev_script_close, 'review acceptance JavaScript starts outside a script tag'
assert next_script_close != -1, 'review acceptance JavaScript is not closed by a script tag'
# Guard against the exact bad condition: the marker appearing as visible body text immediately after </div> without a script wrapper.
visible_prefix = text[max(0, start_i-80):start_i]
assert '<script' in text[prev_script:start_i], 'script opening not found before marker'
print('Pages review script text hiding verification passed.')
