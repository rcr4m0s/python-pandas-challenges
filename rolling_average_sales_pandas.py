import pandas as pd

# Daily Sales Data
data = {
    'Date': ['2026-03-01', '2026-03-02', '2026-03-03', '2026-03-04', '2026-03-05', '2026-03-06'],
    'Sales': [1000.0, 1500.0, 1200.0, 1800.0, 2000.0, 2500.0]
}

df = pd.DataFrame(data)

# 1. Convert 'Date' to datetime and set as Index (kailangan para sa smooth time-series alignment)
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')

# 2. Calculate 3-Day Rolling Average
# window=3 ibig sabihin kukunin ang average ng kasalukuyang araw at nung nagdaang 2 araw
df['3Day_Rolling_Avg'] = df['Sales'].rolling(window=3).mean()
df['3Day_Rolling_Avg'] = df['Sales'].rolling(window=3, min_periods=1).mean()
df['3Day_Rolling_Avg'] = df['3Day_Rolling_Avg'].bfill()

print("--- Daily Sales with 3-Day Rolling Average ---")
print(df)