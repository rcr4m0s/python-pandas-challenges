import pandas as pd

data = {
    'Store': ['North', 'South', 'North', 'West', 'South', 'West'],
    'Category': ['Tech', 'Tech', 'Office', 'Office', 'Tech', 'Tech'],
    'Sales': [12000, 8000, 5000, 3000, 9500, 11000]
}

df = pd.DataFrame(data)

# 1. Total Sales per Store
group_store_sales = df.groupby('Store')['Sales'].sum()
print("Total Sales per store:")
print(group_store_sales)

print("\n" + "="*30 + "\n")

# 2. Average Sales per Category
average_sales_categ = df.groupby('Category')['Sales'].mean()
print("Average Sales per Category:")
print(average_sales_categ)