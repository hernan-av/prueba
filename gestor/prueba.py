import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import sqlite3
from db.base_datos_db import obtener_conexion
from utils.logger import log_error

def listar_productos_simple() -> list[tuple]:
    """Consulta todos los productos desde la tabla 'productos' sin joins."""
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos")
        resultados = cursor.fetchall()
        conexion.close()
        return resultados
    except sqlite3.Error as e:
        log_error(f"Error al consultar productos directamente: {e}")
        return []


def mostrar_productos_simple():
    productos = listar_productos_simple()
    if productos:
        for p in productos:
            print(p)  # Mostrará cada tupla de la tabla
    else:
        print("No se encontraron productos.")
        

mostrar_productos_simple()