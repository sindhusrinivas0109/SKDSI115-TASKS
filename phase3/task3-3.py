# iii) Managing Time Zones in Panda

import pandas as pd

# Create a datetime with time zone (UTC)
dt_with_tz = pd.Timestamp('2024-05-01 12:00:00', tz='UTC')

# Localize to a specific time zone (convert to South Korea time, KST)
dt_localized_korea = dt_with_tz.tz_convert('Asia/Seoul')

print("Datetime with Time Zone (UTC):", dt_with_tz)
print("Localized Datetime (South Korea - KST):", dt_localized_korea)
