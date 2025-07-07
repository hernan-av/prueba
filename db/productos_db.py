# ---------- OPERACIONES CON PRODUCTOS ----------

import sqlite3
from db.base_datos_db import obtener_conexion
from interfaz.mensajes import mostrar_error

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
    Retorna una lista de productos con nombres de categoría y proveedor.
    """
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT 
                p.id_producto,
                p.nombre,
                c.nombre AS categoria,
                prov.nombre AS proveedor,
                p.stock,
                p.precio_unitario
            FROM productos p
            JOIN categorias c ON p.categoria_id = c.id_categoria
            JOIN proveedores prov ON p.proveedor_id = prov.id_proveedor
        """)
        resultados = cursor.fetchall()
        conexion.close()
        return resultados
    except sqlite3.Error as e:
        mostrar_error(f"Error al listar productos: {e}")
        return []

def buscar_productos_por_proveedor_id(proveedor_id):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT 1 FROM productos WHERE proveedor_id = ? LIMIT 1", (proveedor_id,))
    resultado = cursor.fetchone()
    conexion.close()
    return resultado is not None

def buscar_productos_por_categoria_id(categoria_id: int) -> bool:
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT 1 FROM productos WHERE categoria_id = ? LIMIT 1", (categoria_id,))
    resultado = cursor.fetchone()
    conexion.close()
    return resultado is not None
