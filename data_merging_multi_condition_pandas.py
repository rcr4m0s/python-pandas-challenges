import pandas as pd
import numpy as np

# 1. Customer Profiles Dataset
customers = pd.DataFrame({
    'CustomerID': ['C101', 'C102', 'C103', 'C104'],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Membership': ['Gold', 'Silver', 'Bronze', 'Gold']
})

# 2. Orders Dataset (May missing amounts & values)
orders = pd.DataFrame({
    'OrderID': ['ORD01', 'ORD02', 'ORD03', 'ORD04', 'ORD05', 'ORD06'],
    'CustomerID': ['C101', 'C102', 'C101', 'C104', 'C103', 'C102'],
    'Amount_PHP': [2500.0, np.nan, 1800.0, 3200.0, np.nan, 1400.0],
    'Status': ['Completed', 'Completed', 'Cancelled', 'Completed', 'Completed', 'Completed']
})

median_val = orders['Amount_PHP'].median()
orders['Amount_PHP'].fillna(median_val, inplace = True)

merged_df = pd.merge(orders, customers, on='CustomerID', how='inner')

completed_orders = merged_df[merged_df['Status'] == 'Completed']
tier_summary = completed_orders.groupby('Membership')['Amount_PHP'].agg(['sum', 'mean', 'count']).reset_index()

print("--- CLEANED & MERGED DATASET ---")
print(merged_df)
print("\n--- COMPLETED SPENDING PER MEMBERSHIP TIER ---")
print(tier_summary)