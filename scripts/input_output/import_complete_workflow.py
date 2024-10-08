# input_output/import_complete_workflow.py
import sys
import subprocess
from utils.load_compras_ventas import load_compras_ventas
from utils.load_dividendos import load_dividendos
from utils.load_cambio_divisas import load_cambio_divisas

def import_complete_workflow():
    # Cargar las tablas
    load_compras_ventas()
    load_dividendos()
    load_cambio_divisas()

if __name__ == "__main__":
# Verificar si el script debe inicializar la base de datos
    if len(sys.argv) > 1 and sys.argv[1] == 'init_db':
        print("Inicializando la base de datos desde cero...")
        subprocess.run(['python', 'scripts/utils/init_db.py'])
    
    # Ejecutar el flujo de importación de datos
    import_complete_workflow()