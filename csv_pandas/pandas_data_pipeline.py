import pandas as pd

data = {
    'Student_ID': [101, 102, 102, 103, 104, 105],
    'Name': [' alice ', 'BOB', 'BOB', 'charlie', 'DAVID', 'Eve'],
    'Score': [85.0, 92.0, 92.0, None, 88.0, 95.0],
    'City': ['Manila', 'Cebu', 'Cebu', 'Manila', None, 'Davao']
}
df = pd.DataFrame(data)

df = df.drop_duplicates()

df['Name'] = df['Name'].str.strip().str.title()

mean_score = df['Score'].mean()
df['Score'] = df['Score'].fillna(mean_score)
df['City'] = df['City'].fillna('Unknown')

df.to_csv('cleaned_students.csv', index=False)

print("--- CLEANED DATAFRAME ---")
print(df)