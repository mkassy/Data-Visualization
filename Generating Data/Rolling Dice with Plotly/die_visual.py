from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

# Create a D6.
die = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# print(results)

# Analyze the results.
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

# Visualize the results.
# Plotly doesn't accept the results of the range() function directly, so we need to convert the results to a list
# using the list() function.
x_values = list(range(1, die.num_sides+1))
# The Plotly class Bar() represents a data set that will be formatted as a bar chart.
# The class must be wrapped in square brackets bc a data set can have multiple elements.
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}

# The Layout class represents the overall layout of the chart.
# The title attribute gives the chart a title.
# The xaxis attribute is a dictionary that formats the x-axis.
# The yaxis attribute is a dictionary that formats the y-axis.
# The Layout object is wrapped in a dictionary, which Plotly expects.

my_layout = Layout(
    title='Results of rolling one D6 1000 times',
    title_x=0.5, # Center the title horizontally.
    xaxis=x_axis_config, 
    yaxis=y_axis_config
    )
# The offline() function generates the chart file, which is named d6.html.
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')