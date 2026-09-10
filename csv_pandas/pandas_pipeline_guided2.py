import pandas as pd


data = {
    'Employee': [' JOHN DOE ', 'jane smith', 'JOHN DOE', ' Mark Johnson ', 'SARAH LEE'],
    'Department': ['IT', 'HR', 'IT', 'FINANCE', 'IT'],
    'Salary': [60000, None, 60000, 75000, 82000]
}

df = pd.DataFrame(data)

df['Employee'] = df['Employee'].str.strip().str.title()

df = df.drop_duplicates()

median_salary = df['Salary'].median()
df['Salary'] = df['Salary'].fillna(median_salary)

df.to_csv('clean_employees.csv', index=False)

print("--- CLEANED DATAFRAME ---")
print(df)