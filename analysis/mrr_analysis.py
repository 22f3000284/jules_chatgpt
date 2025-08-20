"""
MRR Growth Analysis — 2024 (Quarterly)
Author: Senior Data Analyst
Verification Email: 22f3000284@ds.study.iitm.ac.in

What this script does
- Loads quarterly MRR growth data (2024)
- Computes average vs industry benchmark
- Prints frequency-like stats and key gaps
- Creates visualizations:
  1) Trend by quarter
  2) Benchmark comparison (average vs target)
- Saves figures to ./charts and a short text summary to ./charts/summary.txt
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

TARGET = 15.0  # Industry target benchmark

# -------------------------
# Load data
# -------------------------
here = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(here, "..", "data", "mrr_growth_2024.csv")
df = pd.read_csv(data_path)

# Coerce and validate
df["growth"] = pd.to_numeric(df["growth"], errors="coerce")
df = df.dropna(subset=["growth"])

# -------------------------
# Key calculations
# -------------------------
avg_growth = df["growth"].mean()
gap_to_target = TARGET - avg_growth

# "Frequency count" analogue (quarters meeting target)
quarters_meeting_target = (df["growth"] >= TARGET).sum()

print(f"Average MRR growth (2024): {avg_growth:.2f}")
print(f"Industry target: {TARGET:.2f}")
print(f"Gap to target: {gap_to_target:.2f} points")
print(f"Quarters meeting or exceeding target: {quarters_meeting_target} of {len(df)}")

# Quarter-by-quarter deltas
df["delta_to_target"] = TARGET - df["growth"]

# -------------------------
# Ensure charts directory
# -------------------------
charts_dir = os.path.join(here, "..", "charts")
os.makedirs(charts_dir, exist_ok=True)

# -------------------------
# Visualization 1: Trend by quarter with target line
# -------------------------
plt.figure(figsize=(9, 5))
plt.plot(df["quarter"], df["growth"], marker="o")
plt.axhline(TARGET, linestyle="--")
for i, row in df.iterrows():
    plt.text(i, row["growth"], f'{row["growth"]:.2f}', ha="center", va="bottom")
plt.title("2024 MRR Growth by Quarter (Target = 15)")
plt.xlabel("Quarter")
plt.ylabel("MRR Growth")
plt.tight_layout()
trend_path = os.path.join(charts_dir, "mrr_trend_2024.png")
plt.savefig(trend_path, dpi=150)
plt.close()

# -------------------------
# Visualization 2: Average vs Target (bar chart)
# -------------------------
plt.figure(figsize=(6, 5))
labels = ["Average (2024)", "Industry Target"]
values = [avg_growth, TARGET]
plt.bar(labels, values)
for i, v in enumerate(values):
    plt.text(i, v, f"{v:.2f}", ha="center", va="bottom")
plt.title("Average MRR Growth vs Industry Target")
plt.ylabel("MRR Growth")
plt.tight_layout()
bar_path = os.path.join(charts_dir, "avg_vs_target.png")
plt.savefig(bar_path, dpi=150)
plt.close()

# -------------------------
# Save a brief summary for the PR
# -------------------------
summary = (
    f"Average MRR growth (2024): {avg_growth:.2f}\n"
    f"Industry target: {TARGET:.2f}\n"
    f"Gap to target: {gap_to_target:.2f} points\n"
    f"Quarters >= target: {quarters_meeting_target} / {len(df)}\n"
    f"Recommendation: expand into new market segments to close the gap.\n"
    f"Contact: 22f3000284@ds.study.iitm.ac.in\n"
)
with open(os.path.join(charts_dir, "summary.txt"), "w") as f:
    f.write(summary)
