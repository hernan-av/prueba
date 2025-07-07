# ---------- GESTIÓN DE CATEGORÍAS ----------

from db.categorias_db import insertar_categoria, listar_categorias, modificar_categoria, eliminar_categoria
from interfaz.entrada import pedir_input_con_cancelacion
from interfaz.mostrar_resumen import mostrar_categorias
from interfaz.mensajes import mostrar_error, mostrar_exito, mostrar_cancelado
from utils.utils import normalizar_texto, formatear_nombre
from db.productos_db import buscar_productos_por_categoria_id

def agregar_categoria() -> None:
    while True:
        nombre = pedir_input_con_cancelacion("Ingresá el nombre de la nueva categoría (C para cancelar): ")
        if nombre.lower() == "c":
            mostrar_cancelado("Categorías")
            return

        if not nombre:
            mostrar_error("El nombre de la categoría no puede estar vacío.")
            continue

        nombre_normalizado = normalizar_texto(nombre)
        categorias_existentes = []
        for cat in listar_categorias():
            nombre_categoria = cat[1]
            nombre_categoria_normalizado = normalizar_texto(nombre_categoria)
            categorias_existentes.append(nombre_categoria_normalizado)

        if nombre_normalizado in categorias_existentes:
            mostrar_error("El nombre de la categoría ya existe.")
            continue

        break  # Nombre válido y único

    try:
        nombre_formateado = formatear_nombre(nombre)
        insertar_categoria(nombre_formateado)
        mostrar_exito("Categoría agregada correctamente.")
    except Exception as e:
        mostrar_error(f"No se pudo agregar la categoría: {e}")

def editar_categoria() -> None:
    categorias = listar_categorias()
    if not categorias:
        mostrar_error("No hay categorías registradas.")
        return

    mostrar_categorias(categorias)

    # Solicitar ID válido
    while True:
        entrada = pedir_input_con_cancelacion("Ingresá el ID de la categoría a editar (C para cancelar): ")
        if entrada == "c":
            mostrar_cancelado("Categorías")
            return
        if not entrada.isdigit():
            mostrar_error("El ID debe ser un número.")
            continue

        id_categoria = int(entrada)
        ids_disponibles = []
        for cat in listar_categorias():
            ids_disponibles.append(cat[0])

        if id_categoria not in ids_disponibles:
            mostrar_error("El ID ingresado no corresponde a ninguna categoría.")
            continue

        break  # ID válido

    # Solicitar nuevo nombre
    while True:
        nuevo_nombre = pedir_input_con_cancelacion("Ingresá el nuevo nombre de la categoría (C para cancelar): ")
        if nuevo_nombre.lower() == "c":
            mostrar_cancelado("Categorías")
            return
        if not nuevo_nombre:
            mostrar_error("El nombre no puede estar vacío.")
            continue

        nombre_normalizado = normalizar_texto(nuevo_nombre)
        categorias_existentes = []
        for cat in listar_categorias():
            nombre_categoria = cat[1]
            nombre_categoria_normalizado = normalizar_texto(nombre_categoria)
            categorias_existentes.append(nombre_categoria_normalizado)

        if nombre_normalizado in categorias_existentes:
            mostrar_error("El nombre de la categoría ya existe.")
            continue

        break  # Nombre nuevo válido

    try:
        nombre_formateado = formatear_nombre(nuevo_nombre)
        modificar_categoria(id_categoria, nombre_formateado)
        mostrar_exito("Categoría editada correctamente.")
    except Exception as e:
        mostrar_error(f"No se pudo editar la categoría: {e}")

def borrar_categoria() -> None:
    categorias = listar_categorias()
    if not categorias:
        mostrar_error("No hay categorías registradas.")
        return

    mostrar_categorias(categorias)

    while True:
        entrada = pedir_input_con_cancelacion("Ingresá el ID de la categoría a eliminar (C para cancelar): ")
        if entrada == "c":
            mostrar_cancelado("Categorías")
            return
        if not entrada.isdigit():
            mostrar_error("El ID debe ser un número.")
            continue

        id_categoria = int(entrada)
        ids_disponibles = []
        for cat in categorias:
            ids_disponibles.append(cat[0])

        if id_categoria not in ids_disponibles:
            mostrar_error("El ID ingresado no corresponde a ninguna categoría.")
            continue

        break  # ID válido

    if buscar_productos_por_categoria_id(id_categoria):
        mostrar_error(
    "No se puede eliminar la categoría porque posée porductos asociados.\n"
    "Cambie la categoría de esos productos y vuelva a intentarlo."
    )
        return

    try:
        eliminar_categoria(id_categoria)
        mostrar_exito("Categoría eliminada correctamente.")
    except Exception as e:
        mostrar_error(f"No se pudo eliminar la categoría: {e}")

def mostrar_todas_las_categorias():
    categorias = listar_categorias()
    if categorias:
        mostrar_categorias(categorias)
    else:
        mostrar_error("No hay categorías registradas.")