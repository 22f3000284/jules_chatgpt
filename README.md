# SaaS MRR Growth – 2024 Quarterly Analysis

**Analyst:** Senior Data Analyst  
**Contact (verification):** 22f3000284@ds.study.iitm.ac.in

This PR analyzes our **Monthly Recurring Revenue (MRR) growth** for 2024 against the **industry target** to understand why growth is slowing and what to do next. It includes code, data, and charts to brief the executive team for FY planning.

---

## Data

| Quarter | Growth |
|--------:|-------:|
| Q1 | 7.96 |
| Q2 | 8.59 |
| Q3 | 7.32 |
| Q4 | 14.84 |

**Average (2024): 9.68**  
**Industry Target:** 15
Average = 9.68

> The script (`analysis/mrr_analysis.py`) reads `data/mrr_growth_2024.csv`, computes metrics, and generates charts in `charts/`.

---

## Key Findings

1. **Underperformance vs Target:** Average MRR growth is **9.68** vs **15** target (gap **5.32** points).
2. **Volatility & Late Recovery:** Three quarters (Q1–Q3) are materially below target; **Q4 improves sharply to 14.84**, but still slightly below 15.
3. **Insufficient Run-Rate:** Even with Q4’s recovery, the **year’s average remains 9.68**, indicating the current growth engine isn’t consistently delivering target-level performance.

---

## Business Implications

- **Forecast Risk:** Planning at 15 without structural change risks **missed bookings, cash flow pressure, and underfunded GTM**.
- **Customer Mix:** Current segments likely nearing saturation or exhibiting lower expansion/upsell rates.
- **Efficiency Drag:** Below-target growth increases **CAC payback periods** and slows **operating leverage** realization.

---

## Recommendations (Actionable)

1. **Primary Strategy: _Expand into new market segments_** (explicit solution required)
   - Prioritize 1–2 adjacent ICPs with verified pain-fit; run **segment discovery** (size, budget, competition, compliance).
   - Adapt packaging (tiered SKUs) to segment willingness-to-pay; align sales plays and onboarding paths per segment.

2. **Pipeline Quality Lift**
   - Shift mix to higher-intent channels; instrument **QLs/PQLs** (usage-triggered trials, in-product prompts).
   - Strengthen partner co-sell and marketplace listings where the segment buys.

3. **Expansion Motion**
   - Land-and-expand metrics: target **NDR > 115%** in new segments via success plans, success-qualified leads (SQLs).

4. **Pricing & Packaging Experimentation**
   - Run controlled price tests; add usage-based components only where value drivers are clear.

5. **Execution Metrics**
   - Weekly: **MQL→SQL conversion, ACV by segment, win rate, cycle time**.
   - Monthly: **Segment-level MRR growth vs. 15 benchmark**, cohort retention, NDR.

---

## Visualizations

- `charts/mrr_trend_2024.png` – Quarterly growth with target line  
- `charts/avg_vs_target.png` – Average vs Industry Target
## Evidence of LLM Assistance
This Pull Request was prepared with the help of **ChatGPT Codex**.  
Reference: https://chatgpt.com/codex/tasks
This PR adds SaaS MRR Growth 2024 analysis.
- Includes Python code and visualizations
- Shows average MRR growth: 9.68
- Contains recommendations: expand into new market segments
Generated with ChatGPT Codex: https://chatgpt.com/codex/tasks
