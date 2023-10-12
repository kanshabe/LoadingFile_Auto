
import pyodbc

# SQL Server database configuration
server = 'DESKTOP-F731U4D\SQLEXPRESS'
database = 'Deus'
username = 'root'
password = 'root'
driver = 'ODBC Driver 18 for SQL Server'  # Replace with the appropriate ODBC driver name if needed


# Create a connection to the SQL Server database
#conn_str = f"DRIVER={{{driver}}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
#conn = pyodbc.connect(conn_str)

def sql_db_connection():
    conn_str = f"DRIVER={{{driver}}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
    return pyodbc.connect(conn_str)


try:
    conn = sql_db_connection()
    print("connection successful")
except Exception as e:
    print(f"Error : {e}")
