
# import the relevant functions from other packages
from table_columns import headers
from dsn_connectivity import table_name, conn

# function that loads data into db
def load_data_into_db(data_to_load):
    fields = "?"   
    for _ in range(447):
        fields += ", ""?"
        
    cols = ", ".join(headers)

    sql = f"INSERT INTO {table_name} ({cols}) VALUES ({fields})"
    
    # Create a cursor and execute the INSERT query using executemany
    cursor = conn.cursor()
    try:
        cursor.executemany(sql, data_to_load)
        
        # Commit the transaction
        conn.commit()
    except Exception as err:
        print(f"Error : {err}")
    
