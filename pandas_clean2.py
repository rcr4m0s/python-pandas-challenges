import pandas as pd
import numpy as np

orders = pd.DataFrame({
    'Order_ID': ['ORD1', 'ORD2', 'ORD3', 'ORD4', 'ORD5', 'ORD6'],
    'Payment_Method': ['GCash', np.nan, 'Card', 'GCash', np.nan, 'Cash'],
    'Amount_PHP': [1500, 2300, np.nan, 4100, 1200, np.nan],
    'Delivery_Status': ['Delivered', 'Pending', 'Delivered', np.nan, np.nan, 'Pending']
})

missing_values = orders.isnull().sum()
orders['Payment_Method'] = orders['Payment_Method'].fillna('Unknown')
filterz = orders['Amount_PHP'].median()
orders['Amount_PHP'] = orders['Amount_PHP'].fillna(filterz)
remove_next_np = orders.dropna()

print("=== MISSING VALUES COUNT ===")
print(missing_values)
print("\n=== CLEANED DATAFRAME ===")
print(remove_next_np)
