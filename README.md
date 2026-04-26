# Tamil Nadu 2026 Candidates — Open Dataset

Companion data release for **[ndranandraj.com](https://ndranandraj.com)**.

Two CSVs covering the April 2026 Tamil Nadu Legislative Assembly election: every candidate the Election Commission accepted as contesting, plus the suspect namesake/dummy pairings extracted from that roster.

## Files

| File | Rows | Description |
|---|---|---|
| [`dashboard/data/candidates-2026.csv`](dashboard/data/candidates-2026.csv) | 4,023 | Every contesting candidate, matched to ECI's official count. Party, alliance, age, education, declared assets, liabilities. |
| [`dashboard/data/dummy-pairs-2026.csv`](dashboard/data/dummy-pairs-2026.csv) | 329 | Suspect namesake pairs — major-alliance candidates whose names overlap with another (usually independent) candidate in the same constituency. |

Schema documentation, sources, methodology, and known caveats are in **[`dashboard/data/README.md`](dashboard/data/README.md)**.

## Web pages

Self-contained HTML, no build step required:

- **[`dashboard/candidates-dataset-2026.html`](dashboard/candidates-dataset-2026.html)** — data release page with download buttons, schemas, and caveats
- **[`dashboard/dummy-candidates-2026.html`](dashboard/dummy-candidates-2026.html)** — interactive analysis of the dummy-pair dataset

## Quick start

```python
import pandas as pd
candidates = pd.read_csv("dashboard/data/candidates-2026.csv")
pairs      = pd.read_csv("dashboard/data/dummy-pairs-2026.csv")

# Top wealthy candidates (filter the ~170 ambiguous rows)
(candidates
   .query("assets_declared > 100_000")
   .nlargest(10, "assets_declared")
   [["candidate_name", "party_code", "constituency_name", "assets_declared"]])
```

## Caveats

Three known data-quality gaps documented in [`dashboard/data/README.md`](dashboard/data/README.md):

1. `criminal_cases` is `0` for all rows — both MyNeta and ECI affidavit scrapes were blocked at publication time
2. ~170 asset values are off by a factor of 10⁵–10⁷ (same-name same-party candidates couldn't be disambiguated). Filter with `assets_declared > 100000` if assets matter for your analysis.
3. `C. Joseph Vijay` (TVK) appears in both Perambur and Tiruchirappalli (East) with mismatched declared assets — investigate before quoting

## License

Released under **[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)** — free to use with attribution.

> Anand Raj. *"Tamil Nadu 2026 Candidates + Dummy Match Pairs."* ndranandraj.com, April 2026.

## Sources

- [tnelections2026.in](https://tnelections2026.in/candidates.html) — public Candidates Explorer (canonical roster source)
- [MyNeta — TamilNadu2026](https://www.myneta.info/TamilNadu2026/) — ADR's affidavit aggregation
- [Election Commission of India](https://eci.gov.in/) — official 4,023 count reconciliation
