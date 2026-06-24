# Paste Back Terminal Output Contract Rule

Terminal commands intended for paste-back into the II client must generate decision signal, not full transcripts.

Required behavior:
- successful noisy commands must be redirected to temp logs
- paste-back output must include compact PASS/FAIL lines
- failures must include the relevant failure tail
- successful verifier lists must not be pasted by default
- successful zip file lists must not be pasted by default
- publish commands must summarize source commit, publish completion, GitHub run status, and git status
- full logs may be shown only when diagnosing failure or when explicitly requested

Default paste-back fields:
- VERIFY: PASS or VERIFY: FAIL
- PACK: PASS or PACK: FAIL
- PUBLISH: PASS or PUBLISH: FAIL
- failure tail when failed
- git status --short
- git --no-pager log --oneline -3 when commit context matters
