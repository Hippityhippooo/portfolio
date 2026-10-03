# Engine term → market term (canonical glossary for the site)

Source of truth: Faldo's own lexicon in the gotrade-ic-note skill ("framework term → what the reader is told instead"), plus the wording his Baker Hughes IC note already uses on its cover ("FOR NEW CAPITAL · NO BUY / FOR EXISTING HOLDERS · HOLD"). The rule on the site: the MARKET TERM is the primary text everywhere a visitor reads (headlines, eyebrows, control labels, readout labels, chart titles, tiles, bands, prose); the ENGINE TERM appears once beside it as a small mono tag `<span class="code">…</span>` so the architecture stays visible. Never invent a new engine term; never change a number, a threshold value or a T-code's meaning.

| Engine term (as on the page now) | Market term (primary text) | Code tag text | Notes |
|---|---|---|---|
| the bank / field bank / S1–S13 | the model output: thirteen sections of named fields | bank · S1–S13 | "writes a field bank" → "writes a structured model output, never the report" |
| SM completion manifest | completion checklist | SM | every section present and filled |
| SP provenance ledger | provenance log: where every number came from | SP | |
| D / G / M / A | disclosed / from guidance / modelled / assumed | D G M A | always expand on first use in a section |
| weighted PV / wPV | probability-weighted fair value (per share) | wPV · S10 | never "target price"; keep the engine's own caveat "not a target price" |
| undiscounted (value / return) | expected value at exit, before discounting / expected return before the cost of capital | | BKR note: "absolute gain, before the cost of capital" |
| edge / edge to wPV | upside to fair value, after the cost of capital (expected return over spot) | edge | BKR note: "over the price, after the cost of capital" |
| arm (bear / base / bull arm) | scenario (bear / base / bull) | arm | |
| the roll / g_roll | the year-two earnings roll-forward / year-two growth | g_roll | |
| NTM | next twelve months (NTM) | | NTM is market-standard; keep but expand once |
| twin reconcile | reconciliation against consensus and against the market price | step 6 | |
| priced X / consensus Y / build Z | what the price implies / consensus / our forecast | X · Y · Z | |
| inversion through the hurdle table / implied growth | market-implied growth, backed out of the P/E | 6b | |
| variant view | where we differ from the market | | |
| method tree / routes | valuation method selection / the valuation methods (P/E, EV/EBITDA, EV/FCF, FCF yield, P/B) | tree · routes | |
| bridge (EV to equity) | enterprise-value-to-equity bridge | | market-standard already |
| cross-check band | tolerance between valuation methods | band | |
| exit stance / moat × regime bracket | exit-multiple assumption, bounded by moat quality and the sector regime | stance · T17 | |
| anchor multiple | the multiple the valuation is anchored on | step 7 | |
| dial | input | | "shock every dial" → "shock every input" |
| tornado | sensitivity ranking (tornado chart) | 9c | tornado is market-standard; keep the word |
| breakeven distances | what the price already requires: breakeven growth, multiple and EPS | 9d | |
| asymmetry / asymmetry ratio | upside-to-downside ratio (reward to risk) | 10d | "favourable" / "exhausted" stay |
| s*(1.5) / s*(0.8) / crossover band | entry level / trim level | s*(k) | entry at or below s*(1.5), trim at or above s*(0.8) |
| conviction cells / five cells | the five conviction criteria | 10e | |
| T32 scale / score | conviction score (out of five) | T32 | |
| caps (position cap etc.) | limits | | |
| setup / setup classifier / axes / cascade | positioning / how the positioning is decided / the criteria / the decision order | 10h · setup 1–7 | setup names: 1 pre-catalyst accumulation → "accumulate before the catalyst"; 2 event-imminent → "event imminent"; 3 priced-in confirm → "already priced in, confirm"; 6 short edge / avoid → "negative expected return, avoid"; 0 → "no positioning" |
| Entrant / Holder | new money / existing holders | entrant · holder | the BKR cover wording |
| Entrant map / Holder map | rating for new money / rating for existing holders | 10k | |
| dual rating on two bases | two ratings on two bases: new money on the discounted return, existing holders on the undiscounted return | 10k | |
| the clock | the catalyst calendar | 10b | |
| theta / thesis theta | time decay of the thesis | 10i | |
| reaction matrix | expected price reaction by outcome | 10c | |
| kill switch(es) | thesis-break condition(s) | 10j | "no kill fired" → "no thesis-break condition has been met" |
| gate | the test, named (e.g. the first-quarter anchor test) | | a gate that fires = a test that fails and stops the run |
| Q1 anchor (T9) | the first-quarter anchor: the forecast must match the last reported quarter within tolerance | T9 | |
| T47 anchor-identity guard | a check that the exit value is not just today's price carried forward | T47 | |
| discount-rate category guard | the discount rate must be a cost of equity (CAPM), inside 7.5–20% | | |
| admissibility (gate) | the model output must be complete before a report can be written | | |
| containment C1–C4 | no number may appear in the report that is not in the model output | C1–C4 | |
| register rules R1–R16 | plain-English rules for the report body | R1–R16 | |
| freshness window | data older than its window is rejected | window_d | |
| threshold register / T-codes | the register of every constant the engine uses (T1–T52) | T1–T52 | keep the codes IN the register table; headlines never lead with a code |
| calibration: general / structural / n=1 / PROPOSED | how far to trust each constant: standard practice / follows from the method / fitted on one run / proposed, awaiting review | | |
| p | probability (that the catalyst happens) | p | |
| a / anticipation | how much is already in the price | a | |
| in-window / phasing | within the next twelve months / timing | | |
| catalyst sizing funnel | from full size to the probability-weighted slice inside twelve months | 2–3 | |
| double-conservatism | charging the same uncertainty twice | T-flag | |
| composer | report writer (writes the document, types no number) | composer | |
| renderer | PDF layout | renderer | |
| feeder engines | input models (moat score, hurdle-rate surface, energy store) | | |
| flavor (A/B/C/D) | skill type: analytical / advisory / operational / transform | flavor | |
| authoring standard | the rulebook every skill is written to | | |
| handoff contract (reads / writes / forbidden) | what each skill may read, write and never touch | | |
| run discipline / engine invariant | how a run must behave | | |
| CAPM DR | discount rate (CAPM) | DR | |
| spot | spot price (current share price) | | market-standard |
| pack-limited | limited by missing inputs | T35 | |
| Steps 10b–10j etc. | keep step numbers in the eyebrow, but pair with the plain name: "Step 10e · Conviction" | | |

## Scale of the logic, in plain numbers (use these as the tiles / lead-in, all computed or on the page already)
- 12 steps in one fixed order (the spine)
- 13 output sections, each a set of named fields (S1–S13), plus a completion checklist and a provenance log
- 53 constants in one register, each tagged with how far to trust it
- 5 thesis-break conditions, none of them the price
- 2 ratings on 2 bases (new money / existing holders), 7 positioning outcomes, 5 conviction criteria
- 3 scenarios to 1 probability-weighted value; 4 valuation methods cross-checked

## Phrases to retire everywhere on the site
"Composers type no digits" → "The report writer types no number of its own; every figure is a reference to the model output."
"Gates refuse" → "Tests can stop a run."
"Engines compute" → "The engines do the arithmetic."
"S1–S13 · SM · SP" (as a bare label) → "model output · checklist · provenance"
"references, no digits" → "every number a reference"
"admissibility" (bare) → "output complete?"
"containment C1–C4" (bare) → "no untraced number"
"Q1 anchor · identity guard" (bare) → "matches last quarter · not just today's price"
"freshness window" (bare) → "data in date"
