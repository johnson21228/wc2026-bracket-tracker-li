.PHONY: verify pack clean-hygiene open-site

verify:
	python3 tools/verify_wc2026_bracket_tracker.py

clean-hygiene:
	python3 tools/clean_repo_hygiene.py

open-site:
	open site/index.html
	open site/game1/index.html
	open site/game2/index.html

pack: clean-hygiene verify
	mkdir -p dist
	rm -f dist/wc2026-bracket-tracker-li.pack.zip
	zip -r dist/wc2026-bracket-tracker-li.pack.zip . \
		-x 'dist/*' \
		-x '.git/*' \
		-x '__MACOSX/*' \
		-x '.DS_Store' \
		-x '*/.DS_Store' \
		-x 'wc2026_*_overlay/*' \
		-x 'wc2026_bracket_tracker_cb_001/*' \
		-x 'wc2026_schedule_poster_input_artifact/*'
