import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data.
filename = 'data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

# Extract the title from the metadata
title = all_eq_data['metadata']['title']

# Extract the list of all earthquakes
all_eq_dicts = all_eq_data['features']

mags, lons, lats, hover_texts = [], [], [], [] # empty list to store the magnitudes, longitudes, and latitudes
for eq_dict in all_eq_dicts: # loop through each dictionary in the list
    # mag = eq_dict['properties']['mag'] # extract the value associated with 'mag' key
    # lon = eq_dict['geometry']['coordinates'][0] # extract the value associated with 'coordinates' key
    # lat = eq_dict['geometry']['coordinates'][1] # extract the value associated with 'coordinates' key
    # title = eq_dict['properties']['title']
    if (mag := eq_dict['properties']['mag']) is not None and mag > 1:        
        mags.append(mag) # append the value to the list mags
        lons.append(eq_dict['geometry']['coordinates'][0]) # append the value to the list lons
        lats.append(eq_dict['geometry']['coordinates'][1]) # append the value to the list lats
        hover_texts.append(eq_dict['properties']['title'])


# Map the earthquakes.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    },
}]
# other way to write, but not as good: 
# data = [Scattergeo(lon=lons, lat=lats)]
my_layout = Layout(
    title={
        'text': title, # Use the extracted title
        'x': 0.5,
        'xanchor': 'center',
        'font': {
            'size': 24
        }
    })

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes_30_days.html')
