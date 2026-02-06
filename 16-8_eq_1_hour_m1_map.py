from pathlib import Path
import json
import plotly.express as px


path = Path(__file__).parent / 'eq_1_hour_m1.geojson'
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)


all_eq_dicts = all_eq_data['features']


mags, lons, lats, titles = [], [], [], []

for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    titles.append(eq_dict['properties']['title'])


title = all_eq_data['metadata']['title']


fig = px.scatter_geo(
    lat=lats,
    lon=lons,
    size=mags,
    color=mags,
    hover_name=titles,
    title=title,
    color_continuous_scale='Plasma',
    labels={'color':'Magnitude'},
    projection='natural earth'
)

fig.show()
