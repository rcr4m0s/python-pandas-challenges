import pandas as pd
import numpy as np

tickets = pd.DataFrame({
    'Ticket_ID': ['T01', 'T02', 'T03', 'T04', 'T05'],
    'Category': ['Billing', np.nan, 'Technical', 'Billing', np.nan],
    'Resolution_Time_Hrs': [2.5, 4.0, np.nan, 1.5, 3.0],
    'Customer_Rating': [5.0, 3.0, 4.0, np.nan, np.nan]
})

df = pd.DataFrame(tickets)

missing_value = df.isna().sum()
df['Category'] = df['Category'].fillna('General')

numeric = df['Resolution_Time_Hrs'].mean()
df['Resolution_Time_Hrs'] = df['Resolution_Time_Hrs'].fillna(numeric)
ticket_clean = df.dropna()

print("=== MISSING VALUES COUNT ===")
print(missing_value)
print("\n=== CLEANED DATAFRAME ===")
print(ticket_clean)