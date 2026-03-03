# 05 — Section briefs (blueprint for draft)

Generated: 2026-03-02  
Target publication: Mind the Product  
Target length: ~1,200 words

## Draft structure (sections)

1) Hook (vibe coding panic → reframe)  
2) Judgment is the job (T1)  
3) Builder ≠ “replace engineers” (T2)  
4) From PRDs to pipelines: prompt sets + evals + progressive autonomy (T3 + T7 + T15)  
5) Guardrails are product work: cost/reversibility + security + debt + pricing (T4 + T8 + T13 + T14 + T16)  
6) Moats and distribution in an agent world: context + interop + narrative (T9 + T12 + T11)  
7) Career + org bets: demand shift + K-shape + apprenticeship debt (T5 + T6 + T10)  
8) How‑to / Actionable takeaways (next sprint checklist + template)

---

## Section 0 — Hook (tension + promise)

- Word budget: 90–120
- Goal: state the conflict (execution cheap; roles unclear) + promise (“what to do next sprint”)
- Style constraints: 2–3 short paragraphs + 1 punchy line; no generic “in today’s world”

Hook ingredients (pick 1–2, all sourced):
- YC W25 AI codebase data — https://techcrunch.com/2025/03/06/a-quarter-of-startups-in-ycs-current-cohort-have-codebases-that-are-almost-entirely-ai-generated/ (2025)
- “PM theatre becomes cheap” framing — https://www.svpg.com/product-coaching-and-ai/ (2026)
- “Vibe coding” term — https://x.com/karpathy/status/1886192184808149383 (2025)

Transition to Section 1:
- “If shipping is cheap, the PM job doesn’t disappear — it moves.”

---

## Section 1 — Judgment is the job (T1)

- Thesis: T1 (A1)
- Word budget: 170–220
- Position: early (right after hook)

SUT skeleton (raw):
> Абсолютно критичный навык в эпоху AI — business judgment… (см. `00-must-include.md` → T1-E1)

What the section must *do*:
- Reframe PM value as decision quality under uncertainty (not artifact production).
- Tie it to psychological safety as a product variable (learning speed, willingness to surface risk).

MUST‑INCLUDE (IDs):
- T1-E1 (SUT) — preserve logic, rewrite in English
- T1-E4 (concepts)
- T1-E6 (sources: Cagan + psych safety)

Case + countercase (URLs):
- Case: SVPG / Cagan (2026) — https://www.svpg.com/product-coaching-and-ai/
- Counter/limit: a16z (2024) — https://a16z.com/ai-copilot-ai-agent-white-collar-roles/

Primary segment + JTBD:
- Segment A (product-leads) + Segment B (corporate PMs)
- JTBD: “Build trust via decision logic; avoid being a ‘feature requestor’.”

Transition to Section 2:
- “Once judgment is the bottleneck, your fastest path to better judgment is faster learning loops — and that pushes PMs closer to building.”

Style constraints:
- Use “you” voice; 1 short “if your job is X…” line; 1 trade-off paragraph.

---

## Section 2 — Builder ≠ “PM replaces engineers” (T2)

- Thesis: T2 (A2)
- Word budget: 170–230

SUT skeleton (raw):
> Все PM будут становиться full-stack builder-ами… (см. `00-must-include.md` → T2-E1)

What the section must do:
- Define “full‑stack builder PM” as *prototype + learning loop owner*, not “solo ship to prod”.
- Warn about speed illusions and quality/security risks.

MUST‑INCLUDE (IDs):
- T2-E1 (SUT) — keep core, avoid unsourced specifics
- T2-E3 (Karpathy / vibe coding source)
- T2-E4 (concepts)
- T2-E6 (YC signal)
- T2-E7 (counter signals: METR + quality/security/debt research)

Case + countercase (URLs):
- Case: YC W25 (2025) — https://techcrunch.com/2025/03/06/a-quarter-of-startups-in-ycs-current-cohort-have-codebases-that-are-almost-entirely-ai-generated/
- Counter: Veracode security report (2025) — https://www.veracode.com/resources/analyst-reports/2025-genai-code-security-report/

Primary segment + JTBD:
- Segment A (product-leads)
- JTBD: “Validate faster without blowing up reliability/security.”

