import pandas as pd
import numpy as np

data = {
    'Employee': ['John', 'Sarah', 'Mike', 'Anna', 'Chris'],
    'Department': ['IT', 'HR', np.nan, 'IT', 'HR'],
    'Salary': [60000, np.nan, 55000, 65000, 50000],
    'Experience_Years': [3, 5, 2, np.nan, 1]
}

df = pd.DataFrame(data)

print("Missing Count Values")
print(df.isna().sum())

df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
df['Department'] = df['Department'].fillna("Unknown")
final_df = df.dropna()

print("\n=== FINAL CLEAN DATAFRAME ===")
print(final_df)