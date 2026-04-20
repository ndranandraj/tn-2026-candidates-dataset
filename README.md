# TN 2026 Candidates — Open Dataset

Candidate-level data backing the investigation of suspected **dummy / namesake
candidates** in the Tamil Nadu 2026 Legislative Assembly election.

- Blog write-up: https://ndranandraj.com/posts/tn-2026-dummy-candidates/
- License: **CC-BY-4.0** — use it, remix it, just credit the source.
- Maintainer: Anand Raj ([@ndranandraj](https://github.com/ndranandraj))

> **⚠️ Read `METHODOLOGY.md` before drawing conclusions.**
> A namesake candidate is not automatically a dummy candidate. The dataset
> identifies *patterns consistent with vote-splitting tactics* — it does not
> prove intent. Local reporting, affidavits, and court records are the only way
> to make individual determinations.

---

## What's in here

```
.
├── README.md                   ← you are here
├── LICENSE                     ← CC-BY-4.0 full text
├── DATA_DICTIONARY.md          ← column definitions, types, sample values
├── METHODOLOGY.md              ← how namesakes were grouped; selection criteria
├── data/
│   └── candidates_template.csv ← schema + a few illustrative rows
└── scripts/
    └── make_scatter.py         ← builds the 2021-margin × namesake-count plot
```

> The real dataset CSV is published as a versioned release asset on GitHub
> (see **Releases → v1.0**). The `data/` folder in `main` carries only the
> schema template so contributors can validate their pipelines.

---

## Why this exists

Every election cycle in Tamil Nadu, unusually close 2021 constituencies see
multiple candidates filed under near-identical names in the next cycle. The
pattern is old, suspected, and — until now — not published in a form that
journalists, researchers, or citizens can audit line-by-line.

This repository does three things:

1. **Publishes the raw candidate list** (constituency, name, party, 2026
   filing status, + 2021 result context).
2. **Documents the grouping logic** so you can reproduce, challenge, or
   extend the namesake detection.
3. **Provides plotting scripts** so the charts in the blog post are
   reproducible.

---

## Quickstart

```bash
git clone https://github.com/ndranandraj/tn-2026-candidates-dataset
cd tn-2026-candidates-dataset

# Grab the real data (not checked into main; see Releases)
curl -LO https://github.com/ndranandraj/tn-2026-candidates-dataset/releases/download/v1.0/candidates_2026.csv
mv candidates_2026.csv data/

# Plot
python3 -m venv .venv && source .venv/bin/activate
pip install -r scripts/requirements.txt
python scripts/make_scatter.py data/candidates_2026.csv out/scatter.png
```

---

## How to cite

> Raj, Anand. *TN 2026 Candidates — Open Dataset* (v1.0). 2026. CC-BY-4.0.
> https://github.com/ndranandraj/tn-2026-candidates-dataset

BibTeX is in `CITATION.cff` (added in v1.0 release).

---

## Contributing

Corrections are welcome and encouraged. Two kinds of issues are especially
useful:

- **False positives** — two candidates grouped as namesakes who are clearly
  different individuals (different affidavits, distinct addresses, no
  naming-overlap intent). Please link the evidence.
- **False negatives** — namesake groupings the script missed (e.g. because of
  a transliteration variant not covered by the normalization rules).

Please file an Issue rather than a PR first — the canonical dataset lives in
release assets, not in `main`, and we want to keep an audit trail of every
edit with a source link.

### What this dataset is **not**

- Not a list of "dummy" candidates. That word appears in the blog post as
  shorthand for a pattern. Only a court, election commission, or investigative
  reporter can establish intent in a specific case.
- Not a prediction. No forecasting models are fit here.
- Not political commentary. Every party that has fielded a namesake candidate
  shows up in the data.

---

## Releases

| Version | Date       | Changes                                             |
|---------|------------|-----------------------------------------------------|
| v1.0    | 2026-04-24 | Initial public release of candidates_2026.csv      |

Subscribe to releases (**Watch → Custom → Releases**) to be notified of
corrections.
