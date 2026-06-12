# ============================================================
# UNEMPLOYMENT ANALYSIS WITH PYTHON
# Dataset: Unemployment in India (CMIE Data)
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

# ── Style ────────────────────────────────────────────────────
plt.rcParams.update({
    "figure.facecolor": "#1a1a2e",
    "axes.facecolor":   "#16213e",
    "axes.edgecolor":   "#e94560",
    "axes.labelcolor":  "#eaeaea",
    "xtick.color":      "#eaeaea",
    "ytick.color":      "#eaeaea",
    "text.color":       "#eaeaea",
    "grid.color":       "#2a2a4a",
    "grid.linestyle":   "--",
    "grid.alpha":       0.5,
    "axes.titlesize":   13,
    "axes.titlecolor":  "#e94560",
})

# ── Load Data ────────────────────────────────────────────────
print("Loading datasets...")
df1 = pd.read_csv("Unemployment in India.csv")
df2 = pd.read_csv("Unemployment_Rate_upto_11_2020.csv")

# Clean column names
df1.columns = df1.columns.str.strip()
df2.columns = df2.columns.str.strip()

# Parse dates
df1["Date"] = pd.to_datetime(df1["Date"].str.strip(), format="%d-%m-%Y")
df2["Date"] = pd.to_datetime(df2["Date"].str.strip(), format="%d-%m-%Y")

# Rename for convenience
df1.rename(columns={
    "Estimated Unemployment Rate (%)": "Unemployment_Rate",
    "Estimated Employed":              "Employed",
    "Estimated Labour Participation Rate (%)": "Labour_Participation"
}, inplace=True)

df2.rename(columns={
    "Estimated Unemployment Rate (%)": "Unemployment_Rate",
    "Estimated Employed":              "Employed",
    "Estimated Labour Participation Rate (%)": "Labour_Participation"
}, inplace=True)

print(f"Dataset 1 shape : {df1.shape}")
print(f"Dataset 2 shape : {df2.shape}")
print("\nBasic stats (Dataset 1):\n", df1["Unemployment_Rate"].describe())

# ── Plot 1 · National Average Unemployment Rate Over Time ────
fig, ax = plt.subplots(figsize=(13, 5))
national = df1.groupby("Date")["Unemployment_Rate"].mean().reset_index()
ax.plot(national["Date"], national["Unemployment_Rate"],
        color="#e94560", linewidth=2, marker="o", markersize=3)
ax.fill_between(national["Date"], national["Unemployment_Rate"],
                alpha=0.15, color="#e94560")
ax.set_title("National Average Unemployment Rate Over Time")
ax.set_xlabel("Date")
ax.set_ylabel("Unemployment Rate (%)")
ax.yaxis.set_major_formatter(mticker.FormatStrFormatter("%.1f%%"))
ax.grid(True)
fig.tight_layout()
plt.savefig("plot1_national_trend.png", dpi=150, bbox_inches="tight")
plt.close()
print("Saved → plot1_national_trend.png")

# ── Plot 2 · Unemployment by State (Average) ─────────────────
fig, ax = plt.subplots(figsize=(14, 8))
state_avg = (df1.groupby("Region")["Unemployment_Rate"]
               .mean()
               .sort_values(ascending=False))
colors = ["#e94560" if v > state_avg.mean() else "#0f3460"
          for v in state_avg.values]
state_avg.plot(kind="bar", ax=ax, color=colors, edgecolor="#1a1a2e", width=0.7)
ax.axhline(state_avg.mean(), color="#f5a623", linestyle="--",
           linewidth=1.5, label=f"National Avg: {state_avg.mean():.2f}%")
ax.set_title("Average Unemployment Rate by State")
ax.set_xlabel("State / Region")
ax.set_ylabel("Unemployment Rate (%)")
ax.legend()
plt.xticks(rotation=75, ha="right", fontsize=8)
fig.tight_layout()
plt.savefig("plot2_state_comparison.png", dpi=150, bbox_inches="tight")
plt.close()
print("Saved → plot2_state_comparison.png")

