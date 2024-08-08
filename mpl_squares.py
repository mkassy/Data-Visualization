# Import the pyplot module from the matplotlib library as plt
# This is a simple plot of the first five square numbers
import matplotlib.pyplot as plt 

squares = [1, 4, 9, 16, 25]

# Create a figure and axis using the subplots() function
fig, ax = plt.subplots()

# Plot the squares list on the axis 
ax.plot(squares)

# Display the plot
plt.show()