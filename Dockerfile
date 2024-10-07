# Usa una imagen base de Python
FROM python:3.10-slim

# Instala dependencias del sistema
RUN apt-get update && apt-get install -y sqlite3 libsqlite3-dev

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de requerimientos (si tienes uno)
COPY requirements.txt .

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código de la aplicación al directorio de trabajo
COPY ./scripts ./scripts
COPY ./data ./data
COPY ./readme.md ./readme.md

# Establece la variable de entorno para la base de datos SQLite
ENV DATABASE_URL=sqlite:///data/cartera.db

# Establece la variable de entorno para PYTHONPATH
ENV PYTHONPATH=/app/scripts

# Ejecuta el script principal que inicia el flujo de importación
CMD ["python", "scripts/input_output/import_complete_workflow.py"]