from db.productos_db import listar_productos
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

def confirmar_accion(texto: str) -> bool:
    """
    Pide confirmación al usuario. Devuelve True si confirma con 's' o 'S', False en cualquier otro caso.
    """
    respuesta = input(f"{texto} (s/n): ").strip().lower()
    return respuesta == "s"

def cargar_productos_para_venta() -> list[dict] | str:
    productos = []
    productos_disponibles = {prod[0]: {"nombre": prod[1], "stock": prod[4], "precio_unitario": prod[5]} for prod in listar_productos()}

    while True:
        try:
            producto_id = int(input("🛒 Ingresá el ID del producto (o 'c' para cancelar): ").strip())
        except ValueError:
            print("❌ Ingresá un número válido.")
            continue

        if producto_id not in productos_disponibles:
            print("❌ El producto no existe.")
            continue

        try:
            cantidad = int(input(f"📦 Cantidad de '{productos_disponibles[producto_id]['nombre']}': ").strip())
        except ValueError:
            print("❌ Ingresá una cantidad válida.")
            continue

        if cantidad <= 0 or cantidad > productos_disponibles[producto_id]['stock']:
            print("❌ Cantidad inválida o supera el stock disponible.")
            continue

        productos.append({
            "producto_id": producto_id,
            "cantidad": cantidad
        })

        seguir = input("¿Agregar otro producto? (s/n): ").strip().lower()
        if seguir != "s":
            break

    return productos if productos else "CANCELADO"

def cargar_productos_para_ingreso() -> list[dict] | str:
    productos = []
    productos_disponibles = {prod[0]: prod[1] for prod in listar_productos()}

    while True:
        try:
            producto_id = int(input("📦 Ingresá el ID del producto a ingresar (o 'c' para cancelar): ").strip())
        except ValueError:
            print("❌ Ingresá un número válido.")
            continue

        if producto_id not in productos_disponibles:
            print("❌ El producto no existe.")
            continue

        try:
            cantidad = int(input("Cantidad ingresada: ").strip())
            precio = float(input("Precio unitario del ingreso: ").strip())
        except ValueError:
            print("❌ Ingresá valores numéricos válidos.")
            continue

        if cantidad <= 0 or precio <= 0:
            print("❌ La cantidad o el precio deben ser mayores a 0.")
            continue

        productos.append({
            "producto_id": producto_id,
            "cantidad": cantidad,
            "precio_unitario": precio
        })

        seguir = input("¿Agregar otro producto? (s/n): ").strip().lower()
        if seguir != "s":
            break

    return productos if productos else "CANCELADO"