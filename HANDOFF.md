# Portfolio handoff (2 Oct 2026, Research Desk build)

Published artifact (same URL every republish): https://claude.ai/artifact/XFf39bF1k65Kkz7yHMjYAA
Artifact root page: `index.html`. Supporting files: `research.html`, `engines.html`, `cpv.html`, `analyst.html`, `kopi.html`
and everything under `proof/` except `proof/originals/`. To republish from a new session: read the artifact
once (Artifact tool, action read), then publish `index.html` with `url` set to the link above, `root` = this
folder, and a `files` map for every new or changed file (files already published are kept if left out).

## Site structure
- `index.html` — the home page as seven claim-plates (order by Faldo's priority: the research, the engine,
  clients, Surabaya, the record, then the ATIC call demoted to a compact plate) ("every number has a source"): the opening, a table of
  contents tape, The call (ATIC), The library (fan of covers, IC-note lines), The engine (trace), Clients
  (triptych, roundtable, CV lines), Surabaya (Kopi, Sportfit, Saat Seduh), The record, Write to me. Counts come
  from the DOCS registry; the fan and IC lines are rendered by the page script.
- `research.html` — the Research Library: 21 documents, shelf and ledger views, filter rail, search, hash-routed
  reader pane (`#doc=<slug>`) with page strips and the shared lightbox. Pending documents render as labelled slots.
- `engines.html` — the Engine Library: 25 skill cards lifted from the SKILL.md files, the ladder and pipeline
  diagrams, the stepper, four dossiers, and a hand-off to `cpv.html`.
- `cpv.html` — the CPV engine field guide rebuilt natively: the model arithmetic ported verbatim from the
  original guide (now retired to `proof/originals/retired/`), a control panel for the ExampleCo toy, sixteen
  plates with recomputing SVG charts, the threshold register, the bank. Faldo's rule: never frame the old guide.
- `analyst.html` — CV facts with proofs: education (SAT report, ASEAN slot), experience ledger (Gotrade, City
  Innovation Hub, Maybank with the ATIC chart, note and letter), awards register (17 certificates, TIMO Final photo),
  leadership, skills.
- `kopi.html` — Kopi Satset, unchanged in content, on the shared chrome.

## Shared layer (edit here, then sync)
- `src/base.css` — tokens (light and dark), every shared component. `src/chrome.html` — head (theme script, fonts,
  favicon stub), site bar, footer, lightbox, shared script. `src/docs.js` — the DOCS registry and helpers.
- Every page carries copies of these between marker comments (BASE, HEAD, CHROME, FOOT, DOCS). After editing a
  canonical file run `python3 tools/sync.py`; it rewrites the blocks in every page. Never edit inside a marker
  block in a page. Page-specific CSS and script live outside the blocks. No build step: pages are complete files.
- `src/skeleton.html` — start a new page from this.

## Attaching a research document
1. Drop `<slug>.pdf` into `proof/research/` and render its pages to `<slug>-p01.jpg … -pNN.jpg` (1400px long side,
   PyMuPDF: `PYTHONPATH=<scratchpad>/py python3`; poppler is not installed and the Swift toolchain is broken on
   this Mac). At minimum render page 1.
2. In `src/docs.js` set `attached: true` and `rendered: N` for that slug. Run `python3 tools/sync.py`.
3. Republish with a `files` map listing the new files. Counts, covers, slots and the coverage table update themselves.
Pending at launch (14): nvda-ic-note, nvda-ic-1pager, bkr-ic-note, bkr-ic-1pager, cnq/cop/cve/cvx/fang/mpc/oxy/shel-
writeup, adbe-research, weekly-note-2026-09-20. They sit in ~/Downloads; Faldo must attach them in chat or drop them
into the folder himself (a bulk copy from Downloads was blocked on provenance on 2 Oct 2026; do not retry it).
Excluded by Faldo: the Alpha Selection Book pitch and the Sector Allocation report (never show them).

