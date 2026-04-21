# Methodology

How rows become suspect-candidate pairs, what each match category
actually catches, and the guardrails against false positives.

**TL;DR:** Scrape ECI Form 26 affidavits for the TN 2026 assembly
election. Inside each constituency, compare each major-alliance
candidate's name to every other candidate's name. Flag pairs where the
names are similar enough under one of three rules. Publish the full
pair list, not just the flags.

---

## 1. Data acquisition

Only public sources. No leaks, no paid feeds.

- **2026 filings** — Form 26 affidavits from the ECI affidavit portal.
  One filing per candidate. Scraped as a point-in-time snapshot on the
  CSV's `last_updated` date.
- **Alliance mapping** — published pre-poll alliance declarations
  (DMK-led `INDIA`, AIADMK-led `NDA`, `TVK`, `NTK`, etc.), applied to
  each candidate's `major_party` → `major_alliance`.
- **"Major candidate" definition** — any candidate fielded by DMK,
  ADMK, BJP, INC, TVK, NTK, PMK, DMDK, CPI, or CPM. Independents and
  smaller-party candidates are treated as potential *suspects*, never
  as *majors*.

---

## 2. Name normalization

Before comparison, every candidate name is run through a deterministic
pipeline:

1. **Uppercase** everything.
2. **Strip punctuation** — dots, commas, hyphens — so `R.Kumar` and
   `R. Kumar` and `R-Kumar` become the same.
3. **Collapse single-letter initials** and detach them as a prefix
   token. `T.M.ANBARASAN` → `ANBARASAN` with initials `T M`.
4. **Drop honorifics** (DR, MR, TMT, THIRU, etc.).
5. **Collapse whitespace** to a single space.

The result lands in the `normalized_major` and `normalized_suspect`
columns. This pipeline is the single source of truth — every category
below operates on the normalized forms, not on raw filings.

**Transliteration caveat.** Names filed in Tamil (`ர.குமார்`) are
transliterated to Latin using ISO 15919 before step 1. Distinct Tamil
spellings that transliterate to the same Latin form will collapse;
distinct Latin spellings of the same Tamil name will not. See §6.

---

## 3. The three match categories

Each candidate pair `(major, suspect)` within a constituency is assigned
exactly one category — the strongest one that applies. The `similarity`
column carries a 0–1 numeric score for sorting and threshold tuning.

### `EXACT` — 77 pairs, similarity = 1.0

`normalized_major == normalized_suspect` after the pipeline above.

Example row:
```
constituency        : ALANDUR
major_candidate     : S.Saravanan   (ADMK, NDA)
suspect_candidate   : A.Saravanan   (IND)
normalized_major    : SARAVANAN
normalized_suspect  : SARAVANAN
match_detail        : Identical after normalization: SARAVANAN
```

This is the headline number. Two candidates filed in the same
constituency with the same normalized name — the ballot will list
them on adjacent lines, with only a single-letter initial to tell
voters apart.

### `NEAR_FULL` — 50 pairs, similarity ≈ 0.86–0.96

Fuzzy full-name match. Computed as a combined character-level
edit-distance + phonetic (Soundex-style) score. Catches spelling
variants — the ECI's own data often contains these because affidavits
are transcribed from handwriting:

```
major_candidate     : V. Sampathkumar   (TVK)
suspect_candidate   : K. Sampath Kumar  (IND)
match_detail        : Full name similarity: SAMPATHKUMAR ≈ SAMPATH KUMAR
similarity          : 0.96
```

```
major_candidate     : Ramachandran.S    (ADMK, NDA)
suspect_candidate   : Ramachandiran.R   (IND)
match_detail        : Full name similarity: RAMACHANDRAN ≈ RAMACHANDIRAN
similarity          : 0.96
```

### `WORD_MATCH` — 202 pairs, similarity 0.25–1.0

At least one full name token is shared between the two names, even
though the full names differ. This is the **weakest** signal — treat
these rows as leads for a human reviewer, not as findings:

