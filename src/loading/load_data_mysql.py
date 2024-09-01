import mysql.connector

def load_data_to_mysql(data, table_name):
    conn = mysql.connector.connect(user='myuser', password='mypassword', host='localhost', database='mydatabase')
    cursor = conn.cursor()
    
    for index, row in data.iterrows():
        cursor.execute(
            f"INSERT INTO {table_name} (name, age) VALUES (%s, %s)",
            (row['name'], row['age'])
        )
    
    conn.commit()
    cursor.close()
    conn.close()

# Ejemplo de uso
import pandas as pd
data = pd.DataFrame({'name': ['Alice', 'Bob'], 'age': [25, 30]})
load_data_to_mysql(data, 'my_table')