Transition to Section 3:
- “If you can prototype faster, the PM artifact that matters becomes the pipeline: prompts, evals, and decision rules.”

Style constraints:
- 1 definition paragraph (“builder PM means…”), then a short list of “what it doesn’t mean”.

---

## Section 3 — From PRDs to pipelines: prompt sets + evals + progressive autonomy (T3 + T7 + T15)

- Theses: T3 (A3) + T7 (N1) + T15 (N9)
- Word budget: 260–340

SUT skeletons (raw):
> PM станут управлять конвейером проверки гипотез… (T3-E1)  
> В AI-продуктах “правильность” не бинарна… (T7-E1)  
> AI-диффузия неоднородна… progressive autonomy… (T15-E1)

What the section must do:
- Introduce a PM “pipeline” mental model: hypotheses → prompts → evals → rollout with autonomy gradient.
- Give a next-sprint “minimum viable pipeline” example.

MUST‑INCLUDE (IDs):
- T3-E1, T3-E6, T3-E7 (pipeline + prompt sets + “agent” ambiguity)
- T7-E1, T7-E5 (evals-first)
- T15-E1, T15-E7 + T15-E5 (progressive autonomy + uneven adoption)

Case + countercase (URLs):
- Case: “How to build an Enterprise AI Agent” (2025) — https://www.mindtheproduct.com/how-to-build-an-enterprise-ai-agent/
- Counter/limit: WORKBank (human agency) (2025) — https://arxiv.org/abs/2506.06576

Primary segment + JTBD:
- Segment A + Segment B
- JTBD: “Ship AI incrementally with trust; avoid all‑or‑nothing autonomy.”

Transition to Section 4:
- “Pipelines increase throughput — and they multiply risk. That’s why guardrails are now product work.”

Style constraints:
- Use a numbered mini-framework (3–5 steps) + a small checklist.

---

## Section 4 — Guardrails are product work: cost, reversibility, security, debt, pricing (T4 + T8 + T13 + T14 + T16)

- Theses: T4 (A4) + T8 (N2) + T13 (N7) + T14 (N8) + T16 (N10)
- Word budget: 300–380

SUT skeletons (raw):
> Через год-два появится полный цикл… (T4-E1)  
> AI-фича имеет переменную стоимость… kill criteria… circuit breakers… (T8-E1)  
> …security (~45% случаев)… PM = совладелец… (T13-E1)  
> …tech debt compounding… “скоростная хрупкость”… (T14-E1)  
> …pricing… value per job… seat pricing ломается… (T16-E1)

What the section must do:
- Translate “AI risk” into 4 concrete guardrails PMs can own next sprint:
  1) eval gate (quality)
  2) circuit breaker (cost/steps)
  3) security in DoD (risk)
  4) debt capacity (maintainability)
- Tie guardrails to pricing/unit economics (value per job; caps/tiers).

MUST‑INCLUDE (IDs):
- T4-E4, T4-E6, T4-E7 (constraints + “tools not ready” counter)
- T8-E1, T8-E5 (circuit breakers + kill criteria)
- T13-E1, T13-E5 (security as product work)
- T14-E1, T14-E5 (debt compounding evidence)
- T16-E1, T16-E5 (pricing/value capture)

Case + countercase (URLs):
- Case: MtP AI strategy guide (budgeting/guardrails) (2026) — https://www.mindtheproduct.com/the-2026-ai-product-strategy-huide-how-to-plan-budget-and-build-without-buying-into-the-hype/
- Counter/limit: Chesky “tools not ready” (2025) — https://www.latimes.com/business/story/2025-10-21/chesky-says-openai-tools-not-ready-for-chatgpt-tie-up-with-airbnb-app

Primary segment + JTBD:
- Segment B (corporate PMs) primary; Segment A secondary
- JTBD: “Adopt AI without bleeding money or creating security incidents.”

Transition to Section 5:
- “Once you can ship safely, advantage shifts from ‘who can build’ to ‘who has the best context and distribution’.”

Style constraints:
- Strong subheads + one table or compact checklist; keep paragraphs short.

---

## Section 5 — Moats + distribution in an agent world: context, interop, narrative (T9 + T12 + T11)

- Theses: T9 (N3) + T12 (N6) + T11 (N5)
- Word budget: 180–250

