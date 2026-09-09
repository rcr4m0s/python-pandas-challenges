import pandas as pd

customers = pd.DataFrame({
    'CustomerID': ['C1', 'C2', 'C3'],
    'Name': ['Alex', 'Bea', 'Charlie']
})

# Data 2: Transactions
orders = pd.DataFrame({
    'OrderID': [101, 102, 103, 104],
    'CustomerID': ['C1', 'C2', 'C1', 'C3'],
    'Amount': [250.0, 150.0, 300.0, 400.0]
})

merged_df = pd.merge(orders, customers, on='CustomerID', how='inner')
total_spend = merged_df.groupby('Name')['Amount'].sum().reset_index()

print("--- TOTAL SPEND PER CUSTOMER ---")
print(total_spend)