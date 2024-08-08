import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

# to plot a single point rather than a line:
ax.scatter(2,4)

plt.show()