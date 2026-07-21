# Dataiku Icon Library — build instructions

This repo hosts a self-contained icon browser at `index.html` (served by GitHub Pages).
**`index.html` is generated — never hand-edit it.** Edit the source below and rebuild.

## How to rebuild

```bash
python3 build_app.py
```

This regenerates `index.html` at the repo root from the source files. No dependencies
are required for a normal rebuild (standard library only).

## After rebuilding

Commit and push. GitHub Pages redeploys automatically on push to the default branch:

```bash
git add index.html
git commit -m "Rebuild icon library"
git push
```

## Source files

- `build_app.py` — the generator. Produces `index.html`.
- `data/icons_final.json` — Material Symbols set. Each entry is `{ "p": <svg path>, "c": <category> }`.
  Paths are pre-extracted from the Material Symbols **Sharp** variable font at the locked spec
  **Fill 1 / Weight 500 / Grade 200 / Optical size 24** on a 960-unit em grid. Do not alter the spec.
- `data/brand_final.json` — DKU product icons. Each entry is `{ "c": <category>, "vb": <viewBox>, "s": <inner svg markup> }`.
  Colors are the originals and must be preserved (no recoloring). IDs are already namespaced per icon.
- `logo.svg` — Dataiku logomark, embedded as the page favicon at build time.

## Common tasks

- **Add / update DKU product icons:** edit `data/brand_final.json`. Add a key = icon name, value =
  `{ "c": "<Category>", "vb": "0 0 W H", "s": "<inner svg markup with namespaced ids>" }`, then rebuild.
  When adding many from Figma SVGs, namespace each icon's internal `id`s (prefix them uniquely) and
  rewrite matching `url(#..)`, `href="#.."`, `xlink:href="#.."` references to avoid cross-icon collisions.
- **Refresh the Material set to Google's latest:** re-extract `data/icons_final.json` from the current
  Material Symbols Sharp variable font at the same locked spec (do not change the axis values), then rebuild.
- **Change page text, layout, colors, pagination:** edit `build_app.py`, then rebuild.

## Notes

- Copy PNG in the app needs a secure context (https), which GitHub Pages provides. It will not work
  when opening `index.html` from a local `file://` path — that is expected.
- Keep `index.html` at the repo root so Pages serves it at the site URL.
