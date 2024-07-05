# 2)scatter plot

import numpy as np
import matplotlib.pyplot as plt

# Generate sample data for scatter plot
np.random.seed(0)
x = np.random.normal(loc=0, scale=1, size=100)
y = 2 * x + np.random.normal(loc=0, scale=1, size=100)

# Create scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='green', alpha=0.5)
plt.title('Scatter Plot: Relationship between Two Variables')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)

plt.show()
