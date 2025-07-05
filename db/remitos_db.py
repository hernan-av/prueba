# ---------- OPERACIONES DE REMITOS -----------

import sqlite3
from db.base_datos_db import RUTA_DB

def insertar_remito(fecha, proveedor_id):
    conexion = sqlite3.connect(RUTA_DB)
    cursor = conexion.cursor()
    cursor.execute("""
        INSERT INTO remitos (fecha, proveedor_id) VALUES (?, ?)
    """, (fecha, proveedor_id))
    conexion.commit()
    id_remito = cursor.lastrowid
    conexion.close()
    return id_remito

def insertar_remito_detalle(remito_id, producto_id, cantidad, precio_unitario):
    conexion = sqlite3.connect(RUTA_DB)
    cursor = conexion.cursor()
    cursor.execute("""
        INSERT INTO remito_detalle (remito_id, producto_id, cantidad, precio_unitario)
        VALUES (?, ?, ?, ?)
    """, (remito_id, producto_id, cantidad, precio_unitario))
    conexion.commit()
    conexion.close()

def actualizar_stock(producto_id, cantidad):
    conexion = sqlite3.connect(RUTA_DB)
    cursor = conexion.cursor()
    cursor.execute("""
        UPDATE productos SET stock = stock + ? WHERE id_producto = ?
    """, (cantidad, producto_id))
    conexion.commit()
    conexion.close()

def listar_remitos() -> list:
    """
    Devuelve una lista de tuplas con los remitos registrados.
    Cada tupla incluye: id_remito, fecha, proveedor_id
    """
    conexion = sqlite3.connect(RUTA_DB)
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT id_remito, fecha, proveedor_id FROM remitos
        ORDER BY fecha DESC
    """)
    remitos = cursor.fetchall()
    conexion.close()
    return remitos