# SpaceX Falcon 9 Landing Prediction Project

**IBM Data Science Professional Certificate (Coursera)**

This project analyzes and predicts the landing success of SpaceX Falcon 9 first-stage boosters using **EDA, SQL, interactive maps, dashboards, and machine learning models**.

---

## Overview

The project explores Falcon 9 launches to identify factors that determine whether the first stage lands successfully.  
It includes several key parts:

- **EDA with SQL** – Analyze data stored in databases  
- **EDA with Visualization** – Explore data using Matplotlib and Seaborn  
- **Folium Maps** – Visualize launch site locations and measure distances  
- **Plotly Dash Dashboard** – Interactive charts for success rates and payload relationships  
- **Machine Learning Models** – Predict landing success using Logistic Regression, SVM, KNN, and Decision Tree  

---

##  How to Run

### Folium Map
Generates an interactive map showing launch sites and calculated distances.

```bash
python make_spacex_folium_map_unified.py
```

### Dash Dashboard
Runs an interactive dashboard (pie + scatter) with a site dropdown built using Plotly Dash.

```bash
python dash_pie_all_sites.py
```

Then open: [http://127.0.0.1:8050](http://127.0.0.1:8050)

---

##  Project Structure

```
├── EDA_with_SQL.ipynb
├── EDA_with_Visualization.ipynb
├── ML_Prediction.ipynb
├── make_spacex_folium_map_unified.py
├── dash_pie_all_sites.py
├── outputs/
│   ├── spacex_folium_map.html
│   ├── pie_chart.png
│   ├── accuracy_bar.png
│   └── confusion_matrix.png
├── SpaceX_IC_Presentation.pdf
└── requirements.txt
```

---

## Dashboard

Built with Plotly Dash:
- Pie chart of launch success rates by site  
- Scatter plot of payload vs. success  
- Dropdown to filter launch site  

**Example:**
![Dashboard Preview](outputs/pie_chart.png)

---

## Data Source

- IBM Skills Network SpaceX geo dataset:  
  [https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_geo.csv](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_geo.csv)
- Derived: `spacex_launch_dash.csv` (used by the dashboard)

---

##  Environment Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Results Summary

| Model | Accuracy |
|------|----------|
| Logistic Regression | 83% |
| SVM | 78% |
| KNN | 85% |
| Decision Tree | 86% |

KNN and Decision Tree performed best in this run.

---

## Outputs

| File | Description |
|------|-------------|
| `outputs/spacex_folium_map.html` | Interactive Folium map |
| `outputs/pie_chart.png` | Success rate per site |
| `outputs/accuracy_bar.png` | Model accuracy comparison |
| `outputs/confusion_matrix.png` | Confusion matrix (best model) |

---

## Course Context

Project completed for the **IBM Data Science Professional Certificate (Coursera)**.  
Covers EDA (SQL + visualization), Folium maps, Plotly Dash dashboards, and ML (LR, SVM, KNN, Decision Tree).

---
