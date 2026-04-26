# Tamil Nadu 2026 Assembly Election — Open Datasets

Two datasets covering the April 2026 Tamil Nadu Legislative Assembly election:

1. **`candidates-2026.csv`** — the canonical roster of all 4,023 contesting candidates
2. **`dummy-pairs-2026.csv`** — 329 "suspect" candidate pairs where a major-party nominee shares (or near-shares) a name with another candidate in the same constituency, suggesting deliberate vote-splitter strategy

These two are intentionally bundled because the second only makes sense in the context of the first. Use both; cite both.

---

## 1. `candidates-2026.csv` — Full candidate roster

**Rows:** 4,023 (matches the Election Commission of India's official count)  
**Constituencies:** 234 (every TN assembly seat)  
**Districts:** 32  
**Parties:** 106  
**Schema (21 columns):**

| Column | Type | Notes |
|---|---|---|
| `candidate_id` | int | Internal DB id |
| `constituency_name` | text | Full AC name |
| `constituency_no` | int | Official ECI AC number, 1–234 |
| `district_name` | text | Revenue district |
| `candidate_name` | text | As filed with the returning officer |
| `party_name` | text | Full registered party name |
| `party_code` | text | Short code, e.g. `DMK`, `AIADMK`, `IND` |
| `alliance` | text | `INDIA`, `NDA`, `TVK`, `NTK`, etc., where applicable |
| `gender` | char(1) | `M`, `F`, or `O` |
| `age` | int | At time of nomination |
| `education` | text | Highest qualification declared in Form 26 |
| `criminal_cases` | int | **Currently 0 for all rows — see Caveats** |
| `serious_cases` | int | IPC 302/376 etc. — also 0 currently |
| `assets_declared` | bigint | INR, parsed from "₹X.XX Cr" / "₹X.XX L" strings |
| `liabilities` | bigint | INR |
| `votes_received` | int | Empty pre-poll (election is May 4) |
| `vote_share_pct` | numeric | Empty pre-poll |
| `winner` | bool | `False` for everyone pre-poll |
| `margin` | int | Empty pre-poll |
| `deposit_forfeited` | bool | `False` pre-poll |
| `source_url` | text | Per-candidate URL where applicable |

**Top 12 parties by candidates fielded:**

| # | Party | Candidates | Notes |
|---|---|---|---|
| 1 | IND | 2,208 | Independents — slightly more than half the field |
| 2 | NTK | 234 | Naam Tamilar Katchi — contesting every seat |
| 3 | TVK | 233 | Vijay's Tamilaga Vettri Kazhagam — announced 234, ended at 233 |
| 4 | DMK | 176 | Alliance leader (allies fill the rest) |
| 5 | AIADMK | 172 | Alliance leader |
| 6 | TAVK | 164 | Tamizhaga Vaazhvurimai Katchi |
| 7 | BSP | 119 | Bahujan Samaj Party |
| 8 | AIPTMMK | 78 | Vijayakanth's party |
| 9 | PT | 60 | Puthiya Tamilagam |
| 10 | NIP | 33 | Naam Indiar Party |
| 11 | BJP | 33 | NDA ally |
| 12 | AJPK | 29 | Aanaithinthiya Jananayaka Pathukappu Kazhagam |

---

## 2. `dummy-pairs-2026.csv` — Suspect dummy candidate pairs

**Rows:** 329 suspect pairs across 144 constituencies  
**Schema (12 columns):**

| Column | Type | Notes |
|---|---|---|
| `constituency` | text | Constituency where both candidates contest |
| `major_candidate` | text | The major-alliance nominee being targeted |
| `major_party` | text | E.g. `DMK`, `ADMK` |
| `major_alliance` | text | `INDIA` or `NDA` |
| `suspect_candidate` | text | The candidate whose name overlaps |
| `suspect_party` | text | Usually `IND` (independent) |
| `similarity` | float | 0.0–1.0; 1.0 = identical after normalization |
| `category` | text | `EXACT` (identical post-normalization), `NEAR_FULL` (almost identical), `WORD_MATCH` (one significant word overlaps) |
| `match_detail` | text | Human-readable explanation |
| `matched_words` | text | The shared name fragment |
| `normalized_major` | text | Canonical form of major candidate's name |
| `normalized_suspect` | text | Canonical form of suspect's name |

**Worst-affected constituencies (by pair count):**

| AC | Pairs |
|---|---|
| Tiruvannamalai | 9 |
| Kilpennathur | 7 |
| Kalasapakkam | 7 |
| Avadi | 7 |
| Villivakkam | 6 |

**Category breakdown:** 202 `WORD_MATCH`, 77 `EXACT`, 50 `NEAR_FULL`.

---

## Sources

- **Candidate roster** — scraped from [tnelections2026.in](https://tnelections2026.in/candidates.html) (the public Candidates Explorer maintained alongside the 2026 election cycle), cross-referenced against MyNeta's TN 2026 listings and reconciled against the ECI's official 4,023 count.
- **Dummy-pair detection** — derived from the candidate roster using normalized-name matching: prefixes (`Mr/Shri/Selvi/Thiru`) stripped, single-letter initials dropped, then exact-match + word-overlap scoring. Source code in `pipelines/11_dummy_candidate_analysis.py` of the parent repository.

## Caveats

- **`criminal_cases` is `0` for every row.** Both MyNeta's web pages (current scraper broke against new HTML) and the ECI's affidavit portal (returns 403 to bot requests) refused to yield this field at publication time. Will be backfilled when ADR releases its 2026 analysis report.
- **Asset values for ~170 rows are wrong.** Where a constituency has multiple candidates with the same name *and* same party (e.g. three independents named `Loganathan. M` in Salem), the asset re-parser couldn't tell them apart and skipped the update. Those rows still hold values that are off by a factor of 10⁵–10⁷. Filter them out by checking `assets_declared < 100000` if assets matter for your analysis.
- **Two `C. Joseph Vijay` entries.** The TVK chief appears in both Perambur and Tiruchirappalli (East) with different declared assets (₹809 cr vs ₹603 cr). One of these is likely a data error; the public TVK list should be the tiebreaker.
- **Pre-poll snapshot.** Vote counts, winners, margins, and deposit-forfeiture status are all blank. The dataset will be updated post-results (May 4, 2026).

## License

Released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — use freely with attribution. Suggested citation:

> Anand Raj. "Tamil Nadu 2026 Candidates + Dummy Match Pairs." ndranandraj.com, April 2026.
