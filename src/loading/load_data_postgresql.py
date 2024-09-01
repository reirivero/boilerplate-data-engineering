import psycopg2
from psycopg2 import sql

def load_data_to_postgresql(data, table_name):
    conn = psycopg2.connect("dbname=mydatabase user=myuser password=mypassword host=localhost")
    cur = conn.cursor()
    
    for index, row in data.iterrows():
        cur.execute(
            sql.SQL("INSERT INTO {} (name, age) VALUES (%s, %s)").format(sql.Identifier(table_name)),
            [row['name'], row['age']]
        )
    
    conn.commit()
    cur.close()
    conn.close()

# Ejemplo de uso
import pandas as pd
data = pd.DataFrame({'name': ['Alice', 'Bob'], 'age': [25, 30]})
load_data_to_postgresql(data, 'my_table')
