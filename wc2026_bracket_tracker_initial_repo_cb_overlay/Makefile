.PHONY: verify pack

verify:
	python3 tools/verify_wc2026_bracket_tracker.py

pack:
	mkdir -p dist
	zip -r dist/wc2026-bracket-tracker-li.pack.zip . -x 'dist/*' '.git/*' '__MACOSX/*'
