# input_output/import_complete_workflow.py
from utils.load_compras_ventas import load_compras_ventas
from utils.load_dividendos import load_dividendos
from utils.load_cambio_divisas import load_cambio_divisas

def import_complete_workflow():
    load_compras_ventas()
    load_dividendos()
    load_cambio_divisas()

if __name__ == "__main__":
    import_complete_workflow()