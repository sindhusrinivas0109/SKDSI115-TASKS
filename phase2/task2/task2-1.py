import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generate sample data
np.random.seed(0)
data = np.random.normal(loc=0, scale=1, size=1000)

# Create figure and axes for subplots
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(14, 6))

# Plot histogram with density plot (KDE) on the first subplot (ax1)
sns.histplot(data, kde=True, bins=30, color='skyblue', ax=ax1)
ax1.set_title('Histogram with Density Plot (KDE)')
ax1.set_xlabel('Value')
ax1.set_ylabel('Density')

# Plot KDE (density plot) on the second subplot (ax2)
sns.kdeplot(data, color='orange', ax=ax2)
ax2.set_title('Density Plot (KDE)')
ax2.set_xlabel('Value')
ax2.set_ylabel('Density')

# Adjust layout and display the plots
plt.tight_layout()
plt.show()
