# ---------- OPERACIONES CON PRODUCTOS ----------

import sqlite3
from db.base_datos_db import obtener_conexion

def insertar_producto(nombre, categoria_id, proveedor_id, stock, precio_unitario):
    """
    Inserta un nuevo producto en la base de datos.
    """
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO productos (nombre, categoria_id, proveedor_id, stock, precio_unitario)
            VALUES (?, ?, ?, ?, ?)
        """, (nombre, categoria_id, proveedor_id, stock, precio_unitario))
        conexion.commit()
        conexion.close()
        return True
    except sqlite3.Error as e:
        print(f"❌ Error al insertar producto: {e}")
        return False

def modificar_producto(id_producto, nuevo_nombre, nueva_categoria, nuevo_proveedor, nuevo_stock, nuevo_precio):
    """
    Modifica los datos de un producto existente por su ID.
    """
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("""
            UPDATE productos
            SET nombre = ?, categoria_id = ?, proveedor_id = ?, stock = ?, precio_unitario = ?
            WHERE id_producto = ?
        """, (nuevo_nombre, nueva_categoria, nuevo_proveedor, nuevo_stock, nuevo_precio, id_producto))
        conexion.commit()
        conexion.close()
        return True
    except sqlite3.Error as e:
        print(f"❌ Error al modificar producto: {e}")
        return False

def eliminar_producto(id_producto):
    """
    Elimina un producto de la base de datos por su ID.
    """
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM productos WHERE id_producto = ?", (id_producto,))
        conexion.commit()
        conexion.close()
        return True
    except sqlite3.Error as e:
        print(f"❌ Error al eliminar producto: {e}")
        return False

def listar_productos():
    """
    Retorna todos los productos registrados.
    """
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos")
        resultados = cursor.fetchall()
        conexion.close()
        return resultados
    except sqlite3.Error as e:
        print(f"❌ Error al listar productos: {e}")
        return []