# scripts\utils\load_dividendos.py
import pandas as pd
import sqlite3
import logging

# Configuración de logging
logger = logging.getLogger('load_dividendos')
handler = logging.FileHandler('/app/logs/load_dividendos.log')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

def load_dividendos():
    try:
        logger.info('Cargando datos de dividendos...')
        conn = sqlite3.connect('/app/data/cartera.db')
        dividendos_df = pd.read_csv('/app/data/dividendos.csv')
        dividendos_df.to_sql('Dividendos', conn, if_exists='append', index=False)
        logger.info('Datos de dividendos cargados exitosamente.')
    except Exception as e:
        logger.error(f'Error al cargar dividendos: {e}')
    finally:
        if conn:
            conn.close()
            logger.info('Conexión a la base de datos cerrada.')