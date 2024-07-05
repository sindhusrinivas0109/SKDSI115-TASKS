import pandas as pd

# Create a Series with hierarchical index
index = [['Group1', 'Group1', 'Group2', 'Group2'], [1, 2, 1, 2]]
values = [10, 20, 30, 40]
series = pd.Series(values, index=index)
print("\nSeries with Hierarchical Index:")
print(series)

# Select subsets of data with hierarchical indexing
subset_outer = series.loc['Group1']
subset_inner = series.loc[('Group2', 1)] 

print("\nSubset of Data (Outer Level):")
print(subset_outer)
print("\nSubset of Data (Inner Level):")
print(subset_inner)
