import pandas as pd
import sqlite3

def load_compras_ventas():
    conn = sqlite3.connect('mi_proyecto.db')
    compras_ventas_df = pd.read_csv('../data/compras_ventas.csv')
    compras_ventas_df.to_sql('Compras_Ventas', conn, if_exists='append', index=False)
    conn.close()