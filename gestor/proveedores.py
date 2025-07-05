# ---------- GESTIÓN DE PROVEEDORES ----------

from db.proveedores_db import (
    insertar_proveedor,
    listar_proveedores,
    modificar_proveedor,
    eliminar_proveedor
)

def agregar_proveedor(nombre: str, telefono: str, email: str, cuit: str):
    if not nombre.strip():
        return "El nombre no puede estar vacío."
    if not telefono.strip():
        return "El teléfono no puede estar vacío."
    if not email.strip():
        return "El email no puede estar vacío."
    if not cuit.strip():
        return "El CUIT no puede estar vacío."

    for prov in listar_proveedores():
        if prov[4] == cuit.strip():
            return "Ya existe un proveedor con ese CUIT."

    try:
        insertar_proveedor(nombre.strip(), telefono.strip(), email.strip(), cuit.strip())
        return "ok: Proveedor agregado con éxito."
    except Exception as e:
        return f"Error al agregar el proveedor: {e}"

def editar_proveedor(id_proveedor, nuevo_nombre: str, nuevo_telefono: str, nuevo_email: str, nuevo_cuit: str):
    ids = []
    for prov in listar_proveedores():
        ids.append(prov[0])

    if id_proveedor not in ids:
        return "El ID de proveedor ingresado no existe."
    if not nuevo_nombre.strip():
        return "El nombre no puede estar vacío."
    if not nuevo_telefono.strip():
        return "El teléfono no puede estar vacío."
    if not nuevo_email.strip():
        return "El email no puede estar vacío."
    if not nuevo_cuit.strip():
        return "El CUIT no puede estar vacío."

    for prov in listar_proveedores():
        if prov[4] == nuevo_cuit.strip() and prov[0] != id_proveedor:
            return "Ya existe otro proveedor con ese CUIT."

    try:
        modificar_proveedor(
            id_proveedor,
            nuevo_nombre.strip(),
            nuevo_telefono.strip(),
            nuevo_email.strip(),
            nuevo_cuit.strip()
        )
        return "ok: Proveedor modificado correctamente."
    except Exception as e:
        return f"Error al editar el proveedor: {e}"

def borrar_proveedor(id_proveedor):
    ids = []
    for prov in listar_proveedores():
        ids.append(prov[0])

    if id_proveedor not in ids:
        return "El ID de proveedor ingresado no existe."

    try:
        eliminar_proveedor(id_proveedor)
        return "ok: Proveedor eliminado correctamente."
    except Exception as e:
        return f"Error al eliminar el proveedor: {e}"

def obtener_proveedores():
    return listar_proveedores()