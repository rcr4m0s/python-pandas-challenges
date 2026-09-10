import pandas as pd

data = {
    'Product_ID': [501, 502, 502, 503, 504],
    'Item_Name': [' LAPTOP ', 'mouse', 'MOUSE', ' keyboard ', 'MONITOR'],
    'Price': [45000, 1200, 1200, None, 15000],
    'Stock': [10, 50, 50, 30, None]
}
df = pd.DataFrame(data)

df['Item_Name'] = df['Item_Name'].str.strip().str.title()

df = df.drop_duplicates()

median_price = df['Price'].median()
df['Price'] = df['Price'].fillna(median_price)
df['Stock'] = df['Stock'].fillna(0)

df.to_csv('cleaned_invetory.csv', index=False)
print("--- CLEANED DATAFRAME ---")
print(df)