# ---------- OPERACIONES CON PROVEEDORES ----------

import sqlite3
from db.base_datos_db import obtener_conexion
from utils.logger import log_error

def insertar_proveedor(nombre, telefono, email, cuit):
    """
    Inserta un nuevo proveedor en la base de datos.
    """
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO proveedores (nombre, telefono, email, cuit)
            VALUES (?, ?, ?, ?)
        """, (nombre, telefono, email, cuit))
        conexion.commit()
        conexion.close()
        return True
    except sqlite3.Error as e:
        log_error(f"Error al insertar proveedor: {e}")
        return False

def modificar_proveedor(id_proveedor, nuevo_nombre, nuevo_telefono, nuevo_email, nuevo_cuit):
    """
    Modifica los datos de un proveedor existente.
    """
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("""
            UPDATE proveedores
            SET nombre = ?, telefono = ?, email = ?, cuit = ?
            WHERE id_proveedor = ?
        """, (nuevo_nombre, nuevo_telefono, nuevo_email,nuevo_cuit, id_proveedor))
        conexion.commit()
        conexion.close()
        return True
    except sqlite3.Error as e:
        log_error(f"Error al modificar proveedor: {e}")
        return False

def eliminar_proveedor(id_proveedor):
    """
    Elimina un proveedor por su ID.
    """
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM proveedores WHERE id_proveedor = ?", (id_proveedor,))
        conexion.commit()
        conexion.close()
        return True
    except sqlite3.Error as e:
        log_error(f"Error al eliminar proveedor: {e}")
        return False

def listar_proveedores():
    """
    Retorna todos los proveedores registrados.
    """
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM proveedores")
        resultados = cursor.fetchall()
        conexion.close()
        return resultados
    except sqlite3.Error as e:
        log_error(f"Error al listar proveedores: {e}")
        return []