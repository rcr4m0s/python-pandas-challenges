import numpy as np
import pandas as pd

# 1. SETUP RAW DATA (Do not modify)
raw_data = {
    'Item': ['Laptop', 'Mouse', 'Monitor', 'Keyboard', 'Desk', 'Chair'],
    'Category': ['Tech', 'Tech', 'Tech', 'Tech', 'Office', 'Office'],
    'Price': [1000, 25, 200, 50, 150, 100],
    'Units': [5, np.nan, 3, 10, np.nan, 4],
}
pd.DataFrame(raw_data).to_csv('raw_sales.csv', index=False)

# --- YOUR PIPELINE STARTS HERE ---

# Step 1: Read 'raw_sales.csv'
df = pd.read_csv('raw_sales.csv')

# Step 2: Fill NaN values in 'Units' with 0
df['Units'] = df['Units'].fillna(0)

# Step 3: Filter out rows where Units == 0
clean_df = df[df['Units'] > 0]

# Step 4: Add 'Total_Cost' column (Units * Price)
clean_df['Total_Cost'] = clean_df['Units'] * clean_df['Price']

# Step 5: Group by 'Category' and sum 'Total_Cost'
summary = clean_df.groupby('Category')['Total_Cost'].sum()

# Step 6: Save the summary to 'category_summary.csv'
summary.to_csv('category_summary.csv')

print('=== CATEGORY SUMMARY ===')
print(summary)