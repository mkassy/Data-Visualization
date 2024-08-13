import matplotlib.pyplot as plt
import numpy as np

# Sample data
data = np.random.randn(1000)  # Normally distributed data

# Create a figure and an axis
fig, ax = plt.subplots()

# Plot a histogram
ax.hist(data, bins=30, color='lightgreen')

# Customize the plot
ax.set_title('Histogram Example')
ax.set_xlabel('Data Values')
ax.set_ylabel('Frequency')

# Display the plot
plt.show()
