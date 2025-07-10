# ---------- GESTIÓN DE PROVEEDORES ----------

from db.proveedores_db import insertar_proveedor, listar_proveedores, modificar_proveedor, eliminar_proveedor
from interfaz.mensajes import mostrar_error, mostrar_exito, mostrar_cancelado
from interfaz.entrada import pedir_input_con_cancelacion
from interfaz.mostrar_resumen import mostrar_proveedores
from utils.utils import formatear_nombre, formatear_email
from db.productos_db import buscar_productos_por_proveedor_id
from utils.logger import log_info

def obtener_cuits_proveedores() -> list[str]:
    cuits = []
    for prov in listar_proveedores():
        cuits.append(prov[4])
    return cuits

def obtener_proveedor_por_id(id_proveedor: int):
    for prov in listar_proveedores():
        if prov[0] == id_proveedor:
            return prov
    return None

def agregar_proveedor():
    
        # ---- CUIT ----
    while True:
        cuit = pedir_input_con_cancelacion("Ingresá el CUIT del proveedor (C para cancelar): ")
        if cuit.lower() == "c":
            mostrar_cancelado("Proveedores")
            return
        if not cuit:
            mostrar_error("El CUIT no puede estar vacío.")
            continue
        if not cuit.isdigit():
            mostrar_error("El CUIT solo puede contener números.")
            continue

        # Validación de duplicado
        if cuit in obtener_cuits_proveedores():
            mostrar_error("Ya existe un proveedor con ese CUIT.")
            continue
        break
    
    # ---- Nombre ----
    while True:
        nombre = pedir_input_con_cancelacion("Ingresá el nombre del nuevo proveedor (C para cancelar): ")
        if nombre.lower() == 'c':
            mostrar_cancelado("Proveedores")
            return
        if not nombre:
            mostrar_error("El nombre del proveedor no puede estar vacío.")
            continue
        break

    # ---- Teléfono ----
    while True:
        telefono = pedir_input_con_cancelacion("Ingresá un teléfono de contacto (C para cancelar): ")
        if telefono == 'c':
            mostrar_cancelado("Proveedores")
            return
        if not telefono:
            mostrar_error("El teléfono no puede estar vacío.")
            continue
        if not telefono.isdigit():
            mostrar_error("El teléfono solo puede contener números.")
            continue
        break

    # ---- Email ----
    while True:
        email = pedir_input_con_cancelacion("Ingresá un email de contacto (C para cancelar): ")
        if email.lower() == "c":
            mostrar_cancelado("Proveedores")
            return
        if not email:
            mostrar_error("El email no puede estar vacío.")
            continue
        break

    # ---- Inserción ----
    nombre_formateado = formatear_nombre(nombre)
    email_formateado = formatear_email(email)
    if insertar_proveedor(nombre_formateado, telefono, email_formateado, cuit):
        mostrar_exito(f"Proveedor agregado correctamente → CUIT: {cuit}, Nombre: {formatear_nombre(nombre)}")
        log_info(f"Proveedor agregado → CUIT: {cuit}, Nombre: {formatear_nombre(nombre)}")
    else:
        mostrar_error("No se pudo agregar proveedor")