# ── Plot 3 · Rural vs Urban Comparison ───────────────────────
if "Area" in df1.columns:
    fig, ax = plt.subplots(figsize=(11, 5))
    area_time = (df1.groupby(["Date", "Area"])["Unemployment_Rate"]
                   .mean().reset_index())
    for area, color in [("Rural", "#0f9b8e"), ("Urban", "#e94560")]:
        sub = area_time[area_time["Area"] == area]
        ax.plot(sub["Date"], sub["Unemployment_Rate"],
                label=area, color=color, linewidth=2)
    ax.set_title("Rural vs Urban Unemployment Rate Over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Unemployment Rate (%)")
    ax.yaxis.set_major_formatter(mticker.FormatStrFormatter("%.1f%%"))
    ax.legend()
    ax.grid(True)
    fig.tight_layout()
    plt.savefig("plot3_rural_vs_urban.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("Saved → plot3_rural_vs_urban.png")

# ── Plot 4 · Covid-19 Impact (df2: Jan–Nov 2020) ─────────────
fig, ax = plt.subplots(figsize=(12, 5))
covid = df2.groupby("Date")["Unemployment_Rate"].mean().reset_index()
ax.plot(covid["Date"], covid["Unemployment_Rate"],
        color="#f5a623", linewidth=2.5, marker="D", markersize=5)
ax.fill_between(covid["Date"], covid["Unemployment_Rate"],
                alpha=0.2, color="#f5a623")
ax.axvline(pd.Timestamp("2020-03-25"), color="#e94560", linestyle="--",
           linewidth=1.5, label="Lockdown Begins (Mar 25)")
ax.axvline(pd.Timestamp("2020-06-01"), color="#0f9b8e", linestyle="--",
           linewidth=1.5, label="Unlock 1.0 (Jun 1)")
ax.set_title("Unemployment Rate During Covid-19 (Jan – Nov 2020)")
ax.set_xlabel("Date")
ax.set_ylabel("Unemployment Rate (%)")
ax.yaxis.set_major_formatter(mticker.FormatStrFormatter("%.1f%%"))
ax.legend()
ax.grid(True)
fig.tight_layout()
plt.savefig("plot4_covid_impact.png", dpi=150, bbox_inches="tight")
plt.close()
print("Saved → plot4_covid_impact.png")

# ── Plot 5 · Heatmap: Unemployment by State × Month (2020) ───
df2["Month"] = df2["Date"].dt.strftime("%b-%Y")
pivot = (df2.groupby(["Region", "Month"])["Unemployment_Rate"]
           .mean().unstack())
# Sort months chronologically
month_order = pd.to_datetime(pivot.columns, format="%b-%Y").argsort()
pivot = pivot.iloc[:, month_order]

fig, ax = plt.subplots(figsize=(16, 10))
sns.heatmap(pivot, cmap="RdYlGn_r", linewidths=0.3,
            linecolor="#1a1a2e", annot=True, fmt=".1f",
            ax=ax, cbar_kws={"label": "Unemployment Rate (%)"})
ax.set_title("Unemployment Rate Heatmap: State × Month (2020)")
ax.set_xlabel("Month")
ax.set_ylabel("State")
plt.xticks(rotation=45, ha="right")
plt.yticks(rotation=0, fontsize=8)
fig.tight_layout()
plt.savefig("plot5_heatmap_state_month.png", dpi=150, bbox_inches="tight")
plt.close()
print("Saved → plot5_heatmap_state_month.png")

# ── Plot 6 · Labour Participation vs Unemployment (Scatter) ──
fig, ax = plt.subplots(figsize=(9, 6))
sc = ax.scatter(df1["Labour_Participation"], df1["Unemployment_Rate"],
                c=df1["Employed"], cmap="plasma",
                alpha=0.6, edgecolors="none", s=30)
cbar = fig.colorbar(sc, ax=ax)
cbar.set_label("Estimated Employed")
ax.set_title("Labour Participation Rate vs Unemployment Rate")
ax.set_xlabel("Labour Participation Rate (%)")
ax.set_ylabel("Unemployment Rate (%)")
ax.grid(True)
fig.tight_layout()
plt.savefig("plot6_participation_vs_unemployment.png", dpi=150, bbox_inches="tight")
plt.close()
print("Saved → plot6_participation_vs_unemployment.png")

print("\n✅ All 6 plots generated successfully!")
