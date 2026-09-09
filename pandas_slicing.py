import pandas as pd

data = {
    'Store_ID': ['S01', 'S02', 'S03', 'S04', 'S05'],
    'Region': ['Luzon', 'Visayas', 'Luzon', 'Mindanao', 'Visayas'],
    'Monthly_Revenue': [150000, 95000, 210000, 80000, 125000],
    'Is_Active': [True, True, True, False, True]
}

df = pd.DataFrame(data)

# Task A: Label-based indexing (.loc)
# Kumuha ng row index 0 at 2, at specific column names ('Region' at 'Monthly_Revenue')
loc_subset = df.loc[[0, 2], ['Region', 'Monthly_Revenue']]

# Task B: Position-based indexing (.iloc)
# Kumuha ng rows 0 to 2 (first 3 rows) at columns 0 to 1 (first 2 columns)
iloc_subset = df.iloc[0:3, 0:2]

# Task C: Boolean Masking
# Filter active stores lang
active_stores = df[df['Is_Active'] == True]

print("=== TASK A: LOC SUBSET ===")
print(loc_subset)
print("\n=== TASK B: ILOC SUBSET ===")
print(iloc_subset)
print("\n=== TASK C: ACTIVE STORES ===")
print(active_stores)