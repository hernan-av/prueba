# ---------- GESTIÓN DE BUSQUEDA ----------

from db.clientes_db import listar_clientes
from db.proveedores_db import listar_proveedores
from db.productos_db import listar_productos
from db.remitos_db import listar_remitos
from db.facturas_db import listar_facturas

def buscar_factura(valor: str) -> list:
    resultados = []
    for factura in listar_facturas():
        id_factura = str(factura[0])
        fecha = factura[1].lower()
        if valor.lower() in id_factura or valor.lower() in fecha:
            resultados.append(factura)
    return resultados

def buscar_remito(valor: str) -> list:
    resultados = []
    for remito in listar_remitos():
        id_remito = str(remito[0])
        fecha = remito[1].lower()
        if valor.lower() in id_remito or valor.lower() in fecha:
            resultados.append(remito)
    return resultados

def buscar_cliente(valor: str) -> list:
    resultados = []
    for cli in listar_clientes():
        id_cliente = str(cli[0])
        nombre = cli[1].lower()
        if valor.lower() in id_cliente or valor.lower() in nombre:
            resultados.append(cli)
    return resultados


def buscar_proveedor(valor: str) -> list:
    resultados = []
    for prov in listar_proveedores():
        id_prov = str(prov[0])
        nombre = prov[1].lower()
        if valor.lower() in id_prov or valor.lower() in nombre:
            resultados.append(prov)
    return resultados


def buscar_producto(valor: str) -> list:
    resultados = []
    for prod in listar_productos():
        id_prod = str(prod[0])
        nombre = prod[1].lower()
        if valor.lower() in id_prod or valor.lower() in nombre:
            resultados.append(prod)
    return resultados