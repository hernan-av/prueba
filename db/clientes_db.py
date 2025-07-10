# ---------- OPERACIONES CON CLIENTES ----------

import sqlite3
from db.base_datos_db import obtener_conexion
from utils.logger import log_error

def insertar_cliente(nombre, telefono, email, dni):
    """
    Inserta un nuevo cliente en la base de datos.
    """
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO clientes (nombre, telefono, email, dni)
            VALUES (?, ?, ?, ?)
        """, (nombre, telefono, email, dni))
        conexion.commit()
        conexion.close()
        return True
    except sqlite3.Error as e:
        log_error(f"Error al insertar cliente: {e}")
        return False

def modificar_cliente(id_cliente, nuevo_nombre, nuevo_telefono, nuevo_email, nuevo_dni):
    """
    Modifica los datos de un cliente existente.
    """
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("""
            UPDATE clientes
            SET nombre = ?, telefono = ?, email = ?, dni = ?
            WHERE id_cliente = ?
        """, (nuevo_nombre, nuevo_telefono, nuevo_email,nuevo_dni, id_cliente))
        conexion.commit()
        conexion.close()
        return True
    except sqlite3.Error as e:
        log_error(f"Error al modificar cliente: {e}")
        return False

def eliminar_cliente(id_cliente):
    """
    Elimina un cliente por su ID.
    """
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM clientes WHERE id_cliente = ?", (id_cliente,))
        conexion.commit()
        conexion.close()
        return True
    except sqlite3.Error as e:
        log_error(f"Error al eliminar cliente: {e}")
        return False

def listar_clientes():
    """
    Retorna todos los clientes registrados.
    """
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM clientes")
        resultados = cursor.fetchall()
        conexion.close()
        return resultados
    except sqlite3.Error as e:
        log_error(f"Error al listar clientes: {e}")
        return []