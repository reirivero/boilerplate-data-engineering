import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Definir las variables de entorno que se utilizarán en el proyecto
DATABASE_URL = os.getenv('DATABASE_URL')
API_KEY = os.getenv('API_KEY')

# Puedes agregar más configuraciones según sea necesario
