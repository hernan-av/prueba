# ---------- GESTIÓN DE CLIENTES ----------

from db.clientes_db import insertar_cliente, listar_clientes, modificar_cliente, eliminar_cliente
from interfaz.mensajes import mostrar_error, mostrar_exito, mostrar_cancelado
from interfaz.entrada import pedir_input_con_cancelacion
from utils.utils import formatear_nombre, formatear_email
from interfaz.mostrar_resumen import mostrar_clientes
from utils.logger import log_info

def obtener_dnis_clientes() -> list[str]:
    dnis = []
    for cli in listar_clientes():
        dnis.append(cli[4])
    return dnis

def obtener_cliente_por_id(id_cliente: int):
    for cliente in listar_clientes():
        if cliente[0] == id_cliente:
            return cliente
    return None

def agregar_cliente():
    
        # ---- DNI ----
    while True:
        dni = pedir_input_con_cancelacion("Ingresá el DNI del cliente (C para cancelar): ")
        if dni.lower() == "c":
            mostrar_cancelado("Clientes")
            return
        if not dni:
            mostrar_error("El DNI no puede estar vacío.")
            continue
        if not dni.isdigit():
            mostrar_error("El DNI solo puede contener números.")
            continue
        if dni in obtener_dnis_clientes():
            mostrar_error("Ya existe un cliente con ese DNI.")
            continue
        break
    
    # ---- Nombre ----
    while True:
        nombre = pedir_input_con_cancelacion("Ingresá el nombre del nuevo cliente (C para cancelar): ")
        if nombre.lower() == "c":
            mostrar_cancelado("Clientes")
            return
        if not nombre:
            mostrar_error("El nombre del cliente no puede estar vacío.")
            continue
        break

    # ---- Teléfono ----
    while True:
        telefono = pedir_input_con_cancelacion("Ingresá un teléfono de contacto (C para cancelar): ")
        if telefono.lower() == "c":
            mostrar_cancelado("Clientes")
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
            mostrar_cancelado("Clientes")
            return
        if not email:
            mostrar_error("El email no puede estar vacío.")
            continue
        break

    # ---- Inserción ----
    nombre_formateado = formatear_nombre(nombre)
    email_formateado = formatear_email(email)
    if insertar_cliente(nombre_formateado, telefono, email_formateado, dni):
        mostrar_exito(f"Cliente agregado correctamente: → DNI: {dni}, Nombre: {formatear_nombre(nombre)}")
        log_info(f"Cliente agregado → → DNI: {dni}, Nombre: {formatear_nombre(nombre)}")
    else:
        mostrar_error("No se pudo agregar cliente.")

def editar_cliente():
    clientes = listar_clientes()
    if not clientes:
        mostrar_error("No hay clientes registrados")
        return

    mostrar_clientes(clientes)

    # Solicitar ID válido
    while True:
        entrada = pedir_input_con_cancelacion("Ingresá el ID del cliente a modificar (C para cancelar): ")
        if entrada.lower() == "c":
            mostrar_cancelado("Clientes")
            return
        if not entrada.isdigit():
            mostrar_error("El ID debe ser un número.")
            continue

        id_cliente = int(entrada)
        cliente = obtener_cliente_por_id(id_cliente)
        if cliente is None:
            mostrar_error("El ID ingresado no corresponde a ningún cliente.")
            continue
        break # ID válido

    # --- Guardar valores actuales ---
    nombre_actual = cliente[1]
    telefono_actual = cliente[2]
    email_actual = cliente[3]
    dni_actual = cliente[4]

    # --- DNI ---
    while True:
        nuevo_dni = pedir_input_con_cancelacion(
            f"DNI actual: {dni_actual}\nIngresá el nuevo DNI (Enter para dejar igual, C para cancelar): "
        )
        if nuevo_dni.lower() == "c":
            mostrar_cancelado("Clientes")
            return
        if not nuevo_dni:
            nuevo_dni = dni_actual
            break
        if not nuevo_dni.isdigit():
            mostrar_error("El DNI solo puede contener números.")
            continue
        if nuevo_dni != dni_actual and dni_actual in obtener_dnis_clientes():
            mostrar_error("Ya existe un cliente con ese DNI.")
            continue
        break

    # --- Nombre ---
    nuevo_nombre = pedir_input_con_cancelacion(
        f"Nombre actual: {nombre_actual}\nIngresá el nuevo nombre (Enter para dejar igual, C para cancelar): "
    )
    if nuevo_nombre.lower() == "c":
        mostrar_cancelado("Clientes")
        return
    if not nuevo_nombre:
        nuevo_nombre = nombre_actual

    # --- Teléfono ---
    while True:
        nuevo_telefono = pedir_input_con_cancelacion(
            f"Teléfono actual: {telefono_actual}\nIngresá el nuevo teléfono (Enter para dejar igual, C para cancelar): "
        )
        if nuevo_telefono.lower() == "c":
            mostrar_cancelado("Clientes")
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
        mostrar_cancelado("Clientes")
        return
    if not nuevo_email:
        nuevo_email = email_actual

    # --- Actualización ---
    if modificar_cliente(
        id_cliente,
        formatear_nombre(nuevo_nombre),
        nuevo_telefono,
        formatear_email(nuevo_email),
        nuevo_dni
    ):
        mostrar_exito(f"Cliente editado correctamente → ID: {id_cliente}")
        log_info(f"Cliente editado → ID: {id_cliente}")
    else:
        mostrar_error("No se pudo modificar cliente")

def borrar_cliente():
    clientes = listar_clientes()
    if not clientes:
        mostrar_error("No hay clientes registrados")
        return
    
    mostrar_clientes(clientes)
    
    # ---- Solicitar ID válido ----
    while True:
        entrada = pedir_input_con_cancelacion("Ingresá el ID del cliente a modificar (C para cancelar): ")
        if entrada == "c":
            mostrar_cancelado("Clientes")
            return
        if not entrada.isdigit():
            mostrar_error("El ID debe ser un número.")
            continue
        
        id_cliente = int(entrada)
        cliente = obtener_cliente_por_id(id_cliente)
        if cliente is None:
            mostrar_error("El ID ingresado no corresponde a ningún cliente.")
        break # ID válido

    # --- Elimanación ---
    if eliminar_cliente(id_cliente):
        mostrar_exito(f"Cliente eliminado correctamente → ID: {id_cliente}")
        log_info(f"Cliente eliminado → ID: {id_cliente}")
    else:
        mostrar_error("No se puedo eliminar cliente")

def mostrar_todos_los_clientes():
    clientes = listar_clientes()
    if clientes:
        mostrar_clientes(clientes)
    else:
        mostrar_error("No hay clientes registrados.")
