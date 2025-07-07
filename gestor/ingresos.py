# ---------- GESTIÓN DE INGRESOS ----------

from utils.utils import obtener_fecha_actual
from db.remitos_db import insertar_remito, insertar_remito_detalle, actualizar_stock
from db.proveedores_db import listar_proveedores
from interfaz.mostrar_resumen import mostrar_proveedores, mostrar_resumen_ingreso
from interfaz.entrada import pedir_input_con_cancelacion, cargar_productos_para_ingreso
from interfaz.mensajes import mostrar_error, mostrar_cancelado, mostrar_exito
from db.generador_pdf import generar_pdf_remito

def registrar_ingreso(proveedor_id: int, productos: list[dict]) -> dict | None:
    fecha = obtener_fecha_actual()
    try:
        id_remito = insertar_remito(fecha, proveedor_id)
        for item in productos:
            insertar_remito_detalle(
                id_remito,
                item["producto_id"],
                item["cantidad"],
                item["precio_unitario"]
            )
            actualizar_stock(item["producto_id"], item["cantidad"])
        return {
            "id_remito": id_remito,
            "fecha": fecha,
            "proveedor_id": proveedor_id,
            "productos_recibidos": productos
        }
    except Exception as e:
        mostrar_error(f"Error al registrar el ingreso: {e}")
        return None


def procesar_ingreso_interactivo():
    proveedores = listar_proveedores()
    if not proveedores:
        mostrar_error("No hay proveedores registrados.")
        return

    mostrar_proveedores(proveedores)

    while True:
        entrada = pedir_input_con_cancelacion("Ingresá el ID del proveedor del ingreso (C para cancelar): ")
        if entrada.lower() == "c":
            mostrar_cancelado("Ingresos")
            return
        try:
            proveedor_id = int(entrada)
        except ValueError:
            mostrar_error("El ID debe ser un número.")
            continue
        if proveedor_id not in [prov[0] for prov in proveedores]:
            mostrar_error("El proveedor no existe.")
            continue
        break

    productos = cargar_productos_para_ingreso()
    if productos == "CANCELADO":
        return

    resumen = registrar_ingreso(proveedor_id, productos)
    if resumen:
        mostrar_resumen_ingreso(resumen)
        resultado_pdf = generar_pdf_remito(resumen["id_remito"])
        mostrar_exito(resultado_pdf)