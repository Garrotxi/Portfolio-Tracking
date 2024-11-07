# scripts\utils\load_cambio_divisas.py
import pandas as pd
import sqlite3
import logging

# Configuración de logging
logger = logging.getLogger('load_cambio_divisas')
handler = logging.FileHandler('/app/logs/load_cambio_divisas.log')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

def load_cambio_divisas():
    try:
        logger.info('Cargando datos de cambio de divisas...')
        conn = sqlite3.connect('/app/data/cartera.db')
        cambio_divisas_df = pd.read_csv('/app/data/cambio_divisas.csv')
        cambio_divisas_df.to_sql('Cambio_Divisas', conn, if_exists='append', index=False)
        logger.info('Datos de cambio de divisas cargados exitosamente.')
    except Exception as e:
        logger.error(f'Error al cargar cambio de divisas: {e}')
    finally:
        if conn:
            conn.close()
            logger.info('Conexión a la base de datos cerrada.')