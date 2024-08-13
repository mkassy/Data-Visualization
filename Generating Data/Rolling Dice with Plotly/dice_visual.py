from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create two D6 dice.
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list.
# List comprehension version:
results = [die_1.roll() * die_2.roll() for roll_num in range(1000)]
# or for loop version:
# results = []
# for roll_num in range(1000):
#     result = die_1.roll() * die_2.roll()
#     results.append(result)

# print(results)

# Analyze the results.

# List comprehension version:
max_result = die_1.num_sides * die_2.num_sides
frequencies = [results.count(value) for value in range(1, max_result+1)]

# for loop version:
# frequencies = []
# max_result = die_1.num_sides * die_2.num_sides
# for value in range(1, max_result+1):
#     frequency = results.count(value)
#     frequencies.append(frequency)

# print(frequencies)

# Visualize the results.
# Plotly doesn't accept the results of the range() function directly, so we need to convert the results to a list
# using the list() function.
x_values = list(range(1, max_result+1))
# The Plotly class Bar() represents a data set that will be formatted as a bar chart.
# The class must be wrapped in square brackets bc a data set can have multiple elements.
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}

# The Layout class represents the overall layout of the chart.
# The title attribute gives the chart a title.
# The xaxis attribute is a dictionary that formats the x-axis.
# The yaxis attribute is a dictionary that formats the y-axis.
# The Layout object is wrapped in a dictionary, which Plotly expects.

my_layout = Layout(
    title='Results of rolling two D6 1000 times (multiplication)',
    title_x=0.5, # Center the title horizontally.
    xaxis=x_axis_config, 
    yaxis=y_axis_config
    )
# The offline() function generates the chart file, which is named d6.html.
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6_multiplication.html')