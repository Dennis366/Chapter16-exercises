from pathlib import Path
import csv
import plotly.express as px


path = Path(__file__).parent / 'world_fires_1_day.csv'
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)


lat_index = header_row.index("latitude")
lon_index = header_row.index("longitude")
brightness_index = header_row.index("brightness")


lats, lons, brightness = [], [], []


for row in reader:
    try:
        lat = float(row[lat_index])
        lon = float(row[lon_index])
        bright = float(row[brightness_index])
    except ValueError:
        
        continue
    else:
        lats.append(lat)
        lons.append(lon)
        brightness.append(bright)

        
title = "Active Fires (Past 24 Hours)"

fig = px.scatter_geo(
    lat=lats,
    lon=lons,
    size=brightness,
    color=brightness,
    color_continuous_scale='Hot',
    hover_name=brightness,
    title=title,
    projection='natural earth',
    labels={'color':'Brightness'}
)

fig.show()


