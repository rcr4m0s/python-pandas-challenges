import pandas as pd

data = {
    'Product_Code': ['P101', 'P102', 'P103', 'P104', 'P105'],
    'Category': ['Electronics', 'Grocery', 'Electronics', 'Clothing', 'Grocery'],
    'Price': [1500, 120, 3200, 450, 85],
    'Stock_Qty': [12, 150, 5, 45, 0]
}

df = pd.DataFrame(data)

task1 = df.loc[[1, 3], ['Product_Code', 'Price']]
task2 = df.iloc[3:5, 0:3]
task3 = df[df['Stock_Qty'] < 10]

print("=== LOC SUBSET ===")
print(task1)
print("\n=== ILOC SUBSET ===")
print(task2)
print("\n=== LOW OR OUT OF STOCK ===")
print(task3)
