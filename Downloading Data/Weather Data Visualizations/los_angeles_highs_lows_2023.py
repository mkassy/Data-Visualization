import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/los_angeles_weather_2023_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)

    # to make it easier to understand the file header data, 
    # we can print each header and its position in the list:
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    # Find the indexes for the TMIN, TMAX, and station name columns.
    date_idx = header_row.index('DATE')
    tmin_idx= header_row.index('TMIN')
    tmax_idx= header_row.index('TMAX')
    station_idx = header_row.index('NAME')
    

    # Get dates, and high and low temperatures from this file.
    dates, highs, lows = [], [], []
    station_name = ''
    for row in reader:        
        current_date = datetime.strptime(row[date_idx], '%Y-%m-%d')
        try:
            high = int(row[tmax_idx])
            low = int(row[tmin_idx])
            if station_name == '':
                station_name = row[station_idx] # get the station name
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)


# Plot the high and low temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5) # alpha is the transparency of the line 
ax.plot(dates, lows, c='blue', alpha=0.5) # alpha is the transparency of the line
# the fill_between() method fills the space between the two data series with a color that we specify, 
# it takes the x-values and two y-values
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1) # alpha is the transparency of the fill


# Format plot.
title = f"Daily high and low temperatures - {current_date.year}\n{station_name}"
ax.set_title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

# settings for y-axis scales to match the Death Valley plot
plt.ylim(-20, 130)

plt.show()