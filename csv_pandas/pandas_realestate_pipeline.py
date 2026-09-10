import pandas as pd

data = {
    'Property_ID': [201, 202, 202, 203, 204, 205],
    'Agent_Name': [' JUAN DELA CRUZ ', 'maria santos', 'MARIA SANTOS', ' pedro penduko ', 'SARAH GERONIMO', 'pedro penduko'],
    'Price_PHP': [5000000, 3500000, 3500000, None, 12000000, 4500000],
    'Location': ['Makati', 'Quezon City', 'Quezon City', 'BGC', None, 'BGC']
}
df = pd.DataFrame(data)

df['Agent_Name'] = df['Agent_Name'].str.strip().str.title()

df = df.drop_duplicates()

mean_price = df['Price_PHP'].mean()
df['Price_PHP'] = df['Price_PHP'].fillna(mean_price)
df['Location'] = df['Location'].fillna('Unlisted')

df.to_csv('final_real_estate.csv', index=False)

print("--- FINAL DATAFRAME ---")
print(df)