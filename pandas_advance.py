import pandas as pd

data = {
    'Product': ['Laptop', 'Mouse', 'Monitor', 'Keyboard'],
    'Category': ['Electronics', 'Accessories', 'Electronics', 'Accessories'],
    'Price': [45000, 1200, 15000, 3500],
    'Stock': [10, 50, 15, 30]
}

df = pd.DataFrame(data)

filtered_df = df[(df['Category'] == 'Electronics') & (df['Stock'] > 10)]
print("=== Filtered (Electronics & Stock > 10) ===")
print(filtered_df)
df['Total_Inventory_Value'] = df['Price'] * df['Stock']
print("==== UPDATED FRAME ====")
print(df)