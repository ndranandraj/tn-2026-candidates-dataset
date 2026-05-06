# How Many of the 329 Dummies Actually Mattered

*By Anand Raj · ndranandraj.com · May 2026*

*Companion post to the [Tamil Nadu 2026 Candidates dataset](candidates-dataset-2026.html) and the [Dummy Candidate analysis](dummy-candidates-2026.html). Numbers in this post are computed by [`pipelines/21_dummy_impact_analysis.py`](https://github.com/ndranandraj/tn-2026-candidates-dataset) and refresh against the official ECI tally.*

*All vote counts use the Indian comma format (last 3 digits, then groups of 2). Margins include the absolute number and the share of total votes polled in the constituency.*

---

Three weeks before polling, I published a list of **329 suspect candidate pairs**: major-alliance nominees who shared a name (exactly or near-exactly) with another candidate in the same constituency. Almost always an independent. The thesis was simple. At least some of these are deliberate vote-splitters, fielded to confuse voters at the EVM and bleed the major candidate's tally.

Today the votes are in. So: **did it work?**

The honest answer is the kind of answer that does not write its own headline. In the cleanest test, the strategy did not move a single seat. In the noisiest test, two razor-thin TVK losses had enough flagged-namesake votes to plausibly cover the margin. Both can be true at once, and which one you treat as the "real" answer depends on how generously you classify a dummy.

What is unambiguous: this was a wave year, and waves drown small mechanics. That, more than anything else, is the story.

---

## The headline number, with two definitions

Of the 329 flagged pairs, **263** had both the major and the suspect actually contest. They were spread across **221** distinct major candidates. **152** of those majors lost their seats.

How many of those losses were "consequential," meaning the dummy votes were at least equal to the margin of defeat?

That depends on how strict the test is.

| Dummy classification used | Consequential losses |
|---|---|
| Strict (only EXACT and NEAR\_FULL name matches counted) | **0** |
| Inclusive (all flagged dummies, including WORD\_MATCH) | **2** |

The strict test is the one I ran in the headline pipeline, and the one I think the data supports for any causal claim. EXACT-tier and NEAR\_FULL-tier dummies are the ones least likely to be coincidence. By that definition, no major candidate lost a seat where engineered name-confusion plausibly covered the gap.

The inclusive test, which throws in WORD\_MATCH dummies (one shared name fragment, often a common Tamil first name like Saravanan or Murugan), produces two cases. Both are TVK losses. Margins are reported in absolute votes and as a percent of total votes polled in that AC.

| Constituency | Major (lost) | Party | Margin (votes) | Margin (% of polled) | Dummies | Combined dummy votes |
|---|---|---|---|---|---|---|
| TIRUKKOYILUR | Vijay R Baranibalaaji | TVK | **285** | **0.13%** | 1 (WORD\_MATCH) | 571 |
| PALANI | Dr. Praveen Kumar M | TVK | **693** | **0.33%** | 3 (1 NEAR, 2 WORD) | 1,057 |

I would not stake a causal claim on either of those. WORD\_MATCH dummies are the noisiest signal in the dataset. A constituency with 200 first-name "Vijays" running across 234 seats will throw up a few of these by chance. But they are also the only two seats in the entire 263-pair tally where the arithmetic comes close to working at all, and both being narrow TVK losses is at least worth flagging. Both seats also have margins under half a percent of polled votes, which is the bottom 1% of margin-percent across the whole dataset.

---

## Why the answer is small, and why that is itself the finding

The most honest read of the zero-and-two number is that 2026 was the wrong year to test the dummy-candidate thesis.

The median dummy in the dataset polled about **200 votes** (174 for EXACT, 210 for NEAR\_FULL, 197 for WORD\_MATCH). The median margin of loss across the 152 lost seats was **27,002 votes**, which is roughly **12-15% of polled votes** in a typical TN AC. The 25th-percentile margin was **9,554 votes**. These are not seats where 200 to 1,000 confused voters tip outcomes. They are seats where one of two things happened: the wave carried the winner home by tens of thousands, or the constituency's traditional base voted as it always has, by tens of thousands.

The strategy needs a close election to bite. 2026 did not have many.

To put a number on it: in only **3 of 152 lost seats** did the major lose by under 1,000 votes (under ~0.5% of polled). In only **15** did they lose by under 5,000 votes (under ~2.5% of polled). The rest ran into a winner who was not winning narrowly.

This is the analyst's caveat I would not let any newsroom strip out. The dummy-candidate strategy did not "fail" in 2026. It ran into a year where margins were too wide for it to matter. In 2016, when AIADMK won several seats by under 1,000 votes (under 0.5%), the same 329 pairs would almost certainly have produced a non-zero count. The mechanism is intact and waiting for the next close election.

---

## By tier

The pre-poll classifier put each pair in one of three buckets: **EXACT** (identical name after normalising prefixes and initials), **NEAR\_FULL** (≥ 0.85 string similarity), and **WORD\_MATCH** (one significant word in common). Here is what each tier polled:

| Tier | Pairs | Median dummy vote count | Pairs in lost seats | Strict-consequential |
|---|---|---|---|---|
| EXACT | 64 | 174 | 30 | 0 |
| NEAR\_FULL | 36 | 210 | 19 | 0 |
| WORD\_MATCH | 163 | 197 | 103 | 0 (2 if loose test) |

EXACT-tier dummies (same name, no etymological wiggle) are the ones most likely to register as engineered confusion rather than coincidence. They polled the fewest votes per pair on average. That is a useful corrective to the assumption that more brazen dummies do more damage. The ones that look most engineered are also, in this dataset, the ones drawing the smallest crowds.

---

## By alliance

| Alliance | Targeted majors | Of whom lost | Strict-consequential | Total flagged-dummy votes against |
|---|---|---|---|---|
| INDIA (DMK-led) | 68 | 46 | 0 | 28,516 |
| NDA (AIADMK-led) | 66 | 48 | 0 | 25,702 |
| TVK | 61 | 32 | 0 (2 in inclusive test) | 19,383 |
| NTK | 26 | 26 | 0 | 6,222 |

A few things stand out.

First, the ruling DMK was the most-targeted alliance, which is the predictable pattern. Spoilers cluster on incumbents. Second, the new party (TVK) attracted 61 dummy pairings, almost as many as the established alliances, despite being a debut force. The strategy was deployed defensively against the wave, not just by the usual operators. Third, the NTK row in this table is not what it looks like. NTK lost all 26 of its targeted seats not because dummies bit deep, but because NTK loses everywhere by construction. That is the entire premise of the [earlier "3 crore votes" piece](tn-elections-story-link-here). I would footnote that row, not interpret it.

The total number of votes that went to suspected dummy candidates across all 263 pairings is roughly **79,823**, or **~80,000**. That is small per seat, large in aggregate, and zero in the column that most matters. It is also, almost certainly, the upper bound of the strategy's footprint. Some unknown share of those 79,823 votes belong to genuine candidates with shared names rather than engineered ones.

---

## The closest the math came to working

Even in a year where dummies did not flip seats, it is worth looking at the cases where the arithmetic came nearest. Listed by ratio of combined flagged-dummy votes to margin of loss. A ratio above 1.0 means the dummies polled more than the gap; under 1.0 means the gap was wider than the dummies.

| Constituency | Major (lost) | Party | Margin (votes) | Margin (% polled) | Dummies | Combined dummy votes | Ratio |
|---|---|---|---|---|---|---|---|
| TIRUKKOYILUR | Vijay R Baranibalaaji | TVK | **285** | **0.13%** | 1 | 571 | **2.00** |
| PALANI | Dr. Praveen Kumar M | TVK | **693** | **0.33%** | 3 | 1,057 | **1.53** |
| KALLAKURICHI | Rajeevgandhi S | ADMK | 798 | 0.32% | 2 | 616 | 0.77 |
| TIRUVANNAMALAI | Arul Arumugam | TVK | 2,455 | 1.12% | 3 | 850 | 0.35 |
| RISHIVANDIAM | Ashok Kumar G | TVK | 4,862 | 1.99% | 4 | 1,212 | 0.25 |

The full sorted list lives in the [interactive dashboard](dummy-candidates-2026.html#nearmiss). Of the top 5 near-misses, **four are TVK losses**. That is not random. TVK's losses by definition skew toward closer races (the wave seats they won were not close at all, so the only TVK losses *to* show up here are the narrow ones). The dummy strategy bites where margins are narrow. In 2026 the narrow margins clustered on TVK's losing column.

A note on TIRUKKOYILUR: TVK's Vijay R Baranibalaaji lost to AIADMK's Palanisamy S by **285 votes, or 0.13% of all votes polled in the constituency**. A single flagged independent named Baranibalaaji-ish (one shared significant word) polled 571 votes. The flag is real, the dummy is real, the gap exists. What we cannot say is whether those 571 voters were confused, sincere, or coincidental. The data shows the door is open; it does not show anyone walking through it.

---

## What this is not

A **causal** claim. Dummy votes are not "stolen" votes. The voters who voted for an unknown `R. Saravanan` in some Salem-belt constituency may have been confused by ballot-paper proximity, making a deliberate protest vote against both alliances, abstaining if the dummy had not been on the EVM, or genuine local supporters of an actual `R. Saravanan`. We cannot separate those four populations with the data the ECI publishes.

A **complete** account. Tamil Nadu has a finite stock of common names. There were 200+ "Saravanans" contesting in 2026 alone. The dataset cannot tell you which dummies were strategic and which were coincidence. What it can tell you is the upper bound of the strategy's footprint, and what that footprint converted to in seats.

---

## What "3 crore votes that elected nobody" looks like, three weeks later

In [the earlier post](tn-elections-story-link-here) I argued that NTK's strategy of running a candidate everywhere was the most honest illustration of how Tamil Nadu's elections actually work. Millions of votes that do not move a single seat.

The dummy-pair data is the same arithmetic, lower in the food chain. A few hundred votes per constituency, scattered across 263 pairs, that came within striking distance of mattering in two TVK seats and did not actually flip any.

The 2026 cycle is, in that sense, the cleanest possible illustration of TN's electoral asymmetry. The same vote that elected nobody at the bottom (NTK's 19,72,537 votes statewide, **4.00% vote share, zero seats**) sat alongside the same vote that elected a state government at the top (TVK's 1,72,26,209 votes, **34.92% vote share, 108 seats and counting**). The roughly 80,000 flagged-dummy votes are a third example of the same asymmetry. Citizens cast them, they were counted, they did not change anything. It is the structural feature of first-past-the-post in a fragmented field.

The dummy strategy is waiting for a year where margins are narrow. 2026 was not it.

---

## Methodology and reproducibility

All analysis runs from the open dataset and the analysis pipeline.

- Raw flagged pairs: [`dummy-pairs-2026.csv`](data/dummy-pairs-2026.csv)
- Per-pair joined results: [`dummy_impact_2026.csv`](../processed/dummy_impact_2026.csv) (generated by pipeline 21)
- Per-AC aggregation: [`dummy_impact_by_ac.csv`](../processed/dummy_impact_by_ac.csv)
- Near-miss list with margin-percent (dashboard sidecar): [`dummy_near_misses_2026.json`](data/dummy_near_misses_2026.json)
- Code: [`pipelines/21_dummy_impact_analysis.py`](https://github.com/ndranandraj/tn-2026-candidates-dataset)

The candidate roster, dummy-pair detection logic, and known data-quality caveats are documented in the [dataset README](data/README.md). If you want to run it yourself, the pipeline depends only on `psycopg2` and stdlib. No pandas, no scraping required. It takes about two seconds to run.

The two consequential-test definitions matter. The strict test (EXACT and NEAR\_FULL only) is the one to use for any claim about whether the dummy strategy worked. The inclusive test (all flagged dummies including WORD\_MATCH) is the one to use to find seats worth investigating qualitatively. Both numbers belong in the analysis. Only one belongs in the headline.

Margin percentages are computed as `margin / total_votes_polled_in_AC * 100`.

If you find a pair I missed, or a case study I should highlight, the data is open. Pull request welcome.

---

*Released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Attribution: Anand Raj, ndranandraj.com, May 2026.*