```
major_candidate     : K. Senthilkumar   (NTK)
suspect_candidate   : B. Rajesh Kumar   (BSP)
matched_words       : SENTHILKUMAR
match_detail        : Shared name parts: SENTHILKUMAR
```

Some `WORD_MATCH` pairs are clearly the same target name in different
spellings. Others — like the example above — share only a common token
(`KUMAR` is functionally an honorific in Tamil naming; it's as
diagnostic as "Junior" in English). The `similarity` column exists to
help you filter: for journalism, you'll want `similarity >= 0.7`
within `WORD_MATCH` to strip out the weakest noise.

---

## 4. Why the categories matter for interpretation

| Category     | Pairs | What a reasonable reviewer should do         |
|--------------|-------|----------------------------------------------|
| `EXACT`      | 77    | Treat as strong prima facie evidence. Look at affidavits, address, age to rule out genuine different individuals. |
| `NEAR_FULL`  | 50    | Investigate individually. High base rate of being the same "target name" with a transcription quirk. |
| `WORD_MATCH` | 202   | Filter first (similarity, party, alliance), then investigate selectively. Many will wash out as coincidental shared surnames. |

The blog post leads with the EXACT-category number for a reason — it
is the one tier where the statistical argument for "this is not random"
is effectively airtight within a single constituency.

---

## 5. What this dataset does **not** establish

- **Intent.** Two candidates can share a name by coincidence.
  Establishing that any specific suspect was filed as a dummy — rather
  than a sincere independent bid — requires sources this dataset does
  not contain: affidavit cross-checks, address overlap, history of
  contesting, public statements, or court findings.
- **Party responsibility.** A namesake filing does not prove the major
  candidate (or their party) orchestrated it. Some dummies are
  self-starters. Some are paid proxies. Some are sincere unaffiliated
  candidates who happen to share a common surname.
- **Causal impact on outcomes.** This dataset is descriptive — it
  documents a pattern of filings. It does not model how those filings
  would or would not have altered 2026 results.

---

## 6. Known limitations

- **`WORD_MATCH` has high false-positive rate.** Tamil names frequently
  share tokens like `KUMAR`, `RAJ`, `SELVI`, `PRIYA`. A `WORD_MATCH`
  row is a lead, not a finding.
- **No affidavit address data published.** Candidate addresses appear
  on Form 26 affidavits and would help distinguish genuinely-different
  people sharing a normalized name. We did not republish addresses
  here (privacy); you can re-check any individual pair from the public
  ECI portal.
- **Withdrawals are a moving target.** Some filed candidates withdrew
  before the ballot finalised. This file is a snapshot as of the
  `last_updated` date; later corrections will land in v1.1.
- **Transliteration is lossy.** See §2 caveat. If you find a Tamil-
  spelling variant the pipeline missed, please file an Issue with
  the affidavit URLs.
- **No 2021 results joined in.** A sibling future release may merge
  the 2021 winning margin per constituency so the "tight seats draw
  more suspects" hypothesis can be tested directly. Out of scope for
  v1.0.

---

## 7. Reproducibility

The scraping + normalization + matching pipeline is being prepared
for release. For v1.0 the CSV is shipped as a point-in-time snapshot;
v1.1 will include the generator scripts (`scripts/scrape_affidavits.py`,
`scripts/normalize.py`, `scripts/match.py`) so the entire output can
be reconstructed from public sources by anyone who wants to audit it.

`scripts/make_chart.py` is already in this release and reproduces the
chart used in the blog post from the CSV alone.

---

## 8. Corrections

Two kinds of Issues are especially welcome:

- **False positives** — a flagged pair that is clearly two different
  people. Include the affidavit links from the ECI portal so the next
  release can add an exclusion.
- **False negatives** — two candidates in the same constituency that
  are obviously the same target name but the pipeline did not pair.
  Usually this is a transliteration variant; include the Tamil /
  Latin spellings involved.

This repository is the public record. Every correction is versioned.
