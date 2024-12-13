import argparse
import sqlite3
import subprocess
import pandas as pd
from datetime import datetime

# Función para invocar el script import_complete_workflow.py
def invocar_import_complete_workflow(iniciar_db):
    if iniciar_db:
        print("Inicializando la base de datos y cargando los ficheros...")
        subprocess.run(["python", "scripts/input_output/import_complete_workflow.py", "init_db"], check=True)

# Función para obtener el tipo de cambio actual (simulada para este ejemplo)
def obtener_tipo_cambio(divisa_origen, divisa_destino):
    tipo_cambio = {
        ('USD', 'EUR'): 0.93,  # Ejemplo de tipo de cambio USD -> EUR
        ('EUR', 'USD'): 1.08,  # Ejemplo de tipo de cambio EUR -> USD
        ('USD', 'GBP'): 0.82,  # Ejemplo de tipo de cambio USD -> GBP
        ('GBP', 'USD'): 1.22,  # Ejemplo de tipo de cambio GBP -> USD
    }
    return tipo_cambio.get((divisa_origen, divisa_destino), 1.0)  # Valor predeterminado 1.0 si no se encuentra el par

# Función para consultar la cartera desde la base de datos
def obtener_cartera():
    conn = sqlite3.connect('/app/data/cartera.db')
    query = "SELECT * FROM Estado_Actual_Cartera"
    cartera_df = pd.read_sql(query, conn)
    conn.close()
    return cartera_df

# Función para obtener los datos de compras/ventas, dividendos y cambio de divisas desde las tablas
def obtener_datos_desde_tablas():
    conn = sqlite3.connect('/app/data/cartera.db')

    # Obtener datos de la tabla Compras_Ventas
    query_compras_ventas = "SELECT * FROM Compras_Ventas"
    compras_ventas_df = pd.read_sql(query_compras_ventas, conn)

    # Obtener datos de la tabla Dividendos
    query_dividendos = "SELECT * FROM Dividendos"
    dividendos_df = pd.read_sql(query_dividendos, conn)

    # Obtener datos de la tabla Cambio_Divisas
    query_cambio_divisas = "SELECT * FROM Cambio_Divisas"
    cambio_divisas_df = pd.read_sql(query_cambio_divisas, conn)

    conn.close()
    
    return compras_ventas_df, dividendos_df, cambio_divisas_df

# Función para reconstruir la cartera desde las tablas y llenarla en la tabla Estado_Actual_Cartera
def reconstruir_cartera(divisa_referencia, cargar_ficheros):
    # Limpiar la tabla Estado_Actual_Cartera
    conn = sqlite3.connect('/app/data/cartera.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Estado_Actual_Cartera")
    conn.commit()

    # Invocar el script para cargar los ficheros si es necesario
    if cargar_ficheros:
        invocar_import_complete_workflow(True)

    # Obtener los datos de las tablas
    compras_ventas_df, dividendos_df, cambio_divisas_df = obtener_datos_desde_tablas()

    # Reconstrucción de la cartera
    for ticker in compras_ventas_df['Ticker'].unique():
        # Filtrar datos de compras/ventas para el ticker
        compras_ticker_df = compras_ventas_df[compras_ventas_df['Ticker'] == ticker]

        # Inicializar variables
        cantidad_total = 0
        precio_promedio = 0
        divisa_cartera = compras_ticker_df.iloc[0]['Divisa']
        valor_total = 0
        dividendos_totales = 0

        # Calcular la cantidad total y precio promedio
        for _, row in compras_ticker_df.iterrows():
            cantidad_total += row['Cantidad_de_acciones']
            precio_promedio += row['Precio_total']  # Precio total de la compra (sin comisiones)
        
        precio_promedio /= cantidad_total  # Precio promedio por acción

        # Obtener dividendos para este ticker
        dividendos_ticker_df = dividendos_df[dividendos_df['Ticker'] == ticker]
        dividendos_totales = dividendos_ticker_df['Importe_neto'].sum()

        # Obtener el tipo de cambio actual si la divisa no es la de referencia
        if divisa_cartera != divisa_referencia:
            tipo_cambio = obtener_tipo_cambio(divisa_cartera, divisa_referencia)
            valor_total = cantidad_total * precio_promedio * tipo_cambio
            dividendos_totales *= tipo_cambio  # Convertir los dividendos a la divisa de referencia
        else:
            valor_total = cantidad_total * precio_promedio  # Ya está en la divisa de referencia

        # Insertar los datos en la tabla Estado_Actual_Cartera
        cursor.execute('''
            INSERT INTO Estado_Actual_Cartera (Ticker, Divisa, Cantidad_de_acciones, Precio_promedio, Valor_actual, Dividendo_acumulado, Broker)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (ticker, divisa_referencia, cantidad_total, precio_promedio, valor_total, dividendos_totales, compras_ticker_df.iloc[0]['Broker']))
    
    conn.commit()
    conn.close()

    print("Cartera reconstruida y guardada en la tabla Estado_Actual_Cartera.")

# Función principal
def main():
    # Configuración de los parámetros de entrada
    parser = argparse.ArgumentParser(description='Reconstruir cartera desde ficheros')
    parser.add_argument('--divisa', type=str, default='USD', choices=['USD', 'EUR', 'GBP'], 
                        help='Divisa de referencia para calcular los valores de la cartera (por defecto USD)')
    parser.add_argument('--cargar_ficheros', action='store_true', 
                        help='Opción para cargar los ficheros de compras/ventas, dividendos y cambio de divisas')

    args = parser.parse_args()

    divisa_referencia = args.divisa
    cargar_ficheros = args.cargar_ficheros

    print(f'Calculando la cartera con {divisa_referencia} como divisa de referencia...')

    # Llamada a la función que reconstruye la cartera
    reconstruir_cartera(divisa_referencia, cargar_ficheros)

if __name__ == "__main__":
    main()
