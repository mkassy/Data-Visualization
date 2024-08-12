import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making random walks, as long as the program is active.
while True:
    # Make a random walk, and plot the points.
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('classic')
    # fig, ax = plt.subplots(figsize=(15, 9))
    # the figsize parameter takes a tuple, which tells matplotlib the dimensions of the plotting window in inches
    # the dpi parameter controls the resolution of the plot
    # without the dpi parameter, the plot will be displayed at the default resolution of your monitor (usually 80 dots per inch)
    # so the resolution would not be as good as it could be 
    # a higher dpi value will make the plot smoother and more detailed
    fig, ax = plt.subplots(figsize=(10, 6), dpi=128)

    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)

    # Emphasize the first and last points.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break