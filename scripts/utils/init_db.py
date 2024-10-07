# utils/init_db.py
import sqlite3

# Conexión a la base de datos (se creará si no existe)
conn = sqlite3.connect('mi_proyecto.db')
cursor = conn.cursor()

# Crear tabla de Compras/Ventas
cursor.execute('''
CREATE TABLE IF NOT EXISTS Compras_Ventas (
    id INTEGER PRIMARY KEY,
    Fecha TEXT,
    Ticker TEXT,
    Divisa TEXT,
    Cantidad_de_acciones INTEGER,
    Precio_por_accion REAL,
    Comisiones REAL,
    Impuestos REAL,
    Precio_total REAL,
    Broker TEXT,
    Tipo_de_operacion TEXT,
    Precio_ajustado_en_divisa_local REAL
)
''')

# Crear tabla de Dividendos
cursor.execute('''
CREATE TABLE IF NOT EXISTS Dividendos (
    id INTEGER PRIMARY KEY,
    Fecha TEXT,
    Ticker TEXT,
    Divisa TEXT,
    Cantidad_de_acciones_al_cobrar INTEGER,
    Importe_bruto REAL,
    Retencion_en_origen REAL,
    Retencion_en_destino REAL,
    Importe_neto REAL,
    Broker TEXT,
    Rendimiento_del_dividendo REAL,
    Dividendo_reinvertido BOOLEAN
)
''')

# Crear tabla de Cambio de Divisas
cursor.execute('''
CREATE TABLE IF NOT EXISTS Cambio_Divisas (
    id INTEGER PRIMARY KEY,
    Fecha TEXT,
    Divisa_origen TEXT,
    Divisa_destino TEXT,
    Tipo_de_cambio_aplicado REAL,
    Comisiones_de_cambio REAL,
    Importe_convertido REAL,
    Broker TEXT,
    Fuente_del_tipo_de_cambio TEXT
)
''')

# Crear tabla de Estado Actual de la Cartera
cursor.execute('''
CREATE TABLE IF NOT EXISTS Estado_Actual_Cartera (
    id INTEGER PRIMARY KEY,
    Ticker TEXT,
    Divisa TEXT,
    Cantidad_de_acciones INTEGER,
    Precio_promedio REAL,
    Valor_actual REAL,
    Dividendo_acumulado REAL,
    Rendimiento_por_dividendo REAL,
    Broker TEXT
)
''')

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()