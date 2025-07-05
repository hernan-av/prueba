# ---------- GESTIÓN DE VENTAS ----------

from utils.tiempo import obtener_fecha_actual
from db.clientes_db import listar_clientes
from db.productos_db import listar_productos
from db.facturas_db import insertar_factura, insertar_factura_detalle, descontar_stock

def registrar_venta(cliente_id: int, productos: list[dict]) -> dict | str:
    fecha = obtener_fecha_actual()

    clientes = [cli[0] for cli in listar_clientes()]
    if cliente_id not in clientes:
        return "❌ El ID de cliente ingresado no existe, cree el nuevo cliente y reintente la venta."

    productos_db = {prod[0]: {"stock": prod[4], "precio_unitario": prod[5]} for prod in listar_productos()}

    total_factura = 0
    detalles_validos = []

    for item in productos:
        producto_id = item.get("producto_id")
        cantidad = item.get("cantidad", 0)

        if (
            producto_id not in productos_db
            or cantidad <= 0
            or productos_db[producto_id]["stock"] < cantidad
        ):
            return f"❌ Producto inválido o sin stock suficiente: {item}"

        precio_unitario = productos_db[producto_id]["precio_unitario"]
        total_linea = round(precio_unitario * cantidad, 2)

        total_factura += total_linea
        detalles_validos.append({
            "producto_id": producto_id,
            "cantidad": cantidad,
            "precio_unitario": precio_unitario,
            "total_linea": total_linea
        })

    try:
        id_factura = insertar_factura(fecha, cliente_id, total_factura)
        for detalle in detalles_validos:
            insertar_factura_detalle(
                id_factura,
                detalle["producto_id"],
                detalle["cantidad"],
                detalle["precio_unitario"],
                detalle["total_linea"]
            )
            descontar_stock(detalle["producto_id"], detalle["cantidad"])

        return {
            "id_factura": id_factura,
            "fecha": fecha,
            "cliente_id": cliente_id,
            "total": round(total_factura, 2),
            "productos_vendidos": detalles_validos
        }
    except Exception as e:
        return f"Error al registrar la venta: {e}"