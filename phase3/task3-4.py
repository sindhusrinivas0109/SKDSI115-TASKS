# iv) Performing Period Arithmetic and Using period_range

import pandas as pd

# Create a period and perform arithmetic
start_period = pd.Period('2024-01', freq='M')
end_period = start_period + 3  # Add 3 months to the start period

print("Start Period:", start_period)
print("End Period (Start Period + 3 months):", end_period)

# Create a range of periods
period_range = pd.period_range(start='2024-01', end='2024-12', freq='M')

print("\nPeriod Range for 2024:")
print(period_range)
