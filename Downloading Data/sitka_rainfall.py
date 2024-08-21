import csv
from datetime import datetime

import matplotlib.pyplot as plt

# filename = 'data/sitka_weather_2018_simple.csv'
filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)

    # to make it easier to understand the file header data, 
    # we can print each header and its position in the list:
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    # Get dates, and high and low temperatures from this file.
    dates, prcps= [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        prcp = float(row[3])
        dates.append(current_date)
        prcps.append(prcp)


# Plot the high and low temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, prcps, c='blue') # alpha is the transparency of the line 
# the fill_between() method fills the space between the two data series with a color that we specify, 
# it takes the x-values and two y-values
# ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1) # alpha is the transparency of the fill


# Format plot.
plt.title("Daily rainfall in Death Valley, CA - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Percipitation (mm)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()