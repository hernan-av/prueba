from db.productos_db import insertar_producto, listar_productos, modificar_producto, eliminar_producto
from db.categorias_db import listar_categorias
from db.proveedores_db import listar_proveedores
from interfaz.entrada import pedir_input_con_cancelacion
from interfaz.mensajes import mostrar_error, mostrar_exito, mostrar_cancelado
from utils.utils import formatear_nombre
from interfaz.mostrar_resumen import mostrar_productos, mostrar_categorias, mostrar_proveedores

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
        try:
            id_categoria = int(entrada)
        except ValueError:
            mostrar_error("El ID debe ser un número.")
            continue

        id_categoria = int(entrada)
        
        ids_disponibles = []
        for cat in categorias:
            ids_disponibles.append(cat[0])

        if id_categoria not in ids_disponibles:
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
        try:
            id_categoria = int(entrada)
        except ValueError:
            mostrar_error("El ID debe ser un número.")
            continue
        id_proveedor = int(entrada)
        ids_disponibles = []
        for prov in proveedores:
            ids_disponibles.append(prov[0])
        if id_proveedor not in ids_disponibles:
            mostrar_error("El ID de proveedor no existe.")
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
    try:
        nombre_formateado = formatear_nombre(nombre)
        insertar_producto(nombre_formateado, id_categoria, id_proveedor, stock, precio_unitario)
        mostrar_exito("Producto agregado con éxito.")
    except Exception as e:
        mostrar_error(f"Error al agregar el producto: {e}")

def editar_producto():
    productos = listar_productos()
    if not productos:
        mostrar_error("No hay productos registrados.")
        return

    mostrar_productos(productos)

    # --- ID válido ---
    while True:
        entrada = pedir_input_con_cancelacion("Ingresá el ID del producto a modificar (C para cancelar): ")
        if entrada.lower() == "c":
            mostrar_cancelado("Productos")
            return
        if not entrada.isdigit():
            mostrar_error("El ID debe ser un número.")
            continue
        id_producto = int(entrada)
        ids_disponibles = [prod[0] for prod in productos]
        if id_producto not in ids_disponibles:
            mostrar_error("El ID de producto ingresado no existe.")
            continue
        break

    producto = next(p for p in productos if p[0] == id_producto)
    nombre_actual, categoria_actual, proveedor_actual, stock_actual, precio_actual = producto[1:6]

    # --- Nombre ---
    nuevo_nombre = pedir_input_con_cancelacion(
        f"📦 Nombre actual: {nombre_actual}\nIngresá el nuevo nombre (Enter para dejar igual, C para cancelar): "
    )
    if nuevo_nombre.lower() == "c":
        mostrar_cancelado("Productos")
        return
    if not nuevo_nombre.strip():
        nuevo_nombre = nombre_actual

    # --- Categoría ---
    categorias = listar_categorias()
    if not categorias:
        mostrar_error("No hay categorías disponibles.")
        return
    mostrar_categorias(categorias)

    while True:
        entrada = pedir_input_con_cancelacion(
            f"🏷️ Categoría actual: {categoria_actual}\nIngresá el ID de la nueva categoría (Enter para dejar igual, C para cancelar): "
        )
        if entrada.lower() == "c":
            mostrar_cancelado("Productos")
            return
        if entrada == "":
            nueva_categoria = next(cat[0] for cat in categorias if cat[1] == categoria_actual)
            break
        if not entrada.isdigit():
            mostrar_error("El ID debe ser un número.")
            continue
        nueva_categoria = int(entrada)
        ids = [cat[0] for cat in categorias]
        if nueva_categoria not in ids:
            mostrar_error("La categoría ingresada no existe.")
            continue
        break

    # --- Proveedor ---
    proveedores = listar_proveedores()
    if not proveedores:
        mostrar_error("No hay proveedores registrados.")
        return
    mostrar_proveedores(proveedores)

    while True:
        entrada = pedir_input_con_cancelacion(
            f"🏢 Proveedor actual: {proveedor_actual}\nIngresa el ID del nuevo proveedor (Enter para dejar igual, C para cancelar): "
        )
        if entrada.lower() == "c":
            mostrar_cancelado("Productos")
            return
        if entrada == "":
            nuevo_proveedor = next(pv[0] for pv in proveedores if pv[1] == proveedor_actual)
            break
        if not entrada.isdigit():
            mostrar_error("El ID debe ser un número.")
            continue
        nuevo_proveedor = int(entrada)
        ids = [prov[0] for prov in proveedores]
        if nuevo_proveedor not in ids:
            mostrar_error("El proveedor ingresado no existe.")
            continue
        break

    # --- Stock ---
    while True:
        entrada = pedir_input_con_cancelacion(
            f"📦 Stock actual: {stock_actual}\nIngresá el nuevo stock (Enter para dejar igual, C para cancelar): "
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
            f"💲 Precio actual: ${precio_actual:.2f}\nIngresá el nuevo precio (Enter para dejar igual, C para cancelar): "
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
    try:
        nombre_formateado = formatear_nombre(nuevo_nombre)
        modificar_producto(
            id_producto,
            nombre_formateado.strip(),
            nueva_categoria,
            nuevo_proveedor,
            nuevo_stock,
            nuevo_precio
        )
        mostrar_exito("Producto modificado correctamente.")
    except Exception as e:
        mostrar_error(f"Error al modificar el producto: {e}")

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
        try:
            id_producto = int(entrada)
        except ValueError:
            mostrar_error("El ID debe ser un número.")
            continue

        ids = []
        for prod in productos:
            ids.append(prod[0])

        if id_producto not in ids:
            mostrar_error("El ID de producto ingresado no existe.")
            continue
        break

    try:
        eliminar_producto(id_producto)
        mostrar_exito("Producto eliminado correctamente.")
    except Exception as e:
        mostrar_error(f"Error al eliminar el producto: {e}")

def mostrar_todos_los_productos():
    productos = listar_productos()
    if productos:
        mostrar_productos(productos)
    else:
        mostrar_error("No hay productos registrados.")