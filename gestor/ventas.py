# ---------- GESTIÓN DE VENTAS ----------

from utils.utils import obtener_fecha_actual
from db.clientes_db import listar_clientes
from db.productos_db import listar_productos
from db.facturas_db import insertar_factura, insertar_factura_detalle, descontar_stock
from interfaz.mostrar_resumen import mostrar_clientes, mostrar_resumen_venta
from interfaz.mensajes import mostrar_error,mostrar_exito, mostrar_cancelado
from interfaz.entrada import pedir_input_con_cancelacion, cargar_productos_para_venta
from db.generador_pdf import generar_pdf_factura

def registrar_venta(cliente_id: int, productos: list[dict]) -> dict | str:
    fecha = obtener_fecha_actual()
    productos_db = {prod[0]: {"nombre": prod[1], "stock": prod[4], "precio_unitario": prod[5]} for prod in listar_productos()}

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
        return {
            "id_factura": factura_id,
            "fecha": fecha,
            "cliente_id": cliente_id,
            "total": round(total_factura, 2),
            "productos_vendidos": detalles
        }
    except Exception as e:
        mostrar_error( f"Error al registrar la venta: {e}")

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

    #Carga de productos
    productos = cargar_productos_para_venta()
    if productos == "CANCELADO":
        return

    #Registro en base de datos
    resumen = registrar_venta(cliente_id, productos)
    if not isinstance(resumen, dict):
        mostrar_error(resumen)
        return

    # Mostrar resumen por consola
    mostrar_resumen_venta(resumen)

    #Generar PDF
    resultado_pdf = generar_pdf_factura(resumen["id_factura"])
    mostrar_exito(resultado_pdf)
