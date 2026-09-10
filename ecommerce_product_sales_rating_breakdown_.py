import pandas as pd
import numpy as np

# Data 1: Product Details
products = pd.DataFrame({
    'ProdID': ['P1', 'P2', 'P3', 'P4'],
    'Category': ['Electronics', 'Electronics', 'Furniture', 'Furniture'],
    'Price': [12000.0, 25000.0, 8000.0, 15000.0]
})

# Data 2: Customer Reviews & Ratings (May missing Rating)
reviews = pd.DataFrame({
    'ReviewID': ['R1', 'R2', 'R3', 'R4', 'R5', 'R6'],
    'ProdID': ['P1', 'P2', 'P1', 'P3', 'P4', 'P2'],
    'Rating': [5.0, np.nan, 4.0, 3.0, np.nan, 5.0],
    'Verified': [True, True, False, True, True, True]
})


median_val = reviews['Rating'].median()
reviews['Rating'] = reviews['Rating'].fillna(median_val)
merge_df = pd.merge(reviews, products, on='ProdID', how='inner')

filterz = merge_df[merge_df['Verified'] == True]

average = filterz.groupby('Category')[['Price', 'Rating']].mean().reset_index()

print("--- CLEANED & MERGED REVIEWS ---")
print(merge_df)
print("\n--- CATEGORY SUMMARY (VERIFIED REVIEWS ONLY) ---")
print(average)