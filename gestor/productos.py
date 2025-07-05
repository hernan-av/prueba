# ---------- GESTIÓN DE PRODUCTOS ----------

from db.categorias_db import listar_categorias
from db.proveedores_db import listar_proveedores
from db.productos_db import (
    insertar_producto,
    listar_productos,
    modificar_producto,
    eliminar_producto
)

def agregar_producto(nombre: str, categoria_id, proveedor_id, stock, precio_unitario):
    if not nombre.strip():
        return "❌ El nombre no puede estar vacío."
    if stock < 0:
        return "❌ El stock debe ser un número entero mayor o igual a 0."
    if precio_unitario <= 0:
        return "❌ El precio unitario debe ser un número positivo."

    categorias = []
    for cat in listar_categorias():
        categorias.append(cat[0])

    proveedores = []
    for prov in listar_proveedores():
        proveedores.append(prov[0])

    if categoria_id not in categorias:
        return "❌ La categoría seleccionada no existe."
    if proveedor_id not in proveedores:
        return "❌ El proveedor seleccionado no existe."

    try:
        insertar_producto(nombre.strip(), categoria_id, proveedor_id, stock, precio_unitario)
        return "ok: Producto agregado con éxito."
    except Exception as e:
        return f"Error al agregar el producto: {e}"

def editar_producto(id_producto, nuevo_nombre: str, nueva_categoria, nuevo_proveedor, nuevo_stock, nuevo_precio):
    ids = []
    for prod in listar_productos():
        ids.append(prod[0])

    if id_producto not in ids:
        return "❌ El ID de producto ingresado no existe."
    if not nuevo_nombre.strip():
        return "❌ El nombre no puede estar vacío."
    if nuevo_stock < 0:
        return "❌ El stock debe ser un número entero mayor o igual a 0."
    if nuevo_precio <= 0:
        return "❌ El precio unitario debe ser un número positivo."

    categorias = []
    for cat in listar_categorias():
        categorias.append(cat[0])

    proveedores = []
    for prov in listar_proveedores():
        proveedores.append(prov[0])

    if nueva_categoria not in categorias:
        return "❌ La categoría ingresada no existe. Créala y vuelve a intentarlo."
    if nuevo_proveedor not in proveedores:
        return "❌ El proveedor ingresado no existe. Créalo y vuelve a intentarlo."

    try:
        modificar_producto(
            id_producto,
            nuevo_nombre.strip(),
            nueva_categoria,
            nuevo_proveedor,
            nuevo_stock,
            nuevo_precio
        )
        return "ok: Producto modificado correctamente."
    except Exception as e:
        return f"Error al editar el producto: {e}"

def borrar_producto(id_producto):
    ids = []
    for prod in listar_productos():
        ids.append(prod[0])

    if id_producto not in ids:
        return "❌ El ID de producto ingresado no existe."

    try:
        eliminar_producto(id_producto)
        return "ok: Producto eliminado correctamente."
    except Exception as e:
        return f"Error al eliminar el producto: {e}"

def obtener_productos():
    return listar_productos()