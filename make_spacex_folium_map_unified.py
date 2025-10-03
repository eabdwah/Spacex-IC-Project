# make_spacex_folium_map_unified.py
import os, math
import pandas as pd
import folium
from folium.plugins import Fullscreen, MousePosition, MeasureControl, MarkerCluster
from folium.features import DivIcon

DATA_SOURCE = "local"  # "local" or "url"
LOCAL_CSV_PATH = r"C:\Users\whas3\Desktop\Data World\My projects\I-C\spacex_launch_dash.csv"
IBM_URL = ("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/"
           "IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_geo.csv")

USE_CLUSTER  = False
JITTER_MODE  = "ring"
BASE_RADIUS_M, RING_GAP_M, MAX_PER_RING = 3500, 1200, 12
DRAW_DISTANCE, ADD_LEGEND = True, True
TILES = "CartoDB positron"

def canon_site(name: str) -> str:
    n = str(name).lower()
    if ("slc-40" in n or "lc-40" in n) and any(k in n for k in ["ccafs","ccsfs","cape canaveral"]): return "CCAFS SLC-40"
    if "lc-39a" in n or "39a" in n: return "KSC LC-39A"
    if "slc-4e" in n or "4e" in n or "vafb" in n or "vandenberg" in n: return "VAFB SLC-4E"
    return str(name)

SITE_COORDS = {
    "CCAFS SLC-40": (28.561857, -80.577366),
    "KSC LC-39A":   (28.608389, -80.604333),
    "VAFB SLC-4E":  (34.632093, -120.610829),
}
COAST_REFS = {
    "CCAFS SLC-40": (28.56367, -80.57163),
    "KSC LC-39A":   (28.62700, -80.58550),
    "VAFB SLC-4E":  (34.63550, -120.62650),
}

def haversine_km(lat1, lon1, lat2, lon2):
    R = 6371.0088
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dphi, dlmb = math.radians(lat2 - lat1), math.radians(lon2 - lon1)
    a = math.sin(dphi/2)**2 + math.cos(p1)*math.cos(p2)*math.sin(dlmb/2)**2
    return 2 * R * math.asin(math.sqrt(a))

def pick(cols, *cands, default=None):
    for c in cands:
        if c in cols: return c
    return default

if DATA_SOURCE.lower() == "url":
    df = pd.read_csv(IBM_URL)
    SITE_COL = pick(df.columns, "Launch Site", "LaunchSite", "site")
    LAT_COL  = pick(df.columns, "Latitude", "Lat", "latitude", "lat")
    LON_COL  = pick(df.columns, "Longitude", "Long", "Lng", "lon", "long", "longitude")
    CLS_COL  = pick(df.columns, "class", "Class", "Outcome", "Success", default="class")
    if not all([SITE_COL, LAT_COL, LON_COL]): raise ValueError("Missing site/lat/lon in URL data")
    df = df.dropna(subset=[SITE_COL, LAT_COL, LON_COL]).copy()
    df[CLS_COL] = pd.to_numeric(df.get(CLS_COL, 1), errors="coerce").fillna(1).astype(int)
    df["site_key"] = df[SITE_COL].apply(canon_site)
    df.rename(columns={LAT_COL:"Lat", LON_COL:"Long"}, inplace=True)
else:
    df = pd.read_csv(LOCAL_CSV_PATH)
    SITE_COL = "Launch Site" if "Launch Site" in df.columns else "LaunchSite"
    CLS_COL  = "class" if "class" in df.columns else "Class"
    df["site_key"] = df[SITE_COL].apply(canon_site)
    df["Lat"]  = df["site_key"].map(lambda s: SITE_COORDS.get(s, (None,None))[0])
    df["Long"] = df["site_key"].map(lambda s: SITE_COORDS.get(s, (None,None))[1])
    df = df.dropna(subset=["Lat","Long"]).copy()
    df[CLS_COL] = pd.to_numeric(df[CLS_COL], errors="coerce").fillna(1).astype(int)

