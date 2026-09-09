import numpy as np
import pandas as pd

# Setup raw data (Do not modify)
raw_orders = {
    'Order_ID': [1, 2, 3, 4, 5, 6],
    'Region': ['North', 'South', 'North', 'South', 'North', 'South'],
    'Price_Per_Item': [150, 200, np.nan, 300, 100, 250],
    'Quantity': [2, 1, 4, np.nan, 5, 2],
}
pd.DataFrame(raw_orders).to_csv('raw_orders.csv', index=False)

df = pd.read_csv('raw_orders.csv')
df['Price_Per_Item'] = df['Price_Per_Item'].fillna(df['Price_Per_Item'].mean())
