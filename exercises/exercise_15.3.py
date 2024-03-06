import matplotlib.pyplot as plt

from Matplotlib_example.random_walk import RandomWalk


# Make random walks and plot them
rw = RandomWalk(5000)
rw.fill_walk()

# Display point at the diagram
plt.style.use('classic')
fig, ax = plt.subplots(figsize=(16, 10))
point_numbers = range(rw.num_points)

plt.plot(rw.x_values, rw.y_values, linewidth=2)

# Delete the axes
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()