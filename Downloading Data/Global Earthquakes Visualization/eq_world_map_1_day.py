import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data.
filename = 'data/eq_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

mags, lons, lats = [], [], [] # empty list to store the magnitudes, longitudes, and latitudes
for eq_dict in all_eq_dicts: # loop through each dictionary in the list
    mag = eq_dict['properties']['mag'] # extract the value associated with 'mag' key
    lon = eq_dict['geometry']['coordinates'][0] # extract the value associated with 'coordinates' key
    lat = eq_dict['geometry']['coordinates'][1] # extract the value associated with 'coordinates' key
    if mag > 1:
        mags.append(mag) # append the value to the list mags
        lons.append(lon) # append the value to the list lons
        lats.append(lat) # append the value to the list lats

    # print(mags)
    # print the length of the list

print(len(mags))


# Map the earthquakes.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'size': [5*mag for mag in mags],
    },
}]
# other way to write, but not as good: 
# data = [Scattergeo(lon=lons, lat=lats)]
my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
