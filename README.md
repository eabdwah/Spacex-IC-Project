# SpaceX Falcon 9 – Project (IBM Data Science, Coursera)

EDA + SQL, Folium maps, Plotly Dash, and ML (LR/SVM/KNN/Tree) to predict Falcon 9 landing success.

## How to run
- **Folium map**: `python make_spacex_folium_map_unified.py` → opens `spacex_folium_map.html`
- **Dash pie**: `python dash_pie_all_sites.py` → open http://127.0.0.1:8050

## Files
Notebooks: EDA with SQL, EDA with Visualization, Folium (Lab 6), ML Prediction  
Scripts: `make_spacex_folium_map_unified.py`, `dash_pie_all_sites.py`  
Slides: `SpaceX_IC_Presentation.pdf`  
Images: in `outputs/` (map, pie, accuracy bar, confusion matrix)

## Data
- IBM SpaceX geo CSV (coords):  
  https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_geo.csv
  

## Environment
To install dependencies:
```bash
pip install -r requirements.txt
Course context: IBM Data Science Professional Certificate (Coursera).