## Done 3 Oct 2026
Terminology pass: cpv.html, engines.html, index.html and the shared rating chips relabelled per GLOSSARY.md; code
tags with a switch on the CPV and engines pages; "How to read this page" tables and a scale-of-the-logic row on
both; the two paraphrased dossier lines on engines.html demoted from quotes to plain notes. CPV model block
unchanged (md5 9d33bb9d05d6f70a8ec02e737fd13ff5). Artifact version 14.

## Terminology rule (Faldo, 3 Oct 2026)
Visible text uses market terms; the engine's own names appear only as small `<span class="code">` tags beside them
(body class `codes-off` hides every tag; the CPV and engines pages carry a switch). `GLOSSARY.md` is the canonical
engine-term → market-term table, taken from Faldo's own lexicon in the gotrade-ic-note skill. Rating chips read
"New money · X" and "Holders · Y" (his Baker Hughes cover wording), never Entrant / Holder. Headlines never lead
with a T-code or an S-key; the threshold register keeps its codes as table data.

## GitHub Pages (second home for the site, alongside the artifact)
Repo: https://github.com/Hippityhippooo/portfolio (public, branch main, Pages from main / root). Live URL:
https://hippityhippooo.github.io/portfolio/ . Faldo pushes with GitHub Desktop (commit to main, Push origin);
every push redeploys Pages. Auto mode blocks Claude from creating repos, pushing or toggling Pages. `.nojekyll`
is present so Pages serves the files untouched; `.gitignore` excludes `proof/originals/`, `.claude/`, `.DS_Store`.
All links are relative, so the site works under `https://hippityhippooo.github.io/<repo>/`. Publishable set is
about 45 MB in 179 files. A public repo makes every PDF and certificate crawlable: the Gotrade approval gate
applies here even more than to the unlisted artifact link.

## Rules from Faldo's brief (keep)
- Name "Faldo Lyon" everywhere; the surname never prints (only inside the LinkedIn href). Class of 2029. SAT 1510.
- No phone, no address, no A-level certificate, no ID numbers (the SAT report's record locator is blacked out),
  no Maybank department named in any caption. The Maybank letter image itself prints "Retail Department" in its
  body; Faldo decided to show the genuine letter. Revisit if he changes his mind.
- Nothing on the site that is not on the October 2026 CV (`~/Downloads/Faldo_Lyon_CV_Banking-3.pdf`) or in work he
  did himself. Drafts (FANG, MPC, OXY, SHEL), the MLSW sample and Kopi plan figures are labelled, never hidden.
- Gotrade figures and documents need Justin's written approval before the link is shared; the PENDING APPROVAL
  banners (research.html, index.html Clients band) and the footer sentence stay until Faldo removes them.
- ATIC: the buy was called at Rp438; the note's Rp378 is the price on the morning of 2 Dec 2024 (resolved 2 Oct 2026).
- Meeting photo captions name the setting and place Faldo; never a client, firm or city.

## Still to add (labelled slots on the pages)
Return-offer letter; 1M+ analytics screenshot; Kora Pay, Lime Pay, House of Gains screenshots; dated Alpha Book
performance table; ASEAN letter (crop to letterhead and offer paragraph, remove the reference number); Euclid and
Australian Mathematics Competition results; Cluster Captain and STEM challenge photos; Location Book v13 (Kopi).

## Open questions
- £14k raised (CV) against Rp200m sought / Rp150m committed in the August Kopi deck; the site shows both as what
  they are. LinkedIn slug still says faldo-prasetyo. Rider photo caption quotes the cart livery price (Rp6,000).
- Energy store counts on engines.html are CONTENT.md's (71 / 119 / 53 / 21 / 8); the git mirror shows fewer rows.

## Originals
`proof/originals/` is git-ignored and never published. `drop-2026-10-02/` holds the folder Faldo dropped on
2 Oct 2026 (CVs, HEIC originals, a video, duplicates). The IELTS form and A-level documents must never be published.
