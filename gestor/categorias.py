# ---------- GESTIÓN DE CATEGORÍAS ----------

from db.categorias_db import insertar_categoria, listar_categorias, modificar_categoria, eliminar_categoria
from interfaz.entrada import pedir_input_con_cancelacion
from interfaz.mostrar_resumen import mostrar_categorias
from interfaz.mensajes import mostrar_error, mostrar_exito, mostrar_cancelado
from utils.utils import normalizar_texto, formatear_nombre
from db.productos_db import buscar_productos_por_categoria_id
from utils.logger import log_info

def obtener_nombres_categorias_normalizados() -> list[str]:
    """Devuelve una lista de nombres normalizados de todas las categorías registradas."""
    nombres = []
    for categoria in listar_categorias():
        nombre_normalizado = normalizar_texto(categoria[1])
        nombres.append(nombre_normalizado)
    return nombres

def id_categoria_valido(id_categoria: int) -> bool:
    for categoria in listar_categorias():
        if categoria[0] == id_categoria:
            return True
    return False


def agregar_categoria() -> None:
    while True:
        # --- Solicitar nombre válido ---
        nombre = pedir_input_con_cancelacion("Ingresá el nombre de la nueva categoría (C para cancelar): ")
        if nombre.lower() == "c":
            mostrar_cancelado("Categorías")
            return
        if not nombre:
            mostrar_error("El nombre de la categoría no puede estar vacío.")
            continue

        if normalizar_texto(nombre) in obtener_nombres_categorias_normalizados():
            mostrar_error("El nombre de la categoría ya existe.")
            continue
        break  # Nombre válido y único

    # --- Inserción ---
    nombre_formateado = formatear_nombre(nombre)
    if insertar_categoria(nombre_formateado):
        mostrar_exito(f"Categoría agregada correctamente → {nombre_formateado}")
        log_info(f"Categoría agregada → {nombre_formateado}")
    else:
        mostrar_error("No se pudo agregar la categoría.")

def editar_categoria() -> None:
    categorias = listar_categorias()
    if not categorias:
        mostrar_error("No hay categorías registradas.")
        return

    mostrar_categorias(categorias)

    # --- Solicitar ID válido ---
    while True:
        entrada = pedir_input_con_cancelacion("Ingresá el ID de la categoría a editar (C para cancelar): ")
        if entrada == "c":
            mostrar_cancelado("Categorías")
            return
        if not entrada.isdigit():
            mostrar_error("El ID debe ser un número.")
            continue

        id_categoria = int(entrada)

        if not id_categoria_valido(id_categoria):
            mostrar_error("El ID ingresado no corresponde a ninguna categoría.")
            continue
        break  # ID válido

    # --- Solicitar nuevo nombre ---
    while True:
        nuevo_nombre = pedir_input_con_cancelacion("Ingresá el nuevo nombre de la categoría (C para cancelar): ")
        if nuevo_nombre.lower() == "c":
            mostrar_cancelado("Categorías")
            return
        if not nuevo_nombre:
            mostrar_error("El nombre no puede estar vacío.")
            continue

        if normalizar_texto(nuevo_nombre) in obtener_nombres_categorias_normalizados():
            mostrar_error("El nombre de la categoría ya existe.")
            continue
        break  # Nombre nuevo válido

    # --- Actualización ---
    nombre_formateado = formatear_nombre(nuevo_nombre)
    if modificar_categoria(id_categoria, nombre_formateado):
        mostrar_exito(f"Categoría editada correctamente → ID: {id_categoria}, Nuevo nombre: {nombre_formateado}")
        log_info(f"Categoría editada → ID: {id_categoria}, Nuevo nombre: {nombre_formateado}")
    else:
        mostrar_error("No se pudo modificar la categoría.")

def borrar_categoria() -> None:
    categorias = listar_categorias()
    if not categorias:
        mostrar_error("No hay categorías registradas.")
        return

    mostrar_categorias(categorias)

    # Solicitar ID válido
    while True:
        entrada = pedir_input_con_cancelacion("Ingresá el ID de la categoría a eliminar (C para cancelar): ")
        if entrada == "c":
            mostrar_cancelado("Categorías")
            return
        if not entrada.isdigit():
            mostrar_error("El ID debe ser un número.")
            continue

        id_categoria = int(entrada)

        if not id_categoria_valido(id_categoria):
            mostrar_error("El ID ingresado no corresponde a ninguna categoría.")
            continue
        break  # ID válido

    if buscar_productos_por_categoria_id(id_categoria):
        mostrar_error("No se puede eliminar la categoría porque posée porductos asociados.\n"
    "Cambie la categoría de esos productos y vuelva a intentarlo."
        )
        return

    if eliminar_categoria(id_categoria):
        mostrar_exito(f"Categoría eliminada correctamente → ID: {id_categoria}")
        log_info(f"Categoría eliminada → ID: {id_categoria}")
    else:
        mostrar_error("No se pudo eliminar la categoría.")

def mostrar_todas_las_categorias():
    categorias = listar_categorias()
    if categorias:
        mostrar_categorias(categorias)
    else:
        mostrar_error("No hay categorías registradas.")