SUT skeletons (raw):
> …лучший контекст… context supply chain… (T9-E1)  
> …agent-to-app interop… product for agents… (T12-E1)  
> …дифференциация переезжает в story/positioning/distribution… (T11-E1)

What the section must do:
- Give a practical framing: context is a product surface; interop is a distribution surface; narrative is a decision surface.
- Provide 2–3 “next sprint” actions (e.g., define SoT, freshness SLA, permission model, “agent-ready” API checklist, positioning one-liner).

MUST‑INCLUDE (IDs):
- T9-E1, T9-E5 (context supply chain)
- T12-E1, T12-E4 (agent interop surface)
- T11-E1, T11-E4, T11-E5 (narrative/positioning/distribution shift)

Case + countercase (URLs):
- Case: a16z context wedge (2024) — https://a16z.com/ai-copilot-ai-agent-white-collar-roles/
- Counter/limit: “agent definition is fuzzy” (2025) — https://techcrunch.com/2025/05/12/even-a16z-vcs-say-no-one-really-knows-what-an-ai-agent-is/

Primary segment + JTBD:
- Segment A + B
- JTBD: “Build leverage beyond model choice; avoid a perpetual model race.”

Transition to Section 6:
- “These moats shape the job market too: the PMs who can own context, constraints, and narrative pull ahead.”

Style constraints:
- Use 1–2 crisp analogies (mobile-first → agent-first), but keep grounded.

---

## Section 6 — Career + org bets: demand shift, K‑shape, apprenticeship debt (T5 + T6 + T10)

- Theses: T5 (A5) + T6 (A6) + T10 (N4)
- Word budget: 200–280

SUT skeletons (raw):
> …спрос растёт не “на всех”… а на тех, кто управляет агентами… (T5-E1)  
> …PM-рынок раскалывается в форме K… (T6-E1)  
> …apprenticeship debt… pipeline seniors… (T10-E1)

What the section must do:
- Give a sober view: demand can grow *and* layoffs/junior squeeze can happen.
- Make it actionable: personal bets (skills) + org bets (training/pipeline/psych safety).

MUST‑INCLUDE (IDs):
- T5-E1, T5-E4, T5-E6 + T5-E7 (bridge into AI roles + layoffs reality check)
- T6-E1, T6-E4 (K-shape framing)
- T10-E1, T10-E2 + T10-E5 (apprenticeship debt + junior hiring expectations)

Case + countercase (URLs):
- Case: “Product thinking … fastest-growing jobs in 2026” (2026) — https://www.mindtheproduct.com/product-thinking-driving-fastest-growing-jobs/
- Counter/limit: layoffs report (2025) — https://foushee.house.gov/media/press-releases/amid-historic-layoffs-surge-rep-foushee-releases-report-on-ais-impact-on-american-jobs-and-demands-clarity-from-industry-leaders

Primary segment + JTBD:
- Segment A + B
- JTBD: “Stay employable by owning global outcomes + constraints, not local optimisations.”

Transition to Takeaways:
- “So what does this look like in your next sprint? Here’s the checklist.”

Style constraints:
- Avoid doom tone; keep it practical and specific.

---

## Section 7 — How‑to / Actionable takeaways (next sprint)

- Word budget: 160–220
- Output format: checklist + one small template

Required output:
- “Pick one” next sprint experiment:
  - Add 1 eval gate to an AI feature
  - Add 1 circuit breaker + kill criteria
  - Define 1 context source-of-truth + freshness SLA
  - Prototype 1 workflow end‑to‑end (prototype only) and run a premortem

Style constraint:
- Include at least one H5 block for a compact template.

---

## Coverage & dropped elements

### Dropped (by ID) — with reason

- T1-E3: HBR quote has no URL in thesis (`MISSING_SOURCE`) → drop or replace with a sourced equivalent.
- T5-E2: contains unsourced numbers (“35% more”, “75% employers…”) → drop unless primary sources are found.
- T5-E3: Andreessen quote has no URL in thesis → drop unless primary source is found.
- T2-E2: includes multiple unsourced specifics (turning point, Boris Cherny productivity) → drop unless primary sources are found.

### Coverage check (sanity)

- Each thesis included in at least one section above.
- Deep/medium thresholds: briefs include ≥ ~60% of must-include elements for core theses; missing-source items explicitly dropped above.
