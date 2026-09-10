import pandas as pd

data = {
    'Timestamp': pd.date_range(start='2026-09-01 00:00:00', periods=12, freq='2h'),
    'Clicks': [150, 200, 180, 300, 450, 500, 600, 550, 400, 350, 250, 180]
}
df = pd.DataFrame(data)

df['Hour'] = df['Timestamp'].dt.hour

df = df.set_index('Timestamp')

df['3Period_Rolling'] = df['Clicks'].rolling(window=3, min_periods=1).mean()

six_hour_summary = df['Clicks'].resample('6h').sum().reset_index()

print(df)
print(six_hour_summary)