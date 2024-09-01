from google.cloud import bigquery

def load_data_to_bigquery(data, table_id):
    client = bigquery.Client()
    job = client.load_table_from_dataframe(data, table_id)
    job.result()  # Esperar a que el trabajo termine
    print(f"Datos cargados a {table_id}")

# Ejemplo de uso
import pandas as pd
data = pd.DataFrame({'name': ['Alice', 'Bob'], 'age': [25, 30]})
load_data_to_bigquery(data, 'my_dataset.my_table')
