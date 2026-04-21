# TN 2026 Candidates — Open Dataset

Public dataset of suspected **namesake / dummy candidate** filings for
the Tamil Nadu 2026 Legislative Assembly election.

- Blog write-up: https://ndranandraj.com/posts/tn-2026-dummy-candidates/
- License: **CC-BY-4.0** — use it, remix it, credit the source.
- Maintainer: Anand Raj ([@ndranandraj](https://github.com/ndranandraj))

## What's in the file

`data/candidates_2026.csv` — 329 rows across 144 constituencies.

Each row is **one pair**: a major-alliance candidate and a same-constituency
suspect candidate whose name is similar enough to flag. The file captures
three tiers of similarity:

| Match tier   | Pairs | What it means                                      |
|--------------|-------|----------------------------------------------------|
| `EXACT`      |  77   | Identical name after normalization                 |
| `NEAR_FULL`  |  50   | Fuzzy full-name match (similarity 0.86–0.96)       |
| `WORD_MATCH` | 202   | Shared name token (treat as leads, not findings)   |

**83 % of all suspects are Independents.** Major candidates span every
major alliance — DMK, ADMK/NDA, TVK, NTK, BJP, INC, and smaller parties.

> **⚠️ Read `METHODOLOGY.md` before drawing conclusions.**
> A namesake filing is not automatically a dummy candidacy. The dataset
> documents patterns consistent with vote-splitting tactics — it does
> not prove intent in any specific case. Local reporting, affidavit
> cross-checks, and court records are the only way to settle individual
> claims.

## Repository layout

```
.
├── README.md                   ← you are here
├── LICENSE                     ← CC-BY-4.0 notice
├── DATA_DICTIONARY.md          ← column-by-column schema
├── METHODOLOGY.md              ← how pairs were produced
├── data/
│   └── candidates_2026.csv     ← the dataset
└── scripts/
    ├── make_chart.py           ← top-constituencies chart
    └── requirements.txt        ← matplotlib + pandas
```

## Quickstart

```bash
git clone https://github.com/ndranandraj/tn-2026-candidates-dataset
cd tn-2026-candidates-dataset

# Read the data in Python
python3 -c "import pandas as pd; print(pd.read_csv('data/candidates_2026.csv').head())"

# Reproduce the chart
python3 -m venv .venv && source .venv/bin/activate
pip install -r scripts/requirements.txt
python scripts/make_chart.py data/candidates_2026.csv out/chart.png
```

## How to cite

> Raj, Anand. *TN 2026 Candidates — Open Dataset* (v1.0). 2026. CC-BY-4.0.
> https://github.com/ndranandraj/tn-2026-candidates-dataset

## Contributing

Corrections are encouraged. Two kinds of Issues are especially useful:

- **False positives** — two candidates grouped together who are clearly
  different individuals. Please link the affidavit URLs.
- **False negatives** — suspect candidates the pipeline missed
  (typically a Tamil-Latin transliteration variant). Include both
  spellings.

Please open an Issue rather than a PR so every correction has an
audit trail.

### What this dataset is **not**

- Not a list of "dummy" candidates. Only a court, election commission,
  or investigative reporter can establish intent in a specific case.
- Not political commentary. Every major alliance appears among the
  majors. The file exposes a structural pattern, not a partisan claim.
- Not a prediction. No forecasting models are fit on this data.

## Releases

| Version | Date       | Changes                                                      |
|---------|------------|--------------------------------------------------------------|
| v1.0    | 2026-04-24 | Initial public release: 329 pairs, 144 constituencies        |

Subscribe to releases (**Watch → Custom → Releases**) for corrections
and v1.1 (which will add the scraping + matching scripts).
