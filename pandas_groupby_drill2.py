import pandas as pd

data = {
    'Branch': ['Manila', 'Cebu', 'Manila', 'Davao', 'Cebu', 'Manila'],
    'Category': ['GPU', 'RAM', 'RAM', 'GPU', 'GPU', 'GPU'],
    'Units_Sold': [15, 30, 25, 10, 20, 18],
    'Revenue': [450000, 150000, 125000, 300000, 600000, 540000]
}

df = pd.DataFrame(data)

total_unit = df.groupby('Category')['Units_Sold'].sum()
print("Total Units Sold per Category:")
print(total_unit)
total_revenue = df.groupby('Branch')['Revenue'].sum()
print("\n Total Revenue per Branch:")
print(total_revenue)
average = df.groupby('Category')['Units_Sold'].mean()
print("\n Average Units Sold per Category:")
print(average)
