# ---------- GESTIÓN DE PRODUCTOS ----------

from db.productos_db import insertar_producto, listar_productos, listar_tabla_producto, modificar_producto, eliminar_producto
from db.categorias_db import listar_categorias
from db.proveedores_db import listar_proveedores
from interfaz.entrada import pedir_input_con_cancelacion
from interfaz.mensajes import mostrar_error, mostrar_exito, mostrar_cancelado
from utils.utils import formatear_nombre
from utils.logger import log_info
from interfaz.mostrar_resumen import mostrar_productos, mostrar_categorias, mostrar_proveedores
from gestor.categorias import id_categoria_valido
from gestor.proveedores import obtener_proveedor_por_id

def obtener_ids_productos() -> list[int]:
    ids = []
    for prod in listar_productos():
        ids.append(prod[0])
    return ids

def agregar_producto():
    # ---- Nombre ----
    while True:
        nombre = pedir_input_con_cancelacion("Ingresá el nombre del nuevo producto (C para cancelar): ")
        if nombre.lower() == "c":
            mostrar_cancelado("Productos")
            return
        if not nombre:
            mostrar_error("El nombre del producto no puede estar vacío.")
            continue
        break

    # ---- Categoría ----
    categorias = listar_categorias()
    if not categorias:
        mostrar_error("No hay categorías registradas. Creá una antes de continuar.")
        return
    mostrar_categorias(categorias)

    while True:
        entrada = pedir_input_con_cancelacion("Ingresá el ID de la categoría (C para cancelar): ")
        if entrada.lower() == "c":
            mostrar_cancelado("Productos")
            return
        if not entrada.isdigit():
            mostrar_error("El ID debe ser un número.")
            continue

        id_categoria = int(entrada)
        
        if not id_categoria_valido(id_categoria):
            mostrar_error("El ID de categoría no existe.")
            continue
        break

    # ---- Proveedor ----
    proveedores = listar_proveedores()
    if not proveedores:
        mostrar_error("No hay proveedores registrados. Creá uno antes de continuar.")
        return
    mostrar_proveedores(proveedores)

    while True:
        entrada = pedir_input_con_cancelacion("Ingresá el ID del proveedor (C para cancelar): ")
        if entrada.lower() == "c":
            mostrar_cancelado("Productos")
            return
        if not entrada.isdigit():
            mostrar_error("El ID debe ser un número.")
            continue
        
        id_proveedor = int(entrada)
        proveedor = obtener_proveedor_por_id(id_proveedor)
        if proveedor is None:
            mostrar_error("El ID de proveedor ingresado no existe.")
            continue
        break

    # ---- Stock ----
    while True:
        entrada = pedir_input_con_cancelacion("Ingresá el stock a cargar (C para cancelar): ")
        if entrada.lower() == "c":
            mostrar_cancelado("Productos")
            return
        try:
            stock = int(entrada)
            if stock < 0:
                mostrar_error("El stock no puede ser negativo.")
                continue
            break
        except ValueError:
            mostrar_error("El stock debe ser un número entero.")


    # ---- Precio unitario ----
    while True:
        entrada = pedir_input_con_cancelacion("Ingresá el precio unitario (C para cancelar): ")
        if entrada.lower() == "c":
            mostrar_cancelado("Productos")
            return
        try:
            precio_unitario = float(entrada)
            if precio_unitario <= 0:
                mostrar_error("El precio debe ser mayor que cero.")
                continue
            break
        except ValueError:
            mostrar_error("El precio debe ser un número válido.")

    # ---- Inserción ----
    nombre_formateado = formatear_nombre(nombre)
    if insertar_producto(nombre_formateado, id_categoria, id_proveedor, stock, precio_unitario):
        mostrar_exito(f"Producto agregado correctamente → Nombre: {nombre_formateado}")
        log_info(f"Producto agregado → Nombre: {nombre_formateado}")
    else:
        mostrar_error("No se pudo agregar el producto.")

