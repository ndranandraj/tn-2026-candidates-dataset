# Data Dictionary

Schema for `data/candidates_2026.csv`.

**One row = one *matched pair*** of (major-alliance candidate × suspect
candidate) in the same constituency whose names are similar enough to
flag for review. A single constituency can appear in many rows if it has
several suspect candidates; a single major candidate can appear in
several rows if multiple suspects share a similar name.

| Column               | Type    | Nullable | Example                                        | Description |
|----------------------|---------|----------|------------------------------------------------|-------------|
| `constituency`       | string  | no       | `ALANDUR`                                      | Official ECI constituency name, uppercased. |
| `major_candidate`    | string  | no       | `S.Saravanan`                                  | Candidate fielded by a major alliance (DMK/DMK-alliance, AIADMK-NDA, TVK, NTK, BJP, etc.). As filed on ECI affidavit. |
| `major_party`        | string  | no       | `ADMK`                                         | Party of the major candidate. See "Party abbreviations" below. |
| `major_alliance`     | string  | no       | `NDA`                                          | Alliance grouping (`INDIA`, `NDA`, `TVK`, `NTK`, etc.). |
| `suspect_candidate`  | string  | no       | `A.Saravanan`                                  | Candidate in the same constituency whose name is similar enough to the major candidate's that it could plausibly split votes. |
| `suspect_party`      | string  | no       | `IND`                                          | Party of the suspect. 83% of suspects are `IND` (Independents). |
| `similarity`         | float   | no       | `1.0`                                          | Normalized match score, 0.25–1.00. Higher = closer name match. See METHODOLOGY §2. |
| `category`           | enum    | no       | `EXACT`                                        | One of `EXACT`, `NEAR_FULL`, `WORD_MATCH`. Discrete buckets for `similarity`. See METHODOLOGY §3. |
| `match_detail`       | string  | no       | `Identical after normalization: SARAVANAN`     | Human-readable one-line explanation of why this pair matched. |
| `matched_words`      | string  | no       | `SARAVANAN`                                    | The specific name token(s) that triggered the match. For `WORD_MATCH`, this is the shared surname / partial; for `EXACT` it's the whole normalized name. |
| `normalized_major`   | string  | no       | `SARAVANAN`                                    | `major_candidate` after normalization (uppercase, punctuation / single-letter initials stripped, whitespace collapsed). |
| `normalized_suspect` | string  | no       | `SARAVANAN`                                    | Same normalization applied to `suspect_candidate`. |

## Category values

| `category`   | Rows (of 329) | `similarity` range | Meaning                                                                |
|--------------|---------------|--------------------|------------------------------------------------------------------------|
| `EXACT`      | 77            | 1.00 exactly       | `normalized_major == normalized_suspect`. The strongest signal.        |
| `NEAR_FULL`  | 50            | 0.86 – 0.96        | Full-name fuzzy match (edit-distance + phonetic). Catches spelling variants, e.g. `SAMPATHKUMAR` ≈ `SAMPATH KUMAR`, `RAMACHANDRAN` ≈ `RAMACHANDIRAN`. |
| `WORD_MATCH` | 202           | 0.25 – 1.00        | At least one full name token is shared between the two names. Weakest signal — treat as leads, not findings. |

## Party abbreviations

Short forms used in `major_party` / `suspect_party`, reflecting the way
ECI lists record party names:

| Abbrev       | Party                                                     |
|--------------|-----------------------------------------------------------|
| `DMK`        | Dravida Munnetra Kazhagam                                 |
| `ADMK`       | All India Anna Dravida Munnetra Kazhagam (AIADMK)         |
| `BJP`        | Bharatiya Janata Party                                    |
| `INC`        | Indian National Congress                                  |
| `TVK`        | Tamilaga Vettri Kazhagam (Vijay's party)                  |
| `NTK`        | Naam Tamilar Katchi                                       |
| `PMK`        | Pattali Makkal Katchi                                     |
| `DMDK`       | Desiya Murpokku Dravida Kazhagam                          |
| `CPI`        | Communist Party of India                                  |
| `CPM`        | Communist Party of India (Marxist)                        |
| `IND`        | Independent (no party affiliation)                        |

Suspect parties also include full-text names for smaller outfits (e.g.,
`BAHUJAN SAMAJ PARTY`, `ALL INDIA JANANAYAKA MAKKAL KAZHAGAM`) which
appear verbatim as the ECI returned them.

## Derived quantities used in scripts

`scripts/make_chart.py` computes a per-constituency aggregate:

| Derived                    | From                                                           |
|----------------------------|----------------------------------------------------------------|
| `exact_count`              | `COUNT(*) WHERE category='EXACT'`     per constituency          |
| `near_full_count`          | `COUNT(*) WHERE category='NEAR_FULL'` per constituency          |
| `word_match_count`         | `COUNT(*) WHERE category='WORD_MATCH'`per constituency          |
| `total_suspect_pairs`      | sum of the three above                                          |

## Integrity rules

- Every row has both `major_candidate` and `suspect_candidate` populated.
  There are no orphan suspects or orphan majors in this file.
- `similarity == 1.0` only for `EXACT` and for a minority of `WORD_MATCH`
  cases (shared full-word token with otherwise-different names).
- `normalized_major` and `normalized_suspect` are deterministic — re-running
  the normalization script on `major_candidate` / `suspect_candidate`
  reproduces them byte-for-byte.

## Sources

- Candidate filings: Election Commission of India, Form 26 affidavits
  (public, accessible via the ECI affidavit portal).
- Alliance groupings: cross-checked against published pre-poll alliance
  announcements as of the CSV's `last_updated` date.

## Column pressure & versioning

The file is intentionally "wide-and-descriptive" rather than normalized.
Each row is self-contained so a reader looking at a single line can
understand the match without joining to another table. A normalized
representation (separate `candidates`, `match_pairs` tables) may ship
alongside in a future release — open an Issue if that would be useful.
