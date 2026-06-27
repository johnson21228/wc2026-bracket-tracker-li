# Knockout Runtime Default Background Rule

The single-game Bracketeering runtime must boot with the knockout pub background:

- `site/assets/board/knockout_pub_background.jpeg`

The generated knockout background is a static visual projection of current site truth. JSON remains the source of authority.

Rules:

- The runtime default background must be `site/assets/board/knockout_pub_background.jpeg`.
- The source/reference copy must remain byte-for-byte identical at `source/images/wc2026_knockout_pub_calendar_background.jpeg`.
- `site/js/services/assetPaths.js`, `site/js/mvc/view.js`, and `site/index.html` must not boot/preload the group-stage background.
- Legacy `game-1` and `game-2` presentation aliases may remain, but both must resolve to the knockout background in the one-game runtime.
- This rule is presentation-only. It must not alter gameplay logic, picks, scoring, standings, Supabase state, official truth, or pick menus.
