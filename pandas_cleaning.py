import pandas as pd
import numpy as np

# Sample dirty dataset with missing values (np.nan)
data = {
    'Employee_ID': ['E01', 'E02', 'E03', 'E04', 'E05'],
    'Department': ['IT', 'HR', np.nan, 'IT', 'Finance'],
    'Salary': [60000, 45000, 50000, np.nan, 55000],
    'Performance_Score': [4.5, np.nan, 3.8, 4.0, np.nan]
}

df = pd.DataFrame(data)

missing_count = df.isnull().sum()

df['Department'] = df['Department'].fillna('Unassigned')

mean_salary = df['Salary'].mean()
df['Salary'] = df['Salary'].fillna(mean_salary)

print("=== MISSING VALUES COUNT ===")
print(missing_count)
print("\n=== CLEANED DATAFRAME ===")
print(df)