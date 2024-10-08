# scripts\utils\load_cambio_divisas.py
import pandas as pd
import sqlite3
import logging

# Configuración de logging
logging.basicConfig(filename='/app/logs/load_cambio_divisas.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def load_cambio_divisas():
    try:
        logging.info('Cargando datos de cambio de divisas...')
        conn = sqlite3.connect('/app/data/cartera.db')
        cambio_divisas_df = pd.read_csv('/app/data/cambio_divisas.csv')
        cambio_divisas_df.to_sql('Cambio_Divisas', conn, if_exists='append', index=False)
        logging.info('Datos de cambio de divisas cargados exitosamente.')
    except Exception as e:
        logging.error(f'Error al cargar cambio de divisas: {e}')
    finally:
        if conn:
            conn.close()
            logging.info('Conexión a la base de datos cerrada.')