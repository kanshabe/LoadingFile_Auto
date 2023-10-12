import pyodbc

# DSN configuration
dsn_name = 'deus_data_loading'  # Replace with the name of your DSN

# SQL Server table name
table_name = 'Deus.dbo.Airtel_Voice'

# Create a connection to the SQL Server database using the DSN
try:
    conn = pyodbc.connect(f'DSN={dsn_name}')

    #print(conn.getinfo)
except Exception as e:
    print(e)

'''    
curr = conn.cursor()

sql = f"SELECT * FROM {table_name}"
result = curr.execute(sql)
for row in result:
    print(row)
#print(curr.messages)
#print(curr.rowcount)
'''