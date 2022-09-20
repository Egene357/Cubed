import matplotlib.pyplot as plt

# Data.
x_data = list(range(7001))
cubed = [x**3 for x in x_data]

# Graph.
plt.style.use('seaborn-darkgrid')
fig, ax = plt.subplots()
ax.scatter(x_data, cubed, c=cubed, cmap=plt.cm.Oranges, s=15)

# Chart title and axes labels.
ax.set_title("Cubed Data", fontsize=25)
ax.set_xlabel('Data', fontsize=15)
ax.set_ylabel('Cubed', fontsize=15)

# Range for each axis and size of tick labels.
ax.axis([0, 7100, 0, 7100**3])
ax.tick_params(axis='both', labelsize=15)

# Save and show graph.
plt.savefig('cubed_numbers_graph.png', bbox_inches='tight')
plt.show()
