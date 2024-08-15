import csv

filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)

    # to make it easier to understand the file header data, 
    # we can print each header and its position in the list:
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    # First we'll get high temperatures from this file.
    highs = []
    for row in reader:
        high = int(row[6])
        highs.append(high)

    print(highs)
