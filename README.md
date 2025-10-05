# SpaceX Falcon 9 Landing Prediction Project

**IBM Data Science Professional Certificate (Coursera)**

This project analyzes and predicts the landing success of SpaceX Falcon 9 first-stage boosters using **EDA, SQL, interactive maps, dashboards, and machine learning models**.

---

## Overview

The project explores Falcon 9 launches to identify factors that determine whether the first stage lands successfully.  
It includes several key parts:

- **EDA with SQL** – Analyze data stored in databases  
- **EDA Visualization** – Explore data using Matplotlib and Seaborn  
- **Folium Maps** – Visualize launch site locations and measure distances  
- **Plotly Dash Dashboard** – Interactive charts for success rates and payload relationships  
- **Machine Learning Models** – Predict landing success using Logistic Regression, SVM, KNN, and Decision Tree  

---

##  How to Run

### Folium Map
Generates an interactive map showing launch sites and calculated distances.

```bash
python Folium-map-unified.ipynb
```

### Dash Dashboard
Runs an interactive dashboard (pie + scatter) with a site dropdown built using Plotly Dash.

```bash
python Dash_pie_all_sites.py
```

Then open: [http://127.0.0.1:8050](http://127.0.0.1:8050)

---

##  Project Structure

```
├── outputs/
│   ├── spacex_folium_map.html
│   ├── pie_chart.png
│   ├── accuracy_bar.png
│   └── confusion_matrix.png
├── 1-Data-Collection-SQL.ipynb
├── 2-EDA-with-SQL.ipynb
├── 3-EDA-Visualization.ipynb
├── 4-Folium-Map.ipynb
├── 5-Dashboard.ipynb
├── 7-Falcon9-Landing-Prediction.pdf
├── 8-Presentation.pdf
├── 9-README.md
├──10-requirements.txt

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
| SVM | 83% |
| KNN | 77% |
| Decision Tree | 66% |

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

## Project Context

Developed as part of the **IBM Data Science Professional Certificate (Coursera)** – Capstone Project.  
This project combines skills in data and contains analysis, SQL, visualization, Folium maps, interactive dashboards (Plotly Dash), and machine learning (Logistic Regression, SVM, KNN, Decision Tree).

---

**Author:** Abdullah Wahas




