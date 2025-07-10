# ---------- GESTIÓN DE VENTAS ----------

from utils.utils import obtener_fecha_actual
from db.clientes_db import listar_clientes
from db.productos_db import listar_productos
from db.facturas_db import insertar_factura, insertar_factura_detalle, descontar_stock, obtener_detalle_venta, listar_facturas
from interfaz.mostrar_resumen import mostrar_clientes,mostrar_facturas, mostrar_resumen_venta
from interfaz.mensajes import mostrar_error,mostrar_exito, mostrar_cancelado
from interfaz.entrada import pedir_input_con_cancelacion, cargar_productos_para_venta
from gestor.exportador_pdf import generar_pdf_factura

def registrar_venta(cliente_id: int, productos: list[dict]) -> int | None:
    fecha = obtener_fecha_actual()

    # Construir diccionario de productos desde DB
    productos_db = {}
    productos_raw = listar_productos()
    for prod in productos_raw:
        productos_db[prod[0]] = {
            "nombre": prod[1],
            "stock": prod[4],
            "precio_unitario": prod[5]
        }

    total_factura = 0
    detalles = []

    for item in productos:
        pid = item["producto_id"]
        cantidad = item["cantidad"]
        precio = productos_db[pid]["precio_unitario"]
        subtotal = round(cantidad * precio, 2)
        total_factura += subtotal

        detalles.append({
            "producto_id": pid,
            "cantidad": cantidad,
            "precio_unitario": precio,
            "total_linea": subtotal
        })

    try:
        factura_id = insertar_factura(fecha, cliente_id, total_factura)

        for detalle in detalles:
            insertar_factura_detalle(
                factura_id,
                detalle["producto_id"],
                detalle["cantidad"],
                detalle["precio_unitario"],
                detalle["total_linea"]
            )
            descontar_stock(detalle["producto_id"], detalle["cantidad"])

        return factura_id

    except Exception as e:
        mostrar_error(f"Error al registrar la venta: {e}")
        return None

def procesar_venta_interactiva():
    clientes = listar_clientes()
    if not clientes:
        mostrar_error("No hay clientes registrados. Ingresa al nuevo cliente y luego reintenta la venta")
        return

    mostrar_clientes(clientes)

    # 🧍 Selección de cliente
    while True:
        entrada = pedir_input_con_cancelacion("🧍 Ingresá el ID del cliente para la venta (C para cancelar): ")
        if entrada.lower() == "c":
            mostrar_cancelado("Ventas")
            return
        try:
            cliente_id = int(entrada)
        except ValueError:
            mostrar_error("El ID debe ser un número.")
            continue
        if cliente_id not in [cli[0] for cli in clientes]:
            mostrar_error("El cliente no existe.")
            continue
        break

    # 🛒 Carga de productos
    productos = cargar_productos_para_venta()
    if productos == "CANCELADO":
        return

    # 🧠 Mostrar resumen previo a confirmar la venta
    productos_db = listar_productos()
    productos_dict = {}
    for prod in productos_db:
        productos_dict[prod[0]] = {
            "nombre": prod[1],
            "precio_unitario": prod[5]
        }

    from rich.table import Table
    from rich.panel import Panel
    from rich.console import Console

    console = Console()

    total_final = 0
    tabla = Table(title="🛍️ RESUMEN DE VENTA (A CONFIRMAR)", show_lines=True, header_style="bold cyan")
    tabla.add_column("Producto", style="white", justify="left")
    tabla.add_column("Cantidad", justify="right")
    tabla.add_column("Precio Unitario", justify="right")
    tabla.add_column("Subtotal", justify="right")

    for item in productos:
        pid = item["producto_id"]
        nombre = productos_dict[pid]["nombre"]
        precio_unit = productos_dict[pid]["precio_unitario"]
        cantidad = item["cantidad"]
        subtotal = cantidad * precio_unit
        total_final += subtotal

        tabla.add_row(
            nombre,
            str(cantidad),
            f"${precio_unit:.2f}",
            f"${subtotal:.2f}"
        )

    console.print(tabla)
    panel_total = Panel.fit(f"[bold yellow]TOTAL FINAL: ${total_final:.2f}[/bold yellow]", border_style="green", title="💰 Total")
    console.print(panel_total)

    # Confirmación
    respuesta = pedir_input_con_cancelacion("¿Deseás confirmar esta venta? (S para confirmar, otra tecla para cancelar): ")
    if respuesta.lower() != "s":
        mostrar_cancelado("Venta no confirmada")
        return

    # Registrar venta
    factura_id = registrar_venta(cliente_id, productos)
    if factura_id is None:
        mostrar_error("No se pudo registrar la venta.")
        return

    mostrar_resumen_venta(factura_id)
    ruta = generar_pdf_factura(factura_id)
    mostrar_exito(f"📄 Factura guardada en: {ruta}")

def imprimir_detalle_venta():
    lista_facturas = listar_facturas()
    if not lista_facturas:
        mostrar_error("No hay facturas registradas.")
        return

    mostrar_facturas(lista_facturas)

    while True:
        entrada = pedir_input_con_cancelacion("🧾 Ingresá el ID de la factura para ver el detalle (C para cancelar): ")
        if entrada.lower() == "c":
            mostrar_cancelado("Ventas")
            return

        try:
            id_factura = int(entrada)
        except ValueError:
            mostrar_error("El ID debe ser un número.")
            continue

        ids_disponibles = [fact[0] for fact in lista_facturas]
        if id_factura not in ids_disponibles:
            mostrar_error("El ID de factura no existe.")
            continue

        break  # ID válido

    detalle = obtener_detalle_venta(id_factura)
    mostrar_resumen_venta(id_factura)  # Asumiendo que ya está adaptada
    return detalle  # Por si querés usarlo luego
