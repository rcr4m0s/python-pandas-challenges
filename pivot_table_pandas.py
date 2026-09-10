import pandas as pd

data = {
    'Store': ['Manila', 'Manila', 'Manila', 'Cebu', 'Cebu', 'Cebu', 'Davao', 'Davao'],
    'Category': ['Electronics', 'Clothing', 'Electronics', 'Electronics', 'Clothing', 'Clothing', 'Electronics', 'Clothing'],
    'Sales': [15000, 5000, 12000, 18000, 4000, 6000, 20000, 3000]
}
df = pd.DataFrame(data)

# Pivot Table with 'sum' and 'mean' aggregations
pivot_df = pd.pivot_table(
    df, 
    values='Sales', 
    index='Store', 
    columns='Category', 
    aggfunc=['sum', 'mean'], 
    fill_value=0
)

print(pivot_df)