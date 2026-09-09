import pandas as pd

grid = pd.DataFrame({
    'Server_ID': ['SRV01', 'SRV02', 'SRV03', 'SRV04', 'SRV05'],
    'Zone': ['North', 'South', 'North', 'East', 'South'],
    'Temp_C': [42.5, 38.0, 48.2, 35.1, 51.0],
    'Status': ['Normal', 'Normal', 'Warning', 'Normal', 'Critical']
})

overheating_servers = grid.loc[grid['Temp_C'] > 40.0, ['Server_ID', 'Status']]
system_check = grid.iloc[0:2, 0:3]
critical_filter = grid[(grid['Zone'] == 'South') & (grid['Status'] != 'Normal')]

print("OVERHEATING SERVERS")
print(overheating_servers)
print("SYSTEM CHECK")
print(system_check)
print("CRITICAL FILTER")
print(critical_filter)