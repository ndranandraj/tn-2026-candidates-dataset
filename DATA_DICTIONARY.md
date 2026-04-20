# Data Dictionary

Schema for `data/candidates_2026.csv` (released as a v1.0 asset).

One row = one candidate filing for the TN 2026 Legislative Assembly.

| Column                     | Type     | Nullable | Example                          | Description |
|----------------------------|----------|----------|----------------------------------|-------------|
| `constituency_code`        | string   | no       | `TN-015`                         | ECI constituency code. Stable across years. |
| `constituency_name`        | string   | no       | `Perambur`                       | Official ECI constituency name (English). |
| `constituency_name_ta`     | string   | yes      | `பெரம்பூர்`                       | Tamil name, where available from ECI. |
| `year`                     | integer  | no       | `2026`                           | Election year this row refers to. |
| `candidate_name`           | string   | no       | `R. Kumar`                       | Name as filed on the Form 26 affidavit. |
| `candidate_name_normalized`| string   | no       | `r kumar`                        | Lowercased, punctuation-stripped, transliteration-collapsed. See METHODOLOGY. |
| `party`                    | string   | yes      | `IND`                            | Party symbol shorthand. `IND` = Independent. Null if not yet declared. |
| `alliance`                 | string   | yes      | `DMK-led`                        | Alliance grouping, or null for unaffiliated / independents. |
| `affidavit_url`            | string   | yes      | `https://affidavit.eci.gov.in/…` | Link to the Form 26 affidavit PDF on the ECI portal. |
| `votes_2021`               | integer  | yes      | `87421`                          | Votes received by this exact candidate in 2021 (if ran). Null if new. |
| `rank_2021`                | integer  | yes      | `3`                              | Finishing rank in 2021 for this candidate. |
| `margin_pct_2021`          | float    | yes      | `1.8`                            | **Constituency-level** winning margin in 2021, expressed as percentage points of the total valid votes. Same value repeats across all rows sharing a `constituency_code`. |
| `namesake_group_id`        | string   | yes      | `NS-015-a`                       | Stable ID linking candidates grouped as namesakes. Null = not part of a namesake cluster. See METHODOLOGY for grouping rules. |
| `namesake_group_size`      | integer  | yes      | `3`                              | Count of candidates in the same group, including this row. Denormalized for convenience. |
| `is_primary_candidate`     | boolean  | yes      | `true`                           | Heuristic: the candidate in the group with a prior electoral history or a major-party alliance ticket. `false` for the suspected dummy filings. Null when the group has no clear primary. |
| `notes`                    | string   | yes      | `Matched on Tamil spelling`      | Free-text notes from manual review (e.g., "transliteration variant", "same address", "withdrew on 2026-03-12"). |
| `last_updated`             | date     | no       | `2026-04-22`                     | ISO-8601 date of last edit to this row. |

## Derived fields used in scripts

`scripts/make_scatter.py` computes two per-constituency aggregates:

| Derived                        | From                                           |
|--------------------------------|------------------------------------------------|
| `namesake_count_2026`          | `COUNT(*) WHERE year=2026 AND namesake_group_id IS NOT NULL` per constituency |
| `flag`                         | `TRUE` if `margin_pct_2021 < 5` AND `namesake_count_2026 >= 2`                |

## Integrity rules

- Every row with a non-null `namesake_group_id` must share that ID with at
  least one other row (minimum group size = 2).
- `margin_pct_2021` is constant within a `(constituency_code, year)` pair.
- `candidate_name_normalized` is deterministic — re-running the
  normalization script on `candidate_name` must reproduce it exactly.

## Sources

- Candidate filings: Election Commission of India (ECI), Form 26 affidavits
- 2021 results: ECI Form 20 booth-level tabulations, aggregated to
  constituency level
- Tamil names: ECI's Tamil-language portal, cross-checked with
  state CEO disclosures
