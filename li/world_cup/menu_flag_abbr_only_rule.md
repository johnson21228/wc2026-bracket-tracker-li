# LI Rule — Choice Menu Items Use R32 Compact Identity Rendering

Choice menu team options must render with the same compact identity style as R32 items:

```text
flag + three-letter code
```

Full country names should not be visible inside the choice menu item rows once the menu has been rendered. Full names may remain in data attributes, aria labels, or source data if useful for accessibility or future scoring.

The renderer must preserve selection behavior and must not replace the clickable option element itself.
