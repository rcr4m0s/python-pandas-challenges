import pandas as pd

# Dataset: Store Transactions with Date Strings
data = {
    'TxnID': ['T1', 'T2', 'T3', 'T4', 'T5', 'T6'],
    'Date': ['2026-01-05', '2026-01-10', '2026-01-18', '2026-02-01', '2026-02-14', '2026-02-22'],
    'Amount': [1200.0, 850.0, 2300.0, 3100.0, 1500.0, 4200.0]
}

df = pd.DataFrame(data)

# 1. Convert 'Date' column to datetime using pd.to_datetime()
df['Date'] = pd.to_datetime(df['Date'])

# 2. Extract Month Name and Day Name into new columns
df['Month'] = df['Date'].dt.month_name()
df['Day_Name'] = df['Date'].dt.day_name()

# 3. Create a boolean column 'Is_Weekend' (Saturday/Sunday)
df['Is_Weekend'] = df['Date'].dt.dayofweek >= 5

# 4. Group by 'Month' and compute total Amount
monthly_summary = df.groupby('Month')['Amount'].sum().reset_index()
weekend_summary = df.groupby('Is_Weekend')['Amount'].agg(['sum', 'mean', 'count']).reset_index()
print("--- Parsed Time-Series Data ---")
print(df)

print("\n--- Monthly Revenue Summary ---")
print(monthly_summary)


print("\n--- Weekend vs Weekday Performance ---")
print(weekend_summary)