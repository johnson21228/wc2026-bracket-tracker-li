# Group Panel Highlight Link Storage

The group panel may make a completed match clickable only when the checked-in local highlight model provides a verified highlight URL for that match.

## Storage

Highlight links live in:

```text
site/data/current/match_highlights.json
```

The runtime reads this file as local model data. It must not scrape ESPN, YouTube, FIFA, or any other external page at runtime.

## Rendering rule

- Completed match with a verified highlight URL: render the completed match evidence as an external link/action.
- Completed match without a verified highlight URL: render the completed match as static result evidence.
- Scheduled or incomplete match: render kickoff time or `Time TBD`; do not make it a highlight action unless the local highlight model contains a valid URL.

External highlight links use normal browser best practice:

```html
target="_blank" rel="noopener noreferrer"
```

## Seeded links

This card seeds a small verified set:

- Argentina 3-0 Algeria, using the user-provided URL.
- Brazil 1-1 Morocco, verified from a matching FIFA YouTube highlight title.
- Haiti 0-1 Scotland, verified from a matching FIFA YouTube highlight title.

Additional completed-match links should be added by future Capture Back only when the URL/title/result clearly match the local completed match evidence.
