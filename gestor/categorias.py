# ---------- GESTIÓN DE CATEGORÍAS ----------

from db.categorias_db import insertar_categoria, listar_categorias, modificar_categoria, eliminar_categoria

def agregar_categoria(nombre: str):
    if not nombre.strip():
        return "El nombre de la categoría no puede estar vacío"

    categorias = []
    for cat in listar_categorias():
        categorias.append(cat[1].lower())

    if nombre.strip().lower() in categorias:
        return "El nombre de categoría ya existe"

    try:
        insertar_categoria(nombre.strip())
        return "ok: Categoría agregada con éxito."
    except Exception as e:
        return f"Error al agregar la categoría: {e}"

def editar_categoria(id_categoria, nuevo_nombre: str):
    ids = []
    for cat in listar_categorias():
        ids.append(cat[0])

    if id_categoria not in ids:
        return "❌ El ID de categoría ingresado no existe."

    if not nuevo_nombre.strip():
        return "❌ El nombre no puede estar vacío."

    for cat in listar_categorias():
        if cat[1].lower() == nuevo_nombre.strip().lower() and cat[0] != id_categoria:
            return "El nombre de categoría ya existe"

    try:
        modificar_categoria(id_categoria, nuevo_nombre.strip())
        return "ok: Categoría modificada correctamente."
    except Exception as e:
        return f"Error al editar la categoría: {e}"

def borrar_categoria(id_categoria):
    ids = []
    for cat in listar_categorias():
        ids.append(cat[0])

    if id_categoria not in ids:
        return "❌ El ID de categoría ingresado no existe."

    try:
        eliminar_categoria(id_categoria)
        return "ok: Categoría eliminada correctamente."
    except Exception as e:
        return f"Error al eliminar la categoría: {e}"

def obtener_categorias():
    return listar_categorias()
