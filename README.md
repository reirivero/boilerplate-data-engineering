# boilerplate-data-engineering
Boilerplate for data engineering projets.

## Data Engineering Project

Este es un proyecto de ejemplo de Ingeniería de Datos utilizando Python, Airflow, Docker y otras herramientas. Incluye configuración para Docker, un contenedor de desarrollo para VS Code, pruebas unitarias, logging y validación de datos con Pydantic.

### Estructura del Proyecto

```
data-engineering-project/
│
├── src/
│   ├── extraction/
│   │   ├── __init__.py
│   │   └── extract_data.py
│   ├── transformation/
│   │   ├── __init__.py
│   │   └── transform_data.py
│   ├── loading/
│   │   ├── __init__.py
│   │   └── load_data.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── logging_config.py
│   │   └── config.py
│   ├── __init__.py
│   └── main.py
│
├── dags/
│   └── example_dag.py
│
├── tests/
│   ├── __init__.py
│   ├── test_extraction.py
│   ├── test_transformation.py
│   └── test_loading.py
│
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
│
├── .devcontainer/
│   └── devcontainer.json
│
├── logs/
│   └── airflow.log
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

### Requisitos

- Docker
- Docker Compose
- Python 3.8+
- Visual Studio Code (opcional, para usar el contenedor de desarrollo)

### Instalación

1. Clona el repositorio:

```bash
git clone <URL_DEL_REPOSITORIO>
cd data-engineering-project
```

2. Crea un archivo .env en la raíz del proyecto con las siguientes variables:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/mydatabase
API_KEY=your_api_key_here
```

3. Construye y levanta los servicios de Docker:

``` bash
docker-compose up --build
```

4. Abre el proyecto en VS Code (opcional):

```bash
code .
```

### Uso
#### Ejecutar el Proyecto
Para ejecutar el flujo ETL, puedes usar el archivo main.py:

    ```python
    python src/main.py
    ```

#### Ejecutar Pruebas Unitarias
Para ejecutar las pruebas unitarias, usa el siguiente comando:

```bash
python -m unittest discover tests
```

#### Acceder a la Interfaz Web de Airflow
La interfaz web de Airflow estará disponible en `http://localhost:8080`.

### Estructura del Código
* `src/`: Contiene el código fuente del proyecto.
    - `extraction/`: Funciones para extraer datos de diferentes fuentes.
    - `transformation/`: Funciones para transformar los datos extraídos.
    - `loading/`: Funciones para cargar los datos transformados en la base de datos.
    - `utils/`: Utilidades como configuración de logging y manejo de variables de entorno.
    - `main.py`: Punto de entrada principal del proyecto, donde se orquesta el flujo ETL.
* `dags/`: Contiene los DAGs de Airflow.
* `tests/`: Contiene las pruebas unitarias.
* `docker/`: Contiene la configuración de Docker.
* `.devcontainer/`: Contiene la configuración del contenedor de desarrollo para VS Code.
* `logs/`: Contiene los archivos de log.
* `requirements.txt`: Contiene las dependencias del proyecto.
* `README.md`: Contiene información sobre el proyecto.

### Dependencias
Las dependencias del proyecto están listadas en el archivo requirements.txt:

```txt
# Web scraping
requests
beautifulsoup4
selenium
webdriver-manager

# Validación y serialización de datos
pydantic

# Manejo de datos
pandas
numpy
jupyter

# Formatos de archivo
json
lxml

# Kafka para streaming de datos
kafka-python

# Herramientas de desarrollo y calidad de código
yapf
black
flake8
pylint

# Otros
python-dotenv
```

### Contribuir
Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).
3. Realiza tus cambios y haz commit (git commit -am 'Agrega nueva funcionalidad').
4. Sube tus cambios (git push origin feature/nueva-funcionalidad).
5. Abre un Pull Request.

### Licencia
Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
