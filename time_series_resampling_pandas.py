import pandas as pd

data = {
    'Date': ['2026-03-01', '2026-03-02', '2026-03-03', '2026-03-08', '2026-03-09', '2026-03-15'],
    'Sales': [500.0, 700.0, 800.0, 1200.0, 1500.0, 2000.0]
}

df = pd.DataFrame(data)

df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')
weekly_df = df['Sales'].resample('W').sum().reset_index()

print(weekly_df)