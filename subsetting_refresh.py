import pandas as pd

orders = pd.DataFrame({
    'Order_ID': ['ORD101', 'ORD102', 'ORD103', 'ORD104', 'ORD105', 'ORD106'],
    'Customer_Tier': ['VIP', 'Regular', 'VIP', 'Regular', 'VIP', 'Regular'],
    'Total_Amount': [4500, 1200, 8900, 650, 3100, 2400],
    'Status': ['Shipped', 'Pending', 'Delivered', 'Cancelled', 'Shipped', 'Pending']
})

high_value = orders.loc[orders['Total_Amount'] > 3000,['Order_ID', "Total_Amount"]]
tatlo_logistics_view = orders.iloc[ 0:3, [0, 1, 3]]
filterz = orders[(orders['Customer_Tier'] == 'VIP') & (orders['Status'] == 'Shipped')]

print("High VALUE Orders")
print(high_value)
print("LOGISTICS VIEW")
print(tatlo_logistics_view)
print("VIP SHIPPED ORDERS")
print(filterz)