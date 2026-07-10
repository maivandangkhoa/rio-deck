# Rio — Pitch Deck

Customer presentation for **Rio**, the AI maintenance engineer.
Format: **10 minutes · multiple prospects at once (webinar / broadcast)**.

Built with [Marp](https://marp.app/) — slides are plain Markdown in
[`slides.md`](slides.md). Each `---` is a slide; HTML comments are speaker
notes (with a ⏱ time budget) shown only in presenter view.

## Structure

```
rio-deck/
├── slides.md      # the deck (edit this)
├── assets/        # images/logos used by the slides
├── package.json   # build scripts
└── dist/          # generated output (gitignored)
```

## Prerequisites

Node.js 18+. No install needed — the scripts fetch Marp on first run via `npx`.
(Optionally `npm install` to pin the version from `package.json`.)

## Build & present

```bash
# One-off render (uses npx, no install):
npx @marp-team/marp-cli slides.md -o dist/rio-deck.html --html   # website
npx @marp-team/marp-cli slides.md --pdf                          # PDF
npx @marp-team/marp-cli slides.md --pptx                         # PowerPoint

# Or, after `npm install`, use the shortcuts:
npm run html      # → dist/rio-deck.html
npm run pdf       # → dist/rio-deck.pdf
npm run pptx      # → dist/rio-deck.pptx
npm run watch     # live-reloading HTML while you edit slides.md
npm run serve     # local server with presenter view (press "p")
```

**Presenter view** (speaker notes + timer): open the HTML, press **`P`**.
Navigate with arrow keys; **`F`** for fullscreen.

## Editing tips

- One idea per slide. Keep bullets short — the notes carry the talk track.
- To restyle (dark/indigo Rio look, fonts, logo), add a `<!-- theme -->` block
  or a custom Marp theme CSS and reference it in the front-matter of `slides.md`.
- Drop images into `assets/` and reference them: `![](assets/phone.png)`.

## Language

The deck is in **English** (mirrors the landing page). VI / KO cuts can be
generated on request — keep them as `slides.vi.md` / `slides.ko.md`.