def editar_proveedor():
    proveedores = listar_proveedores()
    if not proveedores:
        mostrar_error("No hay proveedores registrados")
        return

    mostrar_proveedores(proveedores)

    # --- Solicitar ID válido ---
    while True:
        entrada = pedir_input_con_cancelacion("Ingresá el ID del proveedor a modificar (C para cancelar): ")
        if entrada.lower() == "c":
            mostrar_cancelado("Proveedores")
            return
        if not entrada.isdigit():
            mostrar_error("El ID debe ser un número.")
            continue

        id_proveedor = int(entrada)
        proveedor = obtener_proveedor_por_id(id_proveedor)
        if proveedor is None:
            mostrar_error("El ID de proveedor ingresado no existe.")
            continue
        break # ID válido

    # --- Guardar valores actuales ---
    nombre_actual = proveedor[1]
    telefono_actual = proveedor[2]
    email_actual = proveedor[3]
    cuit_actual = proveedor[4]

    # --- CUIT ---
    while True:
        nuevo_cuit = pedir_input_con_cancelacion(
            f"CUIT actual: {cuit_actual}\nIngresá el nuevo CUIT (Enter para dejar igual, C para cancelar): "
        )
        if nuevo_cuit.lower() == "c":
            mostrar_cancelado("Proveedores")
            return
        if not nuevo_cuit:
            nuevo_cuit = cuit_actual
            break
        if not nuevo_cuit.isdigit():
            mostrar_error("El CUIT solo puede contener números.")
            continue
        if nuevo_cuit != cuit_actual and nuevo_cuit in obtener_cuits_proveedores():
            mostrar_error("Ya existe un proveedor con ese CUIT.")
            continue
        break

    # --- Nombre ---
    nuevo_nombre = pedir_input_con_cancelacion(
        f"Nombre actual: {nombre_actual}\nIngresá el nuevo nombre (Enter para dejar igual, C para cancelar): "
    )
    if nuevo_nombre.lower() == "c":
        mostrar_cancelado("Proveedores")
        return
    if not nuevo_nombre:
        nuevo_nombre = nombre_actual

    # --- Teléfono ---
    while True:
        nuevo_telefono = pedir_input_con_cancelacion(
            f"Teléfono actual: {telefono_actual}\nIngresá el nuevo teléfono (Enter para dejar igual, C para cancelar): "
        )
        if nuevo_telefono.lower() == "c":
            mostrar_cancelado("Proveedores")
            return
        if not nuevo_telefono:
            nuevo_telefono = telefono_actual
            break
        if not nuevo_telefono.isdigit():
            mostrar_error("El teléfono solo puede contener números.")
            continue
        break

    # --- Email ---
    nuevo_email = pedir_input_con_cancelacion(
        f"Email actual: {email_actual}\nIngresá el nuevo email (Enter para dejar igual, C para cancelar): "
    )
    if nuevo_email.lower() == "c":
        mostrar_cancelado("Proveedores")
        return
    if not nuevo_email:
        nuevo_email = email_actual


    if modificar_proveedor(
        id_proveedor,
        formatear_nombre(nuevo_nombre),
        nuevo_telefono,
        formatear_email(nuevo_email),
        nuevo_cuit
    ):
        mostrar_exito(f"Proveedor editado correctamente → ID {id_proveedor}")
        log_info(f"Proveedor editado → ID {id_proveedor}")
    else:
        mostrar_error("No se pudo editar proveedor")

def borrar_proveedor():
    proveedores = listar_proveedores()
    if not proveedores:
        mostrar_error("No hay proveedores registrados")
        return

    mostrar_proveedores(proveedores)

    # ---- Solicitar ID válido ----
    while True:
        entrada = pedir_input_con_cancelacion("Ingresá el ID del proveedor a modificar (C para cancelar): ")
        if entrada == 'c':
            mostrar_cancelado("Proveedores")
            return
        if not entrada.isdigit():
            mostrar_error("El ID debe ser un número.")
            continue
        
        id_proveedor = int(entrada)
        proveedor = obtener_proveedor_por_id(id_proveedor)
        if proveedor is None:
            mostrar_error("El ID de proveedor ingresado no existe.")
            continue
        break # ID válido

    if buscar_productos_por_proveedor_id(id_proveedor):
        mostrar_error(
    "No se puede eliminar el proveedor porque posée porductos asociados.\n"
    "Cambie lel proveedor de esos productos y vuelva a intentarlo."
    )
        return

    # ---- Eliminación ----
    if eliminar_proveedor(id_proveedor):
        mostrar_exito(f"Proveedor eliminado correctamente → ID: {id_proveedor}")
        log_info(f"Proveedor eliminado → ID: {id_proveedor}")
    else:
        mostrar_error("No se pudo eliminar proveedor")

def mostrar_todos_los_proveedores():
    proveedores = listar_proveedores()
    if proveedores:
        mostrar_proveedores(proveedores)
    else:
        mostrar_error("No ha proveedores registrados")