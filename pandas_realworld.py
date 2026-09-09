import pandas as pd

inventory = pd.DataFrame({
    'SKU': ['SKU-001', 'SKU-002', 'SKU-003', 'SKU-004', 'SKU-005', 'SKU-006'],
    'Category': ['Electronics', 'Home', 'Electronics', 'Fashion', 'Home', 'Electronics'],
    'Price_PHP': [12500, 850, 45000, 2200, 1500, 32000],
    'Stock': [15, 0, 4, 28, 8, 2],
    'Rating': [4.8, 3.9, 4.9, 4.2, 3.5, 4.7]
})

high_end_electronics_promotion = inventory.loc[(inventory['Category'] == 'Electronics') & (inventory['Price_PHP'] >= 30000), ['SKU', 'Price_PHP', 'Rating']]
inventory_audit = inventory.iloc[0:4, [0, 1, 3]]
critical_reorder = inventory[(inventory['Stock'] < 5) & (inventory['Rating'] >= 4.0)]

print("HIGH END ELECTRONICS PROMOTION")
print(high_end_electronics_promotion)
print("TOP INVENTORY AUDIT")
print(inventory_audit)
print("CRITICAL RE-ORDER ALERT")
print(critical_reorder)

