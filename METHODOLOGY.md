# Methodology

How rows become a "namesake group," how the 77-constituency headline was
arrived at, and the guardrails against false positives.

## 1. Data acquisition

Two sources, both public:

1. **2026 filings** — Form 26 affidavits from the ECI affidavit portal,
   one per candidate. Scraped after the final withdrawal date so
   `is_primary_candidate` reflects the ballot, not the initial filing.
2. **2021 results** — ECI Form 20 (booth-level PDFs). Parsed and
   aggregated to constituency totals. `margin_pct_2021` is
   `(winner_votes − runner_up_votes) / total_valid_votes × 100`.

No private databases, no leaked documents, no paid data sources.

## 2. Name normalization

A candidate name filed as "R. Kumar" and another filed as "R Kumar M." and a
third filed as "ர.குமார்" (Tamil) are, to a human eye, plausibly the same
target. To group them programmatically:

1. **Transliterate Tamil → Latin** using the ISO 15919 convention (library:
   `indic-transliteration`).
2. **Lowercase** everything.
3. **Strip punctuation and single-letter initials** that don't match a full
   first-name elsewhere in the group (so "R. Kumar" and "Ramesh Kumar"
   collapse to the same normalized form only if "R" plausibly expands to
   "Ramesh").
4. **Drop honorifics** (Dr., Mr., Tmt., Thiru., etc.) — maintained in
   `data/honorifics.txt`.
5. **Collapse whitespace**.

The output is `candidate_name_normalized`. The script is
`scripts/normalize_name.py`.

## 3. Grouping rule

Two or more 2026 candidates in the **same constituency** with identical
`candidate_name_normalized` → one namesake group, assigned a stable ID of
the form `NS-{constituency_code}-{a,b,c…}`.

Groups are flagged for manual review when:

- Group size ≥ 2, AND
- At least one member has a major-alliance ticket (DMK-led, AIADMK-led,
  or BJP-NDA), AND
- `margin_pct_2021 < 5` percentage points.

Groups passing manual review (checks against affidavit address, age,
father's name, and occupation to rule out genuine distinct individuals)
land in the dataset with `is_primary_candidate` set on the
alliance-ticketed member.

## 4. The "77" number

77 is the count of **constituencies** (not candidates) where:

- ≥ 1 namesake group survived manual review, AND
- The 2021 margin was < 5 percentage points.

The number is sensitive to the 5-point threshold. At 3 points it drops to
41. At 10 points it expands to 114. The blog post explains why 5 is the
operating threshold (it covers the "swing" band where a few hundred split
votes historically flipped outcomes in TN).

## 5. What this dataset does **not** establish

- **Intent.** Two people can be named R. Kumar in a constituency by pure
  coincidence. The dataset flags statistical patterns; it does not prove
  any individual candidate was filed as a dummy. Use local reporting,
  affidavit analysis, and court records for individual cases.
- **Party responsibility.** A namesake filing does not, on its own, imply
  that a party orchestrated it. Some dummies are self-motivated
  publicity seekers; others are paid proxies; others are exactly who
  they say they are.
- **Causation.** We do **not** claim these filings changed 2021 outcomes.
  The 2021 numbers are shown as context — tight-margin seats are where
  the tactic has the highest expected value for the instigator.

## 6. Known limitations

- **Transliteration is lossy.** Distinct Tamil names can share a
  normalized Latin form. All groups of size ≥ 2 went through manual
  review for this reason; if you spot a remaining false positive, please
  file an Issue.
- **Withdrawals are a moving target.** Some candidates withdrew between
  the filing deadline and the ballot finalization. The release snapshot
  is as of the last withdrawal date. Later corrections go in v1.1.
- **Address data is not published.** Candidate addresses appear on
  Form 26 affidavits and were used internally to distinguish
  genuinely-different people who happened to share a normalized name.
  We are not republishing private addresses in the open dataset. The
  resulting `is_primary_candidate` flag therefore reflects a judgment
  that outside reviewers cannot fully audit from this repo alone — you
  can re-run the address check yourself from the public ECI portal.

## 7. Reproducibility

Every number in the blog post is computed by a script in `scripts/`:

- `scripts/normalize_name.py` — the normalization pipeline
- `scripts/group_namesakes.py` — applies the grouping rule
- `scripts/count_77.py` — computes the 77-constituency figure with
  configurable margin threshold
- `scripts/make_scatter.py` — the visualisation for r/dataisbeautiful

Run `make all` (Makefile shipped in v1.0) to rebuild the headline figures
and the scatter plot from scratch.
