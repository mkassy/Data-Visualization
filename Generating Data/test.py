import matplotlib.pyplot as plt

# Create a figure with a 2x2 grid of subplots (Axes)
fig, axs = plt.subplots(2, 2)

# Each subplot (Axes) can be used to plot different data
axs[0, 0].plot([1, 2, 3], [4, 5, 6])  # This is a subplot (Axes) in the top-left corner
axs[0, 1].scatter([1, 2, 3], [4, 5, 6])  # This is a subplot (Axes) in the top-right corner
axs[1, 0].bar(['A', 'B', 'C'], [1, 2, 3])  # This is a subplot (Axes) in the bottom-left corner
axs[1, 1].hist([1, 2, 2, 3, 3, 3], bins=3)  # This is a subplot (Axes) in the bottom-right corner

plt.show()
