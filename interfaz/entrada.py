from db.productos_db import listar_productos
from interfaz.mensajes import mostrar_cancelado, mostrar_error, mostrar_exito
from interfaz.mostrar_resumen import mostrar_productos
from rich.console import Console

console = Console()

def pedir_input_con_cancelacion(prompt: str) -> str:
    """
    Pide un input al usuario. Si se ingresa 'c' (en cualquier combinación de mayúsculas/minúsculas),
    retorna 'c' para indicar una cancelación universal.
    """
    entrada = input(prompt).strip()
    if entrada.lower() == "c":
        return "c"
    return entrada

def cargar_productos_para_venta() -> list[dict] | str:
    productos_disponibles = listar_productos()
    if not productos_disponibles:
        mostrar_error("No hay productos cargados en el sistema.")
        return "CANCELADO"

    mostrar_productos(productos_disponibles)
    productos = []

    while True:
        entrada = pedir_input_con_cancelacion("Ingresá el ID del producto que querés vender (C para cancelar): ")
        if entrada.lower() == "c":
            mostrar_cancelado("Carga de productos")
            return "CANCELADO"
        try:
            producto_id = int(entrada)
        except ValueError:
            mostrar_error("El ID debe ser un número.")
            continue

        producto_elegido = next((prod for prod in productos_disponibles if prod[0] == producto_id), None)
        if not producto_elegido:
            mostrar_error("El ID ingresado no corresponde a ningún producto.")
            continue

        nombre, stock_disponible, precio_unitario = producto_elegido[1], producto_elegido[4], producto_elegido[5]
        print(f"Stock disponible: {stock_disponible} unidades | Precio unitario: ${precio_unitario:.2f}")

        while True:
            cantidad_input = pedir_input_con_cancelacion(f"Ingresá la cantidad a vender de '{nombre}' (C para cancelar): ")
            if cantidad_input.lower() == "c":
                mostrar_cancelado("Carga de productos")
                return "CANCELADO"
            try:
                cantidad = int(cantidad_input)
            except ValueError:
                mostrar_error("La cantidad debe ser un número entero.")
                continue
            if cantidad <= 0 or cantidad > stock_disponible:
                mostrar_error("Cantidad inválida o supera el stock disponible.")
                continue
            break

        productos.append({
            "producto_id": producto_id,
            "cantidad": cantidad
        })

        continuar = pedir_input_con_cancelacion("¿Querés agregar otro producto? (S para seguir / cualquier otra letra para finalizar): ")
        if continuar.lower() != "s":
            break

    return productos if productos else "CANCELADO"


def cargar_productos_para_ingreso() -> list[dict] | str:
    productos_disponibles = listar_productos()
    if not productos_disponibles:
        mostrar_error("No hay productos cargados en el sistema.")
        return "CANCELADO"

    mostrar_productos(productos_disponibles)
    productos = []

    while True:
        entrada = pedir_input_con_cancelacion("📦 Ingresá el ID del producto a ingresar (C para cancelar): ")
        if entrada.lower() == "c":
            mostrar_cancelado("Carga de ingreso")
            return "CANCELADO"
        try:
            producto_id = int(entrada)
        except ValueError:
            mostrar_error("El ID debe ser un número.")
            continue

        producto = next((prod for prod in productos_disponibles if prod[0] == producto_id), None)
        if not producto:
            mostrar_error("El producto no existe.")
            continue

        nombre_prod = producto[1]
        print(f"📘 Producto: {nombre_prod}")

        # Cantidad
        while True:
            cantidad_input = pedir_input_con_cancelacion("Cantidad ingresada (C para cancelar): ")
            if cantidad_input.lower() == "c":
                mostrar_cancelado("Carga de ingreso")
                return "CANCELADO"
            try:
                cantidad = int(cantidad_input)
                if cantidad <= 0:
                    mostrar_error("La cantidad debe ser mayor que cero.")
                    continue
                break
            except ValueError:
                mostrar_error("La cantidad debe ser un número entero.")

        # Precio unitario
        while True:
            precio_input = pedir_input_con_cancelacion("Precio unitario del ingreso (C para cancelar): ")
            if precio_input.lower() == "c":
                mostrar_cancelado("Carga de ingreso")
                return "CANCELADO"
            try:
                precio_unitario = float(precio_input)
                if precio_unitario <= 0:
                    mostrar_error("El precio debe ser mayor que cero.")
                    continue
                break
            except ValueError:
                mostrar_error("El precio debe ser un número válido.")

        productos.append({
            "producto_id": producto_id,
            "cantidad": cantidad,
            "precio_unitario": precio_unitario
        })

        seguir = pedir_input_con_cancelacion("¿Agregar otro producto? (S para seguir / otra letra para finalizar): ")
        if seguir.lower() != "s":
            break

    return productos if productos else "CANCELADO"