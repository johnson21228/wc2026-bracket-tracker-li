# Interaction Overlay Stack

The group button rail is a bottom-frame launcher and context control. It should never cover the pick menu or group panel.

The runtime uses a simple interaction stack:

- group rail and board controls stay below transient surfaces
- pick menus render above the rail
- group panels render above pick menus

This keeps the user from seeing a menu or standings panel hidden behind the bottom frame. When a group panel is opened from a pick menu group label, it becomes the foremost context surface.
