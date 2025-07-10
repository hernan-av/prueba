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
        SELECT 
        f.id_factura,
        f.fecha,
        c.nombre,
        f.total 
        FROM facturas f
        JOIN clientes c on f.cliente_id = c.id_cliente
        ORDER BY fecha DESC
    """)
    facturas = cursor.fetchall()
    conexion.close()
    return facturas

def obtener_detalle_venta(id_factura: int) -> list:
    """
    Devuelve una lista de tuplas con los datos detallados de una venta específica.
    Cada tupla incluye: id_factura, fecha, cliente, producto, categoría, cantidades y montos.
    """
    conexion = sqlite3.connect(RUTA_DB)
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT 
            f.id_factura,
            f.fecha,
            c.id_cliente,
            c.nombre AS cliente,
            c.email,
            c.dni,
            p.id_producto,
            p.nombre AS producto,
            ct.nombre AS categoria,
            fd.cantidad,
            fd.precio_unitario,
            fd.total_linea,
            f.total
        FROM facturas f
        JOIN clientes c ON f.cliente_id = c.id_cliente
        JOIN factura_detalle fd ON fd.factura_id = f.id_factura
        JOIN productos p ON p.id_producto = fd.producto_id
        JOIN categorias ct ON ct.id_categoria = p.categoria_id
        WHERE f.id_factura = ?
    """, (id_factura,))
    detalle_venta = cursor.fetchall()
    conexion.close()
    return detalle_venta

