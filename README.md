# Portfolio

Faldo Lyon's research-desk site. Static HTML, CSS and JavaScript, no build step. Published as a Claude Artifact
(see HANDOFF.md for the link and the republish map).

- `index.html` — home. `research.html` — the research library. `engines.html` — the engine library. `cpv.html` — the CPV model, live.
  `analyst.html` — the CV with proofs. `kopi.html` — Kopi Satset.
- `src/base.css`, `src/chrome.html`, `src/docs.js` — the shared stylesheet, site chrome and document registry.
  Each page carries a copy between marker comments; after editing a canonical file run `python3 tools/sync.py`.
- `proof/` — web-sized images, rendered document pages and PDFs. `proof/originals/` is git-ignored.
- `GLOSSARY.md` — engine term → market term. Visible text uses the market term; the engine's own name is a small
  `.code` tag beside it (hidden by body class `codes-off`).

To add a research document: drop `proof/research/<slug>.pdf` and its rendered pages `<slug>-p01.jpg …`, set
`attached: true` and `rendered: N` for the slug in `src/docs.js`, run the sync, republish.
