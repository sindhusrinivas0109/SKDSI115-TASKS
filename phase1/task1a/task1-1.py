import pandas as pd
import numpy as np

# Create DataFrame with missing data
data = {
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, 7, 8],
    'C': ['a', 'b', np.nan, 'd']
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Identify missing data
missing_data = df.isna()
print("\nMissing Data:")
print(missing_data)

# Filter out missing data
df_filtered = df.dropna()
print("\nDataFrame after Filtering out Missing Data:")
print(df_filtered)

# Fill missing data
# We can fill missing values in numeric columns with their mean
numeric_cols = df.select_dtypes(include=[np.number]).columns
df_filled = df.copy()  # Make a copy to preserve the original DataFrame
df_filled[numeric_cols] = df_filled[numeric_cols].fillna(df_filled[numeric_cols].mean())
print("\nDataFrame after Filling Missing Data:")
print(df_filled)

# Remove duplicates
df_unique = df.drop_duplicates()
print("\nDataFrame after Removing Duplicates:")
print(df_unique)

