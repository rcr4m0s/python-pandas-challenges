import pandas as pd

# 1. Dataset
data = {
    'Date': pd.date_range(start='2026-04-01', periods=10, freq='D'),
    'Sales': [1200, 1500, 1100, 1800, 2000, 2200, 1900, 2500, 2800, 3000]
}
df = pd.DataFrame(data)

# 2. Extract Day_Name (Dahil datetime object na agad si pd.date_range, pwede agad ang .dt)
df['Day_Name'] = df['Date'].dt.day_name()

df = df.set_index('Date')
df['3Day_Rolling'] = df['Sales'].rolling(window=3, min_periods=1).mean()
weekly_total = df['Sales'].resample('W').sum().reset_index()

print("--- DAILY DATA WITH ROLLING AVERAGE ---")
print(df)
print("\n--- WEEKLY TOTAL SALES ---")
print(weekly_total)