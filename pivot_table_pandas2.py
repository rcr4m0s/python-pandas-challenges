import pandas as pd

data = {
    'Store': ['Manila', 'Manila', 'Manila', 'Cebu', 'Cebu', 'Cebu', 'Davao', 'Davao'],
    'Category': ['Electronics', 'Clothing', 'Electronics', 'Electronics', 'Clothing', 'Clothing', 'Electronics', 'Clothing'],
    'Sales': [15000, 5000, 12000, 18000, 4000, 6000, 20000, 3000]
}

df = pd.DataFrame(data)

pivot_df = pd.pivot_table(
    df, 
    index = 'Store',
    columns = 'Category',
    values = 'Sales',
    aggfunc = ['sum', 'mean'], 
    fill_value = 0
)
print(pivot_df)