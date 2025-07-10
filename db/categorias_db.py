# ---------- OPERACIONES CON CATEGORIAS ----------

import sqlite3
from db.base_datos_db import obtener_conexion
from utils.logger import log_info, log_error

def insertar_categoria(nombre):
    """
    Inserta una nueva categoría en la base de datos.
    """
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO categorias (nombre) VALUES (?)", (nombre,))
        conexion.commit()
        conexion.close()
        return True
    except sqlite3.Error as e:
        log_error(f"Error al insertar categoría: {e}")
        return False

def modificar_categoria(id_categoria, nuevo_nombre):
    """
    Modifica el nombre de una categoría por su ID.
    """
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("UPDATE categorias SET nombre = ? WHERE id_categoria = ?", (nuevo_nombre, id_categoria))
        conexion.commit()
        conexion.close()
        return True
    except sqlite3.Error as e:
        log_error(f"Error al modificar categoría: {e}")
        return False

def eliminar_categoria(id_categoria):
    """
    Elimina una categoría por su ID.
    """
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM categorias WHERE id_categoria = ?", (id_categoria,))
        conexion.commit()
        conexion.close()
        return True
    except sqlite3.Error as e:
        log_error(f"Error al eliminar categoría: {e}")
        return False

def listar_categorias():
    """
    Retorna todas las categorías registradas.
    """
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM categorias")
        resultados = cursor.fetchall()
        conexion.close()
        return resultados
    except sqlite3.Error as e:
        log_error(f"Error al listar categorías: {e}")
        return []