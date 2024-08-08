# Import the pyplot module from the matplotlib library as plt
# This is a simple plot of the first five square numbers
import matplotlib.pyplot as plt 

# Define a list of numbers
# override default behavior of first data point being 0 by setting input values to 1, 2, 3, 4, 5
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# Style the plot 
# plt.style.use('dark_background')
plt.style.use('seaborn-v0_8-pastel')


# available styles:
# ['Solarize_Light2', '_classic_test_patch', '_mpl-gallery', '_mpl-gallery-nogrid', 'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn-v0_8', 'seaborn-v0_8-bright', 'seaborn-v0_8-colorblind', 'seaborn-v0_8-dark', 'seaborn-v0_8-dark-palette', 'seaborn-v0_8-darkgrid', 'seaborn-v0_8-deep', 'seaborn-v0_8-muted', 'seaborn-v0_8-notebook', 'seaborn-v0_8-paper', 'seaborn-v0_8-pastel', 'seaborn-v0_8-poster', 'seaborn-v0_8-talk', 'seaborn-v0_8-ticks', 'seaborn-v0_8-white', 'seaborn-v0_8-whitegrid', 'tableau-colorblind10']

# Create a figure and axis using the subplots() function
fig, ax = plt.subplots()

# Plot the squares list on the axis 
# ax.plot(input_values, squares, linewidth=3)

# Set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', labelsize=14)

# Display the plot
plt.show()

