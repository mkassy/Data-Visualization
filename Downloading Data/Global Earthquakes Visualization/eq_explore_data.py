import json

# Explore the structure of the data.
filename = 'data/eq_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

# readable_file = 'data/readable_eq_data.json'

# with open(readable_file, 'w') as f:
#     json.dump(all_eq_data, f, indent=4)
# once we have the data, we can go ahead and delete the code that writes the data to a file.

all_eq_dicts = all_eq_data['features']
# print(len(all_eq_dicts))
# we took the value associated with 'features', which is a list of dictionaries.
# we printed the length of that list to see how many earthquakes we have data for.


# Extracting Magnitudes and Location Data
mags, lons, lats = [], [], [] # empty list to store the magnitudes, longitudes, and latitudes
for eq_dict in all_eq_dicts: # loop through each dictionary in the list
    mag = eq_dict['properties']['mag'] # extract the value associated with 'mag' key
    lon = eq_dict['geometry']['coordinates'][0] # extract the value associated with 'coordinates' key
    lat = eq_dict['geometry']['coordinates'][1] # extract the value associated with 'coordinates' key
    mags.append(mag) # append the value to the list mags
    lons.append(lon) # append the value to the list lons
    lats.append(lat) # append the value to the list lats

print(mags[:10])
print(lons[:5])
print(lats[:5])















