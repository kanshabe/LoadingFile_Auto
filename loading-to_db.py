
# import the relevant functions from other packages
from table_columns import headers
from dsn_connectivity import table_name,conn
#from files_to_load import data_to_insert


def load_data_into_db(data):
    fields = "?"   
    for _ in range(447):
        fields += ", ""?"
        
    cols = ", ".join(headers)

    sql = f"INSERT INTO {table_name} ({cols}) VALUES ({fields})"
    
    # Create a cursor and execute the INSERT query using executemany
    cursor = conn.cursor()
    try:
        cursor.executemany(sql, data)
        
        # Commit the transaction
        conn.commit()
    except Exception as err:
        print(f"Error : {err}")
    
