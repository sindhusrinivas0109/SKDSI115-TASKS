import matplotlib.pyplot as plt
import numpy as np

# Generate sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create a figure and subplots
fig, ax = plt.subplots()

# Plot the data
ax.plot(x, y1, label='sin(x)', color='blue', linestyle='-', linewidth=2)  # Line for sin(x)
ax.plot(x, y2, label='cos(x)', color='red', linestyle='--', linewidth=2)  # Line for cos(x)

# Customize the plot
ax.set_title('Sine and Cosine Functions')  # Set title
ax.set_xlabel('x-axis')  # Set x-axis label
ax.set_ylabel('y-axis')  # Set y-axis label
ax.set_xticks(np.linspace(0, 10, 5))  # Set x-axis ticks
ax.set_xticklabels(['0', '2.5', '5', '7.5', '10'])  # Set x-axis tick labels
ax.set_yticks([-1, 0, 1])  # Set y-axis ticks
ax.annotate('Peak', xy=(np.pi/2, 1), xytext=(np.pi/2 + 1, 1.5),
            arrowprops=dict(facecolor='black', shrink=0.05))  # Annotate a point

# Add legend
ax.legend()

# Save the plot
plt.savefig('line_graph.png')

# Show the plot
plt.show()
