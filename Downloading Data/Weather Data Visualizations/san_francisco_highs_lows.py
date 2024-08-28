import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/san_francisco_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)

    # to make it easier to understand the file header data, 
    # we can print each header and its position in the list:
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    # Get dates, and high and low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
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
title = "Daily high and low temperatures - 2018\nSan Francisco, CA"
ax.set_title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

# settings for y-axis scales to match the Death Valley plot
plt.ylim(-20, 130)

plt.show()