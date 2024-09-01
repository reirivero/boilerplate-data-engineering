FROM apache/airflow:2.10.0-python3.12

# Configurar el entorno no interactivo para evitar prompts durante la instalación
ENV DEBIAN_FRONTEND=noninteractive
ENV AIRFLOW__CORE__LOAD_EXAMPLES=True

USER root
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
         vim wget unzip \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*


# Instalar Oh My Posh
RUN wget https://github.com/JanDeDobbeleer/oh-my-posh/releases/latest/download/posh-linux-amd64 -O /usr/local/bin/oh-my-posh && \
    chmod +x /usr/local/bin/oh-my-posh && mkdir -p ~/.poshthemes && wget https://github.com/JanDeDobbeleer/oh-my-posh/releases/latest/download/themes.zip -O ~/.poshthemes/themes.zip && \
    unzip ~/.poshthemes/themes.zip -d ~/.poshthemes && chmod u+rw ~/.poshthemes/*.json && rm ~/.poshthemes/themes.zip

# Configurar Oh My Posh
RUN echo 'eval "$(oh-my-posh --init --shell bash --config ~/.poshthemes/kushal.omp.json)"' >> ~/.bashrc

ADD ../requirements.txt .
RUN pip install --no-cache-dir apache-airflow==${AIRFLOW_VERSION} -r /requirements.txt

USER airflow
# Copiar los DAGs y otros archivos necesarios
# COPY dags/ /opt/airflow/dags/
# COPY src/ /opt/airflow/src/
# COPY tests/ /opt/airflow/tests/
# COPY logs/ /opt/airflow/logs/
# COPY .env /opt/airflow/.env
