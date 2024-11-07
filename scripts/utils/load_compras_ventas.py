# scripts\utils\load_compras_ventas.py
import pandas as pd
import sqlite3
import logging

# Configuración de logging
logger = logging.getLogger('load_compras_ventas')
handler = logging.FileHandler('/app/logs/load_compras_ventas.log')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

def load_compras_ventas():
    try:
        logger.info('Cargando datos de compras/ventas...')
        conn = sqlite3.connect('/app/data/cartera.db')
        compras_ventas_df = pd.read_csv('/app/data/compras_ventas.csv')
        compras_ventas_df.to_sql('Compras_Ventas', conn, if_exists='append', index=False)
        logger.info('Datos de compras/ventas cargados exitosamente.')
    except Exception as e:
        logger.error(f'Error al cargar compras/ventas: {e}')
    finally:
        if conn:
            conn.close()
            logger.info('Conexión a la base de datos cerrada.')