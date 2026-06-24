# Paste Back Terminal Output Contract

This repo treats terminal output pasted into the II client as a compact signal surface.

Do not paste by default:
- full successful make verify output
- full successful make pack zip listings
- full gh-pages file dumps
- long generated file inventories

Paste by default:
- command purpose
- PASS/FAIL result
- failure tail when failed
- git status --short
- latest commits when useful
- focused diffs when code review is needed
- publish source commit and publish completion line

Standard quiet verify / pack pattern:

    make verify > /tmp/wc2026_verify.log 2>&1 && echo "VERIFY: PASS" || { echo "VERIFY: FAIL"; tail -n 100 /tmp/wc2026_verify.log; }

    make pack > /tmp/wc2026_pack.log 2>&1 && echo "PACK: PASS" || { echo "PACK: FAIL"; tail -n 100 /tmp/wc2026_pack.log; }

    git status --short
    git --no-pager log --oneline -3

Standard quiet publish pattern:

    python3 tools/force_pages_publish.py > /tmp/wc2026_publish.log 2>&1
    PUBLISH_STATUS=$?

    if [ "$PUBLISH_STATUS" -eq 0 ]; then
      echo "PUBLISH: PASS"
      grep -E "Pages publish complete|Force publish complete|sourceCommit=|publishedAt=|Opening https://" /tmp/wc2026_publish.log || true
    else
      echo "PUBLISH: FAIL"
      tail -n 120 /tmp/wc2026_publish.log
    fi

    gh run list --limit 5
    git status --short
