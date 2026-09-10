import pandas as pd


data = {
    'Transaction_ID': [101, 102, 103, 104],
    'Customer': ['Alice', 'Bob', 'Charlie', 'David'],
    'Amount': [2500, 1200, 3100, 800]
}
df = pd.DataFrame(data)


df.to_csv('sales_data.csv', index=False)
print("CSV File Successfully Saved!")

loaded_df = pd.read_csv('sales_data.csv')

high_value_df = loaded_df[loaded_df['Amount'] > 1500]

print("\n=== HIGH VALUE TRANSACTIONS ===")
print(high_value_df)