def editar_producto():
    productos = listar_productos()
    if not productos:
        mostrar_error("No hay productos registrados.")
        return

    mostrar_productos(productos)

    # --- Solicitar ID válido ---
    while True:
        entrada = pedir_input_con_cancelacion("Ingresá el ID del producto a modificar (C para cancelar): ")
        if entrada.lower() == "c":
            mostrar_cancelado("Productos")
            return
        if not entrada.isdigit():
            mostrar_error("El ID debe ser un número.")
            continue
        id_producto = int(entrada)
        producto = listar_tabla_producto(id_producto)
        if producto is None:
            mostrar_error("El ID de producto ingresado no existe.")
            continue
        break # ID válido

    nombre_actual = producto[1]
    id_categoria_actual = producto[2]
    id_proveedor_actual = producto[3]
    stock_actual = producto[4]
    precio_actual = producto[5]

    # --- Nombre ---
    nuevo_nombre = pedir_input_con_cancelacion(
        f"Nombre actual: {nombre_actual}\nIngresá el nuevo nombre (Enter para dejar igual, C para cancelar): "
    )
    if nuevo_nombre.lower() == "c":
        mostrar_cancelado("Productos")
        return
    if not nuevo_nombre:
        nuevo_nombre = nombre_actual

    # --- Categoría ---
    categorias = listar_categorias()
    if not categorias:
        mostrar_error("No hay categorías disponibles.")
        return
    mostrar_categorias(categorias)

    while True:
        entrada = pedir_input_con_cancelacion(
            f"Categoría actual: {id_categoria_actual}\nIngresá el ID de la nueva categoría (Enter para dejar igual, C para cancelar): "
        )
        if entrada.lower() == "c":
            mostrar_cancelado("Productos")
            return
        if not entrada:
            nueva_categoria = id_categoria_actual
            break
        if not entrada.isdigit():
            mostrar_error("El ID debe ser un número.")
            continue

        nueva_categoria = int(entrada)
        if not id_categoria_valido(nueva_categoria):
            mostrar_error("El ID categoría ingresado no existe.")
            continue
        break  # ID válido


    # --- Proveedor ---
    proveedores = listar_proveedores()
    if not proveedores:
        mostrar_error("No hay proveedores registrados.")
        return
    mostrar_proveedores(proveedores)

    while True:
        entrada = pedir_input_con_cancelacion(
            f"Proveedor actual: {id_proveedor_actual}\nIngresá el ID del nuevo proveedor (Enter para dejar igual, C para cancelar): "
        )
        if entrada.lower() == "c":
            mostrar_cancelado("Productos")
            return
        if not entrada:
            nuevo_proveedor = id_proveedor_actual
            break
        if not entrada.isdigit():
            mostrar_error("El ID debe ser un número.")
            continue

        nuevo_proveedor = int(entrada)
        proveedor = obtener_proveedor_por_id(nuevo_proveedor)
        if proveedor is None:
            mostrar_error("El ID de proveedor ingresado no existe.")
            continue
        break

    # --- Stock ---
    while True:
        entrada = pedir_input_con_cancelacion(
            f"Stock actual: {stock_actual}\nIngresá el nuevo stock (Enter para dejar igual, C para cancelar): "
        )
        if entrada.lower() == "c":
            mostrar_cancelado("Productos")
            return
        if entrada == "":
            nuevo_stock = stock_actual
            break
        try:
            nuevo_stock = int(entrada)
            if nuevo_stock < 0:
                mostrar_error("El stock no puede ser negativo.")
                continue
            break
        except ValueError:
            mostrar_error("El stock debe ser un número entero.")

    # --- Precio unitario ---
    while True:
        entrada = pedir_input_con_cancelacion(
            f"Precio actual: ${precio_actual:.2f}\nIngresá el nuevo precio (Enter para dejar igual, C para cancelar): "
        )
        if entrada.lower() == "c":
            mostrar_cancelado("Productos")
            return
        if entrada == "":
            nuevo_precio = precio_actual
            break
        try:
            nuevo_precio = float(entrada)
            if nuevo_precio <= 0:
                mostrar_error("El precio debe ser mayor que cero.")
                continue
            break
        except ValueError:
            mostrar_error("El precio debe ser un número válido.")

    # --- Actualización ---
    nombre_formateado = formatear_nombre(nuevo_nombre)
    if modificar_producto(
        id_producto,
        nombre_formateado,
        nueva_categoria,
        nuevo_proveedor,
        nuevo_stock,
        nuevo_precio
    ):
        mostrar_exito(f"Producto editado correctamente → ID: {id_producto}")
        log_info(f"Producto editado → ID: {id_producto}")
    else:
        mostrar_error("No se pudo modificar el producto.")

def borrar_producto():
    productos = listar_productos()
    if not productos:
        mostrar_error("No hay productos registrados.")
        return

    mostrar_productos(productos)

    while True:
        entrada = pedir_input_con_cancelacion("Ingresá el ID del producto a eliminar (C para cancelar): ")
        if entrada.lower() == "c":
            mostrar_cancelado("Productos")
            return
        if not entrada.isdigit():
            mostrar_error("El ID debe ser un número.")
            continue
        id_producto = int(entrada)
        if id_producto not in obtener_ids_productos():
            mostrar_error("El ID de producto ingresado no existe.")
            continue
        break # ID válido

    if eliminar_producto(id_producto):
        mostrar_exito(f"Producto eliminado correctamente → ID: {id_producto}")
        log_info(f"Producto eliminado → ID: {id_producto}")
    else:
        mostrar_error("No se pudo eliminar el producto.")

def mostrar_todos_los_productos():
    productos = listar_productos()
    if productos:
        mostrar_productos(productos)
    else:
        mostrar_error("No hay productos registrados.")