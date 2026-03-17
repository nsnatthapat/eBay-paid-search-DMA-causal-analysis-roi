"""
Generate charts for the eBay Paid Search Causal Analysis README.
All metrics are derived directly from the notebook outputs — no new analysis.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np

os.makedirs("outputs", exist_ok=True)

# ── colour palette ──────────────────────────────────────────────────────────
BLUE   = "#1F77B4"
ORANGE = "#FF7F0E"
GREEN  = "#2CA02C"
RED    = "#D62728"
GREY   = "#7F7F7F"

plt.rcParams.update({
    "font.family": "sans-serif",
    "axes.titlesize": 14,
    "axes.labelsize": 12,
    "legend.fontsize": 10,
    "figure.dpi": 300,
})

# ─────────────────────────────────────────────────────────────────────────────
# Chart 1 – Naive vs. Causal ROI
# ─────────────────────────────────────────────────────────────────────────────
labels = ["Naïve ROI\n(Attribution-based)", "Causal ROI\n(DiD Estimate)"]
values = [272.40, -60.23]
colors = [GREEN, RED]

fig, ax = plt.subplots(figsize=(7, 5))
bars = ax.bar(labels, values, color=colors, width=0.45, edgecolor="white", linewidth=1.2)
ax.axhline(0, color="black", linewidth=0.8, linestyle="--", alpha=0.6)

for bar, val in zip(bars, values):
    va = "bottom" if val >= 0 else "top"
    offset = 5 if val >= 0 else -5
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        val + offset,
        f"{val:.1f}%",
        ha="center", va=va, fontweight="bold", fontsize=13
    )

ax.yaxis.set_major_formatter(mtick.PercentFormatter())
ax.set_ylabel("Return on Investment (%)")
ax.set_title("Naïve vs. Causal ROI of Paid Search Advertising", fontweight="bold")
ax.set_ylim(-120, 330)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
fig.tight_layout()
fig.savefig("outputs/naive_vs_causal_roi.png", dpi=300)
plt.close()
print("✓ Chart 1 saved: naive_vs_causal_roi.png")

# ─────────────────────────────────────────────────────────────────────────────
# Chart 2 – Mean Daily Total Sales: Treatment vs. Control (Pre and Post)
# ─────────────────────────────────────────────────────────────────────────────
periods = ["Pre-Treatment", "Post-Treatment"]
control_means = [2806.05, 2825.20]
treatment_means = [2236.85, 2238.46]

x = np.arange(len(periods))
width = 0.35

fig, ax = plt.subplots(figsize=(8, 5))
b1 = ax.bar(x - width/2, control_means,  width, label="Control (Ads On)",  color=BLUE,   alpha=0.88, edgecolor="white")
b2 = ax.bar(x + width/2, treatment_means, width, label="Treatment (Ads Off)", color=ORANGE, alpha=0.88, edgecolor="white")

for bar in list(b1) + list(b2):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 20,
        f"${bar.get_height():,.0f}",
        ha="center", va="bottom", fontsize=9, color="black"
    )

ax.set_ylabel("Mean Daily Total Sales ($)")
ax.set_title("Mean Daily Total Sales by Group & Period", fontweight="bold")
ax.set_xticks(x)
ax.set_xticklabels(periods)
ax.legend()
ax.yaxis.set_major_formatter(mtick.StrMethodFormatter("${x:,.0f}"))
ax.set_ylim(0, 3500)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
fig.tight_layout()
fig.savefig("outputs/mean_sales_treatment_vs_control.png", dpi=300)
plt.close()
print("✓ Chart 2 saved: mean_sales_treatment_vs_control.png")

# ─────────────────────────────────────────────────────────────────────────────
# Chart 3 – DiD Model Comparison (Estimate + 95% CI)
# ─────────────────────────────────────────────────────────────────────────────
models = [
    "Simple OLS",
    "OLS + Covariates",
    "OLS + DMA FEs",
    "OLS + Day FEs",
    "OLS + DMA & Day FEs",
]
estimates  = [-17.54, -17.54, -17.54, -17.54, -17.56]
ci_lower   = [-295.50, -213.89, -20.22, -295.54, -19.04]
ci_upper   = [ 260.42,  178.80, -14.86,  260.46, -16.04]

errs_low   = [e - l for e, l in zip(estimates, ci_lower)]
errs_high  = [u - e for u, e in zip(ci_upper,  estimates)]

fig, ax = plt.subplots(figsize=(9, 5))
y_pos = np.arange(len(models))

for i, (est, el, eh, sig) in enumerate(zip(estimates, errs_low, errs_high,
                                            [False, False, True, False, True])):
    color = GREEN if sig else GREY
    ax.errorbar(est, i, xerr=[[el], [eh]],
                fmt="o", color=color, ecolor=color,
                elinewidth=2, capsize=5, markersize=8, zorder=3)

ax.axvline(0, color="black", linewidth=0.8, linestyle="--", alpha=0.7)
ax.set_yticks(y_pos)
ax.set_yticklabels(models)
ax.set_xlabel("DiD Estimate (Incremental Daily Sales, $)")
ax.set_title("DiD Estimates Across Model Specifications\n(95% CI — Green = Statistically Significant)", fontweight="bold")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
fig.tight_layout()
fig.savefig("outputs/did_model_comparison.png", dpi=300)
plt.close()
print("✓ Chart 3 saved: did_model_comparison.png")

# ─────────────────────────────────────────────────────────────────────────────
# Chart 4 – Sales Gap (Control – Treatment) Before and After
# ─────────────────────────────────────────────────────────────────────────────
stages = ["Pre-Treatment Gap", "Post-Treatment Gap"]
gaps   = [569.19, 586.74]            # Control mean minus Treatment mean
colors = [BLUE, RED]

fig, ax = plt.subplots(figsize=(7, 5))
bars = ax.bar(stages, gaps, color=colors, width=0.45, edgecolor="white", linewidth=1.2, alpha=0.88)

for bar in bars:
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 4,
        f"${bar.get_height():,.2f}",
        ha="center", va="bottom", fontweight="bold", fontsize=13
    )

ax.set_ylabel("Sales Gap: Control − Treatment ($)")
ax.set_title("Average Daily Sales Gap Between Control & Treatment\n(DiD Change ≈ −$17.54 per DMA per Day)", fontweight="bold")
ax.set_ylim(0, 750)
ax.yaxis.set_major_formatter(mtick.StrMethodFormatter("${x:,.0f}"))
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
fig.tight_layout()
fig.savefig("outputs/sales_gap_pre_post.png", dpi=300)
plt.close()
print("✓ Chart 4 saved: sales_gap_pre_post.png")

print("\nAll charts saved to the outputs/ folder.")
