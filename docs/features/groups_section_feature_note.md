# Groups Section Feature Note

## Feature

The WC2026 tracker site should have a Groups section showing Groups A–L with flags and team names.

This supports:

- source review
- Game 1 Round-of-32 pick selection
- later group standings
- visual clarity for users
- screenshots that can be interpreted later

## Initial source

The first group display source is the uploaded pair of images showing Groups A–F and Groups G–L.

These are preserved as source artifacts and converted into JSON.

## Site behavior

The static HTML should show:

```text
Group A
🇲🇽 Mexico
🇿🇦 South Africa
🇰🇷 Korea Republic
🇨🇿 Czechia
```

and similarly for every group.

## Later evolution

After group-stage results begin, this same section can evolve into a standings view:

```text
Team | Pts | W | D | L | GF | GA | GD
```
