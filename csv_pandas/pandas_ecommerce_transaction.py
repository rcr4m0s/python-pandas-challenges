import pandas as pd

data = {
    'Txn_ID': [1001, 1002, 1002, 1003, 1004, 1005],
    'Customer_Name': [' ALEX GONZALES ', 'bea alonzo', 'BEA ALONZO', ' coco martin ', 'DINGDONG DANTES', 'coco martin'],
    'Amount': [12500.0, 4500.0, 4500.0, None, 8900.0, 3200.0],
    'Payment_Method': ['Credit Card', 'GCash', 'GCash', 'Maya', None, 'Maya']
}
df = pd.DataFrame(data)

df['Customer_Name'] = df['Customer_Name'].str.strip().str.title()
df = df.drop_duplicates()

median_fill = df['Amount'].median()
df['Amount'] = df['Amount'].fillna(median_fill)
df['Payment_Method'] = df['Payment_Method'].fillna('Cash')

df.to_csv('cleaned_transaction.csv', index=False)


print("--- FINAL DATAFRAME ---")
print(df)