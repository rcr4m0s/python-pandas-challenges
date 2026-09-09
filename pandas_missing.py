import numpy as np
import pandas as pd

data = {
    'User': ['Alex', 'Bob', 'Charlie', 'David'],
    'Age': [25, np.nan, 30, 22],
    'Score': [85, 90, np.nan, 78],
}

df = pd.DataFrame(data)

print('=== ORIGINAL DATAFRAME ===')
print(df)

# 1. Check kung ilan ang missing values kada column
print('\n=== MISSING VALUES COUNT ===')
print(df.isna().sum())

# 2. Fill missing values sa 'Age' column gamit ang average age
df['Age'] = df['Age'].fillna(df['Age'].mean())

print('\n=== AFTER FILLING AGE ===')
print(df)

# 3. Drop remaining missing values (tatanggalin 'yung row ni Charlie kasi may NaN pa sa Score)
clean_df = df.dropna()

print('\n=== FINAL CLEAN DATAFRAME ===')
print(clean_df)