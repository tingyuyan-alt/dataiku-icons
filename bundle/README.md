# Dataiku Icon Library

An internal, searchable icon browser hosted as a single static page.

- **Live site:** _add your GitHub Pages URL here_ (e.g. `https://<user>.github.io/<repo>/`)
- **Two sets:** Material Symbols (Sharp / Fill 1 / Weight 500 / Grade 200 / opsz 24) and DKU product icons (original colors).
- **Features:** search, category filter, palette recolor (Material set), copy/download as SVG · PNG · name · JSX, pagination.

## Editing

`index.html` is **generated** — do not edit it by hand. Change the source and rebuild:

```bash
python3 build_app.py     # regenerates index.html at the repo root
git add index.html
git commit -m "Rebuild icon library"
git push                 # GitHub Pages redeploys automatically
```

See [`CLAUDE.md`](./CLAUDE.md) for full build details and common tasks (adding product icons,
refreshing the Material set, etc.). That file also lets Claude Code rebuild the site for you.

## Layout

```
build_app.py            generator (standard library only)
logo.svg                favicon source (embedded at build time)
data/
  icons_final.json      Material Symbols paths + categories
  brand_final.json      DKU product icons (viewBox + inner SVG + category)
index.html              GENERATED — the hosted page (keep at repo root)
```
