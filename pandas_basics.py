import pandas as pd

data = {
    'Employee': ["Alice", "Bob", "Charlie"],
    'Department': ["Data Engr", "DevOps", "Data Engr"],
    'Salary': [80000, 75000, 90000]
}

df = pd.DataFrame(data)
print("=== FULL DATAFRAME ===")
print(df)
print("\n === SALARY COLUMN ===")
print(df['Salary'])