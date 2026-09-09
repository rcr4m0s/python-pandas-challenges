import pandas as pd

# 1. Lumikha ng sample DataFrame
data = {
    'Transaction_ID': [101, 102, 103, 104],
    'Customer': ['Alice', 'Bob', 'Charlie', 'David'],
    'Amount': [2500, 1200, 3100, 800]
}
df = pd.DataFrame(data)

# 2. SAVE to CSV (index=False para walang extra row index column)
df.to_csv('sales_data.csv', index=False)
print("CSV File Successfully Saved!")

# 3. READ from CSV
loaded_df = pd.read_csv('sales_data.csv')

# 4. Challenge: Filtering loaded data
# Kuhanin lang ang transactions na ang Amount ay HIGHER than 1500
high_value_df = loaded_df[loaded_df['Amount'] > 1500]

print("\n=== HIGH VALUE TRANSACTIONS ===")
print(high_value_df)