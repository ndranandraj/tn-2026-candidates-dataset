# TVK 233: A Debut, Mapped

*By Anand Raj · ndranandraj.com · May 2026*

*Companion post to the [Tamil Nadu 2026 Candidates dataset](candidates-dataset-2026.html). The interactive map of TVK's per-constituency performance lives at [tvk-debut-2026.html](tvk-debut-2026.html). Numbers below are computed by [`pipelines/23_tvk_debut_analysis.py`](https://github.com/ndranandraj/tn-2026-candidates-dataset) and the new regional roll-up at [`pipelines/25_tvk_regional.py`](https://github.com/ndranandraj/tn-2026-candidates-dataset).*

*All vote counts use the Indian comma format (last 3 digits, then groups of 2). Margins include the absolute number and the share of total votes polled in the constituency.*

---

Of the 234 constituencies in Tamil Nadu's 2026 Legislative Assembly election, Vijay's Tamilaga Vettri Kazhagam fielded a candidate in 233. The one they skipped is **Edappadi**.

That is not random. AC #88 is the home constituency of **Edappadi K. Palaniswami**, sitting general secretary of the AIADMK, former Chief Minister, and the alliance face of the NDA in this state. Vijay's debut campaign promised to take on the establishment "everywhere." The roster says: everywhere except the AIADMK chief's home seat.

The data tells you the rest.

**TVK won 108 of 233 contested seats.** They came second in 72 more, third in 51, and fourth or lower in only 2. They polled **1.72 crore votes (1,72,26,209)**, **34.92% of the statewide vote**, and converted that into **46.15% of the Assembly**. That conversion ratio (1.32 seats per unit of vote share) is the highest of any party with more than 5 seats this cycle, and it is the single most important number for understanding what happened on May 4.

But "TVK won" hides a story that gets sharper region by region. The wave was not uniform. It was a tsunami in Chennai and a ripple in the Cauvery delta, and the gap between those two facts is what the rest of this post is about.

---

## The seat-vs-vote table everyone should read

Total votes polled across all 234 ACs: **4.93 crore (4,93,24,121)**.

| Party | Votes polled | Vote share | Seats | Seat share | Efficiency (seat % ÷ vote %) |
|---|---|---|---|---|---|
| **TVK** | **1,72,26,209** | **34.92%** | **108** | **46.15%** | **1.32** |
| DMK | 1,19,29,144 | 24.19% | 59 | 25.21% | 1.04 |
| AIADMK | 1,04,62,146 | 21.21% | 47 | 20.09% | 0.95 |
| NTK | 19,72,537 | 4.00% | 0 | 0.00% | 0.00 |
| INC | 16,61,312 | 3.37% | 5 | 2.14% | 0.63 |
| BJP | 14,67,024 | 2.97% | 1 | 0.43% | 0.14 |
| PMK | 10,70,745 | 2.17% | 4 | 1.71% | 0.79 |
| IUML | 1,42,465 | 0.29% | 2 | 0.85% | 2.96 |
| CPI(M) | 2,93,817 | 0.60% | 2 | 0.85% | 1.43 |
| CPI | 3,26,488 | 0.66% | 2 | 0.85% | 1.29 |
| Others (DMDK, AMMK, VCK, IND) | ~17 lakh | ~3.5% | 4 | 1.71% | varied |

Two numbers worth circling. TVK's 1.32 is the highest among major parties because the opposition was fragmented in exactly the constituencies TVK won. BJP's 0.14 is the inverse story: nearly 15 lakh votes spread thinly across 33 candidates, none of whom finished first except in one seat. NTK's zero is its own genre, the same one I covered in [the "3 crore votes" piece](tn-elections-story-link-here): nearly 20 lakh voters, no MLAs.

A debut party at 1.32 efficiency is unusual. It means TVK did not win where it had the most absolute support. It won where the rest of the field was most divided. That is the structural reading. The wave is real, and the wave is also amplified by first-past-the-post arithmetic.

---

## Before May 4: who TVK fielded

The roster itself is the most revealing thing about a new party. Compare three rosters across the same dataset:

