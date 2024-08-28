import csv 

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data.
filename = 'data/world_fires_1_day.csv'
lats, lons, brights = [], [], []
# center the title in the middle of the map
title = {'text': 'World Fires in the Last 24 Hours', 'x': 0.5, 'xanchor': 'center'}


with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    latitude_index = header_row.index('latitude')
    longitude_index = header_row.index('longitude')
    bright_index = header_row.index('brightness')

    # Get latitude, longitude and brightness for each fire.
    for row in reader:
        try:
            lat = float(row[latitude_index])
            lon = float(row[longitude_index])
            bright = float(row[bright_index])
        except ValueError:
            print(f'Missing data for {row}')
        else:
            lats.append(lat)
            lons.append(lon)
            brights.append(bright)


data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'size': [bright/100 for bright in brights],
        'color': brights,
        'colorscale': 'hot',
        # 'reversescale': True,
        'colorbar': {'title': 'Brightness'},
    },
}]

my_layout = Layout(title=title)
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='world_fires_map_1_day.html')
