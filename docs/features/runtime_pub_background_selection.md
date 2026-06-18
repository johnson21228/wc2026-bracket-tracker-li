# Runtime pub background selection

Card 204 makes the visible runtime board background use the group-stage pub image for now.

Active runtime asset:

`site/assets/board/pub_background.jpeg`

Retained future/alternate asset:

`site/assets/board/knockout_pub_background.jpeg`

The page preload in `site/index.html` and the MVC board background image in `site/js/mvc/view.js` must point to the same active runtime asset. This prevents the site from preloading one pub scene while rendering another.

The knockout pub/calendar background is retained because it remains useful when the app shifts to knockout schedule/bracket mode.
