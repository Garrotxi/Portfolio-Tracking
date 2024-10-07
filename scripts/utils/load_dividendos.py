import pandas as pd
import sqlite3

def load_dividendos():
    conn = sqlite3.connect('mi_proyecto.db')
    dividendos_df = pd.read_csv('/app/data/dividendos.csv')
    dividendos_df.to_sql('Dividendos', conn, if_exists='append', index=False)
    conn.close()