| Metric | TVK | DMK | AIADMK |
|---|---|---|---|
| Candidates fielded | **233** | 176 | 172 |
| Median age | **44** | 57 | 58 |
| Median declared assets | **₹85 lakh** | ₹2.6 crore | ₹2.2 crore |
| Women candidates | 24 (10.3%) | 20 (11.4%) | 20 (11.6%) |
| Master's-degree holders | **43** | 32 | 24 |

TVK candidates are, on average, a generation younger than the people they were trying to displace, three times less wealthy, and the most educated of the three rosters. It is a recognisable profile: first-time politicians, urban-leaning, professional class, drawn from a younger fanbase. Whether that translates into votes is what May 4 actually answered.

---

## What May 4 did with that roster

233 of 234 contested. They polled **1,72,26,209 votes (1.72 crore)**, about **34.92%** of the state's total. The median TVK candidate took **33.6%** of their constituency's vote. The 90th-percentile candidate, **44.9%**.

**They won 108 seats.**

Finish-position breakdown:

| Where TVK landed | ACs | Share of contested |
|---|---|---|
| 1st (won) | 108 | 46.4% |
| 2nd | 72 | 30.9% |
| 3rd | 51 | 21.9% |
| 4th or lower | 2 | 0.9% |

Translation: in **180 of 233 seats** (77.3%) TVK was either the winner or the runner-up. There is almost no part of Tamil Nadu where TVK did not register as a top-two force. That is the most basic measure of "consolidation" for a debut party, and the number is unusually high.

Across the 108 wins, the **median winning margin was about 8.93% of the votes polled in that constituency** (median absolute margin around 17,000 votes). The 10th-percentile winning margin was just 1.27% of polled votes (these are the seats that hung on a few hundred votes); the 90th-percentile winning margin was 22.05% (these are the Chennai metro sweep-seats). That spread is the story: TVK won by huge margins where the wave was concentrated and by photo-finish margins where it was contested.

The full per-constituency map is at **[tvk-debut-2026.html](tvk-debut-2026.html)**. Gold for seats they won, purple for second place, fading purple as they finish lower.

---

## The Chief Minister lost his seat

Of 234 sitting MLAs from the 2021 Assembly, only **38 retained their seat** in 2026. **140 sitting MLAs did not contest** their same seat at all (retired, denied tickets, or shifted constituency). The remaining **56 incumbents defended and lost**. **37 of those 56 lost directly to TVK** — including the sitting Chief Minister.

