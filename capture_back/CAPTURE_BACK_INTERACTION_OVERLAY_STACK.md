# Capture Back: Interaction Overlay Stack

Card 209 captures the interaction-layer rule for the WC2026 board runtime.

The issue: bottom-frame controls such as the group button rail can visually or interactively compete with transient surfaces. The intended behavior is that a pick menu is above the bottom rail, and the group panel is above the pick menu.

The fix records this in LI and CSS and verifies it as part of `make verify`.
