import numpy as np
import pandas as pd


raw_data = {
    'Item': ['Laptop', 'Mouse', 'Monitor', 'Keyboard', 'Desk', 'Chair'],
    'Category': ['Tech', 'Tech', 'Tech', 'Tech', 'Office', 'Office'],
    'Price': [1000, 25, 200, 50, 150, 100],
    'Units': [5, np.nan, 3, 10, np.nan, 4],
}
pd.DataFrame(raw_data).to_csv('raw_sales.csv', index=False)




df = pd.read_csv('raw_sales.csv')
df['Units'] = df['Units'].fillna(0)

clean_df = df[df['Units'] > 0]
clean_df['Total_Cost'] = clean_df['Units'] * clean_df['Price']

summary = clean_df.groupby('Category')['Total_Cost'].sum()
summary.to_csv('category_summary.csv')

print('=== CATEGORY SUMMARY ===')
print(summary)