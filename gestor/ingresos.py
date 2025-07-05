# ---------- GESTIÓN DE INGRESOS ----------

from utils.tiempo import obtener_fecha_actual
from db.proveedores_db import listar_proveedores
from db.productos_db import listar_productos
from db.remitos_db import insertar_remito, insertar_remito_detalle, actualizar_stock

def registrar_ingreso(proveedor_id, productos: list[dict]):
    fecha = obtener_fecha_actual()

    proveedores = [prov[0] for prov in listar_proveedores()]
    if proveedor_id not in proveedores:
        return "❌ El ID de proveedor ingresado no existe."

    productos_disponibles = [prod[0] for prod in listar_productos()]
    for item in productos:
        if (
            not isinstance(item, dict)
            or "producto_id" not in item
            or "cantidad" not in item
            or "precio_unitario" not in item
            or item["producto_id"] not in productos_disponibles
        ):
            return f"❌ Producto inválido o inconsistente: {item}"

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
        return f"Error al registrar el ingreso: {e}"