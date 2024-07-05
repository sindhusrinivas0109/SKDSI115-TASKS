import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Generate sample data for box plot
np.random.seed(0)
categories = np.random.choice(['A', 'B', 'C', 'D'], size=100)
values = np.random.normal(loc=0, scale=1, size=100)

# Create DataFrame from sample data
df_box = pd.DataFrame({'Category': categories, 'Value': values})

# Create box plot
plt.figure(figsize=(8, 6))
sns.boxplot(x='Category', y='Value', data=df_box, palette='pastel', hue='Category', legend=False)
plt.title('Box Plot: Distribution of Values across Categories')
plt.xlabel('Category')
plt.ylabel('Value')
plt.grid(True)

plt.show()
