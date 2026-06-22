# Floating board surfaces above overlay controls

Pick menus and group panels are transient board-owned surfaces. They must render above fixed app overlay controls such as login, info, and zoom controls.

The implementation may keep login and map controls fixed above the board during normal play, but when a pick menu or group panel is open, the board scroll stacking context must be promoted above app chrome so the open floating surface is never hidden behind the login control or map controls.

This is View/CSS-owned. It must not change pick validity, game state, Supabase identity behavior, or group/result data.
