import logging
from .config import setup_logging, DATABASE_URL, API_KEY

setup_logging()

# Cualquier inicialización necesaria para el subpaquete utils
print("Subpaquete utils inicializado")

# Imprimir las variables de ambiente para verificar que se cargaron correctamente
print(f"Database URL: {DATABASE_URL}")
print(f"API Key: {API_KEY}")
