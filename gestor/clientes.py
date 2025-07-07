# ---------- GESTIÓN DE CLIENTES ----------

from db.clientes_db import insertar_cliente, listar_clientes, modificar_cliente, eliminar_cliente
from interfaz.mensajes import mostrar_error, mostrar_exito, mostrar_cancelado
from interfaz.entrada import pedir_input_con_cancelacion
from utils.utils import formatear_nombre, formatear_email
from interfaz.mostrar_resumen import mostrar_clientes


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

        # Validación de duplicado
        dni_ya_registrado = []
        for cli in listar_clientes():
            dni_ya_registrado.append(cli[4])

        if dni in dni_ya_registrado:
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
    try:
        nombre_formateado = formatear_nombre(nombre)
        email_formateado = formatear_email(email)
        insertar_cliente(nombre_formateado, telefono, email_formateado, dni)
        mostrar_exito("Cliente agregado con éxito.")
    except Exception as e:
        mostrar_error(f"Error al agregar el cliente: {e}")

def editar_cliente():
    clientes = listar_clientes()
    if not clientes:
        mostrar_error("No hay clientes registrados")
        return

    mostrar_clientes(clientes)

    while True:
        entrada = pedir_input_con_cancelacion("Ingresá el ID del cliente a modificar (C para cancelar): ")
        if entrada.lower() == "c":
            mostrar_cancelado("Clientes")
            return
        if not entrada.isdigit():
            mostrar_error("El ID debe ser un número.")
            continue

        id_cliente = int(entrada)
        ids_disponibles = [cli[0] for cli in clientes]
        if id_cliente not in ids_disponibles:
            mostrar_error("El ID ingresado no corresponde a ningún cliente.")
            continue
        break

    # Datos actuales
    cliente = next(cli for cli in clientes if cli[0] == id_cliente)
    nombre_actual, telefono_actual, email_actual, dni_actual = cliente[1:5]

    # --- DNI ---
    while True:
        nuevo_dni = pedir_input_con_cancelacion(
            f"🆔 DNI actual: {dni_actual}\nIngresá el nuevo DNI (Enter para dejar igual, C para cancelar): "
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
        if nuevo_dni != dni_actual:
            dnis = [cli[4] for cli in listar_clientes()]
            if nuevo_dni in dnis:
                mostrar_error("Ya existe un cliente con ese DNI.")
                continue
        break

    # --- Nombre ---
    nuevo_nombre = pedir_input_con_cancelacion(
        f"📝 Nombre actual: {nombre_actual}\nIngresá el nuevo nombre (Enter para dejar igual, C para cancelar): "
    )
    if nuevo_nombre.lower() == "c":
        mostrar_cancelado("Clientes")
        return
    if not nuevo_nombre.strip():
        nuevo_nombre = nombre_actual

    # --- Teléfono ---
    while True:
        nuevo_telefono = pedir_input_con_cancelacion(
            f"📱 Teléfono actual: {telefono_actual}\nIngresá el nuevo teléfono (Enter para dejar igual, C para cancelar): "
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
        f"📧 Email actual: {email_actual}\nIngresá el nuevo email (Enter para dejar igual, C para cancelar): "
    )
    if nuevo_email.lower() == "c":
        mostrar_cancelado("Clientes")
        return
    if not nuevo_email.strip():
        nuevo_email = email_actual

    try:
        modificar_cliente(
            id_cliente,
            formatear_nombre(nuevo_nombre.strip()),
            nuevo_telefono.strip(),
            formatear_email(nuevo_email.strip()),
            nuevo_dni.strip()
        )
        mostrar_exito("Cliente modificado correctamente.")
    except Exception as e:
        mostrar_error(f"Error al editar el cliente: {e}")

def borrar_cliente():
    clientes = listar_clientes()
    if not clientes:
        mostrar_error("No hay clientes registrados")
        return
    
    mostrar_clientes(clientes)
    
    # ---- ID válido ----
    while True:
        entrada = pedir_input_con_cancelacion("Ingresá el ID del cliente a modificar (C para cancelar): ")
        if entrada == "c":
            mostrar_cancelado("Clientes")
            return
        if not entrada.isdigit():
            mostrar_error("El ID debe ser un número.")
            continue
        
        id_cliente = int(entrada)
        
        ids_disponibles = []
        for cli in listar_clientes():
            ids_disponibles.append(cli[0])

        if id_cliente not in ids_disponibles:
            mostrar_error("El ID de cliente ingresado no existe.")
            continue
        break
    try:
        eliminar_cliente(id_cliente)
        mostrar_exito("Cliente eliminado correctamente.")
    except Exception as e:
        mostrar_error(f"Error al eliminar el cliente: {e}")

def mostrar_todos_los_clientes():
    clientes = listar_clientes()
    if clientes:
        mostrar_clientes(clientes)
    else:
        mostrar_error("No hay clientes registrados.")
