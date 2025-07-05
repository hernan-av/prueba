# ---------- OPERACIONES DE FACTURAS ----------

import sqlite3
from db.base_datos_db import RUTA_DB

def insertar_factura(fecha, cliente_id, total):
    conexion = sqlite3.connect(RUTA_DB)
    cursor = conexion.cursor()
    cursor.execute("""
        INSERT INTO facturas (fecha, cliente_id, total) VALUES (?, ?, ?)
    """, (fecha, cliente_id, total))
    conexion.commit()
    id_factura = cursor.lastrowid
    conexion.close()
    return id_factura

def insertar_factura_detalle(factura_id, producto_id, cantidad, precio_unitario, total_linea):
    conexion = sqlite3.connect(RUTA_DB)
    cursor = conexion.cursor()
    cursor.execute("""
        INSERT INTO factura_detalle (factura_id, producto_id, cantidad, precio_unitario, total_linea)
        VALUES (?, ?, ?, ?, ?)
    """, (factura_id, producto_id, cantidad, precio_unitario, total_linea))
    conexion.commit()
    conexion.close()

def descontar_stock(producto_id, cantidad):
    conexion = sqlite3.connect(RUTA_DB)
    cursor = conexion.cursor()
    cursor.execute("""
        UPDATE productos SET stock = stock - ? WHERE id_producto = ?
    """, (cantidad, producto_id))
    conexion.commit()
    conexion.close()

def listar_facturas() -> list:
    """
    Devuelve una lista de tuplas con las facturas registradas.
    Cada tupla incluye: id_factura, fecha, cliente_id, total
    """
    conexion = sqlite3.connect(RUTA_DB)
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT id_factura, fecha, cliente_id, total FROM facturas
        ORDER BY fecha DESC
    """)
    facturas = cursor.fetchall()
    conexion.close()
    return facturas