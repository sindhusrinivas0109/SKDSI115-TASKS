# ii) Using pandas.date_range to Generate a DatetimeIndex

import pandas as pd

# Generate a DatetimeIndex with indicated length (10 days)
date_range = pd.date_range(start='2024-05-01', periods=10, freq='D')

print("DatetimeIndex with 10 Days:")
print(date_range)
