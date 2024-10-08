# scripts\utils\load_dividendos.py
import pandas as pd
import sqlite3
import logging

# Configuración de logging
logging.basicConfig(filename='/app/logs/load_dividendos.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def load_dividendos():
    try:
        logging.info('Cargando datos de dividendos...')
        conn = sqlite3.connect('/app/data/cartera.db')
        dividendos_df = pd.read_csv('/app/data/dividendos.csv')
        dividendos_df.to_sql('Dividendos', conn, if_exists='append', index=False)
        logging.info('Datos de dividendos cargados exitosamente.')
    except Exception as e:
        logging.error(f'Error al cargar dividendos: {e}')
    finally:
        if conn:
            conn.close()
            logging.info('Conexión a la base de datos cerrada.')