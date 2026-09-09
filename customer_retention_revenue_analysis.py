import pandas as pd
import numpy as np


users = pd.DataFrame({
    'UserID': ['U1', 'U2', 'U3', 'U4', 'U5'],
    'Name': ['Kaye', 'Marlon', 'Rhea', 'Jem', 'Paolo'],
    'Region': ['Luzon', 'Visayas', 'Luzon', 'Mindanao', 'Visayas']
})


purchases = pd.DataFrame({
    'TxnID': ['T101', 'T102', 'T103', 'T104', 'T105', 'T106', 'T107'],
    'UserID': ['U1', 'U2', 'U1', 'U4', 'U3', 'U2', 'U5'],
    'Spend_PHP': [1500.0, np.nan, 3000.0, 4500.0, np.nan, 1200.0, 2200.0],
    'Status': ['Success', 'Success', 'Refunded', 'Success', 'Success', 'Success', 'Refunded']
})

median_val = purchases['Spend_PHP'].median()
purchases['Spend_PHP'] = purchases['Spend_PHP'].fillna(median_val)

merged_df = pd.merge(purchases, users, on='UserID', how='inner')
filterz = merged_df[merged_df['Status'] == 'Success']

total_and_ave = filterz.groupby('Region')['Spend_PHP'].agg(['sum', 'mean', 'count']).reset_index()

print("--- CLEANED & MERGED DATASET ---")
print(merged_df)
print("\n--- REGIONAL REVENUE SUMMARY (Success Only) ---")
print(total_and_ave)