M.K. Stalin lost Kolathur to V.S. Babu of TVK by 8,795 votes. Stalin (age 72, ₹6.01 crore in assets, Bachelor's degree) was beaten by V.S. Babu (age 75, ₹36.38 lakh in assets, 8th-grade education) on his first electoral attempt. Stalin had won the same seat in 2021 by 70,384 votes.

The 12 most decisive flips, ranked by 2021 winning margin:

| 2026 AC | Incumbent (2021 winner) | Party | 2021 margin | 2026 margin | Lost to | Now in |
| :--- | :--- | :--- | ---: | ---: | :--- | :--- |
| AC 5 POONAMALLEE | Krishnaswamy A | DMK | 94,110 | 72,740 | Prakasam R | TVK |
| **AC 13 KOLATHUR** | **M.K. Stalin (CM)** | **DMK** | **70,384** | **8,795** | **V.S. Babu** | **TVK** |
| AC 214 THOOTHUKKUDI | P. Geetha Jeevan | DMK | 50,310 | 37,731 | Srinath | TVK |
| AC 142 THIRUVERAMBUR | Anbil Mahesh Poyyamozhi (min.) | DMK | 49,697 | 8,705 | Vijayakumar (A) Navalpattu | TVK |
| AC 189 MADURAI EAST | Moorthy P | DMK | 49,604 | 16,547 | Karthikeyan S | TVK |
| AC 28 ALANDUR | T.M. Anbarasan | DMK | 40,571 | 29,609 | M. Harish | TVK |
| AC 27 SHOZHINGANALLUR | S. Aravindramesh | DMK | 35,405 | 96,780 | ECR P. Saravanan | TVK |
| AC 193 MADURAI CENTRAL | Palanivel Thiaga Rajan (former FM) | DMK | 34,176 | 19,128 | Madhar Badhurudeen | TVK |
| AC 116 SULUR | Kandasamy V.P. | AIADMK | 31,932 | 4,790 | Nm. Sukumar | TVK |
| AC 7 MADURAVOYAL | Ganapathy K | DMK | 31,721 | 61,509 | Rhevanth Charan | TVK |
| AC 183 ARANTANGI | Ramachandran T | INC | 30,893 | 10,062 | Mohamed Farvas J | TVK |
| AC 195 THIRUPARANKUNDRAM | Rajanchellappa V.V. | AIADMK | 29,489 | 41,553 | Nirmalkumar R | TVK |

The wider pattern is a generational reset. The DMK column reads as the elimination of a generation of frontline cabinet talent in one cycle.

---

## The youngest, most educated assembly Tamil Nadu has elected

The 234 winners are the youngest and most-educated cohort Tamil Nadu has elected in living electoral memory. Median age of the new assembly is 52. TVK's median MLA age is **44**, against 59 for DMK and 57 for AIADMK.

| Metric | TVK (108) | DMK (59) | AIADMK (47) |
| :--- | ---: | ---: | ---: |
| Median age | **44** | 59 | 57 |
| Youngest winner | **28** | 35 | 29 |
| MLAs under 40 | **35** (32%) | 2 (3%) | 3 (6%) |
| Women MLAs | **13** (12%) | 0 (0%) | 5 (11%) |
| Postgraduate / doctorate | **18** (17%) | 13 (22%) | 3 (6%) |
| Graduate or higher | 58 (54%) | 38 (64%) | 18 (38%) |
| Median declared assets | **₹1.09 crore** | ₹1.91 crore | ₹2.15 crore |

The 5 youngest MLAs in the new assembly:

| Age | Name | Constituency | Party | Education |
| ---: | :--- | :--- | :--- | :--- |
| 28 | Kamali S | Avanashi | TVK | Master's Degree |
| 28 | Sabari Iyngaran G | Periyakulam | TVK | Master's Degree |
| 29 | Dr. Dhilipan Jaishankar | Sankarankovil | AIADMK | Bachelor's Degree |
| 30 | Rhevanth Charan | Maduravoyal | TVK | Not declared |
| 30 | Sabarinathan R | Virugampakkam | TVK | Bachelor's Degree |

DMK and AIADMK combined have 5 MLAs under 40 across 106 seats. TVK has 35 under 40 across 108. That is a generational replacement happening inside one election cycle. TVK is also the only major party with women representation above token levels — 13 of its 108 MLAs are women, against zero for DMK and 5 for AIADMK. The new assembly is 9.4% women, up from roughly 5% in 2021.

---

## The anatomy of TVK's results: 1st, 2nd, 3rd

A finish-position headcount tells you how many seats. The interesting question is *who else was in the room*.

### When TVK won (108 seats): margin distribution

| Winning margin | Seats | Share of TVK wins |
| :--- | ---: | ---: |
| under 500 votes | 2 | 1.9% |
| 500 to 2,000 | 7 | 6.5% |
| 2,000 to 5,000 | 9 | 8.3% |
| 5,000 to 10,000 | 12 | 11.1% |
| 10,000 to 25,000 | 44 | 40.7% |
| over 25,000 | 34 | 31.5% |

Eight closest TVK wins:

| Constituency | TVK candidate | Margin | Margin % | Beat |
| :--- | :--- | ---: | ---: | :--- |
| TIRUPPATTUR (AC 192) | Seenivasa Sethupathy R | 1 | 0.00% | DMK |
| KUMBAKONAM | Vinoth | 679 | 0.33% | DMK |
| CUMBUM | Jeganathmishra Pla | 751 | 0.36% | DMK |
| KALLAKURICHI | Arul Vignesh C | 798 | 0.32% | ADMK |
| SRIVAIKUNTAM | Saravanan G | 1,186 | 0.67% | ADMK |
| MANAMADURAI | Elangovan D | 1,208 | 0.58% | DMK |
| MANAPPARAI | R Kathiravan | 1,426 | 0.59% | ADMK |
| USILAMPATTI | Vijay M | 1,805 | 0.81% | ADMK |

Eight biggest TVK wins (by absolute margin):

| Constituency | TVK candidate | Margin | Margin % | Beat |
| :--- | :--- | ---: | ---: | :--- |
| SHOZHINGANALLUR | Ecr P Saravanan | 96,780 | 21.64% | DMK |
| MADAVARAM | M L Vijayprabhu | 94,985 | 26.24% | DMK |
| AVADI | R Ramesh Kumar | 76,311 | 22.05% | DMK |
| SALEM (WEST) | Lakshmanan S | 74,867 | 31.94% | PMK |
| POONAMALLEE | Prakasam R | 72,740 | 23.55% | DMK |
| ALANDUR | T M Anbarasan | 72,191 | 27.60% | NTK |
| TIRUPPUR (NORTH) | V Sathyabama | 69,992 | 26.57% | ADMK |
| MADURAVOYAL | Rhevanth Charan | 61,509 | 20.94% | DMK |

### When TVK came 2nd (72 seats)

Gap to winner:

| Gap to winner | Seats | Share |
| :--- | ---: | ---: |
| under 2,000 | 12 | 16.7% |
| 2,000 to 5,000 | 14 | 19.4% |
| 5,000 to 10,000 | 18 | 25.0% |
| 10,000 to 25,000 | 22 | 30.6% |
| over 25,000 | 6 | 8.3% |

When TVK came 2nd, who actually won:

| Winner | Seats |
| :--- | ---: |
| DMK | 35 |
| ADMK | 24 |
| INC | 4 |
| IUML | 2 |
| PMK | 2 |
| CPI(M) | 2 |
| BJP | 1 |
| DMDK | 1 |
| CPI | 1 |

When TVK came 2nd, who got pushed to 3rd:

| Pushed to 3rd | Seats |
| :--- | ---: |
| ADMK | 30 |
| DMK | 18 |
| BJP | 10 |
| DMDK | 4 |
| PMK | 3 |
| INC | 3 |
| AMMK | 2 |
| VCK | 1 |
| CPI(M) | 1 |

The ADMK-30 vs DMK-18 split is the cleanest single number for the "TVK ate AIADMK's lunch" thesis. Across the 72 seats where TVK came 2nd, AIADMK was displaced from contention 30 times versus DMK only 18 times.

Eight closest 2nd-place misses:

| Constituency | TVK candidate | Gap | Gap % | Lost to | 3rd was |
| :--- | :--- | ---: | ---: | :--- | :--- |
| TIRUKKOYILUR | Vijay R Baranibalaaji | 285 | 0.13% | ADMK | DMK |
| KULITHALAI | G Balasubramani | 579 | 0.28% | DMK | ADMK |
| PALANI | Dr Praveen Kumar M | 693 | 0.33% | ADMK | CPI(M) |
| KOVILPATTI | Balasubramanian S | 843 | 0.43% | DMK | ADMK |
| VIKRAVANDI | Vijai Vadivel A | 910 | 0.43% | PMK | DMK |
| UDHAGAMANDALAM | Ibrahim R | 976 | 0.66% | BJP | INC |
| PAPANASAM | Azarudeen Uduman Ali | 1,065 | 0.51% | IUML | ADMK |
| DINDIGUL | Nazeer Raja G | 1,131 | 0.53% | DMK | ADMK |

### When TVK came 3rd (51 seats)

Gap to winner (notice: zero seats within 2,000 votes):

| Gap | Seats | Share |
| :--- | ---: | ---: |
| under 2,000 | 0 | 0.0% |
| 2,000 to 5,000 | 3 | 5.9% |
| 5,000 to 10,000 | 8 | 15.7% |
| 10,000 to 25,000 | 21 | 41.2% |
| over 25,000 | 19 | 37.3% |

Who won when TVK was 3rd: ADMK 22, DMK 22, PMK 2, VCK 2, CPI 1, INC 1, AMMK 1.

Who was 2nd when TVK was 3rd: DMK 23, ADMK 19, BJP 4, PMK 2, AMMK 1, VCK 1, INC 1.

The 22-22 ADMK-DMK split says: in seats where TVK was not really in contention, the older DMK-AIADMK pattern persisted intact. The wave failed to reach those constituencies.

---

## Where the wave actually landed: the regional read

The headline 108 seats hides nine regional stories. I grouped the 234 ACs into nine standard political-geography buckets (Chennai metro and suburbs, North, Northeast Coast, Krishnagiri-Dharmapuri, Kongu, Central, Cauvery Delta, Madurai region, Deep South) and computed TVK's strike rate, vote share, median winning margin, and seat-share-vs-vote-share gap in each.

| Region | ACs | TVK won | Strike rate | TVK vote share | Median TVK win margin (votes) | Median TVK win margin (% of polled) |
|---|---|---|---|---|---|---|
| **Chennai & Suburbs** | 37 | **32** | **86.5%** | 44.7% | 34,463 | 17.08% |
| **Madurai Region** | 21 | 11 | 52.4% | 35.0% | 16,547 | 6.09% |
| **Kongu (West)** | 46 | 24 | 52.2% | 33.8% | 14,942 | 7.13% |
| **Central** | 23 | 10 | 43.5% | 33.5% | 12,716 | 6.13% |
| **North** | 21 | 9 | 42.9% | 33.9% | 6,647 | 3.32% |
| **Deep South** | 37 | 15 | 40.5% | 32.6% | 11,414 | 5.79% |
| **Krishnagiri Belt** | 11 | 3 | 27.3% | 30.2% | 18,844 | 8.19% |
| **Cauvery Delta** | 18 | 2 | 11.1% | 30.3% | 8,817 | 4.43% |
| **Northeast Coast** | 20 | 2 | 10.0% | 29.5% | 8,158 | 4.24% |

The first row is the punch-above-weight story. **Chennai and its immediate suburbs (Chennai, Tiruvallur, Kanchipuram) account for 32 of TVK's 108 wins from only 37 ACs.** A 86.5% strike rate is what a wave looks like at full force. The 17.08% median margin (about a sixth of all votes polled) is what a sweep looks like in the margin column. Combined with a 44.7% vote share in the same region, this is essentially a three-cornered fight collapsing into a one-corner sweep.

The bottom two rows are the punch-below-weight story. **In the Cauvery Delta and the Northeast Coast (combined 38 ACs), TVK won only 4 seats.** Both are DMK fortresses (Cauvery delta is the cultural-political home of the Dravidian movement) and both rejected the wave more decisively than any other region. The TVK wins there were also tighter (median margin 4-4.5% of polled votes) than the Chennai and Kongu wins.

The Kongu read is the most interesting middle case. 46 ACs, 24 TVK wins, 14 AIADMK wins, 7 DMK wins. AIADMK's traditional heartland did flip in part, but it also did not collapse. Salem, Coimbatore, Tiruppur, Erode, and Namakkal are now genuinely three-way territory in a way they were not in 2021.

---

## Where TVK punched above its weight

The "punch above weight" metric is simple: did the region give TVK more seats than its statewide vote share would predict?

If TVK had won uniformly at its 34.9% statewide share with no FPTP amplification, they would have won roughly 81 seats (35% of 234). They actually won 108. The 27-seat gap is concentrated in five regions:

1. **Chennai & Suburbs**: +18.5 seats over uniform expectation. Wave at full force.
2. **Kongu**: +8.4 seats. AIADMK incumbents got knocked off their perches without DMK consolidating a counter-vote.
3. **Madurai Region**: +3.6 seats. Vijay's home turf is Tamil Nadu's south-central belt, and the early polling showed strong cinema-fanbase numbers here. The result tracks.
4. **Deep South**: +2.9 seats. Distribution mostly thanks to seats in Tirunelveli, Tenkasi, and Kanniyakumari that flipped from a fragmented DMK-NDA-INC field.
5. **Central**: +2.3 seats.

The amplification came from the same mechanism in every case: a fragmented opposition. TVK's median winning vote share statewide was about 45-50%. In the regions where TVK punched above weight, the second-place candidate typically polled in the 30s, and the third in the 20s. That is the FPTP gift, and it is also the FPTP risk for 2031, when the opposition will have had time to consolidate.

---

## Where TVK underperformed

Three regions returned fewer seats than the wave should have produced.

**Cauvery Delta (Thanjavur, Tiruvarur, Nagapattinam)**: 18 ACs, 2 TVK wins. DMK won 9, AIADMK 2, INC 1, CPI 1, CPI(M) 1, IUML 1, AMMK 1. This region is the political heart of the Dravidian movement. It has voted DMK in 2011, 2016, 2021, and again in 2026. Vijay's coalition does not yet reach it. **Out of 24 INDIA strongholds (seats DMK-bloc won three Assemblies running) statewide, TVK flipped only 4. Three of those 4 were not in the delta.** The delta itself stayed intact.

**Northeast Coast (Cuddalore, Villupuram)**: 20 ACs, 2 TVK wins. DMK won 7, AIADMK 6, PMK 2, VCK 2, plus a single INC and a small fraction outside the majors. PMK's 4 statewide wins are concentrated here. This is its caste-base region. The complex three-way (DMK, AIADMK, PMK, plus VCK in reserved seats) absorbed the TVK wave more effectively than any other geography in the state.

**Krishnagiri Belt**: 11 ACs, 3 TVK wins. Small region, smaller dataset, but the underperformance is real. AIADMK won 5, DMDK held 1, CPI(M) held 1, DMK 1, PMK 1. This is one of the only regions where DMDK still has a base.

The honest read on these three regions: TVK's vote share floor is real (29-30% even in its worst regions, which is more than DMK or AIADMK got *anywhere* outside their best regions). But vote share floors do not win seats in three- and four-cornered races. The 2031 question is whether TVK can convert 30% floors into 35-40% to start winning these regions, or whether the floor is the ceiling and the rest of the state is the wave.

---

## The stronghold-flip asymmetry

The cleanest single number in the analysis is this:

| Stronghold type (won 2011 + 2016 + 2021 by same camp) | Total | Flipped by TVK | Held |
|---|---|---|---|
| **NDA strongholds (AIADMK-led)** | 46 | **20 (43.5%)** | 26 |
| **INDIA strongholds (DMK-led)** | 24 | 4 (16.7%) | 20 |

TVK ate dramatically more deeply into AIADMK's fortress than DMK's. Of the 20 NDA strongholds TVK flipped, **15 are in the Kongu belt**: Salem (West and South), Tiruppur (North), Kavundampalayam, Thirupparankundram (technically Madurai), Palladam, Arakonam, Coimbatore North, Kilvaithinankuppam, Gobichettipalayam, Avanashi, Madurai West, Kinathukadavu, Mettupalayam, Kumarapalayam. If you wanted a single sentence to summarise TVK's 2026: *the wave broke AIADMK's western Tamil Nadu base, while DMK's delta and southern coast held.*

The second-place data confirms this from another angle. In the 72 seats where TVK came 2nd, the candidate pushed to 3rd was AIADMK 30 times and DMK 18 times. Even in seats TVK did not win, they were more likely to have displaced AIADMK from contention than DMK. This is the "TVK ate AIADMK's lunch" thesis at scale.

---

## Vijay personally: the cleanest performance in the dataset

Vijay contested two seats and won both with majority vote shares. Margins are reported in absolute votes and as a percentage of total votes polled in the constituency.

| Seat | TVK vote share | Margin (votes) | Margin (% of polled) | Runner-up |
|---|---|---|---|---|
| **PERAMBUR (AC 5)** | **58.89%** | **53,715** | **26.28%** | R.D. Shekar (DMK) |
| **TIRUCHIRAPALLI EAST (AC 141)** | **50.07%** | **27,416** | **15.02%** | S. Inigo Irudayaraj (DMK) |

The Perambur result is the more important of the two. Perambur is a Chennai seat with a DMK history. Vijay won it with **58.89% of the vote** and a margin of **53,715 votes (26.28% of all votes polled in the seat)** in a year where his party's median candidate took 33.6%. That is a personal-vote premium of roughly 25 percentage points over the party baseline, in a constituency where the major opposition was DMK rather than a fragmented field. As a measure of personal political capital it is hard to beat. The closest comparison in this dataset is M.K. Stalin in his home seat (62.7% in 2021), and Vijay was on his first electoral attempt.

The Tiruchirappalli East result is the same story at smaller magnitude: a DMK fight in central Tamil Nadu, won at exactly the 50% mark with a 15.02% absolute margin.

What this tells you is that Vijay's *personal* coalition reaches further than his party's, and reaches into DMK strongholds rather than only AIADMK ones. Whether the party can transfer that to candidates without his name on the ballot is the 2031 test.

---

## Edappadi: the seat that wasn't fought

Three things are true about TVK's decision to skip Edappadi.

First, they contested every other AIADMK heavyweight's home seat. O. Panneerselvam's Bodinayakanur, P. Viswanathan's Melur, EPS's lieutenants in Salem and Tiruchengode all had TVK candidates. Only Edappadi itself was left untouched.

Second, AIADMK won Edappadi in 2026 by a substantial margin, with EPS taking the bulk of the vote. The seat would almost certainly have stayed AIADMK regardless of who TVK fielded. So the decision did not change a result.

Third, the decision was made before nominations closed. There was no withdrawal, no rejected paper. TVK simply did not file in AC #88.

Read that as you wish: strategic deference, alliance arithmetic at the margins, a calculation that EPS in his fortress was a fight not worth picking. It is the most interesting single data point in TVK's 2026 ledger, and it is one that no aggregate metric will surface.

---

## What this is, and isn't

**Is**: a clean numerical accounting of where a brand-new party landed on its first electoral attempt. Younger candidates, much less wealthy than the major-party rosters, slightly more educated. 108 seats won out of 233 contested, with a regional concentration in Chennai metro and Kongu and a regional ceiling in the Cauvery delta and Northeast Coast. A vote-share-to-seat-share efficiency of 1.32, the highest among parties with more than 5 seats. A personal performance from Vijay that breaks the party's regional pattern by winning DMK seats outright with margins above a quarter of polled votes.

**Isn't**: a verdict on whether TVK is a "real" force or a "spoiler." That is journalist's work, not a chart's. The data shows a party that pulled high single-digit to low double-digit shares in many places, took 108 seats, broke 20 NDA strongholds, and did not break the DMK delta. What that means for 2029 (Lok Sabha) and 2031 (next Assembly) depends on whether DMK and AIADMK consolidate their opposition in the regions where TVK punched above weight, and whether Vijay's personal vote remains transferable to other candidates.

---

## What it means for 2031

The structural risk for TVK is the same structural advantage they exploited in 2026: FPTP arithmetic is unstable in fragmented fields. TVK won 108 seats with a 34.9% vote share. If by 2031 either of two things happens, that conversion ratio will fall.

The first is opposition consolidation. If DMK and AIADMK find a way to not split the anti-TVK vote in the Kongu belt and the Chennai suburbs, TVK's 86.5% strike rate in Chennai metro and 52.2% in Kongu will compress, possibly sharply. TVK's Chennai share is 44.7%, which is high but not unbeatable in a two-cornered race.

The second is the personal-vote transfer problem. Vijay's 58.89% in Perambur is not the party's. The 33.6% median candidate is the party's. If candidate-level results in 2031 are closer to that median, TVK becomes a 30-35% party with reduced FPTP amplification, and the seat count compresses toward its vote share rather than away from it.

Both of those are 2031 risks, not 2026 facts. The 2026 fact is 108 seats, a regional map that is sharper in places than the headline suggests, and a debut performance that is among the strongest by any new party in Tamil Nadu's electoral history.

---

## Methodology

The roster used here is the canonical [4,023-candidate dataset](candidates-dataset-2026.html). Results are loaded by [`pipelines/11_load_2026_results.py`](https://github.com/ndranandraj/tn-2026-candidates-dataset) from the ECI tally. Per-constituency analysis runs from [`pipelines/23_tvk_debut_analysis.py`](https://github.com/ndranandraj/tn-2026-candidates-dataset). The new regional roll-up reads `processed/tvk_per_ac.csv` and joins to the district mapping in `sql/03_constituency_district_map.sql`, then groups by the nine political-geography buckets defined above. Margin percentages are computed as `margin / total_votes_polled_in_AC * 100`. All sidecar data files for the dashboard are in [`dashboard/data/`](data/).

The "consequential" definition (used in the seat-by-seat note) is intentionally minimal: TVK candidate's vote count ≥ the margin between the actual winner and runner-up in that constituency. It does **not** assume vote transfer.

The map (Leaflet + the existing TN constituency GeoJSON) joins per-AC results via the official ECI AC number. Each polygon's color comes from TVK's finish position; hover for candidate name, vote count, share, and the actual winner.

Known caveats, including the C. Joseph Vijay duplicate filing in Perambur and Tiruchirappalli East and the AC 50 (TIRUPATTUR) incomplete-runner-up issue that affects one of the displayed margins, are documented in the [dataset README](data/README.md).

---

*Released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Suggested citation: Anand Raj, "TVK 233: A Debut, Mapped." ndranandraj.com, May 2026.*
