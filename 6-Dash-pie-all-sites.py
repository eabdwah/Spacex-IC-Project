from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

CSV_PATH = r"C:\Users\whas3\Desktop\Data World\My projects\I-C\spacex_launch_dash.csv"

df = pd.read_csv(CSV_PATH)
site_col = "Launch Site" if "Launch Site" in df.columns else "LaunchSite"
class_col = "class" if "class" in df.columns else "Class"

success_counts = (
    df[df[class_col] == 1]
      .groupby(site_col)
      .size()
      .reset_index(name="Successes")
      .sort_values("Successes", ascending=False)
)

fig = px.pie(success_counts, values="Successes", names=site_col, title="Launch Success Count by Site", hole=0.25)
fig.update_traces(textposition="inside", textinfo="percent+label")
fig.update_layout(margin=dict(l=30,r=30,t=60,b=30))

app = Dash(__name__)
app.title = "SpaceX Success Pie"
app.layout = html.Div(
    style={"maxWidth":"900px","margin":"40px auto","fontFamily":"system-ui, sans-serif"},
    children=[ html.H2("Launch Success Count for All Sites"), dcc.Graph(figure=fig) ]
)

if __name__ == "__main__":
    app.run(debug=True, port=8050)
