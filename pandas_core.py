import pandas as pd

# Data Dictionary
data = {
    'Store_ID': ['S01', 'S02', 'S03', 'S04', 'S05'],
    'Region': ['Luzon', 'Visayas', 'Luzon', 'Mindanao', 'Visayas'],
    'Monthly_Revenue': [150000, 95000, 210000, 80000, 125000],
    'Is_Active': [True, True, True, False, True]
}

df = pd.DataFrame(data)

print("DATA FRAME")
print(df)
revenue = df['Monthly_Revenue']
print("MONTHLY REVENUE")
print(revenue)
average = df['Monthly_Revenue'].mean()
print("MONTHLY AVERAGE")
print(average)