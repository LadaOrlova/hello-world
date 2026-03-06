# Decision Log — PR Draft: How to Find Product-Market Fit Fast — and Pivot the Right Way

## [STAGE 0.4] Word budget check
**Context:** 21 theses (6 author + 15 team) for a 1000-2000 word article. Minimum needed: ~4,010 words.
**Options:** (1) Proceed with all 21 as separate sections (impossible), (2) Group into 5 sections covering all A theses + best N theses, (3) Increase word limit, (4) Fewer sections.
**Decision:** Group into 5 sections, covering all 6 author theses + 12 best team theses. Drop N7 (security risks) and N14 (AI rollback).
**Rationale:** All author theses preserved. Team theses folded as supporting evidence. N7/N14 are domain-specific edge cases, least central to the PMF narrative.
**Trade-off:** N7 and N14 dropped entirely. Some depth sacrificed per section due to tight budget (~300 words/section avg).

## [STAGE 0.5] Section groupings
**Context:** Need to map 19 theses into 5 coherent sections.
**Decision:**
- Section 1 "The Speed Trap": A1 + N5 + N6 + N4
- Section 2 "Your Product Is Already Dead": A3 + A6
- Section 3 "Find the Riskiest Assumption First": A5 + N15 + N13
- Section 4 "The Hypothesis Factory OS": A4 + N8 + N9 + N10 + N12
- Section 5 "Don't Trust Average Metrics": A2 + N2 + N3 + N1 + N11
**Rationale:** Follows the logical flow: problem (speed trap) -> mindset shift (idea is dead) -> method (riskiest assumption) -> system (factory OS) -> diagnostic (metrics/cohorts). Each A thesis anchors a section.
**Trade-off:** Some N theses compressed into 1-2 sentences rather than full exposition.

## [STAGE 2] Hook selection
**Context:** 3 hook variants: A (Shock), B (Story), C (Tension).
**Decision:** Variant C (Tension) — "Here's the contradiction nobody wants to talk about..."
**Rationale:** Best match for HackerNoon's contrarian audience. Sets up the core paradox without requiring a specific case (tight word budget). Style researcher confirmed: contrarian openings dominate HackerNoon top articles.
**Trade-off:** Variant A (Shock with cliff chart) was more vivid but required more words for the case setup.

## [STAGE 2] Close selection
**Context:** 3 close variants: A (Decision reframe), B (Provocation), C (Prediction).
**Decision:** Variant B (Provocation) — "You shipped three features last week. How many assumptions did you test?"
**Rationale:** Strongest match for Ivan's voice. Ends with his signature line: "The fix isn't complicated. It's just uncomfortable." HackerNoon style: short close, single memorable line.
**Trade-off:** Variant A (Monday morning protocol) was more actionable but felt like a summary — banned by brief.

## [STAGE 2] Memorable moment placement
**Decision:** "Murder mystery in reverse" metaphor in Section 3.
**Rationale:** Vivid, unexpected, maps to RAT framework. Inverts hero's journey into detective story. Standalone paragraph for maximum impact.

## [STAGE 2] A5 elements relocated
**Context:** A5 thesis elements about glass slipper cohort and PMF treadmill were better served in Section 5 than Section 3.
**Decision:** Moved Elena Verna quote, a16z glass slipper data, and tourist cohort counter from S3 brief to S5 brief. S3 focuses on RAT formula + killer assumption + local/global optimum.
**Rationale:** S5 is dedicated to metrics/cohorts — natural home for these elements. All content preserved, just repositioned.
**Trade-off:** A5 section coverage appears lower (64%) but effective coverage is ~90% when counting relocated elements.
