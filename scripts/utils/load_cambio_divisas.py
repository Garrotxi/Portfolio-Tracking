import pandas as pd
import sqlite3

def load_cambio_divisas():
    conn = sqlite3.connect('mi_proyecto.db')
    cambio_divisas_df = pd.read_csv('/app/data/cambio_divisas.csv')
    cambio_divisas_df.to_sql('Cambio_Divisas', conn, if_exists='append', index=False)
    conn.close()
