# unemployment_analysis_with_python
 Unemployment Analysis in India > Exploratory Data Analysis on CMIE unemployment data using Python — with a focus on the COVID-19 impact on India's labour market.
## 🗂️ Dataset
- **Source:** [CMIE (Centre for Monitoring Indian Economy)](https://www.cmie.com/)
- **Files used:**
  - `Unemployment in India.csv` — state-wise monthly data (2018–2021)
  - `Unemployment_Rate_upto_11_2020.csv` — granular 2020 data for COVID analysis

---

## 📌 Objectives
- Track national unemployment trends over time
- Compare unemployment rates across Indian states
- Analyse the Rural vs Urban divide
- Quantify the COVID-19 lockdown impact (Mar–Nov 2020)
- Visualise state × month heatmaps for 2020
- Explore the relationship between labour participation and unemployment

---

## 📈 Visualisations

### 1. National Average Unemployment Rate Over Time
![National Trend](plots/plot1_national_trend.png)

### 2. Average Unemployment Rate by State
![State Comparison](plots/plot2_state_comparison.png)
> States highlighted in red exceed the national average.

### 3. Rural vs Urban Unemployment Rate Over Time
![Rural vs Urban](plots/plot3_rural_vs_urban.png)

### 4. COVID-19 Impact on Unemployment (Jan–Nov 2020)
![COVID Impact](plots/plot4_covid_impact.png)
> Vertical markers indicate the national lockdown start (Mar 25) and Unlock 1.0 (Jun 1).

### 5. Heatmap: State × Month Unemployment (2020)
![Heatmap](plots/plot5_heatmap_state_month.png)

### 6. Labour Participation Rate vs Unemployment Rate
![Scatter](plots/plot6_participation_vs_unemployment.png)
> Color encodes the estimated employed population (plasma scale).

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| `pandas` | Data loading, cleaning, groupby aggregations |
| `numpy` | Numerical operations |
| `matplotlib` | Core plotting engine |
| `seaborn` | Heatmap rendering |

---

## 🚀 How to Run

```bash
# 1. Clone the repo
git clone https://github.com/<your-username>/unemployment-analysis-india.git
cd unemployment-analysis-india

# 2. Install dependencies
pip install pandas numpy matplotlib seaborn

# 3. Place the datasets in the root directory
#    - Unemployment in India.csv
#    - Unemployment_Rate_upto_11_2020.csv

# 4. Run the analysis
python unemployment_analysis.py
```

All 6 plots will be saved as `.png` files in the working directory.

---

## 📂 Project Structure

```
unemployment-analysis-india/
│
├── unemployment_analysis.py       # Main analysis script
├── Unemployment in India.csv      # Dataset 1 (2018–2021)
├── Unemployment_Rate_upto_11_2020.csv  # Dataset 2 (2020)
├── plots/
│   ├── plot1_national_trend.png
│   ├── plot2_state_comparison.png
│   ├── plot3_rural_vs_urban.png
│   ├── plot4_covid_impact.png
│   ├── plot5_heatmap_state_month.png
│   └── plot6_participation_vs_unemployment.png
└── README.md
```

---

## 🔍 Key Findings

- 📈 **COVID-19 spike:** Unemployment surged sharply after the national lockdown in March 2020, peaking around April–May 2020.
- 🏙️ **Urban > Rural:** Urban unemployment was consistently higher than rural, likely due to industry/service sector shutdowns.
- 🗺️ **State disparities:** Certain states (e.g., Haryana, Tripura) recorded significantly higher unemployment compared to the national average.
- 📉 **Recovery:** Post Unlock 1.0, unemployment gradually declined but did not return to pre-COVID levels within 2020.
- 🔗 **Participation paradox:** States with higher labour participation rates did not always exhibit lower unemployment — suggesting underemployment issues.

---

## 🤝 Connect

**Brahmini Seelam** — CSE Undergraduate @ AUCE, Visakhapatnam  
🔗 [LinkedIn](https://linkedin.com/in/brahminiseelam) · [GitHub](https://github.com/Brahminiseelam)

---

*This project was completed as part of an internship task at Oasis Infobyte.*
