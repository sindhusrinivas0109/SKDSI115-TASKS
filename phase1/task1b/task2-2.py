import pandas as pd
import matplotlib.pyplot as plt

# Create sample DataFrame for side-by-side bar plots
data_side_by_side = {
    'Category': ['A', 'B', 'C'],
    'Value1': [10, 20, 30],
    'Value2': [15, 25, 35]
}
df_side_by_side = pd.DataFrame(data_side_by_side)
df_side_by_side.set_index('Category', inplace=True)  # Set 'Category' column as index

# Create sample DataFrame for stacked bar plots
data_stacked = {
    'Category': ['A', 'B', 'C'],
    'Value1': [10, 20, 30],
    'Value2': [15, 25, 35]
}
df_stacked = pd.DataFrame(data_stacked)
df_stacked.set_index('Category', inplace=True)  # Set 'Category' column as index

# Create a figure and subplots for both plots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))

# Plot side-by-side bar plots
df_side_by_side.plot(kind='bar', ax=axes[0], width=0.4)
axes[0].set_title('Side-by-Side Bar Plots')
axes[0].set_xlabel('Category')
axes[0].set_ylabel('Value')

# Plot stacked bar plots
df_stacked.plot(kind='bar', stacked=True, ax=axes[1])
axes[1].set_title('Stacked Bar Plots')
axes[1].set_xlabel('Category')
axes[1].set_ylabel('Value')

# Adjust layout and display the combined plots
plt.tight_layout()  # Adjust subplot parameters to give specified padding
plt.show()
