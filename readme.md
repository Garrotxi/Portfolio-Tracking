# Docker

1. Construir imagen:

`docker build -t mi-imagen .`

2. Ejecutar contenedor

`docker run -it mi-imagen /bin/bash`

3. Listar todos los contenedores docker

`docker ps -a `

4. Parar todos los contenedores

`docker stop $(docker ps -a -q)`

5. Borrar todos los contenedores

`docker rm $(docker ps -a -q)`

# Python

1. Ejecutar workflow crear cartera con los ficheros compra/venta, dividendos y cambio_divisas creando la base de datos

`python scripts/input_output/import_complete_workflow.py init_db`

# Base de datos

1. Acceder a la base de datos una vez creada:

`sqlite3 data/cartera.db`

# Misc

# Must Read