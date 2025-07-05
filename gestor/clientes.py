# ---------- GESTIÓN DE CLIENTES ----------

from db.clientes_db import (
    insertar_cliente,
    listar_clientes,
    modificar_cliente,
    eliminar_cliente
)

def agregar_cliente(nombre: str, telefono: str, email: str, dni: str):
    if not nombre.strip():
        return "❌ El nombre no puede estar vacío."
    if not telefono.strip():
        return "❌ El teléfono no puede estar vacío."
    if not email.strip():
        return "❌ El email no puede estar vacío."
    if not dni.strip():
        return "❌ El DNI no puede estar vacío."

    # Validar que el DNI no esté duplicado
    for cli in listar_clientes():
        if cli[4] == dni.strip():
            return "❌ Ya existe un cliente con ese DNI."

    try:
        insertar_cliente(nombre.strip(), telefono.strip(), email.strip(), dni.strip())
        return "ok: Cliente agregado con éxito."
    except Exception as e:
        return f"Error al agregar el cliente: {e}"

def editar_cliente(id_cliente, nuevo_nombre: str, nuevo_telefono: str, nuevo_email: str, nuevo_dni: str):
    ids = []
    for cli in listar_clientes():
        ids.append(cli[0])

    if id_cliente not in ids:
        return "❌ El ID de cliente ingresado no existe."
    if not nuevo_nombre.strip():
        return "❌ El nombre no puede estar vacío."
    if not nuevo_telefono.strip():
        return "❌ El teléfono no puede estar vacío."
    if not nuevo_email.strip():
        return "❌ El email no puede estar vacío."
    if not nuevo_dni.strip():
        return "❌ El DNI no puede estar vacío."

    # Validar que el nuevo DNI no esté duplicado en otro cliente
    for cli in listar_clientes():
        if cli[4] == nuevo_dni.strip() and cli[0] != id_cliente:
            return "❌ Ya existe otro cliente con ese DNI."

    try:
        modificar_cliente(
            id_cliente,
            nuevo_nombre.strip(),
            nuevo_telefono.strip(),
            nuevo_email.strip(),
            nuevo_dni.strip()
        )
        return "ok: Cliente modificado correctamente."
    except Exception as e:
        return f"Error al editar el cliente: {e}"

def borrar_cliente(id_cliente):
    ids = []
    for cli in listar_clientes():
        ids.append(cli[0])

    if id_cliente not in ids:
        return "❌ El ID de cliente ingresado no existe."

    try:
        eliminar_cliente(id_cliente)
        return "ok: Cliente eliminado correctamente."
    except Exception as e:
        return f"Error al eliminar el cliente: {e}"

def obtener_clientes():
    return listar_clientes()