m = folium.Map(location=[df["Lat"].mean(), df["Long"].mean()], zoom_start=5, tiles=TILES)
Fullscreen().add_to(m)
MousePosition(position="bottomright", prefix="Lat/Lon:", num_digits=6).add_to(m)
MeasureControl(position="topright", primary_length_unit="kilometers").add_to(m)

success_fg = folium.FeatureGroup(name="Success (green)")
failure_fg = folium.FeatureGroup(name="Failure (red)")
cluster = MarkerCluster(name="Launches") if USE_CLUSTER else None
(cluster or success_fg.add_to(m)) and (cluster or failure_fg.add_to(m))
if cluster: cluster.add_to(m)

def add_marker(lat, lon, site, outcome):
    tip = f"{site} | ({lat:.5f}, {lon:.5f}) | {'Success' if outcome==1 else 'Failure'}"
    color = "green" if outcome==1 else "red"
    marker = folium.CircleMarker([lat, lon], radius=7, weight=0, color=None,
                                 fill=True, fill_opacity=0.9, fill_color=color, tooltip=tip)
    marker.add_to(cluster if cluster else (success_fg if outcome==1 else failure_fg))

if JITTER_MODE == "ring":
    for site, grp in df.groupby("site_key"):
        slat, slon = float(grp["Lat"].iloc[0]), float(grp["Long"].iloc[0])
        n = len(grp)
        for idx, (_, r) in enumerate(grp.iterrows()):
            ring_idx, idx_in_ring = divmod(idx, MAX_PER_RING)
            on_this_ring = min(MAX_PER_RING, n - ring_idx*MAX_PER_RING)
            angle = 2*math.pi*idx_in_ring/on_this_ring if on_this_ring else 0.0
            radius_m = BASE_RADIUS_M + ring_idx*RING_GAP_M
            dlat = (radius_m/111000.0)*math.sin(angle)
            dlon = (radius_m/(111000.0*math.cos(math.radians(slat))))*math.cos(angle)
            add_marker(slat + dlat, slon + dlon, site, int(r[CLS_COL]))
else:
    for _, r in df.iterrows():
        add_marker(float(r["Lat"]), float(r["Long"]), str(r["site_key"]), int(r[CLS_COL]))

if DRAW_DISTANCE:
    for site, grp in df.groupby("site_key"):
        slat, slon = float(grp["Lat"].mean()), float(grp["Long"].mean())
        ref = COAST_REFS.get(site);  
        if not ref: continue
        clat, clon = ref; dist_km = haversine_km(slat, slon, clat, clon)
        folium.PolyLine([[slat, slon], [clat, clon]], weight=3, opacity=0.7).add_to(m)
        label = f"<div style='font-size:12px;background:#fff;padding:2px 4px;border-radius:6px;'><b>{site}</b><br/>{slat:.5f}, {slon:.5f}<br/>Distance to coast: {dist_km:.2f} km</div>"
        folium.Marker([clat, clon], icon=DivIcon(icon_size=(180,42), icon_anchor=(0,0), html=label)).add_to(m)

m.fit_bounds([[df["Lat"].min(), df["Long"].min()], [df["Lat"].max(), df["Long"].max()]])
if ADD_LEGEND:
    legend = ("<div style='position:fixed;bottom:30px;left:30px;z-index:9999;"
              "background:rgba(255,255,255,0.95);padding:8px 10px;border-radius:8px;"
              "font-size:13px;line-height:1.4;'><b>Launch Outcome</b><br>"
              "<span style='display:inline-block;width:10px;height:10px;background:green;margin-right:6px;'></span>Success<br>"
              "<span style='display:inline-block;width:10px;height:10px;background:red;margin-right:6px;'></span>Failure</div>")
    m.get_root().html.add_child(folium.Element(legend))

folium.LayerControl().add_to(m)
out_file = os.path.abspath("spacex_folium_map.html")
m.save(out_file)
print(f"[OK] Map saved to: {out_file}")
