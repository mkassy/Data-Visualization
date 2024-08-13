import matplotlib.pyplot as plt
from die import Die

# Create two D6 dice.
die_1 = Die()
die_2 = Die()

# List comprehension version:
results = [die_1.roll() * die_2.roll() for roll_num in range(1000)]

# Analyze the results.
# List comprehension version:
max_result = die_1.num_sides * die_2.num_sides
frequencies = [results.count(value) for value in range(1, max_result+1)]

# Visualize the results using matplotlib
x_values = list(range(1, max_result+1))

# plt.bar(x_values, frequencies, color='skyblue')                
                
# plt.title('Results of rolling two D6 1000 times (multiplication)')
# plt.xlabel('Result', fontsize=14)
# plt.ylabel('Frequency of Result', fontsize=14)

# plt.xticks(x_values)
# plt.yticks(range(0, max(frequencies)+1, 10))

# Create a figure and axis
fig, ax = plt.subplots(figsize=(12, 6), dpi=128)

# plot a bar chart
ax.bar(x_values, frequencies, color='skyblue')

ax.set_title('Results of rolling two D6 1000 times (multiplication)')
ax.set_xlabel('Result')
ax.set_ylabel('Frequency of Result')

# ax.tick_params(axis='both', which='major', labelsize=14)

# ax.hist takes a list of results, the number of bins, and the range of the results.
# the number of bins is the number of possible results
# the range is the range of possible results
# align='left' aligns the bars with the left edge of the bin
# rwidth=0.8 sets the width of the bars to 80% of the bin width

# ax.hist(results, bins=max_result, range=(1, max_result+1), align='left', rwidth=0.8)



# plt.bar(x_values, frequencies, )

plt.xticks(x_values)

plt.show()