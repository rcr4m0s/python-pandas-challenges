import pandas as pd


data = {
    'Product': ['Laptop', 'Mouse', 'Monitor', 'Keyboard'],
    'Category': ['Electronics', 'Accessories', 'Electronics', 'Accessories'],
    'Price': [45000, 1200, 15000, 3500],
    'Stock': [10, 50, 15, 30]
}

df = pd.DataFrame(data)

electronics_df = df[df['Category'] == 'Electronics']
print("============ Filtering ===========")
print(electronics_df)
high_value_filter = df[df['Price'] >= 15000]
print("======== High Value Filter =========")
print(high_value_filter)
analytics = (df['Price'].mean())
print("Analytics:", analytics)