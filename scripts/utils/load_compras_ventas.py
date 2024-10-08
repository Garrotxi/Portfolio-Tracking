# scripts\utils\load_compras_ventas.py
import pandas as pd
import sqlite3
import logging

# Configuración de logging
logging.basicConfig(filename='/app/logs/load_compras_ventas.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')


def load_compras_ventas():
    try:
        logging.info('Cargando datos de compras/ventas...')
        conn = sqlite3.connect('/app/data/cartera.db')
        compras_ventas_df = pd.read_csv('/app/data/compras_ventas.csv')
        compras_ventas_df.to_sql('Compras_Ventas', conn, if_exists='append', index=False)
        logging.info('Datos de compras/ventas cargados exitosamente.')
    except Exception as e:
        logging.error(f'Error al cargar compras/ventas: {e}')
    finally:
        if conn:
            conn.close()
            logging.info('Conexión a la base de datos cerrada.')