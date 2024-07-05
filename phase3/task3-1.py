# i) Creating Time Series Using datetime Object in Pandas

import pandas as pd

# Create a time series with datetime index
dates = ['2024-05-01', '2024-05-02', '2024-05-03', '2024-05-04', '2024-05-05']
values = [10, 20, 15, 25, 30]

# Convert dates to datetime objects
date_index = pd.to_datetime(dates)

# Create a Series with datetime index
time_series = pd.Series(values, index=date_index)

print("Time Series with Datetime Index:")
print(time_series)
